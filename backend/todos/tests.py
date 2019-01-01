from django.test import TestCase

from .models import Todo

# Create your tests here.
class TodoModelCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Initial todo')
        Todo.objects.create(description='Learning react')
    
    def test_todo_title(self):
        todo = Todo.objects.get(id=1)
        expect = f'{todo.title}'
        self.assertEquals(expect, 'Initial todo')

    def test_todo_description(self):
        todo = Todo.objects.get(id=2)
        expect = f'{todo.description}'
        self.assertEquals(expect, 'Learning react')

