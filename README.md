# Movie Studio App

 In this app, we are trying to show you the movies with actors on it, so you can have better information about what actors are involved in this movie, what are the upcoming movies, and how many one of them is still acting in the new releases of the movies. However, you will get more infomation about the cinema world from this app.
 
 ## URL for the API (Base URL)
  Our API is hosted live via Heroku
 ```bash
http://myfinal-145454.herokuapp.com
 ```
  ## Getting Started
  To get started, make a new directory `movie_studio` for the project files, `cd` to the project directory and make a [`virtual environment`](https://docs.python.org/3/library/venv.html), you should install the dependencies of this application, prepare the local development, and follow the hosting instructions.
  
  ### Dependencies
  
 - Python-3.8 and above.
 - VS code editor (or any code editer).
 - heroku cli.
 - git.
 - PostgreSQL.
 
 And for the python packages, you can get them from the `requirements.txt` file in the project directory. You can install them all using the following command:
 
 ```
  pip3 install -r requirements.txt
 ```
  
  You can see your python packages using the following commands:
  ```
  pip3 freeze
  ```
  
  after installing the dependencies, you should change a few things in the files to match your settings and configurations:
  - `DATABASE_URL, AUTH0_DOMAIN, CLIENT_ID` in setup.sh file.
  
  after you finish, you can run the app locally (in the project directory) using:
  ```
  python3 app.py
  ```
 - BUT you will have to setup Auth0 account to start using the application or testing it.
 
 
## Authentication Login URL
 
 There are three predefined users I have prepared for you, you can use them to login into Auth0 and test the RBAC, they are different based on the Role. However, you have to logout to test the other user.
 
#### Login Info:
 
 - Assistant:
   - email: assistant@gmail.com
   - password: Admin123
 - Director:
   - email: director@gmail.com
   - password: Admin123
 - Producer:
   - email: producer@gmail.com
   - password: Admin123

Each role have some permissions, see the following:

 - Assistant: 
   - Can view movies and actors
     - `get:actors`
     - `get:movies`
 
 - Director: 
   - All permissions a Casting Assistant has, Add or Delete actor, and modify actors or movies
     - `get:actors`
     - `get:movies`
     - `post:actors`
     - `delete:actors`
     - `patch:movies`
     - `patch:actors`
     
 - Director: 
   - All permissions a Casting Director has and Add or delete a movie from the database
     - `get:actors`
     - `get:movies`
     - `post:actors`
     - `delete:actors`
     - `patch:movies`
     - `patch:actors`
     - `delete:movies`
     - `post:movies`
 
 
 
 #### Login URL using Auth0
```bash
https://zshinoz.us.auth0.com/authorize?audience=movieStudioAPI&response_type=token&client_id=MMD81FKcgD0Mzek7TNCP6l2Tw7QVNVOC&redirect_uri=http://localhost:8080/login-results
```
 
 ### After Login
  After login, copy the access_token from url arguments, you will need it to test or use an API endpoint properly.
 
 Example of an access_token:
 ```
 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkliYkQ4THBuOGZYdy1PYkN4bWZOZSJ9.eyJpc3MiOiJodHRwczovL3pzaGlub3oudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzM2E2NTA0ZmY2N2ZmYTVhNWVhYzNlNSIsImF1ZCI6Im1vdmllU3R1ZGlvQVBJIiwiaWF0IjoxNjY0Nzc2MjQ2LCJleHAiOjE2NjQ3ODM0NDYsImF6cCI6Ik1NRDgxRktjZ0QwTXplazdUTkNQNmwyVHc3UVZOVk9DIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ZT6tl-ybulM0nFMpJ2nEJiWv43RXC_nPnGF16s0qGetcfN3w0t8DF7AYvfzBedTf3n63QNXDNYUH1PssQ9YCNTPiqGW8t_jThLdsRsmW5iC8kExz27i5enESDuDq8LxVq42l54k2QB2oZz4tQ4SGwsl7nxPp9vQgQV2_rZPWTZo4euonTYMLTKYiCw2svDDsdfMC4lMTeUNimcEdJdxLJWGGyxr9u9Smgb3ZqxEoTfkJwa8FuK_47jTJTYJzUmjgNNMMfGXClGIG4eiD3WlZheryLQziQWcPV3gWM2I262II4HN0mVISUGWLxydzsrPxjYFZweOCwtyR-DEIfDk3yw
 ```
 
 `NOTE`: you can go to [`jwt.io`](https://jwt.io/) website to see the content of this token.
 
  
 
 ## Hosting Instructions
 
 We are using Heroku to host our application and its DB. However, you can install Heroku CLI to start using it properly through the following commands:
 ```bash
 # Install, if Heroku as Standalone
curl https://cli-assets.heroku.com/install.sh | sh
# Or, use Homebrew on Mac
brew tap heroku/brew && brew install heroku
# Verify the installation
heroku --version
# Verify the download
which heroku
 ```
 
 Once you have the Heroku CLI installed, you can login using Heroku commands:
  ```bash
heroku login -i
 ```
 
 - You can setup Environment variables in Heroku through (you will need this later)
 `Heroku dashboard >> Particular App >> Settings >> Reveal Config Vars section`
 And you will have the access to the env variables in Heroku.
 
 - ### Migrations
 
 install the following dependencies if you haven't already!
 ```bash
 pip install Flask-Script==2.0.6
pip install Flask-Migrate==2.7.0
pip install psycopg2-binary==2.9.1
 ```
 
 then, you should run the following commands to setup the DB & Migrations on Heroku:
 ```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
 ```
 
 
 ## API Endpoints
 
 There are several API endpoints in this application, and it's 8 endpoints in total but it's kind of repeated between two entities which is Movie and Actor.
 
### GET /movies
- Description: retrieve all the movies ordered by id.
- Results are paginated in groups of 10, include a request argument to choose page number (start from 1)

#### JSON Response body
```bash
{
  "movies": formatted_movies,
  "total_movies": len(Movie.query.all()),
}
```
#### Attributes
+ `movies`: paginated movies list that is ordered by id (groups of 10).
+ `total_movies`: the number of current movies.

----------------------------------------------------------------------------------------------------------------------

### POST /movies
- Description: create a new movie object.

#### Request JSON body:
+ `title`: the title of the movie.
+ `release_date`: the release date of the movie.

#### JSON Response body
```bash
{
  "id": new_movie.id,
  "movies": formatted_movies,
  "total_movies": len(Movie.query.all()),
}
```

#### Attributes
+ `id`: indicate the id of the new created movie.
+ `movies`: paginated movies list that is ordered by id (groups of 10).
+ `total_movies`: the number of current movies.

----------------------------------------------------------------------------------------------------------------------

### DELETE /movies/{movie_id}
- Description: delete an existing movie object based on the id.
- `movie_id`: `request argument` that indicates the movie id with the type `int`.

#### JSON Response body (Delete an existing book)
```bash
{
  "deleted": movie_id,
  "success": True,
}
```

#### Attributes
+ `deleted`: indicate the id of the deleted movie.
+ `success`: indicate the success or failure of the request.

----------------------------------------------------------------------------------------------------------------------

### PATCH /movies
- Description: update the information of an existing movie object with the attribute value from the JSON request body.

#### Request JSON body:
+ `id`: the id of the movie.
+ `title`: the title of the movie.
+ `release_date`: the release date of the movie.

#### JSON Response body
```bash
{
  "updated_movie": movie.format(),
  "success": True,
}
```

#### Attributes
+ `updated_movie`: indicate the updated movie information.
+ `success`: indicate the success or failure of the request.

----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------

### GET /actors
- Description: retrieve all the actors ordered by id.
- Results are paginated in groups of 20, include a request argument to choose page number (start from 1)

#### JSON Response body
```bash
{
  "actors": formatted_actors,
  "total_actors": len(Actor.query.all()),
}
```
#### Attributes
+ `actors`: paginated actors list that is ordered by id (groups of 20).
+ `total_actors`: the number of current actors.

----------------------------------------------------------------------------------------------------------------------

### POST /actors
- Description: create a new actor object.

#### Request JSON body:
+ `name`: the name of the actor.
+ `age`: the age of the actor.
+ `gender`: the gender of the actor.

#### JSON Response body
```bash
{
  "id": new_actor.id,
  "name": new_actor.name,
  "actors": formatted_actors,
  "total_actors": len(Actor.query.all()),
}
```

#### Attributes
+ `id`: indicate the id of the new created actor.
+ `name`: indicate the name of the new created actor.
+ `actors`: paginated actors list that is ordered by id (groups of 20).
+ `total_actors`: the number of current actors.

----------------------------------------------------------------------------------------------------------------------

### DELETE /actors/{actor_id}
- Description: delete an existing actor object based on the id.
- `actor_id`: `request argument` that indicates the actor id with the type `int`.

#### JSON Response body
```bash
{
  "deleted": actor_id,
  "success": True,
}
```

#### Attributes
+ `deleted`: indicate the id of the deleted actor.
+ `success`: indicate the success or failure of the request.

----------------------------------------------------------------------------------------------------------------------

### PATCH /actors
- Description: update the information of an existing actor object with the attribute value from the JSON request body.

#### Request JSON body:
+ `id`: the id of the actor.
+ `name`: the name of the actor.
+ `age`: the age of the actor.
+ `gender`: the gender of the actor.

#### JSON Response body
```bash
{
  "updated_actor": actor.format(),
  "success": True,
}
```

#### Attributes
+ `updated_actor`: indicate the updated actor information.
+ `success`: indicate the success or failure of the request.

----------------------------------------------------------------------------------------------------------------------
 
 ## Error Handling

In our app, uses conventional JSON objects to indicate the success or failure of an API request. It will return json response with a body that have the following attributes:
- `error`: indicate the HTTP status code.
- `message`: indicate a short description for the error type.
- `success`: indicate the success or the failure of the request.

#### Error Types:

 - ##### Not Found (404)

 - ##### Method Not Allowed (405)

 - ##### Unprocessable (422)

 - ##### Bad Request (400)

 - ##### Internal Server Error (500)
 - ##### Auth Error (AuthError)

 
 ----------------------------------------------------------------------------------------------------------------------
 
  ## Testing
  
  We are doing the testing using Postman Collection, this collection have:
  - One test for success behavior of each endpoint
  - One test for error behavior of each endpoint
  - At least two tests of RBAC for each role
  
  In order to test the application properly, a collection of tests have been added to the project repository to be imported using Postman.

 ### Postman testing
 
 JSON file is included in the project repository, and by following the steps below you will be able to test the application's functionalities:
 - Open `Postman` program.
 - Go to `Collections` tab.
 - Click on `Import` button.
 - Select the JSON file.
 - Run the tests.
 
 #### NOTE
 
 + You may have to change the request body or argument in some tests because some of the IDs (either for actors or movies) may not be found.
 + Check the following tests to make sure there's nothing wrong with the test arguments or body:
   - DELETE movies - Correct (see the request argument).
   - DELETE actors - Correct (see the request argument).
   - PATCH movies - Correct (see the request body).
   - PATCH actors - Correct (see the request body).
 
