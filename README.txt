This is a Dockerized app.
The app downloads Movie Posters to its MongoDB database and then displays it to the user in his web browser.

Important Notice:
**** I have manualy uploaded the Secrets.py file whcih contains my APi key for you to test the app *****
*** Keys should never be uploaded to a repository

WorkFlow :

movie name is requested in browser ---> The flask web server activates the TMDBdownloader----> TMDB downloader searchers the movie name in the TMDB database --->
----> the TMDBdownloader activates The MongoAPI ----> MongoAPI downloads the poster to myapp's MongoDB -----> MongoAPI retrieves the poster from MongoDB
and displays it to the user.


How to use:

* clone the Docker-Flask-Mongo-App repository
* run Docker-compose -f mongo-server.yaml up -d
* got to your web browser and go to "localhost:5000/search" url
* Enter movie name and submit
* Movie Will be displayed

