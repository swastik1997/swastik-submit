var username;

function getUsername()
{
	var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data = xhr.responseText;
            makeUsername(data);
            getAlbumList(data);
        }
    }
    xhr.open('GET', '../username/', true);
    xhr.send(null);
}

function makeUsername(data)
{
	var temp=JSON.parse(data);
	document.getElementById('username').innerHTML=temp.username;
    var x=document.getElementById('profile');
    x.setAttribute('src',temp.profilepic);
}

function getAlbumList(data)
{
    var temp=JSON.parse(data);
    username=temp.username;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data1 = xhr.responseText;
            makeAlbumList(data1,temp.username);
        }
    }
    xhr.open('GET', '../'+temp.username+'/', true);
    xhr.send(null);
}

function editUser(){
    window.location="http://127.0.0.1:8000/PhotoDrive/home/editUser/?username="+username;
}

function createAlbum(){
    window.location="http://127.0.0.1:8000/PhotoDrive/home/createAlbum/?username="+username;
}

function makeAlbumList(data,username)
{
    var c=document.getElementById('albums');
    var temp=JSON.parse(data);
    var editButton=document.getElementById('editUser');
    var createAlbumButton=document.getElementById('createAlbum');
    editButton.addEventListener("click", editUser);
    createAlbumButton.addEventListener("click", createAlbum);
    var albumTitle=document.getElementById('albumTitle');
    if(temp.length==null || temp.length==0)
    {
        albumTitle.innerHTML="No albums found";
    }
    else
    {
        var ttag = document.createElement('tr');
        for(var i=0;i<temp.length;i++)
        {
            var tdTag= document.createElement('td');
            var aTag = document.createElement('a');
            date = new Date(temp[i].date);
            aTag.innerHTML = date.getFullYear()+'-' + (date.getMonth()+1) + '-'+date.getDate();
            tdTag.appendChild(aTag);
            ttag.appendChild(tdTag);
        }
        c.appendChild(ttag);
        ttag = document.createElement('tr');
        for(var i=0;i<temp.length;i++)
        {
            var tdTag= document.createElement('td');
            var aTag = document.createElement('img');
            aTag.setAttribute('src',temp[i].cover);
            aTag.setAttribute('height',200);
            aTag.setAttribute('width',225);
            tdTag.appendChild(aTag);
            ttag.appendChild(tdTag);
        }
        c.appendChild(ttag);
        ttag = document.createElement('tr');
        for(var i=0;i<temp.length;i++)
        {
            var tdTag= document.createElement('td');
            var aTag = document.createElement('a');
            aTag.setAttribute('href',"album/?albumId="+temp[i].album_id);
            aTag.innerHTML = temp[i].description;
            tdTag.appendChild(aTag);
            ttag.appendChild(tdTag);
        }
        c.appendChild(ttag);
        ttag = document.createElement('tr');
        for(var i=0;i<temp.length;i++)
        {
            var tdTag= document.createElement('td');
            var aTag = document.createElement('a');
            var likedBy="liked by -";
            for(var j=0;j<temp[i].liked.length;j++){
                likedBy+=temp[i].liked[j]+",";
            }
            if (temp[i].liked.length==0)
                likedBy+="NO ONE";
            aTag.innerHTML = likedBy;
            tdTag.appendChild(aTag);
            ttag.appendChild(tdTag);
        }
        c.appendChild(ttag);
    }
}
