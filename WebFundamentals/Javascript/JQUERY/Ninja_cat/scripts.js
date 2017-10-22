$(document).ready(function() {

$('.ninja').click(function(){
$(this).toggleClass('cat ninja');
    });

$('.ninja1').click(function(){
$(this).toggleClass('cat1 ninja1');
    });

$('.ninja2').click(function(){
$(this).toggleClass('cat2 ninja2');
    });

$('.ninja3').click(function(){
$(this).toggleClass('cat3 ninja3');
    });

$('.ninja4').click(function(){
$(this).toggleClass('cat4 ninja4');
    });
                

$('img').click(function() {
    console.log('data-alt-src value is', $(this).attr('data-alt-src'));
  });


});