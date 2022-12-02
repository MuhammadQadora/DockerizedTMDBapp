*** STILL WORKING ON IMPROVING THE APP *****
This is a Dockerized app.
The app downloads Movie Posters to its MongoDB database and then displays it to the user in his web browser.


WorkFlow :

movie name is requested in browser ---> The flask web server activates the TMDBdownloader----> TMDB downloader searchers the movie name in the TMDB database --->
----> the TMDBdownloader activates The MongoAPI ----> MongoAPI downloads the poster to myapp's MongoDB -----> MongoAPI retrieves the poster from MongoDB
and displays it to the user.

- To get your own API:
  * go to https://www.themoviedb.org/
  * Rigester an account
  * go to your profile --> Settings --> API --> request new API

How to use:

* clone the Docker-Flask-Mongo-App repository
* run Docker-compose -f mongo-server.yaml up -d
* got to your web browser and go to "localhost:5000/search" url
* Enter movie name and submit
* Movie Will be displayed

