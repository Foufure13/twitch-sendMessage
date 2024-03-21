import asyncio
from pytmi import Client

async def main():
    nick = "foufure13"
    token = "oauth:aaptlok62b9h988jzgc52cqb7rrjjp"
    channel = "https://www.twitch.tv/whipotttv"

    async with Client() as client:
        try:
            await client.login_oauth(token, nick)
            await client.join(channel)
            await client.send_message("Salut, Twitch !")
        except Exception as e:
            print(f"Erreur lors de l'interaction avec Twitch: {e}")

if __name__ == "__main__":
    asyncio.run(main())
