$(document).ready(function() {
// alert("test");
    // $('button').click(function(){
    //     console.log("first one clicked...");
    //     var newFname = $('input[name="fName"]').val();
    //     var newLname = $('input[name="lName"]').val();
    //     var newDesc = $('input[name="description"]').val();
       
    //     $('.main_content').append("<div class='inside_content'>"+newFname+'<br>'+newLname+'<br>'+newDesc+'</div>' );
    //     console.log(newFname + ' ' + newLname + ' ' + newDesc);
       
    // });

$(document).on('click', 'button', function(){
    var newFname = $('input[name="fName"]').val();
    var newLname = $('input[name="lName"]').val();
    var newDesc = $('textarea[name="description"]').val();
   
    $('.main_content').append('<div class="inside_content"><strong> First Name:</strong>' + newFname + 
    '<br><strong> Last Name:</strong>' + newLname + 
    '<br><span class="show_desc">Show description...</span><span class="descrip_hide"><br> <strong>Description:</strong> ' + newDesc + 
    '</span></div>' );
    return false;
});

$(document).on('click', '.show_desc', function(){
    $(this).siblings().toggleClass('descrip_show');
    if($(this).text() == "Show description..."){
        $(this).text("Hide description...");
        $(this).css("background-color", "red");
    }else{
        $(this).text("Show description...");
        $(this).css("background-color", "green");
        }
});


});