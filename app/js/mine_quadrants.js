// https://bl.ocks.org/mbostock/3885304

function createSvg(container, height, width) {
	return d3.select(container).append('svg')
	.attr('height', height)
	.attr('width', width)
	.attr('class', 'col center align-center')
}


var quadGraph = d3.select('#mine_quadrants');
var margin = {top: 20, right: 20, bottom: 20, left: 50};
var quadGraphHeight = quadGraph._groups[0][0].offsetHeight;
var quadGraphWidth = quadGraph._groups[0][0].offsetWidth ;



var x = d3.scaleBand().rangeRound([0, quadGraphWidth - margin.left - margin.right]).padding(0.2),
    y = d3.scaleLinear().rangeRound([quadGraphHeight -margin.top - margin.bottom, 0]);


  d3.json("minedataforpia.json", function(error, data) {
  if (error) throw error;

    var count = 0;
    setInterval(function(){ 
        if(count <= data.length - 2) {
            count ++;
        } 
        d3.select("#mine_quadrants svg").remove();
          
          var quadSvg = createSvg('#mine_quadrants', quadGraphHeight, quadGraphWidth );

            x.domain(data[count].map(function(d) { return d.quadrant; }));
            // y.domain([0, d3.max(data[count], function(d) { return d.mines; }) + 2]);
            y.domain([0, 20]);

            var g = quadSvg.append("g")
                .attr("transform", "translate(" + margin.left/2 + ", -" + margin.top + ")");

            g.append("g")
              .attr("class", "axis axis--x")
              .attr("transform", "translate(0," + quadGraphHeight + ")")
              .call(d3.axisBottom(x));

            g.append("g")
              .attr("class", "axis axis--y")
              .call(d3.axisLeft(y).ticks(5))
            .append("text")
              .attr("transform", "rotate(-90)")
              .attr("y", 6)
              .attr("dy", "0.71em")
              // .attr("text-anchor", "end")
              // .text("# of Mines");

              g.selectAll(".bar")
            .data(data[count])
            .enter().append("rect")
              .attr("class", "bar")
              .attr("x", function(d) { return x(d.quadrant); })
              .attr("y", function(d) { return y(d.mines); })
              .attr("width", x.bandwidth())
              .attr("height", function(d) { return quadGraphHeight - y(d.mines); });



    }, 200);



    

});



















