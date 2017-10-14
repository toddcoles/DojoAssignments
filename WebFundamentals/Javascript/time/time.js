
    var hour = 8;
    var minute = 24;
    var period = 'PM';
    
    var myPeriod = '';
    if(period == 'AM'){
        myPeriod = 'morning';
    } else{
        myPeriod = 'afternoon';
    }

    if(minute > 30){
        console.log('It\'s almost', hour + 1, 'o\'clock in the ', myPeriod);
    } else {
        console.log('It\'s a bit after', hour, 'o\'clock in the ', myPeriod);
    }

    var date = new Date();
    var time = date.getTime();

    var minutes = 1000*60;
    var hours = minutes*60;
    var days = hours*24;
    var years = days*365;
    
    var y = Math.round(time/days);
    console.log('Number of years since 1 Jan 1970 is ',y/365);

    console.log('Time:', time);

  
    // console.log('Period: ', myPeriod);
    