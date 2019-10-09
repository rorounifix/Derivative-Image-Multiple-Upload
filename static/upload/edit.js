$(function() {
		$('.pop').on('click', function() {
      window.open(location.origin + $(this).attr('src'))
		});
});

$('#modal-content').modal('show')
