function ValidateEmail()
{
    console.log('validate called');
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const aa=document.getElementById("email").value;
    const bb=document.getElementById("pass").value;
    if(value.match(mailformat))
    {
        alert("Valid email address!");
        
      return true;
    }
    else
    {
    alert("You have entered an invalid email address!");
    
    return false;
    }
}