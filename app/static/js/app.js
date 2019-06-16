$('nav a').click(function(e){
    e.preventDefault();
    var id = $(this).attr('href'),
        targetOffset = $(id).offset();
    $('html, body').animate({
        scrollTop: targetOffset
    }, 500);    
});