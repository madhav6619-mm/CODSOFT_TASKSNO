# ============================================
#       CONTACT MANAGEMENT SYSTEM
# ============================================

contacts = {}


def add_contact():
    """Add a new contact."""

    print("\n========== ADD CONTACT ==========")

    name = input("Enter name: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    if name.lower() in [contact.lower() for contact in contacts]:
        print("❌ Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print(f"✅ Contact '{name}' added successfully!")


def view_contacts():
    """Display all saved contacts."""

    print("\n========== CONTACT LIST ==========")

    if not contacts:
        print("📭 No contacts saved.")
        return

    print(f"{'Name':<20} {'Phone Number':<18}")
    print("-" * 40)

    for name, details in contacts.items():
        print(f"{name:<20} {details['phone']:<18}")


def search_contact():
    """Search contacts by name or phone number."""

    print("\n========== SEARCH CONTACT ==========")

    search = input("Enter name or phone number: ").strip().lower()

    found = False

    for name, details in contacts.items():

        if search in name.lower() or search in details["phone"]:
            print("\nContact Found!")
            print("-" * 35)
            print("Name    :", name)
            print("Phone   :", details["phone"])
            print("Email   :", details["email"])
            print("Address :", details["address"])
            print("-" * 35)

            found = True

    if not found:
        print("❌ No matching contact found.")


def update_contact():
    """Update an existing contact."""

    print("\n========== UPDATE CONTACT ==========")

    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    print("\nEnter new details.")
    print("Press Enter to keep the existing value.\n")

    new_phone = input(
        f"Phone [{contacts[name]['phone']}]: "
    ).strip()

    new_email = input(
        f"Email [{contacts[name]['email']}]: "
    ).strip()

    new_address = input(
        f"Address [{contacts[name]['address']}]: "
    ).strip()

    if new_phone:
        contacts[name]["phone"] = new_phone

    if new_email:
        contacts[name]["email"] = new_email

    if new_address:
        contacts[name]["address"] = new_address

    print("✅ Contact updated successfully!")


def delete_contact():
    """Delete a contact."""

    print("\n========== DELETE CONTACT ==========")

    name = input("Enter the name of the contact to delete: ").strip()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{name}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        del contacts[name]
        print("✅ Contact deleted successfully!")
    else:
        print("❌ Delete operation cancelled.")


def main():
    """Main program."""

    while True:

        print("\n")
        print("=" * 45)
        print("       CONTACT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\n👋 Thank you for using Contact Management System!")
            break

        else:
            print("❌ Invalid choice! Please select 1-6.")


# Start the application
if __name__ == "__main__":
    main()