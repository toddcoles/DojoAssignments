$(document).ready(function() {

        for (var x = 1; x < 152; x++) {
            $('.poke').append(`<img id=${x} src="https://pokeapi.co/media/sprites/pokemon/${x}.png">`) 
          }
        
          $('img').click(function(){
            var id = $(this).attr('id');
            $.get("https://pokeapi.co/api/v2/pokemon/" + id +"/", function(response){
            console.log(response);
            var pokeID = response.id;
            var myString +=`
            <div class='inside_pic'>
            <img src='https://pokeapi.co/media/sprites/pokemon/${pokeID}.png'>
            <h2>${response.name}</h2>
            Types <ul>`
            for(var x = 0; x <= response.types.length){
              myString+=`<li>${response.types[x].name}</li>`;
            }
              
            myString+=`<h3>Height: 
            </h3>${response.height}
            <h3>Weight: </h3>${response.weight}
            </div>`);
            $('.side').html(myString);
            }, "json");
        })

});