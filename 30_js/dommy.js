var changeHeading = function(e){
    var h = document.getElementById("h");
    h.innerHTML = 'REPLACE';
};

var removeItem = function(e){
    //REPLACE
};

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++){
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeading);
    //lis[i].addEventListener('click', ???)
}

/*

var addItem = function(e){
    var list = ???;
    var item = document.createElement("li");
    q?? = "WORD";
    //STUFF HERE
    list.???(item);
};

var button = document.getElementsById("b");
button.addEventListener('click', addItem);

var fib = function(n){
    if(n < 2){
	return 1;
    }
    else{
	return fib(n-1) + fib(n-1)
    }
};

var addFib() = function(e){
    console.log(e)
    //INSERT STUFF HERE
};
	
var addFib2 = function(e){
    console.log(e);
    //INSERT STUFF HERE, THIS ONE IS DYNAMIC PROGRAMMING (SEE QAF)
};

var fb = document.getElementsById('fb');
fb.addEventListener("click", addFib);


/*
// THE THINGS WE DID TOGETHER IN CLASS
var title = document.getElementById("thelist");
title.addEventListener('mouseover', function(e){console.log(e);});


var button = document.getElementById("b");
button.addEventListener('click',function(e){ console.log(e);});

var button2 = document.getElementById("fb");
button2.addEventListener('click',function(e){ console.log(e);});
*/
