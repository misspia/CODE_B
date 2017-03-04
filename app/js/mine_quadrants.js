// https://bl.ocks.org/mbostock/3885304

function createSvg(container, height, width) {
	return d3.select(container).append('svg')
	.attr('height', height)
	.attr('width', width)
	.attr('class', 'col center align-center')
	// .style('border', 'solid 0.1em black');
}


var quadGraph = d3.select('#mine_quadrants');
var margin = {top: 20, right: 20, bottom: 20, left: 50};
var quadGraphHeight = quadGraph._groups[0][0].offsetHeight;
var quadGraphWidth = quadGraph._groups[0][0].offsetWidth ;

var quadSvg = createSvg('#mine_quadrants', quadGraphHeight, quadGraphWidth );


var fakeQuadData = [
	{quadrant:1, mines: 10},
	{quadrant:2, mines: 20},
	{quadrant:3, mines: 5},
	{quadrant:4, mines: 15},

];

var x = d3.scaleBand().rangeRound([0, quadGraphWidth]).padding(0.2),
    y = d3.scaleLinear().rangeRound([quadGraphHeight, 0]);

x.domain(fakeQuadData.map(function(d) { return d.quadrant; }));
y.domain([0, d3.max(fakeQuadData, function(d) { return d.mines; })]);

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
  .attr("text-anchor", "end")
  .text("# of Mines");



g.selectAll(".bar")
.data(fakeQuadData)
.enter().append("rect")
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.quadrant); })
  .attr("y", function(d) { return y(d.mines); })
  .attr("width", x.bandwidth())
  .attr("height", function(d) { return quadGraphHeight - y(d.mines); });



















