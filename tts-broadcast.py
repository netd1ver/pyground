from gtts import gTTS
from playsound import playsound 
from datetime import datetime
import schedule
import time

text = '''
임직원 여러분 점심 시간입니다. 
오전 내내 일하시느라 고생하셨습니다. 
구내 식당에 맛있는 점심을 준비해놨으니 식사하러 이동하세요.
'''

tts = gTTS(text, lang='ko')
tts.save('tts_audio.mp3')


def broadcast():
    now = datetime.now()
    print(now, "방송시작!")
    print(text)
    # # # playsound exits with an error
    # # # okay to play the mp3 with vlc player
    # playsound('tts_audio.mp3')


b_time = input("Enter the time of broadcast (ex. 13:10): ")

schedule.every().day.at(b_time).do(broadcast)

while True:
    schedule.run_pending()
    time.sleep(1)
