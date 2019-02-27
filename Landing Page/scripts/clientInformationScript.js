$(function() {
	getClientInformationById();
	getClientId();

    console.log(getCookie("clientId"));

	$('#clientSelect').change(function() {
        setCookie($(this).val());
        getClientInformationById();
    });
});

function getClientId() {
	$.ajax({
        url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=getClientId",
        method: "GET",
        dataType: "json",
        success: function(response) {
            setSelect(response.clients);
        }
    });
}

function getClientInformationById() {
    var clientId = getCookie("clientId");
    $.ajax({
        url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=getClientInformationById&clientId=" + clientId,
        method: "GET",
        dataType: "json",
        success: function(response) {
            setText(response.client);
        }
    });
}

function setSelect(response) {
	$.each(response, function (i, item) {
	    $('#clientSelect').append($('<option>', {
	        text: item.clientId 
	    }));
	});

    if (checkCookie()) {
        $('#clientSelect').val(getCookie("clientId"));
    }
}

function setText(jsonObj) {
    if (checkCookie()) {
        $("#clientForm")[0].reset();
        $("#fullName").attr("value", jsonObj[0].fullName);
        $("#address").attr("value", jsonObj[0].address);
        $("#city").attr("value", jsonObj[0].city);
        $("#state").attr("value", jsonObj[0].state);
        $("#zipCode").attr("value", jsonObj[0].zipCode);
        $("#phone").attr("value", jsonObj[0].phone);
        $("#email").attr("value", jsonObj[0].email);
    } else {
        $("#clientForm")[0].reset();
        $("#fullName").attr("value", null);
        $("#address").attr("value", null);
        $("#city").attr("value", null);
        $("#state").attr("value", null);
        $("#zipCode").attr("value", null);
        $("#phone").attr("value", null);
        $("#email").attr("value", null);
    }
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

(function() {
  'use strict';
  window.addEventListener('load', function() {
    var forms = document.getElementsByClassName('needs-validation');
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          form.classList.add('was-validated');
          event.preventDefault();
          event.stopPropagation();
        } else {
          event.preventDefault();
          event.stopPropagation();

          var clientId = getCookie("clientId")
          var fullName = $('#fullName').val();
          var address = $('#address').val();
          var city = $('#city').val();
          var state = $('#state').val();
          var zipCode = $('#zipCode').val();
          var phone = $('#phone').val();
          var email = $('#email').val();

          if (checkCookie()) {
            $.ajax({
                url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=updateClient",
                method: "POST",
                data: {
                    clientId: clientId,
                    fullName: fullName,
                    address: address, 
                    city: city, 
                    state: state, 
                    zipCode: zipCode, 
                    phone: phone, 
                    email: email
                },
                dataType: "json",
                success: function(response) {
                    $("#modalHeading").html(response.error);
                    $("#modalBody").html(response.message);
                    $("#myModal").modal('show');
                    getClientInformationById();
                    getClientId();
                }
            });
          } else {
            $.ajax({
                url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=createClient",
                method: "POST",
                data: {
                    fullName: fullName,
                    address: address, 
                    city: city, 
                    state: state, 
                    zipCode: zipCode, 
                    phone: phone, 
                    email: email
                },
                dataType: "json",
                success: function(response) {
                    $("#modalHeading").html(response.error);
                    $("#modalBody").html(response.message);
                    $("#myModal").modal('show');
                    getClientInformationById();
                    getClientId();
                }
            });
          }

          // clear the form
          form.classList.remove('was-validated');
          form.reset();
        }
      }, false);
    });
  }, false);
})();