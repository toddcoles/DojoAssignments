$(document).ready(function() {

        var APIkey = '2c3f125fc613625b6f805f6a262add06';
        var location = '';
        var weatherURL = 'http://api.openweathermap.org/data/2.5/weather?q=';// + location + '&&appid=' + APIkey;

        $('form').submit(function(){
            var location = $('#location').val();
       
        $.get(weatherURL + location + '&&appid=' + APIkey, function(weatherResult){
            console.log(weatherResult);
            var newTemp = (1.8 * (weatherResult.main.temp - 273)) + 32;
        $('#temp').html(`<h1>${weatherResult.name}</h1><h2>Temperature: ${newTemp.toFixed(2)} F</h2>`);
        }, 'json');
        return false;

    });
});