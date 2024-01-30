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


x = AddressBookMain()
x.add_contact(Contact("Raj","Kumar","1234567890","raj@gmail.com","abc","xyz","abc","123456"))   
    
