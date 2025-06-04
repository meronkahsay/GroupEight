def add_contact(contact, contacts):
    contacts.append(contact)

def remove_contact(name, contacts):
    if name in contacts:
        contacts.remove(name)
    else:
        print(f"{name} not found in contacts")

def modify_contact(name, new_phone, new_email, contacts):
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = new_phone
            contact["email"] = new_email
            break
        else:
            print(f"{name} not found in contacts")

def get_contact_details(name, contacts):
    for contact in contacts:
        if contact["name"] == name:
            return f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
        return "Contact not found"