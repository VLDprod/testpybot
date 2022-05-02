import logging
# import telebot
import random
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
import configparser
import os
import speech_recognition as sr
import random
import time
import playsound
from gtts import gTTS




# from telebot import types

help = "Пока что нету хэлпов"


API_TOKEN = "hyjgftyjjyjtfyjo"



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



def command():

    r = sr.Recognizer()

  
    with sr.Microphone() as source:
      
        print("Говорите")
     
        r.pause_threshold = 1
     
        r.adjust_for_ambient_noise(source, duration=1)
      
        audio = r.listen(source)

    try: 
       
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        # Просто отображаем текст что сказал пользователь
        #await bot.send_message(message.chat.id, "!: " + zadanie)
    # Если не смогли распознать текст, то будет вызвана эта ошибка
    except sr.UnknownValueError:
        # Здесь просто проговариваем слова "Я вас не поняла"
        # и вызываем снова функцию command() для
        # получения текста от пользователя
        
        zadanie = command()

    # В конце функции возвращаем текст задания
    # или же повторный вызов функции
    return zadanie

def say_message(zadanie):
    voice = gTTS(zadanie, lang="ru")
    file_voice_name = "_audio"+str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("gs: " + zadanie)


def makeSomething(zadanie):
   
    if 'админ панель' in zadanie:
    	say_message("молодец")
    else:
    	async def send_welcom33e(message: types.Message):
    		await bot.send_message(message.chat.id, "!: " + zadanie)





@dp.message_handler(content_types=['text'])
#@auth
async def send_welcome(message: types.Message):
	#await bot.forward_message(message.chat.id, )
	print(message.message_id)
	say_message(message.text)
	await bot.send_message(message.chat.id, message.text)




import os
import time
import asyncio

#apihelper.SESSION_TIME_TO_LIVE= 1 * 60

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)




