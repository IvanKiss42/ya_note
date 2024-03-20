from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from notes.models import Note


User = get_user_model()


class TestNoteList(TestCase):
    NOTES_URL = reverse('notes:list')

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Заметочник')
        cls.reader = User.objects.create(username='Ценитель заметок')
        cls.auth_client = Client()
        cls.auth_client.force_login(cls.author)
        cls.authors_note = Note.objects.create(
            title='Заголовок',
            text='Текст',
            author=cls.author,
            slug='slug'
        )

    def test_note_is_on_the_list(self):
        response = self.auth_client.get(self.NOTES_URL)
        object_list = response.context['object_list']
        self.assertTrue(self.authors_note in object_list)

    def test_form_at_add_and_edit_pages(self):
        for name, args in (
            ('notes:edit', (self.authors_note.slug,)),
            ('notes:add', None)
        ):
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.auth_client.get(url)
                self.assertIn('form', response.context)

    def test_only_right_notes_on_the_list(self):
        response = self.auth_client.get(self.NOTES_URL)
        object_list = response.context['object_list']
        all_authors = [note.author for note in object_list
                       if note.author != self.author]
        self.assertEqual(len(all_authors), 0,
                         'Заметки видны не только своим авторам')
