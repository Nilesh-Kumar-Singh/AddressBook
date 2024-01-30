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



class AddressBookMain:
    """
    This class is used to create address book objects
    """
    def __init__(self):
        self.address_book = []

    def add_contact(self,contact):
        self.address_book.append(contact)
    
    def edit_contact(self,first_name,last_name, contact):
        for i in range(len(self.address_book)):
            if self.address_book[i].first_name == first_name and self.address_book[i].last_name == last_name:
                self.address_book[i] = contact
                print("Contact edited successfully")
                break
    def delete_contact(self,first_name,last_name):
        for i in range(len(self.address_book)):
            if self.address_book[i].first_name == first_name and self.address_book[i].last_name == last_name:
                del self.address_book[i]
                print("Contact deleted successfully")
                break

x = AddressBookMain()

x.add_contact(Contact("Raj","Kumar","1234567890","raj@gmail.com","abc","xyz","abc","123456"))  
x.edit_contact("Raj","Kumar",Contact("Raj","Kumar","1234567890","rah@gmail.com","abc","xyz","abc","123456")) 
x.delete_contact("Raj","Kumar")