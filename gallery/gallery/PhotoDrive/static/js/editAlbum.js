var username,albumId;

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
            getUserlist(data);
        }
    }
    xhr.open('GET', '../../usernamealbum/'+albumId+'/', true);
    xhr.send(null);
}

function getUserlist(data1)
{
	var temp=JSON.parse(data1);
    username=temp.username;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data = xhr.responseText;
            setUsername(data);
        }
    }
    xhr.open('GET', '../../', true);
    xhr.send(null);
}

function setUsername(data)
{
	var temp=JSON.parse(data);
    var editAlbum=document.getElementById('editAlbum');
    var visible=document.getElementById('visible');
    editAlbum.setAttribute('action',"/PhotoDrive/"+username+"/"+albumId+"/edit/");
    var visibleTo=document.getElementById('visibleTo');
    for(var i=0;i<temp.length;i++){
    	var option = document.createElement("option");
    	option.text = temp[i].username;
    	option.setAttribute('value',temp[i].username);
    	visibleTo.add(option);
    }
}
