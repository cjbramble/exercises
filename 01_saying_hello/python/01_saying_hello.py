class Greeting():
    def init(self, name):
        self.name = name
    
    def get_name(self):
        name = input('What is your name? ')
        return name


if __name__ == "__main__":
    name =  Greeting().get_name()
    print(f'Hello {name}, nice to meet you!')
