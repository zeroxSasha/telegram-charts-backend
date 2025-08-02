from pyrogram import Client
from pyrogram.raw.types.input_user import InputUser
from pyrogram.raw.functions.messages import RequestMainWebView
from pyrogram.raw.types.input_peer_empty import InputPeerEmpty

async def request_webview_url(name_tg_session, api_id, api_hash, tg_bot):
    import time
    time.sleep(10)
    async with Client(
        name=name_tg_session,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        bot_peer = await app.resolve_peer(tg_bot)
        iu = InputUser(
            user_id=bot_peer.user_id,
            access_hash=bot_peer.access_hash,
        )
        ipe = InputPeerEmpty()
        rmwv = RequestMainWebView(
            peer=ipe,
            bot=iu,
            platform="desktop"
        )

        result = await app.invoke(rmwv)

        return result.url
