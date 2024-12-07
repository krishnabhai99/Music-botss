from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Initialize the bot


# Developer callback
@app.on_callback_query(filters.regex("developer"))
async def about_callback(client: Client, callback_query: CallbackQuery):
    buttons = [
        [
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=5738579437),  # Replace with owner ID
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ur_support07"
            ),
        ],
        [
            InlineKeyboardButton(text="ɴᴇᴛᴡᴏʀᴋ", url=f"t.me/RishuNetwork"),
            InlineKeyboardButton(text="ᴀʟʟ ʙᴏᴛs", url=f"https://t.me/Vip_robotz/4"),
        ],
        [
            InlineKeyboardButton(text="𖨠Back𖨠", callback_data="about")
        ],
    ]
    await callback_query.message.edit_text(
        "✦ **ᴛʜɪs ʙᴏᴛ ɪs ᴍᴀᴅᴇ ʙʏ ᴀ sᴋɪʟʟᴇᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴛᴏ ᴍᴀᴋᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇᴀsʏ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ᴍᴏʀᴇ ғᴜɴ.**\n\n✦ **ᴡɪᴛʜ ᴊᴜsᴛ ᴀ ғᴇᴡ ᴄʟɪᴄᴋs, ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛʀᴏʟ ᴇᴠᴇʀʏᴛʜɪɴɢ—ʟɪᴋᴇ sᴇᴛᴛɪɴɢ ᴜᴘ ᴏᴡɴᴇʀ sᴇᴛᴛɪɴɢs**\n\n✦ **ᴛʜᴇ ʙᴏᴛ ɪs ᴅᴇsɪɢɴᴇᴅ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴍᴏᴏᴛʜʟʏ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴛᴏᴏ. ᴊᴜsᴛ ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴇᴇ ʜᴏᴡ ᴇᴀsʏ ɪᴛ ɪs!**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )

# Feature callback
@app.on_callback_query(filters.regex("feature"))
async def feature_callback(client: Client, callback_query: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(
                text="ᴋɪᴅɴᴀᴘ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="music"),
            InlineKeyboardButton(text="ᴍᴀɴᴇɢᴇᴍᴇɴᴛ", callback_data="settings_back_helper"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    await callback_query.message.edit_text(
        f"**Wᴇʟᴄᴏᴍᴇ ᴛᴏ** {app.mention}\n\n**Exᴘʟᴏʀᴇ ᴀ ᴡɪᴅᴇ ʀᴀɴɢᴇ ᴏғ ғᴇᴀᴛᴜʀᴇs ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ. Tᴀᴘ  ᴛᴏ ɪɴᴠɪᴛᴇ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴏᴡɴ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ sᴇᴀᴍʟᴇss ᴍᴜsɪᴄ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ. Usᴇ ᴛʜᴇ ᴍᴜsɪᴄ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss ᴀʟʟ ᴛʜᴇ ᴍᴜsɪᴄ-ʀᴇʟᴀᴛᴇᴅ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛɪᴇs, ғʀᴏᴍ sᴛʀᴇᴀᴍɪɴɢ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢs ᴛᴏ ᴄʀᴇᴀᴛɪɴɢ ᴘʟᴀʏʟɪsᴛs.!**",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

