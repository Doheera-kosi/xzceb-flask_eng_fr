"""
This module provides functions for 
translating text using the IBM Watson
Language Translator API.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

# Set up the authentication for the Watson Language Translator API
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version='2021-05-01', authenticator=authenticator)

# Set the service URL for the Watson Language Translator API
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        english_text (str): The English text to translate.

    Returns:
        str: The translated French text, or None if the input text is None or empty.
    """
    if english_text is None:
        return None

    if len(english_text.strip()) == 0:
        return ''

    # Use the Language Translator to translate English to French
    translation_response = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract the translated text and return it
    french_text = translation_response['translations'][0]['translation'].strip()
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        french_text (str): The French text to translate.

    Returns:
        str: The translated English text, or None if the input text is None.
    """
    if french_text is None:
        return None

    if len(french_text.strip()) == 0:
        return ''

    # Use the Watson Language Translator service to translate the French text to English
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Return the translated English text
    english_text = translation['translations'][0]['translation'].strip()
    return english_text
