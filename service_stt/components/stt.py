import speech_recognition as sr



class Stt:
    def __init__(self,logger):
        self.recognizer = sr.Recognizer()
        self.logger = logger


    def conversion_to_text(self,file_audio):
        with sr.AudioFile(file_audio) as source:
            audio_data = self.recognizer.record(source)

        try:
            text = self.recognizer.recognize_google(audio_data)
            self.logger.info(f'3️⃣I was able to convert it to text')
            return text

        except sr.UnknownValueError:
            self.logger.error("3️⃣Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            self.logger.error(f"3️⃣Could not request results from service; {e}")




