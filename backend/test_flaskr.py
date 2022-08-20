import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_user = 'student'
        self.database_password = 'student'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(self.database_user, self.database_password, '127.0.0.1:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # new question
        self.new_question = {
            "question": "test question",
            "answer": "test answer",
            "difficulty": 2,
            "category": 1,
        }    
        
        # new invalid question
        self.new_invalid_question = {
            "question": None,
            "answer": "",
            "difficulty": 2,
            "category": 1,
        }    
        
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """
        Tests retrieve categories
    """
    def test_retrieve_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertGreaterEqual(len(data["categories"]), 1)
        self.assertIsInstance(data['categories'], list)
        
    def test_405_sent_requesting_categories(self):
        res = self.client().post('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
        Tests retrieve questions
    """
    def test_retrieve_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
        self.assertIsInstance(data['questions'], list)
        self.assertGreaterEqual(data['total_questions'], 1)

        self.assertEqual(data['current_category'], None)
        self.assertGreaterEqual(len(data['categories']), 1)
        self.assertIsInstance(data['categories'], list)
        
    def test_404_sent_requesting_questions(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
    """
        Tests create question
    """
    def test_create_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        last_question = Question.query.order_by(self.db.desc(Question.id)).first()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['created'], last_question.id)
        
    def test_400_create_question(self):
        res = self.client().post('/questions', json=self.new_invalid_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')
        
    """
        Tests delete question
    """
    def test_delete_question(self):
        last_question = Question.query.order_by(self.db.desc(Question.id)).first()
        
        res = self.client().delete('/questions/' + str(last_question.id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], last_question.id)

    def test_404_send_invalid_id_for_delete_question(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
    """
        Tests search questions
    """
    def test_search_questions_with_results(self):
        last_question = Question.query.order_by(self.db.desc(Question.id)).first()
        
        res = self.client().post('/questions/search', json={'searchTerm': last_question.question})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)
        self.assertGreaterEqual(data['total_questions'], 1)
        self.assertEqual(data['current_category'], None)
        
    def test_search_questions_without_results(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'no-results-test'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)
        self.assertGreaterEqual(data['total_questions'], 0)
        self.assertEqual(data['current_category'], None)

    """
        Tests retrieve questions by category
    """
    def test_retrieve_questions_by_category(self):
        category = Category.query.order_by(self.db.desc(Category.id)).first()
        nbre_questions = Question.query.filter(Question.category == category.id).count()
        
        res = self.client().get('/categories/' + str(category.id) + '/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)
        self.assertEqual(data['total_questions'], nbre_questions)
        self.assertEqual(data['current_category'], category.id)

    def test_404_send_category_without_questions(self):
        category = Category.query.order_by(self.db.desc(Category.id)).first()
        res = self.client().get('/categories/' + str(category.id + 1) + '/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
    """
        Tests quizzes
    """
    def test_quizzes_without_category_and_without_previous_questions(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'type': 'All', 'id': 0}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['question'], dict)
        
    def test_quizzes_with_category_and_without_previous_questions(self):
        category = Category.query.first()
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'id': category.id, 'type': category.type}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertIsInstance(data['question'], dict)
        
    def test_quizzes_with_category_and_with_previous_questions(self):
        res = self.client().post('/quizzes', json={
            'previous_questions': [13, 14],
            'quiz_category': {
                'id': 3,
                'type': 'Geography'
            }
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertIsInstance(data['question'], dict)
        
    def test_quizzes_with_category_and_with_all_the_previous_questions(self):
        res = self.client().post('/quizzes', json={
            'previous_questions': [13, 14, 15],
            'quiz_category': {
                'id': 3,
                'type': 'Geography'
            }
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['question'], None)
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()