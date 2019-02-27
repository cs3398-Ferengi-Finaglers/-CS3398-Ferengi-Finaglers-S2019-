$(function() {
	displayResults();
	console.log(getCookie("clientId"));

	if (checkCookie()) {
		$("#clientId").html(getCookie("clientId"));
	} else {
		$("#clientId").html("Please select a client ID in the client information page");
	}
});

function displayResults() {
	var clientId = getCookie("clientId");

	var xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var jsonObj = JSON.parse(this.responseText);
			populateTable(jsonObj.quotes);
			console.log(jsonObj.quotes);
		}
	};
	
	xmlhttp.open("GET", "/fuelrate/FuelRateAPI/v1/API.php?apicall=getquotehistory&clientId=" + clientId, true);
	xmlhttp.send();
}

function populateTable(response) {
	var trHTML = '';
	$.each(response, function (i, item) {
		trHTML += '<tr><td>' + item.clientId + '</td><td>' + item.requestDate + '</td><td>' + item.deliveryDate + '</td><td>' + item.gallonsRequested + '</td><td>' + item.suggestedPrice + '</td><td>' + item.totalAmountDue + '</td></tr>';
	});
	$('#records_table').append(trHTML);
}

function setCookie(cvalue) {
	document.cookie = "clientId=" + cvalue + "; expires=Thu, 18 Dec 2020 12:00:00 UTC; path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var user = getCookie("clientId");
    if (user == "" || user == "Create new client") {
        return false;
    } else {
        return true;
    }
}