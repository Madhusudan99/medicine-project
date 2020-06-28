from doctor.models import Drug, Prescription_direction_frequency_count, Prescription_direction_day_week_month
import speech_recognition as sr

class Find:
	def drug(self, word):
		try:
			return Drug.objects.get(drug_name__startswith=word)
		except:
			return False
	def prescription_direction_frequency_count(self, word):
		try:
			return Prescription_direction_frequency_count.objects.get(frequency_count__startswith=word)
		except:
			return False
	def prescription_direction_day_week_month(self, word):
		try:
			return Prescription_direction_day_week_month.objects.get(day_week_month__startswith=word)
		except:
			return False


class Text_to_speech:

	def __init__(self):	
		self.r = sr.Recognizer()
		self.mic = sr.Microphone()
		with self.mic as self.source:
			print("Please be in a quite enviroment")
			print("Wait for a seconds and then speek 'Hello' into the microphone and wait for 1-2 seconds.... ")
			print("This will adjust the ambient noise")
			self.audio = self.r.adjust_for_ambient_noise(self.source, duration=8)
			print("Done")

	def run_tts(self):
		with self.mic as self.source:
			print("Speek Now")
			self.audio = self.r.listen(self.source,timeout=5, phrase_time_limit=15)

		print("Running speech recognition engine....")

		try:
			self.generated_text = self.r.recognize_google(self.audio)
			print(self.generated_text)
			return self.generated_text
		except sr.RequestError:
			return "API was unreachable or unresponsive"
		except sr.UnknownValueError:
			return "Unable to recognize speech, speech was unintelligible"
		except sr.WaitTimeoutError:
			return "A WaitTimeoutError has occurred this happened probably because either there was no input given to the microphone or the microphone was not detected"

		
# tts_object = Text_to_speech()

# print(tts_object.print_tts())








class Get_formated_prescription_data:
	def __init__(self, input_text):
		self.input_text = input_text
		self.find = Find()
		for self.word in self.input_text.split():
			if self.find.drug(self.word) != False:
				self.drug_name = self.find.drug(self.word).drug_name

			elif self.find.prescription_direction_frequency_count(self.word) != False:
				self.frequency_count = self.find.prescription_direction_frequency_count(self.word).frequency_count

			elif self.find.prescription_direction_day_week_month(self.word) != False:
				self.day_week_month = self.find.prescription_direction_day_week_month(self.word).day_week_month

	def print_data(self):
		print('Drug: ', self.drug_name)
		print('Frequency: ', self.frequency_count)
		print('Days/Weeks/Month: ', self.day_week_month)

