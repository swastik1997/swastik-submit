Description - This is the backend of the photo gallery application in Django REST Framework with sqlite3 as database. You can do multiple operations through AJAX by hitting the desired URL and retrive data as a JSON object or you can put data according to the requirement.

How to use?



Step-1: install django.

Step-2: go to gallery/ on terminal

Step-3: activate virtualenv through "source /bin/activate" on terminal

Step-4: go to gallery/ on terminal

Step-5: run command "python manage.py makemigrations PhotoDrive"

Step-6: run command "python manage.py migrate"

Step-7: run command "python manage.py runserver"

Step-8: install XAMPP server

Step-9: put the front file on application/xampp/htdocs folder

Step-10: run the parent.html on localhost/front/parent.html



The app is running now.

URLs and there functionality-

	127.0.0.1/ :- Login page
	127.0.0.1/PhotoDrive/logout :- logout button
	127.0.0.1/PhotoDrive/ :- list all users
	127.0.0.1/PhotoDrive/create :- register user
	127.0.0.1/PhotoDrive/<username>/edit/ :- update user details
	127.0.0.1/PhotoDrive/<username>/delete/ :- delete user with all albums
	127.0.0.1/PhotoDrive/<username>/ :- list of albums visible to you
	127.0.0.1/PhotoDrive/<username>/<album_id> :- list of photos visble to you
	127.0.0.1/PhotoDrive/<username>/<album_id>/like :- like album
	127.0.0.1/PhotoDrive/<username>/create :- create album
	127.0.0.1/PhotoDrive/<username>/<album_id>/edit :- edit album
	127.0.0.1/PhotoDrive/<username>/<album_id>/delete :- delete album with all photos
	127.0.0.1/PhotoDrive/<username>/<album_id>/setvisibleto :- set album visible to which users
	127.0.0.1/PhotoDrive/<username>/<album_id>/setvisiblity :- set album visiblity which users
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/setvisibleto :- set visible to which users photo
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/like :- like photo
	127.0.0.1/PhotoDrive/<username>/<album_id>/create :- create photo
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/edit :- edit photo
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/delete :- delete photo
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/setvisibleto :- set photo visible to which users 
	127.0.0.1/PhotoDrive/<username>/<album_id>/<photo_id>/setvisiblity :- set photo visiblity which users

Drawbacks/Constraints : You have to provide set_visiblity through a number
											1 ->public
											2 ->private
											3 ->Set visiblity to particular users










