document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(function (e) {
    e.preventDefault();
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function (e) {
    e.preventDefault();
    $('.my_list li').last().remove();
  });
  $('#clear_list').click(function (e) {
    e.preventDefault();
    $('.my_list li').remove();
  });
});
