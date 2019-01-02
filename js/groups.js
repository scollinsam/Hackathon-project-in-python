$(document).ready(function(){
    $.ajax({
    type: "GET",
    url: "/set_input",
    contentType: "application/json"
}).done(function (data) {
    $("#groups").empty();
    var groups = JSON.stringify(data);
    $("#groups").text(groups)
})  ;
})
