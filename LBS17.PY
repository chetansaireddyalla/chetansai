import speech_recognition as sr

#record audio
r = sr.Recognizer()
with sr.microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("say something!")
	audio = r.listen(source)

# speech recognition using google speech recognition
try:
	# for testing purposes, we're just using the default api key
	# to use another api key, use r.recognise_google(audio, key="google_speech_recognition_api_key")
	# instead of 'r.recognise_google(audio)'
	print("you said: " + r.recognise_google(audio))
except sr.UnknownValueError:
	print("google speech Recognition could not understand audio")
except sr.RequestError as e:
PRINT("cloud not request results from google speech recognition service; {0}" ,format(e))