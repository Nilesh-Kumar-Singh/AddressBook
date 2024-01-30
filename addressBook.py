class Contact:
    """
    This class is used to create contact objects
    """
    def __init__(self,first_name,last_name,phone_number,email,address,city,state,zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.phone_number + " " + self.email + " " + self.address + " " + self.city + " " + self.state + " " + self.zip_code



class AddressBookMain:
    """
    This class is used to create address book objects
    """
    def __init__(self, address_book_name):
        self.address_book = {}
        self.address_book_name = address_book_name
        print("Address book created successfully")
    
    def check_duplicate(self,first_name):
        if self.address_book.get(first_name):
            print("Contact already exists")
            return True
        return False

    def add_contact(self,contact):
        if self.check_duplicate(contact.first_name):
            return
        self.address_book.update({contact.first_name:contact})
        print("Contact added successfully")

    
    def edit_contact(self,first_name,updated_contact={}):
        contact = self.address_book.get(first_name)
        if not contact:
            print("Contact not found")
            return
        for key, value in updated_contact.items():
            if getattr(contact,key):
                setattr(contact,key,value)



    def delete_contact(self,first_name):
        self.address_book.pop(first_name)
        print("Contact deleted successfully")

    def get_contact(self,first_name):
        contact = self.address_book.get(first_name)
        if not contact:
            print("Contact not found")
            return
        print(contact.__dict__)

    def add_multiple_contacts(self,contacts):
        for contact in contacts:
            self.add_contact(contact)

    def search_by_city_or_state(self,city_or_state):
        contacts = list(filter(lambda contact: contact.city == city_or_state or contact.state == city_or_state, self.address_book.values()))
        print(contacts)

    @staticmethod
    def get_contact_details(contact,city_or_state):
        if city_or_state in [contact.city,contact.state]:
            print(contact.__dict__)     

    def view_by_city_or_state(self,city_or_state):
        list(map(lambda x: self.get_contact_details(x, city_or_state), self.address_book.values()))


class MultipleAddressBook:
    def __init__(self,address_book_name):
        self.address_books = {}
        self.address_book_name = address_book_name

    def check_duplicate(self,address_book_name):
        if self.address_books.get(address_book_name):
            print("Address book already exists")
            return True
        return False

    def add_address_book(self,address_book):
        if self.check_duplicate(address_book.address_book_name):
            return
        self.address_books.update({address_book.address_book_name:address_book})

    def search_by_city_or_state(self,city_or_state):
        # for address_book in self.address_books.values():
        #     address_book.search_by_city_or_state(city_or_state)
        list(map(lambda address_book: address_book.search_by_city_or_state(city_or_state), self.address_books.values()))

    

x = AddressBookMain("Address Book 1")
x.add_contact(Contact("Raj","Kumar","1234567890","raj@gmail.com","abc","xyz","abc","123456"))  
x.get_contact("Raj")
x.edit_contact("Raj",{"email":"as@gmail.com","last_name":"Kumar"}) 

x.add_contact(Contact("Raj","Kumar","1234567890","raj@gmail.com","abc","xyz","abc","123456")) 
x.get_contact("Raj")
#x.delete_contact("Raj")

x.search_by_city_or_state("abc")

y = AddressBookMain("Address Book 2")
y.add_contact(Contact("Ath","Kumar","1234567890","a@gmail.com","abc","xyz","abc","123456"))

z = MultipleAddressBook("Multiple Address Book")
z.add_address_book(x)
z.add_address_book(y)
z.search_by_city_or_state("abc")
x.view_by_city_or_state("abcd")