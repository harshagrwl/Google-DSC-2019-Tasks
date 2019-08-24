var APIKEY = '576a4d222c629b22dd9b57dcfe810fbb';
var latitude = 0;
var longitude = 0;
var lastResult = null;

function getLocation(callback) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    }

    if (callback) {
    	callback();
    }
}

function showPosition(position) {
	latitude = position.coords.latitude;
	longitude = position.coords.longitude;

	getJSON('https://api.forecast.io/forecast/' + APIKEY + '/' + 
		latitude + ',' + longitude + '?units=si&lang=pt&exclude=minutely,hourly,daily,alerts,flags', 
		function(result) {
			chrome.browserAction.setIcon({
	            path: "/" + result.currently.icon + ".png"
	        });

	        lastResult = result;
		});
}


function getJSON(url, callback) {
	var x = new XMLHttpRequest();
	x.open('GET', url);
	x.responseType = 'json';
	x.onload = function() {
		callback(x.response);
	};
	x.send();
}

function showError(error) {
	var statusDiv = document.getElementById("status");

    switch(error.code) {
        case error.PERMISSION_DENIED:
            console.log("Geolocation Request denied by User.");
            break;
        case error.POSITION_UNAVAILABLE:
            console.log("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            console.log("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            console.log("An unknown error occurred.");
            break;
    }
}

chrome.runtime.onInstalled.addListener(function() { //The .onInstalled listener runs during the installation of the extension or during the updation of the chrome
	chrome.alarms.create("forecast", {
	   delayInMinutes: 0,
	   periodInMinutes: 10
	});
});

chrome.alarms.onAlarm.addListener(function( alarm ) {//We create an alarm for 10 min and the function runs every 10 min
	getLocation();
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
	if (request.action == "getCurrentForecast") {
		getLocation(function() {
			sendResponse(lastResult);
		});
	}
});