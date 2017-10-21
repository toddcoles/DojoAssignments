$(document).ready(function() {

    $('.click').click(function(){
        alert("You have clicked a button!");
     });

     $('.hide').click(function(){
        $('.first').hide('slow');
     });

     $('.show').click(function(){
        $('.first').show('slow');
     });

     $('.toggle').click(function(){
        $('.first').toggle('slow');
     });

     $('.slidedown').click(function(){
        $('.first').slideDown('slow');
     });
     
     $('.slideup').click(function(){
        $('.first').slideUp('slow');
     });
     
     $('.slidetoggle').click(function(){
         $('.first').slideToggle('slow');
        });
        
     $('.fadeIn').click(function(){
        $('.first').fadeIn('slow');
     });

     $('.fadeOut').click(function(){
        $('.first').fadeOut('slow');
     });

     $('.addClass').click(function(){
        $('.first').addClass('first_in');
     });

     $('.removeClass').click(function(){
        $('.first').removeClass('first_in');
     });

     $('.before').click(function(){
        $('.first').before('This is added before the div');
     });

     $('.after').click(function(){
        $('.first').after('This is added after the div');
     });

     $('.append').click(function(){
        $('.first').append('This is added within the div.');
     });

     $('.html').click(function(){
        $('.first').append('This is <b>HTML </b>added within the div.');
     });

     $('.attr').click(function(){
        $('#checker').attr('checked', true);
     });


     function selectValues() {
     var mySelection = $('#theSelector').val();
     $( "#selection" ).html( "<b>Picked:</b> " + mySelection);
     };

     $( "#theSelector" ).change( selectValues );
     selectValues();

     $('.text').click(function(){
        $('.second').text('This is text!!!');
     });



     $(".attachData").click(function(){
        $("div").data("greeting", "This data is attached now!");
    });
    $(".showData").click(function(){
        alert($("div").data("greeting"));
    });
     
});