$(document).ready(function(){
    $.ajax({
    type: "GET",
    url: "/set_input",
    contentType: "application/json"
}).done(function (data) {
    $("#groupslist").empty();
    $("#groupslist").append($("<ul/>"));
    var groups =JSON.parse(data);
    groups.forEach(function (element) {
    var group = $("<ul/>")
    var cat = $("<li/>")
    cat.text(element.category)
    group.append(cat)
    var addr =  $("<li/>")
    addr.text(element.address)
    group.append(addr)
    var dist = $("<li/>")
    dist.text(element.distance)
    group.append(dist)
    var hours = $("<li/>")
    hours.text(element.hours)
    group.append(hours)
    $("#groupslist").append(group)})
})  ;
})
