import string
import random
class CreatePass:
    def __init__(self):
        self.password_data = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.password = ""

    def no_set_len_pass(self):
        for i in range(0, random.randint(8, 14)):
            self.password += random.choice(self.password_data)

    def set_len_pass(self, n):
        for i in range(0, n):
            self.password += random.choice(self.password_data)

