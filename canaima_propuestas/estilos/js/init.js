(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$('#js-captcha-refresh').click(function(){

	var $form = $(this).parents('form');
	var url = location.protocol + "//" + window.location.hostname + ":"
                    + location.port + "/captcha/refresh/";

		// Make the AJAX-call
	$.getJSON(url, {}, function (json) {
	$form.find('input[name="captcha_0"]').val(json.key);
	$form.find('img.captcha').attr('src', json.image_url);
	});

	return false;
});


$(document).ready(function() {
  $('#id_tipo_doc').bind('change', function(e) {
    if ($('#id_tipo_doc').val() == 'USU') {
      $("#caso_usuario").show();
      $("#caso_desarrollador").hide();
      $("#caso_otro").hide();
    } else if ($('#id_tipo_doc').val() == 'DEV') {
      $("#caso_usuario").hide();
      $("#caso_desarrollador").show();
      $("#caso_otro").hide();
    } else if ($('#id_tipo_doc').val() == 'OTRO') {
      $("#caso_usuario").hide();
      $("#caso_desarrollador").hide();
      $("#caso_otro").show();
    }
  }).trigger('change');

});