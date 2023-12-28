import os
from pathlib import Path

from src.model_tasks.transcribe import transcribe 
from src.settings import Settings

def process_all_recordings():
    for recording_file_path in get_unprocessed_recordings():
        recording_file_path = Path(recording_file_path)
        transcript = process_recording(recording_file_path.resolve())
        save_transcript(recording_file_path.stem, transcript)

def process_recording(recording_path):
    # TODO: Add summary section, title, Obsidian links, etc
    return transcribe(recording_path)

def save_transcript(transcript_name, transcript):
    file_name = f"{Settings.transcript_location()}/{transcript_name}.md"
    
    with open(file_name, 'w') as file:
        file.write(transcript)

def get_unprocessed_recordings() -> list[str]:
    processed_stems = map(lambda file_name: Path(file_name).stem, get_processed_recordings())
    return [
        recording for recording in get_all_recordings()
        if Path(recording).stem not in processed_stems
    ]


def get_processed_recordings() -> list[str]:
    return [
        os.path.join(Settings.transcript_location(), file_name) 
        for file_name in os.listdir(Settings.transcript_location())
    ]


def get_all_recordings() -> list[str]:
    return [
        os.path.join(Settings.recordings_location(), file_name) 
        for file_name in os.listdir(Settings.recordings_location())
    ]
