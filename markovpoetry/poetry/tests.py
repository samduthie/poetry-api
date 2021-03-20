from django.test import TestCase

from poetry.poetry import generate_sentence


class TestPoetrySentenceGeneration(TestCase):
    def test_sentence_contains_more_than_one_character(self):
        sentence = generate_sentence()
        self.assertTrue(len(sentence > 1))
