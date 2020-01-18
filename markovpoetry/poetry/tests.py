from django.test import TestCase

from poetry.poetry import generate_sentence


class TestPoetrySentenceGeneration(TestCase):
    def test_sentence(self):
        generate_sentence()
