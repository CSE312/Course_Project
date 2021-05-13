CSE 312 Project
------

This application does the following things
1) Has secure authentication. This entails registration, login, and changing profile details.
2) Sharing multimedia. This is currently accomplished via uploading profile pictures and having it be visible to all users.
3) Having the ability to see all logged in users. You will be able to see all users logged when you are logged in. In addition, you will also be able to see all signed up users.
4) Sending Direct Messages. This includes the abaility to 'contact' a member, and send them a private message that will appear in their inbox.

Features going to be implemented:

1) Live interactions

## Docker Compose Instructions
1) Change the directory to the root directory Course_Project.
   >`cd Course_Project`

2) Build the image
   >`docker-compose build`
   
3) Run docker compose
   >`docker-compose up --detach`

4) Migrate database
   >`docker-compose run web python manage.py migrate`

5) Open http://localhost:8000/
   >`http://localhost:8000`
 [If nothing pops up on locahost:8000, please run step 3 again.]

6) (OPTIONAL) Once you are done with testing the database and web application, delete the docker composer.
   >`docker-compose down`
   

