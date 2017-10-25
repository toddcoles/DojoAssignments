$(document).ready(function() {
    // var pokedirect = "https://pokeapi.co/api/v2/pokemon/16";
    // $.get(pokedirect, function(data){
    //     console.log(data);
    //     $(".wrapper").append(data);
    //     }, "json");


        for (var x = 1; x < 152; x++) {
            $('.wrapper').append(`<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/${x}.png">`) 
          }

});