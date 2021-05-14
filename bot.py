import telebot as tb
import random
import difflib
import time
import datetime


def sravnen(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    matcher = difflib.SequenceMatcher(None, str1, str2)
    return matcher.ratio()


string_stack = []
with open("files/fraze.txt","r",encoding="UTF-8") as f:
    string_stack = f.read().split("v")

imgs_stack = []
with open("files/link_img.txt", "r",encoding="UTF-8") as f:
    imgs_stack = f.read().split("\n")

img_night_stack = []
with open("files/link_img_night.txt", "r",encoding="UTF-8") as f:
    img_night_stack = f.read().split("\n")

stack = []
with open("files/all_peoples.txt", "r",encoding="UTF-8") as f:
    stack = f.read().split()
print(stack)

bot = tb.AsyncTeleBot("1781324497:AAG3WAkzs_dwSG9zoQDUguJbWSV_h1R9Mdc")

for i in stack:
    pikch = imgs_stack[random.randrange(0, len(imgs_stack))]
    bot.send_message(int(i), "Солнышко, я тебя очень сильно люблю. Будь всегда такой же прекарсной и неповторимой. Никогда не грусти, и будь позитивной. Люблю тебя.❤️")
    bot.send_photo(int(i), pikch)
print("Бот запущен!")
@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if str(message.from_user.id) not in stack:
        with open("files/all_peoples.txt", "a") as f:
            f.write(" "+str(message.from_user.id))
    if message.text == 'я тебя люблю' or message.text == "Я тебя люблю":
        print(message.text)
        bot.send_message(message.from_user.id, "Я тебя тоже люблю")
    elif sravnen(message.text, "Спокойной ночки") > 0.70:
        print(message.text)
        bot.send_message(message.from_user.id, "Спокойной ночки, зайчик")
        bot.send_photo(message.from_user.id,
                    img_night_stack[random.randrange(0, len(img_night_stack))])
    elif message.text == "Спасибо" or message.text == "спасибо":
        print(message.text)
        bot.send_message(message.from_user.id,
                        "Пожалуйста солнышко, я на все ради тебя готов")
    elif message.text == "Расскажи мне пожалуйста все" or message.text == "расскажи мне пожалуйста все" or message.text == "Расскажи мне пожалуйста всё" or message.text == "расскажи мне пожалуйста всё":
        print(message.text)
        bot.send_message(message.from_user.id, ". ".join(stack))
    elif sravnen(message.text, "Хочу пикча")>0.60 or sravnen(message.text, "Хочу пикчу")>0.60:
        print(message.text)
        pikch = imgs_stack[random.randrange(0, len(imgs_stack))]
        bot.send_message(message.from_user.id, "Лови, солнышко")
        bot.send_photo(message.from_user.id,pikch)
    elif sravnen(message.text, "Поздравить с днем рождения") > 0.70:
        pikch = imgs_stack[random.randrange(0, len(imgs_stack))]
        bot.send_message(1204114004,"С днём рождения солнышко, желаю тебе всего самого наилучшего, чтобы твои мечты всегда сбывались, ты была здоровенькая, и никогда не грустила. Люблю тебя!")
    elif message.text == "Команды" or message.text == "команды":
        print(message.text)
        bot.send_message(
            message.from_user.id, 'Солнышко, я могу тебе показать лишь что я знаю, просто напши мне "Расскажи мне пожалуйста все"')
    else:
        print(message.text)
        bot.send_message(message.from_user.id,
                        string_stack[random.randrange(0, len(string_stack))])
bot.polling(none_stop=True, interval=0)

