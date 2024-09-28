import os
import csv
from telethon.sync import TelegramClient
from telethon import functions, types
from dotenv import load_dotenv

load_dotenv()

with TelegramClient('having_fun', os.getenv("API_ID"), os.getenv("API_HASH")) as client:
    # list of contact objects
    contacts = client(functions.contacts.GetContactsRequest(
        hash=-12398745604826
    )).users

    for contact in contacts:
        print(contact) # or use contact.attribute_name to get a specific attribute