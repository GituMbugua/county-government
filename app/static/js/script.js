$(window).scroll(function(){
    if($(document).scrollTop()>10){
        $('nav').addClass("shrink");
    }else{
        $('nav').removeClass('shrink');
    }
});
$('.carousel').carousel();
