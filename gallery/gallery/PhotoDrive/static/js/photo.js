var albumId,username,photoId;

function getUrlVars() { 
	var vars = {}; 
	var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) { vars[key] = value; });
	return vars; 
}

function getAlbum()
{
	photoId=getUrlVars()['photoId'];
	var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data = xhr.responseText;
            getUsername(data);
        }
    }
    xhr.open('GET', '../../usernamephoto/'+photoId+'/', true);
    xhr.send(null);
}

function getUsername(data1)
{
    var temp=JSON.parse(data1);
    albumId=temp.album_id;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data = xhr.responseText;
            getPhotoList(data);
        }
    }
    xhr.open('GET', '../../usernamealbum/'+albumId+'/', true);
    xhr.send(null);
}

function getPhotoList(data)
{
    var temp=JSON.parse(data);
    username=temp.username;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data1 = xhr.responseText;
            isOwner(data1,photoId,albumId,username);
        }
    }
    xhr.open('GET', '../../'+username+'/'+albumId+'/'+photoId+'/', true);
    xhr.send(null);
}

function isOwner(data,photoId,albumId,username){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState == 4) 
        {
            var owner = xhr.responseText;
            makePhoto(data,photoId,albumId,username,owner);
        }
    }
    xhr.open('GET', "../album/"+username+"/", true);
    xhr.send(null);
}

function likePhoto(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){}
    xhr.open('GET', "../../"+username+"/"+albumId+"/"+photoId+"/like/", true);
    xhr.send(null);
}

function editPhoto(){
    window.location="http://127.0.0.1:8000/PhotoDrive/home/editPhoto/?photoId="+photoId;
}

function deletePhoto(){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState == 4) 
        {
            window.location="http://127.0.0.1:8000/PhotoDrive/home/album/?albumId="+albumId;
        }
    }
    xhr.open('DELETE', "../../"+username+"/"+albumId+"/"+photoId+"/delete/", true);
    xhr.send(null);
}

function makePhoto(data,photoId,albumId,username,owner){
    var likeButton=document.getElementById('likePhoto');
    var temp=JSON.parse(data);
    var photoTitle=document.getElementById('photoTitle');
    var per=JSON.parse(owner);
    var editButton=document.getElementById('editPhoto');
    var deleteButton=document.getElementById('deletePhoto');
    if (per.bool=="false"){
        editButton.style.visibility = "hidden";
        deleteButton.style.visibility = "hidden";
    }
    likeButton.addEventListener("click", likePhoto);
    editButton.addEventListener("click", editPhoto);
    deleteButton.addEventListener("click", deletePhoto);
    if(temp.photo_id==null || temp.photo_id==0)
    {
        photoTitle.innerHTML="No photo found ";
    }
    else
    {
        var x=document.getElementById('photo');
        x.setAttribute('src',temp.photo);
    }
}
