class NameTooShortError(Exception):
    """the error is raised when the name in the email is less than or equal to 4
    ("peter" will be the name in the email "peter@gmail.com")"""


class MustContainAtSymbolError(Exception):
    """the error is raised when there is no "@" in the email"""


class InvalidDomainError(Exception):
    """the error is raised when the domain of the email is invalid
    (valid domains are: .com, .bg, .net, .org)"""

def is_invalid_domain(extension, valid_extensions):
    output = True
    for valid_extension in valid_extensions:
        if extension.endswith(valid_extension):
            output = False
            break
    return output



valid_extensions = ['com', 'bg', 'org', 'net']

e_mail = input()
while e_mail != "End":

    if "@" not in e_mail:
        raise MustContainAtSymbolError("Email must contain @")

    domain_name, extension = e_mail.split("@")
    if len(domain_name)<=4:
        raise NameTooShortError("Name must be more than 4 characters")

    if is_invalid_domain(extension, valid_extensions):
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_extensions)}')

    print("Email is valid")
    e_mail = input()
