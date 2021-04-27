CSE 312 Project
------

This application does the following things
1) Has secure authentication. This entails registration, login, and changing profile details.
2) Sharing multimedia. This is currently accomplished via uploading profile pictures and having it be visible to all users.
3) Having the ability to see all logged in users. You will be able to see all users logged when you are logged in. In addition, you will also be able to see all signed up users.

Features going to be implemented:
1) Sending Direct Messages
2) Live interactions

## Docker Compose Instructions
1) Change the directory to the root directory Course_Project.
   >`cd Course_Project`

2) Build the image
   >`docker-compose build`
   
3) Run docker compose
   >`docker-compose up --detach`

4) Open http://localhost:8000/
   >`http://localhost:8000`
 [If nothing pops up on localhost:8000, please run step 3 again. If nothing continues to pop up, please run step 5, and run steps 2 and 3 again]

5) (OPTIONAL) Once you are done with testing the database and web application, delete the docker composer.
   >`docker-compose down`
   
## Side Note
This is a Django application and it is currently deployed on a Heroku server.

**Link to site:**
https://cse312-web-project.herokuapp.com/
