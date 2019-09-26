document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    const lng = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lng;
    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
