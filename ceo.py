from user import User
from datetime import date

class CEO(User):
    """
    A CEO is a type of user who can access extra features than a normal user

    Args:
        first_name (str): The first name of the person, required
        last_name (str): The last or family name of the person, required
        email (str): Email address, required
        password (str): Password, required
        dob (date): Date of birth, optional with default None if value isn't provided.
        company_name (str):
        company_type (str):
        countries_followed (list):
    Attributes:
        first_name (str): The first name of the person, required
        last_name (str): The last or family name of the person, required
        email (str): Email address, required
        password (str): Password, required
        dob (date): Date of birth, optional with default None if value isn't provided.
        company_name (str):
        company_type (str):
        countries_followed (list):
    Methods:
        create_full_name: Creates the full names by concatenating the first names and last name
        calculate_age: Calculates the age from the date of birth
        hash_password: Create a hashed value of the string password
        is_correct_password: Checks if the string password matches the hashed password
    """
    def __init__(self, first_name: str, last_name: str, email: str, password: str, company_name: str, company_type: str,
                 countries_followed:list, dob: date = None):
        super(CEO, self).__init__(first_name, last_name, email, password, dob)
        self.company_name = company_name
        self.company_type = company_type
        self.countries_followed = countries_followed

    def __repr__(self):
        """ String representation of a user object """
        return f" {self.first_name} {self.last_name} {self.email} {self.dob} {self.company_name} {self.company_type} " \
               f" {self.countries_followed}"
