$(document).ready(function() {

        for (var x = 1; x < 152; x++) {
            $('.poke').append(`<img id=${x} src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/${x}.png">`) 
          }
        
          $('img').click(function(){
            var id = $(this).attr('id');
            $.get("https://pokeapi.co/api/v2/pokemon/" + id +"/", function(response){
            console.log(response);
            var pokeID = response.id;
            $('.side').append("<div class='inside_pic'><img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+ pokeID + ".png'><br><h2>" +response.name + "</h2><p> Types " + response.type + "</p><p> <h3>Height: </h3>" + response.height + "</p><p><h3>Weight: </h3>" + response.weight + "</p></div>");
            }, "json");
        })

});