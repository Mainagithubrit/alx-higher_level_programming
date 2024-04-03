// a JavaScript script that adds a
// <li> element to a list when the user
// clicks on the tag DIV#add_item

$('DIV#add_item').click(function () {
  $('UL.my.List').append('<li>Item</li>');
});
