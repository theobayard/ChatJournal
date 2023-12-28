import json


class Settings:
    @staticmethod
    def settings():
        with open('settings.json') as settings_file:
            return json.load(settings_file)
        
    @staticmethod
    def recordings_location() -> str:
        return Settings.settings()['recordings_location']

    @staticmethod
    def transcript_location() -> str:
        return Settings.settings()['transcript_location']