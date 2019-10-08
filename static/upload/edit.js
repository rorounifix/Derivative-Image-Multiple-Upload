$(function() {
		$('.pop').on('click', function() {
      window.open(location.origin + $(this).attr('src'))
		});
});
