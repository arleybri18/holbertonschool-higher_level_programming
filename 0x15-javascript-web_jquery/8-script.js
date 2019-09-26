$.getJSON("https://swapi.co/api/people/5/?format=json", function (data) {
    $.each(data.films, function ( _, val) {
        $("#list_movies").append("<li>" + val + "</li>");
    });
});