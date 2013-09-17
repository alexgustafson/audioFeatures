var chart = d3.select("#AbsoluteMaximum")
                .append("div").attr("class", "chart")

var svg = d3.select("body")
            .append("svg").attr("width", "500")
            .attr("height", "100")
            .append("g")
              .attr("class", "y axis")
              .call(yAxis).append("text")
              .attr("transform", "rotate(-90)")
              .attr("y", 6)
              .attr("dy", ".71em")
              .style("text-anchor", "end")
              .text("Temperature (ºF)");
