$(document).ready(function() {

$('div').click(function(){
$(this).hide("slow");
});

$('#myButton').click(function(){
$('div').show("slow");
});

});