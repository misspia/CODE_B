// var color = d3.scaleOrdinal(d3.schemeCategory20);
// https://bl.ocks.org/santi698/f3685ca8a1a7f5be1967f39f367437c0

var pieGraph = d3.select('#pie_graph');
var pieGraphHeight = pieGraph._groups[0][0].offsetHeight;
var pieGraphWidth = pieGraph._groups[0][0].offsetWidth ;

var radius = Math.min(pieGraphWidth, pieGraphHeight) / 2;

var color = d3.scaleOrdinal(d3.schemeCategory20b);

var arc = d3.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);

var labelArc = d3.arc()
    .outerRadius(radius - 40)
    .innerRadius(radius - 40);

var pie = d3.pie()
    .sort(null)
    .value(function(d) { return d.mines; });




d3.json("scoredataforpia.json", function(error, data) {
  if (error) throw error;

  var count = 0;
    setInterval(function(){ 

        if(count <= data.length - 2) {
            count ++;
        } else {
            // alert('data set end')
            document.getElementById('data_status').innerHTML = "data set end";
        }
         
            d3.select("#pie_graph svg").remove();
            // console.log(data[count]);
            
        var pieSvg = pieGraph.append("svg")
        .attr("width", pieGraphWidth)
        .attr("height", pieGraphHeight)
      .append("g")
        .attr("transform", "translate(" + pieGraphWidth / 2 + "," + pieGraphHeight / 2 + ")");

          var g = pieSvg.selectAll(".arc")
          .data(pie(data[count]))
         .enter()
         .append("g")
          .attr("class", "arc");

          g.append("path")
              .attr("d", arc)
              // .style("fill", function(d) { return color(d.data.mines); });
              .style("fill", "#bcbd22");

          g.append("text")
              .attr("transform", function(d) {  
                return "translate(" + labelArc.centroid(d) + ")"; })
              .attr("dy", ".35em")
              .text(function(d) { 
               return d.data.name; });

    }, 200);

});
