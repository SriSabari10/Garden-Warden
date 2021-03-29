function ValidateEmail(inputText)
{
var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
if(inputText.value.match(mailformat))
{
alert("Valid email address!");
const aa=document.getElementById("email").value;
return true;
}
else
{
alert("You have entered an invalid email address!");
const bb=document.getElementById("email").value;
return false;
}
}