import csv
import os

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}\n{self.address}\n{self.city}, {self.state} {self.zip_code}\nPhone: {self.phone_number}\nEmail: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []
        self.city_person_dict = {}
        self.state_person_dict = {}

    def add_contact(self, contact):
        self.contacts.append(contact)

        # Update city-person and state-person dictionaries
        if contact.city in self.city_person_dict:
            self.city_person_dict[contact.city].append(contact)
        else:
            self.city_person_dict[contact.city] = [contact]

        if contact.state in self.state_person_dict:
            self.state_person_dict[contact.state].append(contact)
        else:
            self.state_person_dict[contact.state] = [contact]

    def display_contacts(self):
        # Sort contacts alphabetically by Person's name
        sorted_contacts = sorted(self.contacts, key=lambda x: (x.first_name, x.last_name, x.city, x.state, x.zip_code))
        for contact in sorted_contacts:
            print(contact)
            print("\n" + "-"*20 + "\n")

    def find_contact_by_name(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def search_by_city_state(self, city=None, state=None):
        results = []
        if city in self.city_person_dict:
            results.extend(self.city_person_dict[city])
        if state in self.state_person_dict:
            results.extend(self.state_person_dict[state])
        return results

    def get_contact_count_by_city_state(self):
        city_count = {city: len(persons) for city, persons in self.city_person_dict.items()}
        state_count = {state: len(persons) for state, persons in self.state_person_dict.items()}
        return city_count, state_count

    def edit_contact(self, first_name, last_name):
        contact = self.find_contact_by_name(first_name, last_name)
        if contact:
            print("Current Contact Details:")
            print(contact)

            # for new details
            new_address = input("Enter New Address (press Enter to keep current): ")
            new_city = input("Enter New City (press Enter to keep current): ")
            new_state = input("Enter New State (press Enter to keep current): ")
            new_zip_code = input("Enter New ZIP Code (press Enter to keep current): ")
            new_phone_number = input("Enter New Phone Number (press Enter to keep current): ")
            new_email = input("Enter New Email (press Enter to keep current): ")

            # Update contact details
            contact.address = new_address if new_address else contact.address

            # Update city-person and state-person dictionaries
            if contact.city in self.city_person_dict:
                self.city_person_dict[contact.city].remove(contact)
            if new_city in self.city_person_dict:
                self.city_person_dict[new_city].append(contact)
            else:
                self.city_person_dict[new_city] = [contact]
            contact.city = new_city if new_city else contact.city

            # Update state-person dictionary
            if contact.state in self.state_person_dict:
                self.state_person_dict[contact.state].remove(contact)
            if new_state in self.state_person_dict:
                self.state_person_dict[new_state].append(contact)
            else:
                self.state_person_dict[new_state] = [contact]
            contact.state = new_state if new_state else contact.state

            contact.zip_code = new_zip_code if new_zip_code else contact.zip_code
            contact.phone_number = new_phone_number if new_phone_number else contact.phone_number
            contact.email = new_email if new_email else contact.email

            print("Contact Updated Successfully!")
            print(contact)
        else:
            print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact_by_name(first_name, last_name)
        if contact:
            self.contacts.remove(contact)

            # Update city-person and state-person dictionaries
            if contact.city in self.city_person_dict:
                self.city_person_dict[contact.city].remove(contact)
            if contact.state in self.state_person_dict:
                self.state_person_dict[contact.state].remove(contact)

            print("Contact Deleted Successfully!")
        else:
            print("Contact not found. Deletion failed.")

class AddressBookManager:
    def __init__(self):
        self.address_books = {}
        self.file_path = os.path.join(os.getcwd(), "address_book.csv")

    def create_address_book(self, book_name):
        if book_name not in self.address_books:
            address_book = AddressBook()
            self.address_books[book_name] = address_book
            return address_book
        else:
            print(f"Address book '{book_name}' already exists.")
            return None

    def get_address_book(self, book_name):
        return self.address_books.get(book_name)

    def add_new_contact(self, book_name):
        address_book = self.get_address_book(book_name)
        if address_book:
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")

            # Check for duplicate entry based on person's name
            existing_contact = address_book.find_contact_by_name(first_name, last_name)
            if existing_contact:
                print("Duplicate entry! This person already exists in the Address Book.")
            else:
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                zip_code = input("Enter ZIP Code: ")
                phone_number = input("Enter Phone Number: ")
                email = input("Enter Email: ")

                new_contact = Contact(
                    first_name, last_name, address, city, state, zip_code, phone_number, email)
                address_book.add_contact(new_contact)
                print("Contact added successfully!")
        else:
            print(f"Address book '{book_name}' not found.")

    def display_contacts(self, book_name):
        address_book = self.get_address_book(book_name)
        if address_book:
            address_book.display_contacts()
        else:
            print(f"Address book '{book_name}' not found.")

    def edit_contact(self, book_name, first_name, last_name):
        address_book = self.get_address_book(book_name)
        if address_book:
            address_book.edit_contact(first_name, last_name)
        else:
            print(f"Address book '{book_name}' not found.")

    def delete_contact(self, book_name, first_name, last_name):
        address_book = self.get_address_book(book_name)
        if address_book:
            address_book.delete_contact(first_name, last_name)
        else:
            print(f"Address book '{book_name}' not found.")

    def search_across_address_books(self, city=None, state=None):
        results = []
        for book_name, address_book in self.address_books.items():
            search_results = address_book.search_by_city_state(city, state)
            if search_results:
                results.extend([(book_name, contact) for contact in search_results])
        return results

    def get_contact_count_across_address_books(self, city=None, state=None):
        city_count = 0
        state_count = 0
        for address_book in self.address_books.values():
            city_count_book, state_count_book = address_book.get_contact_count_by_city_state()
            city_count += city_count_book.get(city,0)
            state_count += state_count_book.get(state,0)
        return city_count, state_count

    def save_address_book_to_csv(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "ZIP Code", "Phone Number", "Email"])
            for address_book in self.address_books.values():
                for contact in address_book.contacts:
                    writer.writerow([contact.first_name, contact.last_name, contact.address, contact.city, contact.state,
                                    contact.zip_code, contact.phone_number, contact.email])
        print(f"Address book saved to CSV file: {self.file_path}")

    def load_address_book_from_csv(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    first_name, last_name, address, city, state, zip_code, phone_number, email = row
                    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                    book_name = os.path.splitext(os.path.basename(self.file_path))[0]  # Use file name as book name
                    if book_name not in self.address_books:
                        self.address_books[book_name] = AddressBook()
                    self.address_books[book_name].add_contact(contact)
            print(f"Address book loaded from CSV file: {self.file_path}")
        else:
            print("No existing address book CSV file found.")

class AddressBookMain:
    def __init__(self):
        self.address_book_manager = AddressBookManager()

    def perform_address_book_operations(self):
        while True:
            book_name = input("Enter the name of the Address Book (type 'exit' to quit): ")
            if book_name.lower() == 'exit':
                break

            address_book = self.address_book_manager.create_address_book(book_name)

            if address_book:
                while True: 
                    ask = input("Do you want to add a contact? (yes/no): ")
                    if ask.lower() == "yes":
                        self.address_book_manager.add_new_contact(book_name)
                    else:
                        break

                self.address_book_manager.display_contacts(book_name)

                first_name_to_edit = input("Enter the First Name of the contact to edit: ")
                last_name_to_edit = input("Enter the Last Name of the contact to edit: ")
                self.address_book_manager.edit_contact(book_name, first_name_to_edit, last_name_to_edit)

                first_name_to_delete = input("Enter the First Name of the contact to delete: ")
                last_name_to_delete = input("Enter the Last Name of the contact to delete: ")
                self.address_book_manager.delete_contact(book_name, first_name_to_delete, last_name_to_delete)

                self.address_book_manager.display_contacts(book_name)

                search_city = input("Enter City to search across Address Books (press Enter to skip): ")
                search_state = input("Enter State to search across Address Books (press Enter to skip): ")
                search_results = self.address_book_manager.search_across_address_books(search_city, search_state)
                
                if search_results:
                    print("\nSearch Results across Address Books:")
                    for book_name, contact in search_results:
                        print(f"Address Book: {book_name}")
                        print(contact)
                        print("\n" + "-"*20 + "\n")
                else:
                    print("No matching results found across Address Books.")

                city_count, state_count = self.address_book_manager.get_contact_count_across_address_books(search_city, search_state)
                print(f"\nNumber of contact persons by City: {city_count}")
                print(f"Number of contact persons by State: {state_count}")

            self.address_book_manager.save_address_book_to_csv()
            self.address_book_manager.load_address_book_from_csv()

if __name__ == "__main__":
    address_book_main = AddressBookMain()
    address_book_main.perform_address_book_operations()