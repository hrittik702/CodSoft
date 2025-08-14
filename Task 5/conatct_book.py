#for storing contacts
contacts = []
def add_contact():
    name = input("Name : ")
    phone = input("Phone : ")
    email = input("E-mail : ")
    address = input("Address : ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Conatct Saved Successfully!\n")

#view-contact
def view_conatact():
    ab = int


#search-conatct
def search_contact():
    ba = int


#update-contact
def update_contact():
    aa = int


#delete-contact
def delete_contact():
    hd = int


#main-menu
def main_menu():
    print("\n     CONTACT BOOK        ")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")


        