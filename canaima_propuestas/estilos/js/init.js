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
