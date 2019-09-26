$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (_, val) {
    $('#list_movies').append('<li>' + val.title + '</li>');
  });
});
