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
            # self.logger.info(f'I was able to convert it to text')
            return text

        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")










from mongo_gridFs import x


# audio_file = "C:/podcasts/download (33).wav"
# audio_file_2 = "C:/podcasts/download (4).wav"
#
# s = Stt('ss')
# print(s.conversion_to_text(x))


