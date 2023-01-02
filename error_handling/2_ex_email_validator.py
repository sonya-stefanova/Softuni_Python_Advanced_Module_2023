class NameTooShortError(Exception):
    """ Raise it when the name in the email is less than or equal to 4 """


class MustContainAtSymbolError(Exception):
    """ Raise it when there is no "@" in the email """


class InvalidDomainError(Exception):
    """ Raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org) """


valid_domains = ['com', 'bg', 'org', 'net']

while True:
    email = input()
    if email == 'End':
        break

    if '@' in email:
        name_email, domain = email.split('@')[0], email.split('@')[1]
        domain = domain.split('.')[1]
        if len(name_email) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print('Email is valid')
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

