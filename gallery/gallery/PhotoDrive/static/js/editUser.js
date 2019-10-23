function getUrlVars() { 
    var vars = {}; 
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) { vars[key] = value; });
    return vars; 
}

function setUsername()
{
	var username=getUrlVars()['username'];
    var albumCreate=document.getElementById('editUser');
    albumCreate.setAttribute('action',"/PhotoDrive/"+username+"/edit/");
}