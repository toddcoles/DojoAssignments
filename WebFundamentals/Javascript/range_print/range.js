function printRange(first, last, interval){
    x=0;

        if(first>last){    
        for(var x = first; x > last; x-=interval){
        console.log(x);}  
                      }  

            for(var x = first; x < last; x + interval){
            console.log(x);
            x=x+interval;
            }
    console.log(' ');
}

printRange(-5,20,2);

printRange(40,1,5);
