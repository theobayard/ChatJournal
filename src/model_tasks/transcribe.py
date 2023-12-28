from openai import OpenAI

def transcribe(input_file_path, client: OpenAI = OpenAI()):
    with open(input_file_path, "rb") as audio_file:
        return client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format="text",
            language='en'
        )
    