document.addEventListener('DOMContentLoaded', function () {
  function langu () {
    const lng = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lng;
    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(langu);
  $('#language_code').keydown(function (e) {
    if (e.which === 13) {
      langu();
    }
  });
});
