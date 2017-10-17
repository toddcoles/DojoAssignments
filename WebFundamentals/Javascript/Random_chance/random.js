function currencyFormat (num) {
    return "$" + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
}

function pickNumber(){
    // document.getElementById("finalNumber").innerHTML = document.getElementById("myNum").innerHTML;
    var randNum = Math.floor((Math.random()*50)+50);
    document.getElementById("finalNumber").innerHTML = document.getElementById("quarters").innerHTML;
    document.getElementById("randNumber").innerHTML = randNum; //Math.floor((Math.random()*50)+50);

    // var newNum = Number(document.getElementById("quarters").innerHTML) - Number(document.getElementById("randNumber").innerHTML);
    // document.getElementById("quarters").innerHTML = newNum;
    // document.getElementById("quarters").innerHTML = Number(document.getElementById("randNumber").innerHTML) - Number(document.getElementById("quarters").innerHTML);

    if(Number(document.getElementById("myNum1").value) == randNum){ //document.getElementById("randNumber").innerHTML){
        var newNum = Number(document.getElementById("quarters").innerHTML) + Number(document.getElementById("randNumber").innerHTML);
        document.getElementById("quarters").innerHTML = newNum;
        document.getElementById("randNumber").style.backgroundColor = "green";
    } else {
        var newNum = Number(document.getElementById("quarters").innerHTML) - Number(document.getElementById("randNumber").innerHTML);
        document.getElementById("quarters").innerHTML = newNum;
        document.getElementById("randNumber").style.backgroundColor = "red";
    }

    // var results = +document.getElementById("quarters").value;
    document.getElementById("dollars").innerHTML = currencyFormat(Number(document.getElementById("quarters").innerHTML)*.25);
    
}

