var leaderBoard = d3.select('#leaderboard table');

var testData = [
	{
		name: 'team1',
		score: 13,
		mines: 2
	},
	{
		name: 'team2',
		score: 50,
		mines: 5
	},
	{
		name: 'team3',
		score: 3,
		mines: 0
	},
	{
		name: 'team4',
		score: 1,
		mines: 10
	},
	{
		name: 'team5',
		score: 1,
		mines: 0
	},
	{
		name: 'team6',
		score: 8,
		mines: 10
	},
	{
		name: 'team7',
		score: 5,
		mines: 30
	},
	{
		name: 'algowinthis',
		score: 3,
		mines: 0
	}

];

populateLeaderBoard(leaderBoard, testData);

function populateLeaderBoard(board, data) {

	var thead = board.select('thead');
	var tbody = board.select('tbody');
	var headers = ['rank', 'team name', 'score', 'mines owned'];

	populateTableHeader(thead, headers);

	d3.json("scoredataforpia.json", function(error, data) {
	  if (error) throw error;
		
	  var count = 0;
	    setInterval(function(){ 
	         if(count <= data.length - 2) {
		            count ++;
		        } 
	            d3.select("tbody").selectAll('tr').remove();
	            // console.log(data[count]);
				populateTableBody(tbody, data[count]);
				// d3.select("tbody").selectAll('tr').remove();

	    }, 200)
	 });
	
}

function populateTableHeader(thead, data) {
	var headerRow = thead.append('tr');

	data.forEach(function(d) {

		headerRow.append('td')
			.text(d.toUpperCase())
	});

}


function populateTableBody(tbody, data) {

	data.slice(0, 5).forEach(function(d, i) {
		

		if(d.name == 'algowinthis') {

			var bodyRow = tbody.append('tr')
				.attr('class', 'algowin');

		} else {
			
			var bodyRow = tbody.append('tr');

		}
		bodyRow.append('td')
			.text(i + 1);

		for(var teamStat in d) {
			
			bodyRow.append('td')
				.text(d[teamStat])
		}

	})
	data.filter(function( obj, index) {

		if(obj.name == 'algowinthis' && index > 4) {

			var bodyRow = tbody.append('tr')
				.attr('class', 'algowin');

			bodyRow.append('td')
				.text(index + 1);

			for(var teamStat in obj) {
				
				bodyRow.append('td')
					.text(obj[teamStat])
			}

			return;

		} else if (obj.name == 'algowinthis' && index <= 4) {
			return;
		}
	})
}

