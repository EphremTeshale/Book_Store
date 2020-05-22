# books/tests.py

from django.test import TestCase,Client
from django.urls import reverse

from .models import Book

class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='ፍቅር እስከመቃብር',
            author='Haddis Alemayehu',
            price='100.00',
        )
    
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}','ፍቅር እስከመቃብር')
        self.assertEqual(f'{self.book.author}','Haddis Alemayehu')
        self.assertEqual(f'{self.book.price}','100.00')
    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'ፍቅር እስከመቃብር')
        self.assertTemplateUsed(response,'books/book_list.html')
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/1234/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'ፍቅር እስከመቃብር')
        self.assertTemplateUsed(response,'books/book_detail.html')
