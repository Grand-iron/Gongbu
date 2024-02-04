$(document).ready(function () {
  $("#first").click(function () {
    $(this).fadeOut("slow", function () {
      $(this).hide();
    });
  });
});
