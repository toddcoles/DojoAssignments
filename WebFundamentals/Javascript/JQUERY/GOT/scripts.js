$(document).ready(function() {

        var gotURL = 'https://anapioficeandfire.com/api/houses/';
       
        for(var x = 1; x <= 12; x++){
            console.log(x);
            $.get(gotURL + x, function(gotResult){
            $('.wrapper').append(`<div class='boxes'><div class='line'></div><h3 id=${x}>${gotResult.name}</h3></div>`);
            }, 'json');
        };
        
        $(document).on('click', '.title', function(){
            var myid = $(this).attr('id');
            console.log('https://anapioficeandfire.com/api/houses/' + myid);
            $.get(gotURL + myid, function(final){
                $('#gotDescription').html(`<h4>Name:</h4>${final.name}<h4>Words:</h4>${final.words}<h4>Titles:</h4>${final.titles}`);
            });
            
        });
});