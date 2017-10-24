$(document).ready(function() {

$('form').submit(function(){
    var newFname = $('input[name="fName"]').val();
    var newLname = $('input[name="lName"]').val();
    var newEmail = $('input[name="email"]').val();
    var newContact = $('input[name="contact"]').val();
    $('table').append('<tr><td>'+newFname+'</td><td>'+newLname+'</td><td>'+newEmail+'</td><td>'+newContact+'</td></tr>' );

    return false;
})

});