"""
This module provides unit tests for the functions in the translator module.
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    # Test for null input for english_to_french
    def test_null_input_english_to_french(self):
        self.assertEqual(english_to_french(None), None)
    
    # Test for null input for french_to_english
    def test_null_input_french_to_english(self):
        self.assertEqual(french_to_english(None), None)
    
    # Test for the translation of 'Hello' to French
    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    # Test for the translation of 'Bonjour' to English
    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    # Test for the translation of an empty string
    def test_empty_string_translation(self):
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(french_to_english(''), '')
        
    # Test for the translation of a sentence
    def test_sentence_translation(self):
        self.assertEqual(english_to_french('I am a student'), 'Je suis étudiant')
        self.assertEqual(french_to_english('Je suis étudiant'), 'I am a student')
        
if __name__ == '__main__':
    unittest.main()
