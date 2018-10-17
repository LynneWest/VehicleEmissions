// Script for vehicle class emissions project

$(window).load(function()
{	
	var scrollPosition;
	var headerHeight;	

	function getHeaderHeight() //return header height
	{
		headerHeight = $('header').outerHeight();		
			
			return headerHeight;	
	}	

	function navBack()//change navbar background color based on scroll bar position
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
	}

	$(document).scroll(function() 
	{
		navBack();
	});

	$(window).resize(function() //get header height when window is resized
	{
		getHeaderHeight()	
	});

	navBack();
});
	

