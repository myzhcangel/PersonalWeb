$(function () {
	$("#collapse-button").blur(function (event) {
		setTimeout(function () {
			var screenWidth = window.innerWidth;
			if(screenWidth < 768) {
				$("#navbarSupportedContent").collapse("hide");
			}
		}, 100);		
	});
});