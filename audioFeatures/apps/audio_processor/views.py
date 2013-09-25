from django.shortcuts import render
from audio.models import AudioFile, ProcessFile
from audio_processor.models import AudioProcessNode, AudioProcessChain, AudioProcess
from af_documentation.models import Section
from django.http import HttpResponse

import numpy
from scipy.io import wavfile
import wave
import json

class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
            if isinstance(obj, numpy.ndarray) and obj.ndim == 1:
                    return [x for x in obj]
            return json.JSONEncoder.default(self, obj)


def process(request):

    audioFile = AudioFile.objects.get(pk=1).audiofile

    audioData = wave.open(audioFile.path, 'r')

    title = audioFile.name
    number_of_channels = audioData.getnchannels()
    frequency = audioData.getframerate()
    number_of_samples = audioData.getnframes()

    return render(request,
                  'audio_processor/audio_info.html',
                  {
                      'title': title,
                      'number_of_channels': number_of_channels,
                      'frequency': frequency,
                      'number_of_samples': number_of_samples,
                      'audioFileID': 1,
                  })


def getSamples(request):

    if request.method == 'POST':

        data = request.POST
        startPos = int(data['startPos'])
        length = int(data['length'])

    else:
        startPos = 0
        length = 44100

    skip = length / 1000
    audioFileID = 1

    audioFile = AudioFile.objects.get(pk=audioFileID).audiofile.file
    audioData = wave.open(audioFile, 'r')
    audioData.setpos(startPos)
    samples = audioData.readframes(length)
    numchannels = audioData.getnchannels()

    from struct import unpack              # Import unpack -- this is what does the conversion
    npts=len(samples)                      # Number of data points to be converted
    formatstr = '%ih' % (npts/2)                 # The format to convert the data; use '%iB' for unsigned PCM
    int_data = unpack(formatstr, samples)

    format_data = []
    counter = 0
    i = 0
    skip *= numchannels

    for sample in int_data:
        i += numchannels
        if i % skip != 0:
            continue
        format_data.append({'x': counter, 'y': sample})
        counter += 1

    return HttpResponse(json.dumps(format_data), mimetype='application/json')


def process_chain(request):

    if request.method == 'POST':
        data = request.POST
        featureID = data['featureID']
        audioFileID = data['audioFileID']

    else:
        featureID = 1
        audioFileID = 1

    audioFile = AudioFile.objects.get(pk=1).audiofile
    audioData = wave.open(audioFile.path, 'r')
    title = audioFile.name
    number_of_channels = audioData.getnchannels()
    frequency = audioData.getframerate()
    number_of_samples = audioData.getnframes()

    html = render(request,
              'audio_processor/process.html',
              {
                  'title': title,
                  'number_of_channels': number_of_channels,
                  'frequency': frequency,
                  'number_of_samples': number_of_samples,
                  'audioFileID': 1,
              })

    return HttpResponse( html)