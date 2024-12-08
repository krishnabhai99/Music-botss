from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    InputMediaPhoto,
    InputMediaVideo,
)

from SONALI import app
from SONALI.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
)
from SONALI.utils.decorators.admins import ActualAdminCB
from SONALI.utils.decorators.language import language, languageCB
from SONALI.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from SONALI.utils.inline.start import private_panel
from config import BANNED_USERS, OWNER_ID, START_IMG_URL


@app.on_message(
    filters.command(["settings", "setting"]) & filters.group & ~BANNED_USERS
)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(app.mention, message.chat.id, message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
#ya main callback hai#

@app.on_callback_query(filters.regex("gib_source") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/RYX.mp4", 
            caption= f"**Wᴇʟᴄᴏᴍᴇ ᴛᴏ {app.mention}**\n\n**Exᴘʟᴏʀᴇ ᴀ ᴡɪᴅᴇ ʀᴀɴɢᴇ ᴏғ ғᴇᴀᴛᴜʀᴇs ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ.**\n\n**Tᴀᴘ ᴛᴏ ɪɴᴠɪᴛᴇ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
[InlineKeyboardButton(
                text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖",
                url=f"https://t.me/{app.username}?startgroup=true",
            )],

[InlineKeyboardButton(text="• ᴍᴜsɪᴄ •", callback_data=f"settings_back_helper"),
InlineKeyboardButton(text="• ᴛᴏᴏʟs •", callback_data=f"mbot_cb")],

[InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"settingsback_helper")],
             ],   
     ),
    )

#ya about wla hai#

@app.on_callback_query(filters.regex("gibt_source") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/RYX.mp4", 
            caption= f"**❖ ๏ ʟᴇᴛ's ɪɴᴛʀᴏᴅᴜᴄᴇ ʀɪsʜᴜ-ᴍᴜsɪᴄ ʙᴏᴛ\n\n➻ [ʀɪsʜᴜ-ᴍᴜsɪᴄ](https://t.me/{app.username})  ɪs ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴍᴜsɪᴄ | ᴠɪᴅᴇᴏ sᴛꝛᴇᴀᴍɪɴɢ ʙᴏᴛ ᴏɴ ᴛᴇʟᴇɢꝛᴧᴍ ғᴏꝛ ʏᴏᴜꝛ ɢꝛᴏᴜᴘs ᴀɴᴅ ᴄʜᴧɴɴᴇʟ\n\n๏ ᴡʜʏ [˹ ʀɪsʜᴜ ᴍᴜsɪᴄ ˼](https://t.me/UR_RISHU_143) ɪs ʙᴇsᴛ ?\n\n⦿━━━━━━━━━━━━━━━━━━━━━⦿\n➻ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ\n➻ ᴍᴜsɪᴄ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs\n➻ ɴᴏ ʏᴛ ɪᴘ ʙʟᴏᴄᴋ ɪssᴜᴇ\n➻ ɴᴏ ᴘꝛᴏᴍᴏᴛɪᴏɴᴧʟ ᴧᴅs \n➻ ꝛᴇ-ᴇᴅɪᴛᴇᴅ ᴄᴏꝛᴇ | ʜɪɢʜʟʏ ᴏᴘᴛɪᴍɪsᴇ\n➻ ɴᴏ ʟᴧɢ ᴀɴᴅ ᴅᴏᴡɴ-ᴛɪᴍᴇ\n➻ ᴍᴀɴʏ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs........\n⦿━━━━━━━━━━━━━━━━━━━━━⦿\n\nᴀʟʟ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ\n\n❖ [Jᴏɪɴ ᴄʜᴀɴɴᴇʟ](https://t.me/UR_RISHU_143) |×| [ɢʀᴏᴜᴘ](https://t.me/UR_support07)**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
[InlineKeyboardButton(
                text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖",
                url=f"https://t.me/{app.username}?startgroup=true",
            )],

[InlineKeyboardButton(text="• ʙᴧsɪᴄ ɢᴜɪᴅᴇ •", callback_data=f"basict"),
InlineKeyboardButton(text="• ᴅᴏɴᴀᴛᴇ •", callback_data=f"doniiyyf")],
[InlineKeyboardButton(text="• sᴜʙsᴄʀɪʙᴇ •", callback_data=f"subplanh"),
[InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"settingsback_helper")],
             ],   
     ),
    )

#ya basic guide hai #

@app.on_callback_query(filters.regex("basict") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/Rke.mp4", 
            caption= f"**❖ ʜᴇʏ ᴅᴇᴀʀ ᴛʜɪs ɪs ᴀ ǫᴜɪᴄᴋ ᴀɴᴅ sɪᴍᴘʟᴇ ɢᴜɪᴅᴇ ᴛᴏ ᴜsɪɴɢ [ʀɪsʜᴜ-ᴍᴜsɪᴄ](https://t.me/UR_RISHU_143)\n\n1) ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ 'ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ' ʙᴜᴛᴛᴏɴ\n2) sᴇʟᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɴᴀᴍᴇ\n3) ɢʀᴀɴᴛ ᴛʜᴇ ʙᴏᴛ ᴀʟʟ ɴᴇᴄᴇssᴀʀʏ ᴘᴇʀᴍɪssɪᴏɴs ғᴏʀ sᴍᴏᴏᴛʜ ᴀɴᴅ ғᴜʟʟ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛʏ\n\nᴛᴏ ᴀᴄᴄᴇss ᴄᴏᴍᴍᴀɴᴅs, ʏᴏᴜ ᴄᴀɴ ᴄʜᴏᴏsᴇ ʙᴇᴛᴡᴇᴇɴ ᴍᴜsɪᴄ ᴘʀᴇғᴇʀᴇɴᴄᴇs ɪғ ʏᴏᴜ sᴛɪʟʟ ғᴀᴄᴇ ᴀɴʏ ɪssᴜᴇs, ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴀᴄʜ ᴏᴜᴛ ғᴏʀ sᴜᴘᴘᴏʀᴛ**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [

[InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"gibt_source")],
             ],   
     ),
    )

#donate wala #

@app.on_callback_query(filters.regex("doniiyyf") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/Rke.mp4", 
            caption= f"**❖ ʜᴇʏ, ɪ ᴀᴍ ɢʟᴀᴅ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜ ᴀʀᴇ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ᴅᴏɴᴀᴛɪɴɢ ᴜs ᴛʜᴀᴛ ᴍᴇᴀɴ ᴀ ʟᴏᴛ :)\n\nᴡᴇ ᴘʀᴏᴠɪᴅᴇ 24×7 ᴍᴜsɪᴄ sᴇʀᴠɪᴄᴇ sᴏ ᴡᴇ ᴀʟsᴏ ɴᴇᴇᴅ sᴏᴍᴇ ʜᴇʟᴘ ғᴏʀ ɪᴛ, ᴅᴏɴᴀᴛᴇ ɴᴏᴡ ᴠɪᴀ :-\n\n• ᴜᴘɪ ɪᴅ » <code>rishabhxdev@fam</code> \n• ǫʀ ᴄᴏᴅᴇ » [ᴛᴀᴘ ᴛᴏ sᴇᴇ ǫʀ ᴄᴏᴅᴇ](https://t.me/RishuQR/8) \n• ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ʙʏ ᴄᴏɴᴛᴀᴄᴛɪɴɢ [ᴅᴇᴠᴇʟᴏᴘᴇʀ 🚩](https://t.me/Rishu1286)\n\nʏᴏᴜʀ sᴍᴀʟʟ ᴀᴍᴏᴜɴᴛ ᴄᴀɴ ʜᴇʟᴘ ᴜs ᴀɴᴅ ʀɪsʜᴜ ᴛᴏ ɢʀᴏᴡ ᴍᴏʀᴇ**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [

[InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"gibt_source")],
             ],   
     ),
    )

#sub plan hai #

@app.on_callback_query(filters.regex("subplanh") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/Rke.mp4", 
            caption= f"**⌬ ๏ Bᴇɴɪғɪᴛ ᴏғ sᴜʙsᴄʀɪᴘᴛɪᴏɴ\n\n⌬ Yᴏᴜ ᴄᴀɴ ғʀᴇᴇ ᴘʀᴏᴍᴏᴛɪᴏɴ ᴏғ ʀɪsʜᴜ-ᴍᴜsɪᴄ Aʟʟ\n\n\n𝗢𝗡𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗨𝗦𝗘𝗥 [𝗖𝗠𝗗]\n\n\n⤿ [/broadcast -user -pin -pinloud -nobot -assistant] - Tᴏ ᴘʀᴏᴍᴏᴛɪᴏɴ ʟɪᴋᴇ\n\n⤿ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀᴅᴠᴀɴᴄᴇ ᴀɪ ᴛᴏᴏʟ**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [

[InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data=f"gibt_source")],
             ],   
     ),
    )


@app.on_callback_query(filters.regex("settingsback_helper") & ~BANNED_USERS)
@languageCB
async def settings_back_markup(client, CallbackQuery: CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    if CallbackQuery.message.chat.type == ChatType.PRIVATE:
        await app.resolve_peer(OWNER_ID)
        OWNER = OWNER_ID
        buttons = private_panel(_)
        return await CallbackQuery.edit_message_media(
            InputMediaPhoto(
                media=START_IMG_URL,
                caption=_["start_2"].format(
                    CallbackQuery.from_user.first_name, app.mention),
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = setting_markup(_)
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@app.on_callback_query(
    filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_2"], show_alert=True)
        except:
            return
    if command == "PLAYMODEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_5"], show_alert=True)
        except:
            return
    if command == "PLAYTYPEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_6"], show_alert=True)
        except:
            return
    if command == "AUTHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_3"], show_alert=True)
        except:
            return
    if command == "VOTEANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_8"],
                show_alert=True,
            )
        except:
            return
    if command == "ANSWERVOMODE":
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        try:
            return await CallbackQuery.answer(
                _["setting_9"].format(current),
                show_alert=True,
            )
        except:
            return
    if command == "PM":
        try:
            await CallbackQuery.answer(_["set_cb_2"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "AU":
        try:
            await CallbackQuery.answer(_["set_cb_1"], show_alert=True)
        except:
            pass
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            buttons = auth_users_markup(_, True)
        else:
            buttons = auth_users_markup(_)
    if command == "VM":
        mode = await is_skipmode(CallbackQuery.message.chat.id)
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        buttons = vote_mode_markup(_, current, mode)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("FERRARIUDTI") & ~BANNED_USERS)
@ActualAdminCB
async def addition(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    mode = callback_data.split(None, 1)[1]
    if not await is_skipmode(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(_["setting_10"], show_alert=True)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    if mode == "M":
        final = current - 2
        print(final)
        if final == 0:
            return await CallbackQuery.answer(
                _["setting_11"],
                show_alert=True,
            )
        if final <= 2:
            final = 2
        await set_upvotes(CallbackQuery.message.chat.id, final)
    else:
        final = current + 2
        print(final)
        if final == 17:
            return await CallbackQuery.answer(
                _["setting_12"],
                show_alert=True,
            )
        if final >= 15:
            final = 15
        await set_upvotes(CallbackQuery.message.chat.id, final)
    buttons = vote_mode_markup(_, final, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(
    filters.regex(pattern=r"^(MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def playmode_ans(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = None
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "MODECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            await set_playmode(CallbackQuery.message.chat.id, "Inline")
            Direct = None
        else:
            await set_playmode(CallbackQuery.message.chat.id, "Direct")
            Direct = True
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = False
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "PLAYTYPECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            await set_playtype(CallbackQuery.message.chat.id, "Admin")
            Playtype = False
        else:
            await set_playtype(CallbackQuery.message.chat.id, "Everyone")
            Playtype = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS)
@ActualAdminCB
async def authusers_mar(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "AUTHLIST":
        _authusers = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _authusers:
            try:
                return await CallbackQuery.answer(_["setting_4"], show_alert=True)
            except:
                return
        else:
            try:
                await CallbackQuery.answer(_["set_cb_4"], show_alert=True)
            except:
                pass
            j = 0
            await CallbackQuery.edit_message_text(_["auth_6"])
            msg = _["auth_7"].format(CallbackQuery.message.chat.title)
            for note in _authusers:
                _note = await get_authuser(CallbackQuery.message.chat.id, note)
                user_id = _note["auth_user_id"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name
                    j += 1
                except:
                    continue
                msg += f"{j}➤ {user}[<code>{user_id}</code>]\n"
                msg += f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=_["BACK_BUTTON"], callback_data=f"AU"
                        ),
                        InlineKeyboardButton(
                            text=_["CLOSE_BUTTON"],
                            callback_data=f"close",
                        ),
                    ]
                ]
            )
            try:
                return await CallbackQuery.edit_message_text(msg, reply_markup=upl)
            except MessageNotModified:
                return
    try:
        await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
    except:
        pass
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_)
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("VOMODECHANGE") & ~BANNED_USERS)
@ActualAdminCB
async def vote_change(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
    except:
        pass
    mod = None
    if await is_skipmode(CallbackQuery.message.chat.id):
        await skip_off(CallbackQuery.message.chat.id)
    else:
        mod = True
        await skip_on(CallbackQuery.message.chat.id)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    buttons = vote_mode_markup(_, current, mod)

    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return
