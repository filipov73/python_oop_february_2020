class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        # if len(name) >= self.__min_length:
        #     return True
        # return False
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        # if mail in self.__mails:
        #     return True
        # return False
        return mail in self.mails

    def __validate_domain(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        name, data = email.split("@")
        mail, domain = data.split(".")
        # valid = [
        #     self.__validate_name(name),
        #     self.__validate_mail(mail),
        #     self.__validate_domain(domain)
        # ]
        # return all(valid)
        return self.__validate_name(name) \
            and self.__validate_mail(mail) \
            and self.__validate_domain(domain)

    """
    -	validate_name(name) - returns whether the name is greater than or equal to the min_length (True/False)
    -	validate_mail(mail) - returns whether the mail is in the possible mails list (True/False)
    -	validate_domain(domain) - returns whether the domain is in the possible domains list (True/False)
    Create one public method:
    -	validate(email) - using the three private methods returns whether the email is valid (True/False)

    """


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

"""
True
False
False
False
"""
