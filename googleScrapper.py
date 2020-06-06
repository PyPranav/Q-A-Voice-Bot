import requests as req
from bs4 import BeautifulSoup
import random


def sattrs(attrs):
    return soup.find(attrs=attrs).get_text().strip()


def sid(id):
    return soup.find(id=id).get_text().strip()


def searcher(your_question):
    global soup, conversation, choice, url

    url = "https://www.google.com/search?q=" + your_question.replace("%", "%25").replace("+", "%2B").replace(" ", "+")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    page = req.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    try:
        # for basic facts like height of mt everest
        bot_answer = sattrs("Z0LcW")
    except AttributeError:
        try:
            # for math calculations like 1+2 :-
            bot_answer = sattrs("qv3Wpe")
        except AttributeError:
            try:
                # for more tricky questions like who is the finance minister of india
                bot_answer = sattrs("e24Kjd")
            except AttributeError:
                try:
                    # for english definations like- define Exception
                    bot = sattrs("QIclbb XpoqFe")
                    if ("defin" or "mean") in your_question.lower():
                        if "(e.g." not in bot:
                            bot_answer = bot.split(".", 1)[0] + "."
                        else:
                            bot_answer = bot.split(")", 1)[0] + ")."
                    else:
                        bot_answer = sattrs("qv3Wpe")
                        # this to cause an error and move on to the except statement
                except AttributeError:
                    try:
                        # for dates related question like today's date
                        bot_answer = sattrs("vk_bk dDoNo")
                    except AttributeError:
                        try:
                            # for conversational factors like 1 cm in inch
                            bot = soup.find(id="NotFQb")
                            a = str(bot).find("value")
                            str_bot = str(bot)[a:a + 30]
                            bot_answer = ""
                            for z in range(len(str_bot)):
                                if str_bot[z] in "0123456789.-":
                                    bot_answer += str_bot[z]
                            if bot_answer != "":
                                bot = sattrs("dtp2jf")
                                bot = bot[:7] + " Used:" + bot[9:]
                                bot_answer += f"\n{bot}"
                            else:
                                bot_answer = sattrs("vk_bk dDoNo")
                                # this to cause an error and move on to the except statement

                        except AttributeError:
                            try:
                                # for conversations based on money like 32 dollar to inr
                                bot_answer = sattrs("dDoNo vk_bk gsrt")
                            except AttributeError:
                                try:
                                    # for translation related questions
                                    bot_answer = sid("tw-target-text")
                                    bot = sid("z6maec")
                                    if bot != "":
                                        bot_answer += f"\nPronunciation: {bot}"
                                except AttributeError:
                                    try:
                                        # for speed related questions like speed of light
                                        bot_answer = sattrs("dDoNo vk_bk")
                                    except AttributeError:
                                        try:
                                            # for stock price related questions
                                            b = sattrs("OiIFo")
                                            bot_answer = sattrs("N9cLBc").replace(b, "").split(")", 1)[0] + ")"
                                        except AttributeError:
                                            try:
                                                # for weather forecasting questions like panvel weather
                                                bot_answer = "-\n" + sid("wob_loc")
                                                bot = sid("wob_dts")
                                                bot_answer += f"\nTime: {bot}"
                                                bot = sid("wob_dc")
                                                bot_answer += f"\nWeather Type: {bot}"
                                                bot = sid("wob_tm") + " C"
                                                bot_answer += f"\nTemperature: {bot}"
                                                bot = sid("wob_pp")
                                                bot_answer += f"\nPrecipitation: {bot}"
                                                bot = sid("wob_hm")
                                                bot_answer += f"\nHumidity: {bot}"
                                                bot = sid("wob_ws")
                                                bot_answer += f"\nWind: {bot}"
                                            except AttributeError:
                                                try:
                                                    # for some questions with multiple answers
                                                    # (note: only returns one but the most valid answer)
                                                    bot_answer = sattrs("rl_item rl_item_base")
                                                except AttributeError:
                                                    try:
                                                        # for some questions with multiple answers
                                                        # (note: only returns one but the most valid answer)
                                                        bot_answer = sattrs("mdFQt mVpQ0e")
                                                    except AttributeError:
                                                        try:
                                                            bot = sattrs("kno-rdesc")
                                                            if "wikipedia"  in bot.lower():
                                                                bot_answer = bot[11:len(bot) - 9]
                                                            elif "MORE" in bot:
                                                                bot = sattrs("PZPZlf hb8SAc")
                                                                bot_answer = bot[11:len(bot) - 7] + "."
                                                            else:
                                                                bot_answer = bot[11:len(bot)]
                                                        except AttributeError:
                                                            if (("toss" or "flip") and "coin") in your_question.lower():
                                                                bot = random.randint(1, 2)
                                                                bot_answer = "Tails" if bot == 1 else "Heads"
                                                            elif(("die" or "dice") and "roll") in your_question.lower():
                                                                bot_answer = str(random.randint(1, 6))
                                                            else:
                                                                bot_answer = "Unable to Find an answer"

    return bot_answer


if __name__ == '__main__':
    print(searcher(input()))