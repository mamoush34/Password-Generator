import random
import string
import secrets


class PasswordGenerator:

    def __init__(self) -> None:
        self.pass_len = 16
        self.char_set = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

    
    def produce_random_pass(self) -> str:
        password = []
        for _ in range(self.pass_len):
            password.append(secrets.choice(self.char_set))
        
        random.shuffle(password)

        return str.join("", password)

if __name__ == "__main__":
    passGen =  PasswordGenerator()
    new_pass = passGen.produce_random_pass()
    print(new_pass)


