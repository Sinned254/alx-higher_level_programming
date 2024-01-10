/**
 * 2-script.js: Changes the color of the div#red_header to red when
 * the user clicks on it.
 */
// Wait for the document to be ready
$(document).ready(function () {
  // Attach a click event handler to the DIV#red_header element
  $('div#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
