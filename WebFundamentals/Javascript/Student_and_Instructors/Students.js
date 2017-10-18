var students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
]

for(var names in students){
    console.log(students[names].first_name, students[names].last_name);
}
console.log('');

var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }


console.log('Students');
    
        for(var x = 0; x < users.Students.length; x++){
            var str = '';
            var str = (users.Students[x].first_name + users.Students[x].last_name);
            var count = 0;
            
            for (var i = 0, len = str.length; i < len; i++) {
                if (str[i] !== ' ')
                    count++;
            }
            console.log(x+1 + ' - ' + users.Students[x].first_name, users.Students[x].last_name+ ' - '+ count);
        }
        console.log('');
        console.log('Instructors');

        for(var x = 0; x < users.Instructors.length; x++){
            var str = '';
            var str = (users.Instructors[x].first_name + users.Instructors[x].last_name);
            var count = 0;
            
            for (var i = 0, len = str.length; i < len; i++) {
                if (str[i] !== ' ')
                    count++;
            }
            console.log(x+1 + ' - ' + users.Instructors[x].first_name, users.Instructors[x].last_name+ ' - '+ count);
        }
    
