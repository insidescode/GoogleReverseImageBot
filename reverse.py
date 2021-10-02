import telebot
import requests
from telebot import types
<<<<<<< HEAD
# Example Bot Token. You can get it from @BotFather and replace it here.
bot_token = "2038613226:AAHQw-k0wg4i3CSLWAnNLQEsGNQ3Cquvvwc"
=======
bot_token = "2038613226:AAHQw-k0wg4i3CSLWAnNLQEsGNQ3Cquvvwc" # This is a example token Change this token with your own.
>>>>>>> 9e693527def05edbbd01800cad02568ea4778e22

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        """Hello, %s!\n\nGoogle Reverse Image Bot let's you reverse search images on Google. You can try sending an image to me and I will reverse search that image. \nI can also be added to groups and you can reverse image by replying /reverse command to an image.\n\nDeveloped by @w3Abhishek\nThanks for using."""
        % message.from_user.first_name,
    )


@bot.message_handler(commands=["reverse"])
def reverse_image(message):
    if message.reply_to_message.content_type == "photo":
        image_file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(image_file_id)
        reverse_final_url = requests.get(
            "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
            % (bot_token, file_info.file_path)
        ).url
        reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
        bot.send_message(
            message.chat.id,
            "Reverse Image Search Completed!!! Click the Search Results button to view results.",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(
                            text="Search Results", url=reverse_final_url
                        )
                    ],
                    [
                        types.InlineKeyboardButton(
                            text="Kronos Support", url="https://t.me/KeevChat"
                        )
                    ],
                ]
            ),
        )
    elif message.reply_to_message.content_type == "sticker":
        sticker_file_id = message.reply_to_message.sticker.thumb.file_id
        file_info = bot.get_file(sticker_file_id)
        reverse_final_url = requests.get(
            "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
            % (bot_token, file_info.file_path)
        ).url
        reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
        bot.send_message(
            message.chat.id,
            "Reverse Image Search Completed!!! Click the Search Results button to view results.",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(
                            text="Search Results", url=reverse_final_url
                        )
                    ],
                    [
                        types.InlineKeyboardButton(
                            text="Kronos Support", url="https://t.me/KeevChat"
                        )
                    ],
                ]
            ),
        )
    elif message.reply_to_message.content_type == "video":
        video_file_id = message.reply_to_message.video.thumb.file_id
        file_info = bot.get_file(video_file_id)
        reverse_final_url = requests.get(
            "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
            % (bot_token, file_info.file_path)
        ).url
        reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
        bot.send_message(
            message.chat.id,
            "Reverse Image Search Completed!!! Click the Search Results button to view results.",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(
                            text="Search Results", url=reverse_final_url
                        )
                    ],
                    [
                        types.InlineKeyboardButton(
                            text="Kronos Support", url="https://t.me/KeevChat"
                        )
                    ],
                ]
            ),
        )
    elif message.reply_to_message.content_type == "animation":
        try:
            animation_file_id = message.reply_to_message.animation.thumb.file_id
            file_info = bot.get_file(animation_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        except:
            bot.send_message(
                message.chat.id,
                "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit",
            )


@bot.message_handler(content_types=["photo"])
def reverse_image(message):
    if message.chat.type == "private":
        if message.content_type == "photo":
            image_file_id = message.photo[-1].file_id
            file_info = bot.get_file(image_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        elif message.content_type == "sticker":
            sticker_file_id = message.sticker.file_id
            file_info = bot.get_file(sticker_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        elif message.reply_to_message.content_type == "video":
            video_file_id = message.reply_to_message.video.thumb.file_id
            file_info = bot.get_file(video_file_id)
            reverse_final_url = requests.get(
                "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                % (bot_token, file_info.file_path)
            ).url
            reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
            bot.send_message(
                message.chat.id,
                "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                text="Search Results", url=reverse_final_url
                            )
                        ],
                        [
                            types.InlineKeyboardButton(
                                text="Kronos Support", url="https://t.me/KeevChat"
                            )
                        ],
                    ]
                ),
            )
        elif message.reply_to_message.content_type == "animation":
            try:
                animation_file_id = message.reply_to_message.animation.thumb.file_id
                file_info = bot.get_file(animation_file_id)
                reverse_final_url = requests.get(
                    "https://images.google.com/searchbyimage?image_url=https://api.telegram.org/file/bot%s/%s"
                    % (bot_token, file_info.file_path)
                ).url
                reverse_final_url = reverse_final_url.replace("/webhp?", "/search?")
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search Completed!!! Click the Search Results button to view results.",
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    text="Search Results", url=reverse_final_url
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    text="Kronos Support", url="https://t.me/KeevChat"
                                )
                            ],
                        ]
                    ),
                )
            except:
<<<<<<< HEAD
                bot.send_message(
                    message.chat.id,
                    "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit",
                )


=======
                bot.send_message(message.chat.id, "Reverse Image Search is not possible for GIFs sent through Telegram GIF section. Try downloading and send again to reverse search. \nErr: Telegram API Limit")
>>>>>>> 9e693527def05edbbd01800cad02568ea4778e22
bot.polling(none_stop=True)
