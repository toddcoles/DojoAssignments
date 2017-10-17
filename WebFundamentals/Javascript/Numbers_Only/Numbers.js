
function myNumber(){
    var myArray = new Array(1, "apple", -3, "orange", 0.5);
    var newArray = [];
        for(var x = 0; x < myArray.length; x++)
        {
            var whatIs = myArray[x];
            if(typeof myArray[x] === "number"){
                newArray.push(myArray[x]);
            } 
        }
    return newArray;
}

function removeNumbers() {
    var theArray = new Array(1, "apple", -3, "orange", 0.5);
    // var newArray2 = [];
        for(var x = 0; x < theArray.length; x++)
        {
            var whatIs = theArray[x];
            if(typeof theArray[x] === "number"){
                // console.log(theArray[x]);
                delete theArray[x];
            } 
        }
    return theArray;
}

var y = myNumber();
console.log(y);

var m = removeNumbers();
console.log(m);