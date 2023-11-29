from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

from django.http import HttpResponse
from django.conf import settings
from telegram import Bot
import telebot

API_TOKEN = '6372700016:AAGirBgxaCvg8AMxs3qUBvFbNPLMkENl9h4'

bot = telebot.TeleBot(API_TOKEN)

def send_telegram_message(request, content=str):
    bot.send_message('5051659343', content)
    return HttpResponse("Message sent to Telegram!")



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":

        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            send_telegram_message(request, form.cleaned_data['Telephone'])
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data['Telephone'])
            return HttpResponseRedirect("")



    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, "flatpages/main.html",context={'form': form})



