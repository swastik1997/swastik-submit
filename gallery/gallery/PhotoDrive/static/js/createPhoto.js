var albumId,username;

function getUrlVars() { 
    var vars = {}; 
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) { vars[key] = value; });
    return vars; 
}

function getUsername()
{
	albumId=getUrlVars()['albumId'];
	var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data = xhr.responseText;
            setUsername(data);
        }
    }
    xhr.open('GET', '../../usernamealbum/'+albumId+'/', true);
    xhr.send(null);
}

function setUsername(data)
{
	var temp=JSON.parse(data);
    username=temp.username;
    var albumCreate=document.getElementById('albumCreate');
    albumCreate.setAttribute('action',"/PhotoDrive/"+username+"/"+albumId+"/create/");
}