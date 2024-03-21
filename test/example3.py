import asyncio
from urllib.parse import urlparse
from pytmi import Client  

async def send_message_to_twitch_stream(nick, token, stream_url, message):
    parsed_url = urlparse(stream_url)
    channel = parsed_url.path.lstrip('/')

    async with Client() as client:
        try:
            await client.login_oauth(token, nick)
            await client.join(channel)
            await client.send_message(message)
            print("Message envoyé avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'interaction avec Twitch: {type(e).__name__}, {e}")

async def main():
    nick = "foufure13"
    token = "oauth:aaptlok62b9h988jzgc52cqb7rrjjp"
    stream_url = "https://www.twitch.tv/whipotttv"
    message = "Salut  !"

    await send_message_to_twitch_stream(nick, token, stream_url, message)

if __name__ == "__main__":
    asyncio.run(main())
