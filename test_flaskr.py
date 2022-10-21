import os
import unittest
import json
from urllib import response as resp
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'abc')
DB_NAME = os.getenv('DB_NAME', 'test_movies_studio')
DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = DB_NAME
        self.database_path = DB_PATH
        setup_db(self.app, self.database_path)

        # Temp Objects
        self.new_question = {
            "question": "Say my name!",
            "answer": "Shino",
            "difficulty": "1", "category": "3"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Write at least one test for each test
    for successful operation and for expected errors.
    """

    def test_get_movies_with_no_auth(self):
        res = self.client().get("/movies")

        # get the jwt token
        auth = res.headers.get("Authorization")
        data = json.loads(res.data)

        self.assertEqual(auth, None)
        self.assertEqual(data["status_code"], 401)
        self.assertFalse(data["success"])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
