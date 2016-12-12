# -*- coding: utf-8 -*-

from django.shortcuts import render
import telebot

# Create your views here.


def post_list(request):
    return render(request, 'bot/post_list.html', {})


def run_bot():
    bot = telebot.TeleBot("301583096:AAFIj_0jfY5Xoy8WivDoieZKSczIDCGO3zg")

    bot.send_message(message.chat.id, "Hi")
    if __name__ == '__main__':
        bot.polling(none_stop=True)