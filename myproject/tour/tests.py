from django.test import TestCase
from .models import Author, Tour


class TestAuthorModel(TestCase):
    
    @classmethod
    def setUp(cls): # funkcjonalność wywoływana przed każdym testem
        Author.objects.create(first_name='Jan', last_name='Kowalski')        
        cls.jan = Author.objects.get(first_name='Jan', last_name='Kowalski')
        cls.new_author = Author(first_name='Jan', last_name='Kowalski')
    
    @classmethod
    def tearDownClass(cls):
        del cls.jan, cls.new_author
    
    def test_initialization(self):
        self.assertTrue(self.new_author)
    
    def test_full_name_of_author(self):
        self.assertEqual(self.new_author.full_name(), 'Jan Kowalski', msg='Full name should be consists of the first name and last name.')
    
    def test_string_representation(self):
        self.assertEqual(str(self.jan), 'Jan Kowalski')


class TestTourModel(TestCase):
    
    @classmethod
    def setUp(cls):
        cls.tour = Tour()
    
    @classmethod
    def tearDownClass(cls):
        del cls.tour
    
    def test_tour_creation(self):
        self.assertTrue(isinstance(self.tour, Tour))
    
    def test_initialization(self):
        self.assertTrue(self.tour)
    
    def test_tour_string_representation(self):
        self.assertEqual(str(self.tour), f"{str(self.tour.date)} {self.tour.author}")
