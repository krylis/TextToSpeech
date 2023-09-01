import os
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\cmcsh\OneDrive\Desktop\Google API\days-of-code-397702-3bbdf2c60dbb.json"

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text="Wassup freak bitches!")

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
