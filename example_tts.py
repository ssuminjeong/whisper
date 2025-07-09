import pyttsx3

text = "안녕하세요, 텍스트를 음성으로 바꾸기 테스트 중입니다."

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 속도 조절
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yuna')  # 한국어 음성
engine.say(text)  
# engine.save_to_file(text, 'output_tts.mp3')
engine.runAndWait()

print("텍스트가 음성으로 변환되어 'output_tts.mp3' 파일로 저장.")