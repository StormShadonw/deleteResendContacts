import resend
import time
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

print("Getting contacts...")


contacts = resend.Contacts.list()
contactsDeleted = 0
deletionRounds = 0

print("Contacts data retrieved")

try:
    while len(contacts["data"]) > 0:
        deletionRounds += 1
        print("**************************************************************************************************************************************")
        print(f"Deletion round: {deletionRounds}")
        for contact in contacts["data"]:
            time.sleep(1)
            print("---------------------------------------------------------------------------------------------------------------")
            print(f"Deleting contact: {contact["email"]}...")
            deleteResponse = resend.Contacts.remove(
            email=contact["email"]
            )
            if(deleteResponse["deleted"] == True):
                print(f"Contact deleted: {contact["email"]}")
                contactsDeleted += 1
                print(f"Contacts deleted: {contactsDeleted}")
        contacts = resend.Contacts.list()

    print("All contacts deleted!")
    
except Exception as e:
        print(f"A critical error occurred: {e}")