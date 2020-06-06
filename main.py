import os
import playsound
import speech_recognition as sr
from gtts import gTTS
from googleScrapper import searcher


breakLi = ['quit', 'stop']


def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = 'voice{}.mp3'.format(n)
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)


def getAudio():
	r = sr.Recognizer()
	with sr.Microphone() as src:
		audio = r.listen(src)
		said = ''

		try:
			said = r.recognize_google(audio)
			if str(said).strip() not in breakLi:
				print(f'{n+1})', said)
		except Exception as e:
			if str(e).strip()=='':
				return getAudio()
			else:
				print('Exception:', e)

	return said

n=0
print('Ask Questions!!')
while True:
	s = getAudio()
	if s.strip() in breakLi:
		print('Hope u come back Soon :)')
		speak('Hope u come back Soon')
		break
	else:
		ans = searcher(s)
		print()
		print('Answer:')
		print(ans)
		speak(ans)
		print()
	n+=1
