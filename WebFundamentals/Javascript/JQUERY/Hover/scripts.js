$(document).ready(function() {

$('#svx').hover(function(){
$('#svx').attr('src', 'Sevilla_white.png');
},
function(){
$('#svx').attr('src', 'Sevilla_red.png');
});


$('#fcb').hover(function(){
    $('#fcb').attr('src', 'Barca_back.jpg');
    },
    function(){
    $('#fcb').attr('src', 'Barca_front.jpg');
    });


$('#usa').hover(function(){
    $('#usa').attr('src', 'usa_back.png');
    },
    function(){
    $('#usa').attr('src', 'usa_front.png');
    });

$('#rm').hover(function(){
    $('#rm').attr('src', 'RM_back.jpg');
    },
    function(){
    $('#rm').attr('src', 'RM_front.jpg');
    });

});