

class Contact:

    def __init__(self, first_name, last_name, number, chosen=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.number = str(number)
        self.chosen = chosen
        if self.chosen:
            self.chosen_str = 'да'
        else:
            self.chosen_str = 'нет'
        self.other = args
        self.other_info = ''
        self.other_2_info = ''
        if self.other:
            count = 0

            while count < len(self.other):
                self.other_info = self.other_info + '\n' + self.other[count]
                count += 1


        self.other_2 = str(kwargs).replace('{', '}').replace('}', '').replace("'", "").split(', ')
        if self.other_2:
            count = 0

            while count < len(self.other_2):
                self.other_2_info = self.other_2_info + '\n' + self.other_2[count]
                count += 1

    def __str__(self):
        self.output = 'Имя: ' + self.first_name + '\nФамилия: ' + self.last_name + '\nТелефон: ' + self.number\
                      + '\nВ избранных: ' + self.chosen_str + '\nДополнительная информация:\n' + \
                      self.other_2_info + self.other_info
        return self.output



# с контактом закончил

class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.numbers = []

    def add(self, contact):
        self.numbers.append(contact)

    def __str__(self):
        line = self.name
        return line

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(jhon)
home = PhoneBook('home')
home.add(jhon)
print(home)
print(home.numbers)

