// var fakeLineData = [
// 	{
// 		name:'team1',
// 		score: 10,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 20,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 30,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 40,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 40,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 41,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 45,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 45,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 50,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 55,
// 		mines:3,
// 		time_elapsed:1
// 	},
// 	{
// 		name:'team1',
// 		score: 55,
// 		mines:3,
// 		time_elapsed:1
// 	}
// ]

// console.log(JSON.stringify(fakeLineData))
var testData = [1,1,1,1,2,3,4,4,5,6,7,7,5,4,3,5,7,8,8,9,];

var lineGraph = d3.select('#line_graph');
var margin = {top: 20, right: 20, bottom: 20, left: 20};
var lineGraphHeight = lineGraph._groups[0][0].offsetHeight;
var lineGraphWidth = lineGraph._groups[0][0].offsetWidth ;

var lineSvg = createSvg('#line_graph', lineGraphHeight, lineGraphWidth );
var lineGraphHeight = lineGraph._groups[0][0].offsetHeight;
var lineGraphWidth = lineGraph._groups[0][0].offsetWidth ;
 
 //start
var margin = {top: 20, right: 20, bottom: 30, left: 50};


  var valueline = d3.line()
  .x(function(d, i) { return x(i); })
  .y(function(d) { return y(d) / 2; });

  var x = d3.scaleLinear().range([0, lineGraphWidth]);
  var y = d3.scaleLinear().range([lineGraphHeight, 0]);

  lineSvg.append("path")
  .attr("class", "line")
  .attr("d", valueline(testData));

  function renderChart() {
     requestAnimationFrame(renderChart);

     analyser.getByteFrequencyData(frequencyData);

     x.domain(d3.extent(frequencyData, function(d, i) { return i; }));
     y.domain([0, d3.max(frequencyData, function(d) { return d * 2; })]);

     svg.selectAll("path")
     .attr('d', valueline(frequencyData))
     .attr('stroke', function(d){
        return graphColors(d);
     })
     .attr({
      'stroke-width': 2,
      'fill': 'none'
    })
 }







// set the dimensions and margins of the graph
// var margin = {top: 20, right: 20, bottom: 30, left: 50},
//     width = 960 - margin.left - margin.right,
//     height = 500 - margin.top - margin.bottom;

// // parse the date / time
// var parseTime = d3.timeParse("%d-%b-%y");

// // set the ranges
// var x = d3.scaleTime().range([0, width]);
// var y = d3.scaleLinear().range([height, 0]);

// // define the line
// var valueline = d3.line()
//     .x(function(d) { return x(d.date); })
//     .y(function(d) { return y(d.close); });

// // append the svg obgect to the body of the page
// // appends a 'group' element to 'svg'
// // moves the 'group' element to the top left margin
// var svg = d3.select("#line_graph").append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform",
//           "translate(" + margin.left + "," + margin.top + ")");

// d3.json("/app/js/test.json", function(error, data) {
//   if (error) throw error;

//   // format the data
//   data.forEach(function(d) {
//       // d.date = parseTime(d.date);
//       d.date = d.date;
//       d.close = +d.close;
//   });

//   // Scale the range of the data
//   x.domain(d3.extent(data, function(d) { return d.date; }));
//   y.domain([0, d3.max(data, function(d) { return d.close; })]);

//   // Add the valueline path.
//   svg.append("path")
//       .data([data])
//       .attr("class", "line")
//       .attr("d", valueline);

//   // Add the X Axis
//   svg.append("g")
//       .attr("transform", "translate(0," + height + ")")
//       .call(d3.axisBottom(x));

//   // Add the Y Axis
//   svg.append("g")
//       .call(d3.axisLeft(y));

// });



















