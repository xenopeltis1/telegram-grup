from pyrogram import Client
from pyrogram.filters import media
import os


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'


app = Client(
    session_name="my_account",
    api_id=123456,
    api_hash="hash"
    )


def temizle():
    os.system("cls") if os.name == "nt" else os.system("clear")


def progress(current, total):
    temizle()
    print(f"İndiriliyor {current/100000:.2f}%")


def getMediaFromChat(chatId, historyCount, filterA):
    count = 0
    for file in app.search_messages(chatId, filter=filterA):
        fileId = getattr(file, filterA).file_id
        print(app.download_media(fileId, progress=progress)+" indirildi")
        temizle()
        count += 1

    print(f"""{bcolors.OKBLUE}[{bcolors.OKGREEN}{count}
    {bcolors.OKBLUE}] adet dosya başarıyla
     downloads klasörüne indirildi.""")


def getMessagesFromGroup(app):
    count = 0
    for channel in app.get_dialogs():
        if "group" in channel.chat.type:
            print(f"""{bcolors.OKBLUE}[ {bcolors.OKGREEN}{count}{bcolors.OKBLUE} ] - """ + str(channel.chat.title))
        count += 1

    g_index = int(input("chat seç: "))
    chatId = app.get_dialogs()[g_index].chat.id
    historyCount = app.get_history_count(chatId)

    print(f"""hangi tür dosyaları kaydetmek istiyorsun\n{bcolors.OKBLUE}[ {bcolors.OKGREEN}0 {bcolors.OKBLUE} ] - photo\n{bcolors.OKBLUE}[ {bcolors.OKGREEN}1 {bcolors.OKBLUE} ] - video\n{bcolors.OKBLUE}[ {bcolors.OKGREEN}2 {bcolors.OKBLUE} ] - document\n{bcolors.OKBLUE}[ {bcolors.OKGREEN}3 {bcolors.OKBLUE} ] - audio""")

    filterChoice = int(input(f"\t{bcolors.OKGREEN}Seçiminiz: "))
    choices = ["photo", "video", "document", "audio"]
    getMediaFromChat(chatId, historyCount, choices[filterChoice])


with app:
    getMessagesFromGroup(app)

app.run()
