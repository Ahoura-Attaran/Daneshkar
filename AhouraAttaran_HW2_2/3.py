import re


class customer():
    def __init__(self, name, email, phoneNumber):
        self.name = str(name)
        self.Email = customer.validate_email(email)
        self.PhoneNumber = customer.validate_phone(phoneNumber)

    @staticmethod
    def validate_email(mail):
        pattern = r"^[A-Za-z0-9_]+@[A-Za-z0-9.-]+\.(com|org|net)$"

        if re.match(pattern, mail):
            return mail
        else:
            raise ValueError("Email not valid")

    @staticmethod
    def validate_phone(number):
        pattern = r"^[0-9+\-]+$"

        if not re.fullmatch(pattern, number):
            raise ValueError("Phone not valid")
        
        else:
            if len(re.findall(r"\d", number)) >= 10:
                return number
            
            else:
                raise ValueError("Phone not valid")