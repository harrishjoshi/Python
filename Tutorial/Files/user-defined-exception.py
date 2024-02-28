# User-Defined Exception
class InvalidAgeException(Exception):
    "Raised when the age is less than 18"
    pass

valid_age = 18

try:
    age = int(input("Enter a age: "))
    if age < valid_age:
        raise InvalidAgeException
    else:
        print("Eligible to vote!")
except InvalidAgeException:
    print("You're not eligible to vote.")

# Customizing Exception Classes
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message = "Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)