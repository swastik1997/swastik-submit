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
            getPhotoList(data);
        }
    }
    xhr.open('GET', '../../usernamealbum/'+albumId+'/', true);
    xhr.send(null);
}

function getPhotoList(data)
{
    var temp=JSON.parse(data);
    var xhr = new XMLHttpRequest();
    username=temp.username;
    xhr.onreadystatechange = function() 
    {
        if (xhr.readyState == 4) 
        {
            var data1 = xhr.responseText;
            isOwner(data1,albumId,temp.username);
        }
    }
    xhr.open('GET', '../../'+temp.username+'/'+albumId+'/', true);
    xhr.send(null);
}

function isOwner(data,albumId,username){
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == 4) 
        {
			var owner = xhr.responseText;
			makePhotoList(data,albumId,username,owner);
		}
	}
    xhr.open('GET', "../album/"+username+"/", true);
    xhr.send(null);
}

function likeAlbum(){
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function(){}
    xhr.open('GET', "../../"+username+"/"+albumId+"/like/", true);
    xhr.send(null);
}

function editAlbum(){
	window.location="http://127.0.0.1:8000/PhotoDrive/home/editAlbum/?albumId="+albumId;
}

function deleteAlbum(){
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == 4) 
        {
			window.location="http://127.0.0.1:8000/PhotoDrive/home";
		}
	}
    xhr.open('DELETE', "../../"+username+"/"+albumId+"/delete/", true);
    xhr.send(null);
}

function createPhoto(){
    window.location="http://127.0.0.1:8000/PhotoDrive/home/createPhoto/?albumId="+albumId;
}

function makePhotoList(data,albumId,username,owner){
	var c=document.getElementById('photos');
	var likeButton=document.getElementById('likeAlbum');
	var per=JSON.parse(owner);
	var editButton=document.getElementById('editAlbum');
	var deleteButton=document.getElementById('deleteAlbum');
	var createPhotoButton=document.getElementById('createPhoto');
    if (per.bool=="false"){
        editButton.style.visibility = "hidden";
        deleteButton.style.visibility = "hidden";
        createPhotoButton.style.visibility = "hidden";
    }
    console.log(data);
	var temp=JSON.parse(data);
	var photoTitle=document.getElementById('photoTitle');
	likeButton.addEventListener("click", likeAlbum);
	editButton.addEventListener("click", editAlbum);
	deleteButton.addEventListener("click", deleteAlbum);
	createPhotoButton.addEventListener("click", createPhoto);
    if(temp.length==null || temp.length==0)
    {
        photoTitle.innerHTML="No photos found";
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
            aTag.setAttribute('src',temp[i].photo);
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
            aTag.setAttribute('href',"../photo/?photoId="+temp[i].photo_id);
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










