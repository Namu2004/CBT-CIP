import json
from pathlib import Path

# File where all contacts will be stored
DATA_FILE = Path("contact_data.json")


class Contact:
    """A simple data structure to hold individual contact information."""
    def __init__(self, name, phone, email):
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"{self.name} | 📞 {self.phone} | 📧 {self.email}"


class ContactMaster:
    """Main class for managing a list of contacts."""
    def __init__(self):
        self.contacts = []
        self._load()

    def _load(self):
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, "r") as f:
                    loaded = json.load(f)
                    self.contacts = [Contact(**item) for item in loaded]
            except json.JSONDecodeError:
                print("⚠️ Couldn't read contact file. Starting fresh.")
        else:
            DATA_FILE.touch()

    def _save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)

    def add(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self._save()
        print("✅ Contact saved.")

    def list(self):
        if not self.contacts:
            print("No contacts yet.")
            return
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact}")

    def search(self, keyword):
        keyword = keyword.lower()
        results = [c for c in self.contacts if keyword in c.name.lower()]
        if results:
            print(f"🔍 Found {len(results)} contact(s):")
            for c in results:
                print(c)
        else:
            print("No match found.")

    def delete(self, name):
        original_len = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_len:
            self._save()
            print("🗑️ Contact removed.")
        else:
            print("No such contact found.")

    def update(self, name, new_phone=None, new_email=None):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                if new_phone:
                    c.phone = new_phone
                if new_email:
                    c.email = new_email
                self._save()
                print("✏️ Contact updated.")
                return
        print("No contact found with that name.")


def run_cli():
    cm = ContactMaster()
    menu = """
==== ContactMaster ====
1. Add Contact
2. View Contacts
3. Search Contacts
4. Update Contact
5. Delete Contact
0. Exit
Choose an option: """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            n = input("Name: ")
            p = input("Phone: ")
            e = input("Email: ")
            cm.add(n, p, e)
        elif choice == "2":
            cm.list()
        elif choice == "3":
            k = input("Search name: ")
            cm.search(k)
        elif choice == "4":
            n = input("Enter name to update: ")
            p = input("New phone (leave blank to skip): ") or None
            e = input("New email (leave blank to skip): ") or None
            cm.update(n, p, e)
        elif choice == "5":
            n = input("Enter name to delete: ")
            cm.delete(n)
        elif choice == "0":
            print("👋 Exiting ContactMaster. Bye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    run_cli()
