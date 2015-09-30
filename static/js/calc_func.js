var num = [];
var num_sec = [];
var action = "";
var result = 0;
var output = "";
var theEnd = false;

function GetResult(num1, num2, action){
    switch(action){
        case '+':
            return (num1 + num2);
        case '-':
            return (num1 - num2);
        case '/':
            if(num2 == 0){
                return 0;
            }else{
                return (num1 / num2);
            }
        case '*':
            return (num1 * num2);
    }
};

function ClearAll(){
    result = 0;
    action = "";
    num = [];
    num_sec = [];
    document.getElementById('state').value = 0;
    output = "";
    theEnd = false;
};

document.addEventListener("DOMContentLoaded", function(){
    var elemArray = document.getElementsByClassName("set_value");

    Array.prototype.forEach.call(elemArray, function(el){
        el.onclick = function(){
        console.log(theEnd);
        console.log(action);

        if(theEnd && action == "="){
            ClearAll();
        }
            if(action == ""){
                num.push(el.childNodes[1].textContent);
                console.log(num);
                output = num.join("");
                document.getElementById('state').value = output;
            }else{
                if(result != 0){
                    num.push(result);
                    document.getElementById('state').value = num.join("");
                }
                num_sec.push(el.childNodes[1].textContent);
                console.log(num_sec);
                output += num_sec.join("");
                document.getElementById('state').value = output;
            }
        }
        });
    });

function DoIt(){
    if(num.length == 0 && num_sec.length == 0){
        result = 0;
    }else{
        result = GetResult(parseFloat(num.join("")),
         parseFloat(num_sec.join("")), action);
    }
    document.getElementById('state').value = result;
    action = "=";
    theEnd = true;
    num = []; num_sec = [];
};

function SetAction(id){
    action = id;
    output += action.toString();
    theEnd = false;
    document.getElementById('state').value = output;
};
