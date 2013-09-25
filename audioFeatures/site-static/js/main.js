$(document).ready( function () {

    var process = function($element, $featureID, $audioFileID) {

        var csrftoken = $.cookie('csrftoken');

        $.ajax({
        type: "POST",
        url: "process_chain/",
        data: {
            featureID: $featureID,
            audioFileID: $audioFileID,
            csrfmiddlewaretoken: csrftoken
        }

        }).done(function (d) {

                //alert(d)
                $element.append(d)

            }
        );

    }

    $(".showGraph").click( function() {

        svgElement = $(this).parent().parent().find('.chain')
        if(svgElement.length == 0)
        {
            process($(this).parent().parent(), 1,1)
        }else{

        }
        //



    });



});