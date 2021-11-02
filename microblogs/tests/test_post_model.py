"""Unit test for the User model."""
from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import Post


class PostModelTestCase(TestCase):
    """Unit tests for the User model."""
    def setUp(self):
        self.post= Post.objects.create(
            author='@johndoe',
            text='Doe',
            created_at= '2018-11-20T15:58:44.767594-06:00'
        )

    def test_valid_post(self):
        self.assert_post_is_valid()

    def test_author_cannot_be_blank(self):
        self.post.author=''
        self.assert_user_is_invalid()

    def test_author_must_exist_as_user(self):
        pass

    def test_text_cannot_be_over__280_characters_long(self):
        self.post.text = 'x' * 281
        self.assert_user_is_invalid()


    def assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()
