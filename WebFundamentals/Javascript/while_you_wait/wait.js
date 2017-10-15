   

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear();
    var date1 = (mm + '/' + dd + '/' + yyyy);
    var newdate = today.getDate() + 1;
   
    var bday = new Date('12/08/2017');
    var bday_dd = bday.getDate();
    var bday_mm = bday.getMonth()+1;
    var bday_yyyy = bday.getFullYear();
    var mybday = (bday_mm + '/' + bday_dd + '/' + bday_yyyy);
    
    var oneDay = 24*60*60*1000; // one day
    var firstDate = new Date(yyyy, mm, dd); //today's date
    var secondDate = new Date(bday_yyyy, bday_mm, bday_dd); //birth date
    
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));

    console.log('Today\'s date is: ',date1);
    console.log('My birthday is: ', mybday);
    console.log(diffDays, 'days left!');

    var y = diffDays-1;

    for(var x = 1; x < diffDays; x++){
        
        switch(mm){
            case 0:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 1:
            if(dd>=28){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 2:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 3:
            if(dd>=30){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 4:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 5:
            if(dd>=30){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 6:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 7:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 8:
            if(dd>=30){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 9:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 10:
            if(dd>=31){
                mm=mm+1;
                dd=0;
                break;
            }
            
            case 11:
            if(dd>=30){
                mm=mm+1;
                dd=0;
                break;
            }
            
           
        }

        dd=dd+1;
        y=y-1;


        if(x<=diffDays-5){
            console.log('It\'s ' + mm + '/' + dd + '/' + yyyy + ' and there are still ' + y + ' days left until my birthday!');
                        } else{
                            if(y == 0){
                                console.log('It\'s my birthday!!!');
                                console.log(mm + '/' + dd + '/' + yyyy);
                                console.log('HAPPY BIRTHDAY TO ME!!!');
                            }else{
            console.log('It\'s ' + mm + '/' + dd + '/' + yyyy + ' and there are only', y + ' days left!');}
                        }
                       
    }



    