from telethon import TelegramClient, events

# Itt add meg a saját API adataidat
api_id = 22564650          # Például: 1234567
api_hash = 'ff279c038285670dbade45205af41755'    # Például: 'abcd1234efgh5678ijkl9012mnop3456'
session_name = 'userbot_session'

# Állítsd be a forrás és a cél csoportot (felhasználónév vagy numerikus ID)
source_group = '-1001518839458'
target_group = '-4600638769'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    # Ha az üzenet szöveges, akkor elküldjük egyszerűen a szöveget
    if event.message.text:
        await client.send_message(target_group, event.message.text)
        print("Szöveges üzenet elküldve.")
    # Ha az üzenet médiát tartalmaz (pl. kép, videó, dokumentum)
    elif event.message.media:
        # Küldjük el a médiát a megfelelő felirattal, ha van
        caption = event.message.text or ""
        await client.send_file(target_group, event.message.media, caption=caption)
        print("Médiaüzenet elküldve.")
    else:
        # Egyéb típusok esetén, például ha nincs szöveg vagy média
        print("Nem támogatott üzenettípus.")

async def main():
    await client.start()
    print("Userbot elindult. Figyeli a forrás csoport üzeneteit...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
