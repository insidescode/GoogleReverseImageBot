import telebot
import requests
from telebot import types
bot_token = input("Enter your bot token: ")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Hello, %s!\n\nGoogle Reverse Image Bot let's you reverse search images on Google. You can try sending an image to me and I will reverse search that image. I can also be added to groups and you can reverse image by replying /reverse command to an image.\n\nDeveloped by @w3Abhishek\nThanks for using.''' % message.from_user.first_name)
@bot.message_handler(commands=['reverse'])
def reverse_image(message):
    if message.reply_to_message.content_type == 'photo':
        print("I am here")
        image_file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(image_file_id)
        print(file_info)
        reverse_final_url = requests.get("https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"%(bot_token,file_info.file_path)).url
        print(reverse_final_url)
        reverse_final_url = reverse_final_url.replace("/webhp?","/search?")
        bot.send_message(message.chat.id, "Reverse Image Search Completed!!! Click the Search Results button to view results.",reply_markup=types.InlineKeyboardMarkup([ [types.InlineKeyboardButton(text='Search Results', url=reverse_final_url)], [types.InlineKeyboardButton(text='Kronos Support', url='https://t.me/KronosSupport')]]))
    elif message.reply_to_message.content_type == 'sticker':
        sticker_file_id = message.reply_to_message.sticker.file_id
        file_info = bot.get_file(sticker_file_id)
        print(file_info)
        reverse_final_url = requests.get("https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"%(bot_token,file_info.file_path)).url
        print(reverse_final_url)
        reverse_final_url = reverse_final_url.replace("/webhp?","/search?")
        bot.send_message(message.chat.id, "Reverse Image Search Completed!!! Click the Search Results button to view results.",reply_markup=types.InlineKeyboardMarkup([ [types.InlineKeyboardButton(text='Search Results', url=reverse_final_url)], [types.InlineKeyboardButton(text='Kronos Support', url='https://t.me/KronosSupport')]]))

@bot.message_handler(content_types=['photo'])
def reverse_image(message):
    if message.chat.type == 'private':
        if message.content_type == 'photo':
            print("I am here")
            image_file_id = message.photo[-1].file_id
            file_info = bot.get_file(image_file_id)
            print(file_info)
            reverse_final_url = requests.get("https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"%(bot_token,file_info.file_path)).url
            print(reverse_final_url)
            reverse_final_url = reverse_final_url.replace("/webhp?","/search?")
            bot.send_message(message.chat.id, "Reverse Image Search Completed!!! Click the Search Results button to view results.",reply_markup=types.InlineKeyboardMarkup([ [types.InlineKeyboardButton(text='Search Results', url=reverse_final_url)], [types.InlineKeyboardButton(text='Kronos Support', url='https://t.me/KronosSupport')]]))
        elif message.content_type == 'sticker':
            sticker_file_id = message.sticker.file_id
            file_info = bot.get_file(sticker_file_id)
            print(file_info)
            reverse_final_url = requests.get("https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"%(bot_token,file_info.file_path)).url
            print(reverse_final_url)
            reverse_final_url = reverse_final_url.replace("/webhp?","/search?")
            bot.send_message(message.chat.id, "Reverse Image Search Completed!!! Click the Search Results button to view results.",reply_markup=types.InlineKeyboardMarkup([ [types.InlineKeyboardButton(text='Search Results', url=reverse_final_url)], [types.InlineKeyboardButton(text='Kronos Support', url='https://t.me/KronosSupport')]]))

bot.polling(none_stop=True)