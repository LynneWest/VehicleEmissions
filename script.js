$(window).load(function()
{	
	var scrollPosition;
	var headerHeight;	

	function getHeaderHeight() //return header height
	{
		headerHeight = $('header').outerHeight();		
			
			return headerHeight;	
	}	

	$(document).scroll(function() 
	{
		scrollPosition = $(document).scrollTop();	
		var navH = $(".navbar").height();
		
		if(getHeaderHeight()-scrollPosition <= navH) //darken navbar when it gets past header image
		{
			$(".navbar").addClass("scroll-nav");									
		}
		else //remove background color when navbar is above bottom of header image
		{
			$(".navbar").removeClass("scroll-nav");			
		}
	});

	$(window).resize(function() //get header height when window is resized
	{
		getHeaderHeight()	
	});
});
	

