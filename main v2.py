

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
        self.members = []

    def add(self, contact):
        self.members.append(contact)

    def __str__(self):
        line = 'Записная книжка "' + self.name + '" содержит ' + str(len(self.members)) + ' записей'
        return line

    def output_pbook(self):
        print('Записная книжка', self.name)
        for member in self.members:
            print(member, '\n')

    def delete_number(self, number):
        count = 0
        for member in self.members:
            if number == member.number:
                self.members.pop(count)
            count += 1

    def all_chosen_numbers(self):
        chosen_numbers = []
        for member in self.members:
            if member.chosen:
                chosen_numbers.append(member)
        print('Количество избранных контактов -', len(chosen_numbers))
        for chosen in chosen_numbers:
            print(chosen)

    def find_contact(self, name, last_name):
        find = False
        for member in self.members:
            if member.first_name.capitalize() == name.capitalize() and member.last_name.capitalize() == last_name.capitalize():
                print(member)
                find = True
        if find == False:
            print('Данного контакта нет в записной книжке')

    def find_contact_v2(self, name):
        name = name.split(' ')
        find = False
        for member in self.members:
            if member.first_name.capitalize() == name[0].capitalize() and member.last_name.capitalize() == name[1].capitalize():
                print(member)
                find = True
        if find == False:
            print('Данного контакта нет в записной книжке')


asd = 'asd'
asd.capitalize()
jhon = Contact('Jhon', 'Smith', '+71234567809', True, telegram='@jhony', email='jhony@smith.com')
sara = Contact('Sara', 'Smith', '+71234877809', telegram='@sara', email='sara@smith.com')

home = PhoneBook('home')
home.add(jhon)
home.add(sara)

home.find_contact('jhon', 'smith')
home.find_contact_v2('jhon smith') #не знаю какую надо оставить

