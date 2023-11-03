import os
import openai
from googletrans import Translator

openai.api_key = "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"
audio_file = open(r"C:\Users\Hannan\Desktop\text to speech\i-want-to-work-2.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file, response_format="text")
print("Original transcript in english")
print(transcript)
translator = Translator()
translated_text = translator.translate(transcript, src="en", dest="ur")
print("\nTranslated Transcript (Urdu):")
print(translated_text.text)