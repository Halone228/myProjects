import telebot as tb
import random
import difflib
def sravnen(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    matcher = difflib.SequenceMatcher(None, str1, str2)
    return matcher.ratio()
string_stack = [
    'Я тебя люблю', 'Мое солнышко, люблю тебя', 'Котеночек обожаю тебя',
    'Кусь, люблю тебя', 'Чмоки чмоки, люблю тебя',
    "Ты моя радость, люблю тебя", 'Я готов на весь мир кричать, что я тебя люблю',
    'Как же хочется обнять тебя, Люблю солнышко', 'Смысл теряется, когда ты куда-то уходишь',
    'Какое же ты солнце', 'Вот, ты, даже не представляешь какая мы милая пара', "Такого милого зайчика я ещё не видал",
    "Какая ты красивая,а-а-а, зачем такая милая", "Я не могу перестать думать о тебе...", "Твоя улыбка самая милая"
    "Мы только попрощались, а я уже дико скучаю", "Единственное что мне нужно - это ты", "Давай будем смотреть кино и обниматься",
    "Когда нет тебя рядом — мне так пусто и одиноко. И солнце не так ярко светит, и трава не такая зеленая. Давай будем больше времени проводить вдвоем?",
    "Мне не хватает слов, чтобы выразить как я тебя люблю", "Только от одного твоего голоса мне становится тепло",
    "Я не представляю, чтобы я делал без тебя", "Дороже тебя у меня нет никого...", "Я никогда, и никому, тебя не отдам, ведь ты мое солнце",
]
imgs_stack = [
    "https://sun9-64.userapi.com/impg/W3g4acvG8-0Gl6JxQ_PkaNpcs55WaxaTOFwxpw/7PmWmEo4-fQ.jpg?size=564x564&quality=96&sign=c5bc765991231b9f24624e9d7958cdf9&type=album",
    "https://sun9-48.userapi.com/impg/TN_xDZ8mQzExHgIAqUGWm3wKNf6RmWIZiVwbRg/UHkZxfc3PPQ.jpg?size=730x730&quality=96&sign=161f97c3874cf093f88f606c45d00f0d&type=album",
    "https://sun9-56.userapi.com/impg/3yn51bHTkOC8D69mmiyIrEDBqM_VEAYqzH1uAA/JGPXfZyZE0Y.jpg?size=604x515&quality=96&sign=f223726a33e4c92098677bb66c222dce&type=album",
    "https://sun9-71.userapi.com/impg/fIm9Wk00RzzU126CHtEWYW33B7RAtiPmsKRB9w/ZYCbPXfP7Q4.jpg?size=942x1080&quality=96&sign=c3fde4cad86298cee68e5d28b86327a9&type=album",
    "https://sun9-25.userapi.com/impg/Ts17v8N3bq9uP7huMLOMNajtTEEvMJvtS4gvPA/err0bj1fVbk.jpg?size=736x460&quality=96&sign=26bf12960ae33fa7812044607f76ac96&type=album",
    "https://sun9-66.userapi.com/impg/b0QWTPf52wfHCYGqKvEK-PPKk8_qpMIQ6CRiGw/pFdCBWwB3OY.jpg?size=603x604&quality=96&sign=d81b4c0097c2e3c1f31771b7484223aa&type=album",
    "https://sun9-18.userapi.com/impg/_3-LO-_wVhhV0hjSMFh6p0ZKkT_BNIla_QH8Lg/fYGgU8qc5ig.jpg?size=625x597&quality=96&sign=d93df95202e5082127460b173fca5502&type=album",
    "https://sun9-59.userapi.com/impg/xrvCBpcPSormh3eYnInpJtmpwEnguxZ5XlyUeQ/g4ZfvACQ8Sw.jpg?size=631x555&quality=96&sign=55cfd7de741b669f4178b1f875025440&type=album",
    "https://sun9-54.userapi.com/impg/xCRJXCAAGu1oKuVwdHFV5rLHYi4bH0ZVTH1l2g/u-rCGqU3sLs.jpg?size=749x729&quality=96&sign=26e3341fc6637954608e70127482229b&type=album",
    "https://sun9-67.userapi.com/impg/1gmZQhAYO2-hv9FWpUXXyf3_PLaNeBsrEcPnCg/nmzI2AsxCH4.jpg?size=749x741&quality=96&sign=5d58368b2bf50d937709da23a244f479&type=album"
]
img_night_stack = [
    "https://i.pinimg.com/originals/81/0c/9a/810c9af3268cf91fb7da54bba68587f9.jpg",
    "https://pbs.twimg.com/media/EQxA7CSWkAAq95Q.jpg:large",
    "https://pristor.ru/wp-content/uploads/2017/04/%D0%A1%D0%BF%D0%BE%D0%BA%D0%BE%D0%B9%D0%BD%D0%BE%D0%B9-%D0%BD%D0%BE%D1%87%D0%B8-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BF%D1%80%D0%B8%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D1%8B%D0%B5-%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-2.jpg",
    "http://risovach.ru/upload/2014/05/mem/u-tebya-iq-kak-u-hlebushka_51211943_orig_.jpeg"
]

bot = tb.AsyncTeleBot("1781324497:AAG3WAkzs_dwSG9zoQDUguJbWSV_h1R9Mdc")

@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if message.text == 'я тебя люблю' or message.text == "Я тебя люблю":
        print(message.text)
        bot.send_message(message.from_user.id, "Я тебя тоже люблю")
    elif sravnen(message.text, "Спокойной ночки") > 0.70:
        print(message.text)
        bot.send_message(message.from_user.id, "Спокойной ночки, зайчик")
        bot.send_photo(message.from_user.id, img_night_stack[random.randrange(0, len(img_night_stack))])
    elif message.text == "Спасибо" or message.text == "спасибо":
        print(message.text)
        bot.send_message(message.from_user.id, "Пожалуйста солнышко, я на все ради тебя готов")
    elif message.text == "Расскажи мне пожалуйста все" or message.text == "расскажи мне пожалуйста все" or message.text == "Расскажи мне пожалуйста всё" or message.text == "расскажи мне пожалуйста всё":
        print(message.text)
        bot.send_message(message.from_user.id, ". ".join(stack))
    elif message.text == "Хочу пикчу" or message.text == "хочу пикчу":
        print(message.text)
        bot.send_message(message.from_user.id, "Лови, солнышко")
        bot.send_photo(message.from_user.id, imgs_stack[random.randrange(0, len(imgs_stack))])
    elif message.text == "Команды" or message.text == "команды":
        print(message.text)
        bot.send_message(message.from_user.id, 'Солнышко, я могу тебе показать лишь что я знаю, просто напши мне "Расскажи мне пожалуйста все". Люблю тебя.')
    else:
        print(message.text)
        bot.send_message(message.from_user.id, string_stack[random.randrange(0, len(string_stack))])

bot.polling(none_stop=True, interval=0)
