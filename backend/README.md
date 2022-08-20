
# Backend - Trivia API

This API is part of my training on UDACITY, and allows employees and students to play by answering questions.

The purpose of this application is to enable learners to have practical skills to configure and test APIs.

#### The functionalities covered by the API are :

1. Show questions - all questions and by category. Questions should display the default question, category, and difficulty level and can show or hide the answer.
2. Delete questions.
3. Add questions with their answer.
4. Search questions from a query text string.
5. Play by answering questions from a specific category or all categories.


## Getting started
To work with this project, you must know python precisely the FLASK framework

### Configuration for local development

#### Install depencies

1. **Python >= 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

Using the Postgres command line to create a `trivia` database by running the following command:

```bash
CREATE DATABASE trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

Default URL should be http://127.0.0.1:5000/

### Testing
Tests are not required to run the API. But if you contribute, please run the tests before pushing to GitHub.

Using the Postgres command line to create a `trivia_test` database by running the following command:

```bash
CREATE DATABASE trivia_test
```
Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia_test < trivia.psql
```

First make sure you are working with your virtual environment and run the tests with the following command:
```bash
python test_flaskr.py
```
## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:

```bash
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return one of the errors below on requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error

#### Endpoints

#### Get available categories
```http
  GET /categories
```
- General: returns a available categories, success value. If no category exists, a 404 error is returned
- Sample: ```bash curl http://127.0.0.1:5000/categories ```

```bash
  {
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "success": true
}
```

#### Get questions
```http
  GET /questions?page={page}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page`      | `int` | **Optional**. number of page |

- General: returns a list of categories, current category, questions, success value and total number of questions. If no question exists, a 404 error is returned
- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions `

```bash
  {
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "current_category": null,
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 19
}
```

#### Delete question

```http
  DELETE /questions/{question_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `question_id`      | `int` | **Required**. Id of question to delete |

- General: delete the question of the given ID if it exists. Returns the id of the deleted question, success value. If ID does not exist a 404 error is returned
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/1`
```bash
{
    "deleted": 2,
    "success": true
}
```


#### Create question

```http
  POST /questions
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `question`      | `string` | **Required**. Text of question |
| `answer`      | `string` | **Required**. Answer of question |
| `difficulty`      | `int` | **Required**. Difficulty of question |
| `category`      | `int` | **Required**. Category ID of question |

- General: Create a new question using the submitted parameters. Returns the id of the created question and success value. 
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"question": "How long in minutes does a football match last", "answer": "90 minutes", "difficulty": 3, "category": 6}' http://127.0.0.1:5000/questions `
```bash
{
  "created": 39,
  "success": true
}
```

#### Search questions

```http
  POST /questions/search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `searchTerm`      | `string` | **Required**. Search term |

- General: search for questions that include some of the search terms. Returns list of questions, current category, success value and total number of questions. 
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "How long in minutes"}' http://127.0.0.1:5000/questions/search `
```bash
{
    "current_category": null,
    "questions": [
        {
            "answer": "90 minutes",
            "category": 6,
            "difficulty": 3,
            "id": 39,
            "question": "How long in minutes does a football match last"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

#### Get category questions

```http
  GET /categories/{category_id}/questions
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category_id`      | `int` | **Required**. Id of category|

- General: Returns list of questions, current category ID, success value and total number of questions. If category_id does not exist a 404 error is returned 
- Sample: `curl http://127.0.0.1:5000/categories/6/questions`
```bash
{
    "current_category": 6,
    "questions": [
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "90 minutes",
            "category": 6,
            "difficulty": 3,
            "id": 39,
            "question": "How long in minutes does a football match last"
        }
    ],
    "success": true,
    "total_questions": 3
}
```

#### Get questions to play the quiz

```http
  POST /quizzes
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `quiz_category`      | `json object` | **Required**. json object that contains category ID and type|
| `previous_questions`      | `list` | **Required**. list contains previously answered questions|

- General: Returns a random question to answer and success value. 
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "All", "id": 0}}' http://127.0.0.1:5000/quizzes `
```bash
{
    "question": {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
    },
    "success": true
}
```


## Authors
This project is the result of the work of the Udacity team and me.

The base of the project was made by the Udacity team and I made corrections to make it work

- [Udacity](https://www.udacity.com/)
- [Bakary FOFANA](https://github.com/FOFANA12)

## Acknowledgements

 - [Udacity](https://www.udacity.com/) 
