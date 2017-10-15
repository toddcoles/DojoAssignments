   
function currencyFormat (num) {
    return "$" + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
}

    var reward = .01;
    var sum = 0;
    var x = 1;
    
    // while(x < 31)   //******THIS IS THE WAY TO CALCULATE THIS PROJECT WITH THE "WHILE" LOOP */
    // {
    //     // if(x==1)
    //     // {console.log(x + '--' + currencyFormat(reward) + ' is the daily amount and the running sum is:', currencyFormat(reward));}
    //     if(x==1){sum=0.01;}
    //     console.log(x + '--' + currencyFormat(reward) + ' is the daily amount and the running sum is:', currencyFormat(sum));
    //     reward=reward*2;
    //     sum = sum + reward;
    //     x++;
    // }

    // console.log('The total amount for the reward is: ', currencyFormat(sum - reward));

    for( var x = 1; x < 31; x++){   //******THIS IS THE WAY TO CALCULATE THIS PROJECT WITH THE "FOR" LOOP */
            if(x==1){sum=0.01;}
            console.log(x + ' $' + currencyFormat(reward) + ' is the daily amount and the running sum is: $', currencyFormat(sum));
            reward=reward*2;
            sum = sum + reward;
            }
            console.log('The total amount for the reward is: ', currencyFormat(sum - reward));