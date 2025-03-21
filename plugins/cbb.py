from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"@Hentai_Cinema Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\n1. 𝗖𝗼𝗿𝗻_𝗖𝗶𝗻𝗲𝗺𝗮\n2. 𝗰𝗼𝘀𝗽𝗹𝗮𝘆_𝗖𝗶𝗻𝗲𝗺𝗮\n3. 𝗛𝗲𝗻𝘁𝗮𝗶_𝗖𝗶𝗻𝗲𝗺𝗮\n4. 𝗜𝗻𝗱𝗶𝗮𝗻_𝗖𝗶𝗻𝗲𝗺𝗮\n5. 𝗢𝗻𝗹𝘆_𝗳𝗮𝗻𝘀_𝗰𝗶𝗻𝗲𝗺𝗮\n6. 𝗽𝗮𝗿𝗼𝗱𝘆_𝗰𝗶𝗻𝗲𝗺𝗮\n7. Japanese_Cinema\n8. 𝗛𝗲𝗻𝘁𝗮𝗶 𝗜𝗻 𝗛𝗶𝗻𝗱𝗶 \n9. 𝗙𝗮𝗺𝗶𝗹𝘆 𝗙𝗮𝗻𝘁𝗮𝘀𝘆 \n<blockquote>Pricing Rates\n1 Month - INR 100\n3 Months - INR 250\n6 Months - INR 400\n12 Month - Contact <a href=https://t.me/Kira_Yagamai>Kira Yagamai</a></blockquote>\n\n<blockquote>Want To Buy?\n<a href=https://t.me/Kira_Yagamai>Kira Yagamai</a></blockquote>\n\nWe Have Limited Seats For Premium Users",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kira Yagamai", url="https://t.me/Kira_Yagamai"),
                        InlineKeyboardButton("All Channel", url="https://t.me/addlist/Mgnn8uZEPu4yNmM1")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
