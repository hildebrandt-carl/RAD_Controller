// client
var s = require('net').Socket();

s.connect(4242,'160.119.248.176');

s.write('web');

var i = 0;

s.on('data', function(d){
    console.log(d.toString());
    i = i + 1;
    if(i==1)
    {
        console.log("sending first message");
        s.write('firstMessage');
    }

    if(i==2)
    {
        console.log("sending second message");
        s.write('secondMessage');
    }

    if(i >= 3)
    {
        s.end();
    }

});