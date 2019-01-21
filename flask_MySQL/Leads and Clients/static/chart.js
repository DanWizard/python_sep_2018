w = function (all_data){
	console.log(all_data);

	var result = [];
	for (var i = 0; i < all_data.length; i++) {
		result.push({y: all_data[i]['Number_of_Leads'], label: all_data[i]['Customer_Name']});
	};

	var options = {
		title: {
			text: "Desktop OS Market Share in 2017"
		},
		subtitles: [{
			text: "As of November, 2017"
		}],
		animationEnabled: true,
		data: [{
			type: "pie",
			startAngle: 40,
			toolTipContent: "<b>{label}</b>: {y}%",
			showInLegend: "true",
			legendText: "{label}",
			indexLabelFontSize: 16,
			indexLabel: "{label} - {y}%",
			dataPoints: result
		}]
	};
	$("#chartContainer").CanvasJSChart(options);
	console.log('yo')
}