import string

class Atbash:
    def __init__(self,data,message):
        self.message=message
        self.data=data

    def encode(self):
        self.encode_message=''
        for letter in self.message:
            if letter in self.data:
                for i,j in enumerate(self.data):
                    if j == letter:
                        self.encode_message+=self.data[-(i+1)]
            else:
                self.encode_message+=letter


    def decode(self,encode_message):
        self.decode_message = ''
        for letter in encode_message:
            if letter in self.data:
                for i, j in enumerate(self.data):
                    if j == letter:
                        self.decode_message += self.data[-(i+1)]
            else:
                self.decode_message += letter


    def save(self,encode_message):
        with open('secret.txt' "w") as f:
            f.write(encode_message)


    def read_back(self,file):
        with open(f'{file} "r"') as f:
            self.encode_message=f.read()


data=a = list(string.ascii_lowercase)
m=input("Request message from the user")
f=Atbash(data,m)
f.encode()
print(f.encode_message)