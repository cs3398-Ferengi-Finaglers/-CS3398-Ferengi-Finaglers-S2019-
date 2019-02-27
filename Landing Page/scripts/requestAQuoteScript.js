var quoteHistory;

$(function() {
  if (checkCookie()) {
    $("#clientId").html(getCookie("clientId"));
  } else {
    $("#clientId").html("Please select a client ID in the client information page");
  }
  checkQuote();
});

function checkQuote() {
  var clientId = getCookie("clientId");

  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var jsonObj = JSON.parse(this.responseText);
      console.log(jsonObj.quotes);
      if (jsonObj.quotes.length == 0) {
        quoteHistory = false;
        console.log(quoteHistory);
      } else {
        quoteHistory = true;
        console.log(quoteHistory);
      }
    }
  };
  
  xmlhttp.open("GET", "/fuelrate/FuelRateAPI/v1/API.php?apicall=getquotehistory&clientId=" + clientId, true);
  xmlhttp.send();
}

// $("#requestAQuoteForm").submit(function(event) {
//     /* stop form from submitting normally */
//     event.preventDefault();

//     /* get some values from elements on the page: */
//     var gallonsRequested = $('#gallonsRequested').val();
//     var deliveryDate = $('#deliveryDate').val();
//     var deliveryAddress = $('#deliveryAddress').val();
//     var deliveryCity = $('#deliveryCity').val();
//     var deliveryState = $('#deliveryState').val();
//     var deliveryZipCode = $('#deliveryZipCode').val();
//     var deliveryContactPersonName = $('#deliveryContactPersonName').val();
//     var deliveryContactPersonPhone = $('#deliveryContactPersonPhone').val();
//     var deliveryContactPersonEmail = $('#deliveryContactPersonEmail').val();
//     var suggestedPricePerGallon = $('#suggestedPricePerGallon').val();
//     var totalAmountDue = $('#totalAmountDue').val();

//     $("#requestAQuoteForm")[0].reset();

//     // /* Send the data using post */
//     // xmlhttp = new XMLHttpRequest();
//     // xmlhttp.onreadystatechange = function() {
//     //   if (this.readyState == 4 && this.status == 200) {
//     //     myObj = JSON.parse(this.responseText);
//     //     console.log(myObj);
//     //     $("#contactResponse").html(myObj.message);
//     //     $("#modalHeading").html(myObj.error);
//     //     $("#modalBody").html(myObj.message);
//     //     $("#myModal").modal('show');
//     //   }
//     // };

//     // xmlhttp.open("POST", "/fuelrate/FuelRateAPI/v1/API.php?apicall=setfuelquote", true);
//     // xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//     // xmlhttp.send (
//     //     "gallonsRequested=" + gallonsRequested + 
//     //     "&deliveryDate=" + deliveryDate + 
//     //     "&deliveryAddress=" + deliveryAddress + 
//     //     "&deliveryCity=" + deliveryCity + 
//     //     "&deliveryState=" + deliveryState + 
//     //     "&deliveryZipCode=" + deliveryZipCode + 
//     //     "&deliveryContactName=" + deliveryContactPersonName + 
//     //     "&deliveryContactPhone=" + deliveryContactPersonPhone + 
//     //     "&deliveryContactEmail=" + deliveryContactPersonEmail + 
//     //     "&suggestedPrice=" + suggestedPricePerGallon + 
//     //     "&totalAmountDue=" + totalAmountDue
//     // );

//     $.ajax({
//         url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=setfuelquote",
//         method: "POST",
//         data: {
//             gallonsRequested: gallonsRequested,
//             deliveryDate: deliveryDate, 
//             deliveryAddress: deliveryAddress, 
//             deliveryCity: deliveryCity, 
//             deliveryState: deliveryState, 
//             deliveryZipCode: deliveryZipCode, 
//             deliveryContactName: deliveryContactPersonName, 
//             deliveryContactPhone: deliveryContactPersonPhone, 
//             deliveryContactEmail: deliveryContactPersonEmail, 
//             suggestedPrice: suggestedPricePerGallon, 
//             totalAmountDue: totalAmountDue
//         },
//         dataType: "json",
//         success: function(response) {
//             $("#modalHeading").html(response.error);
//             $("#modalBody").html(response.message);
//             $("#myModal").modal('show');
//         }
//     });
// });

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

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {

        var suggestedPricePerGallon2 = $('#suggestedPricePerGallon').val();
        var totalAmountDue2 = $('#totalAmountDue').val();

        if (form.checkValidity() === false) {
          form.classList.add('was-validated');
          event.preventDefault();
          event.stopPropagation();
        } else if (suggestedPricePerGallon2 == "" && totalAmountDue2 == "") {
          event.preventDefault();
          event.stopPropagation();
          $("#modalHeading").html("Failure");
          $("#modalBody").html("Please push the Get Price button");
          $("#myModal").modal('show');
        } else {
          event.preventDefault();
          event.stopPropagation();

          // do ajax call here
            var clientId = getCookie("clientId");
            var gallonsRequested = $('#gallonsRequested').val();
            var deliveryDate = $('#deliveryDate').val();
            var deliveryAddress = $('#deliveryAddress').val();
            var deliveryCity = $('#deliveryCity').val();
            var deliveryState = $('#deliveryState').val();
            var deliveryZipCode = $('#deliveryZipCode').val();
            var deliveryContactPersonName = $('#deliveryContactPersonName').val();
            var deliveryContactPersonPhone = $('#deliveryContactPersonPhone').val();
            var deliveryContactPersonEmail = $('#deliveryContactPersonEmail').val();
            var suggestedPricePerGallon = $('#suggestedPricePerGallon').val();
            var totalAmountDue = $('#totalAmountDue').val();

            if (checkCookie()) {
              $.ajax({
                url: "/fuelrate/FuelRateAPI/v1/API.php?apicall=setfuelquote",
                method: "POST",
                data: {
                    clientId: clientId,
                    gallonsRequested: gallonsRequested,
                    deliveryDate: deliveryDate, 
                    deliveryAddress: deliveryAddress, 
                    deliveryCity: deliveryCity, 
                    deliveryState: deliveryState, 
                    deliveryZipCode: deliveryZipCode, 
                    deliveryContactName: deliveryContactPersonName, 
                    deliveryContactPhone: deliveryContactPersonPhone, 
                    deliveryContactEmail: deliveryContactPersonEmail, 
                    suggestedPrice: suggestedPricePerGallon, 
                    totalAmountDue: totalAmountDue
                },
                dataType: "json",
                success: function(response) {
                    $("#modalHeading").html(response.error);
                    $("#modalBody").html(response.message);
                    $("#myModal").modal('show');
                }
              });
            } else {
              $("#modalHeading").html("Failure");
              $("#modalBody").html("Please select a client ID in the client information page");
              $("#myModal").modal('show');
            }

          // clear the form
          form.classList.remove('was-validated');
          form.reset();
        }
      }, false);
    });
  }, false);
})();

document.getElementById("clickMe").onclick = function () {
  var clientId = getCookie("clientId");
  var gallonsRequested = $('#gallonsRequested').val();
  var deliveryDate = $('#deliveryDate').val();
  var deliveryAddress = $('#deliveryAddress').val();
  var deliveryCity = $('#deliveryCity').val();
  var deliveryState = $('#deliveryState').val();
  var deliveryZipCode = $('#deliveryZipCode').val();
  var deliveryContactPersonName = $('#deliveryContactPersonName').val();
  var deliveryContactPersonPhone = $('#deliveryContactPersonPhone').val();
  var deliveryContactPersonEmail = $('#deliveryContactPersonEmail').val();
  var suggestedPricePerGallon = $('#suggestedPricePerGallon').val();
  var totalAmountDue = $('#totalAmountDue').val();

  if (gallonsRequested != "" && deliveryState != "") {
    var currentPrice = 2.19;
    var margin = 0;
    var locationFactor = 0;
    var rateHistoryFactor = 0;
    var gallonsRequestedFactor = 0;
    var companyProfitFactor = 0.05;
    var rateFluctuation = 0.04;

    if (deliveryState == "TX") {
      locationFactor = 0.02;
    } else {
      locationFactor = 0.04;
    }

    if (quoteHistory) {
      rateHistoryFactor = 0.02;
    } else {
      rateHistoryFactor = 0.03;
    }

    if (gallonsRequested >= 1000) {
      gallonsRequestedFactor = 0.02;
    } else {
      gallonsRequestedFactor = 0.03;
    }

    var suggPrice = currentPrice + (locationFactor + rateHistoryFactor + gallonsRequestedFactor + companyProfitFactor + rateFluctuation) * currentPrice;
    console.log(suggPrice);
    var totalAmount = gallonsRequested * suggPrice;
    console.log(totalAmount);

    $('#suggestedPricePerGallon').val(suggPrice);
    $('#totalAmountDue').val(totalAmount);
  }
};