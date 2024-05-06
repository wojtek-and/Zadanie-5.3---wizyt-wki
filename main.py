from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, imię, nazwisko, telefon, email):
        self.imię = imię
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

        # Variables
        self._label_length = 0

    def __str__(self):
        return f'{self.imię} {self.nazwisko} {self.telefon} {self.email}'
    
    def __repr__(self):
        return f"BaseContact(imię={self.imię}, nazwisko={self.nazwisko}, telefon={self.telefon}, email={self.email})"
    
    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imię} {self.nazwisko}")
    
    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = value + 1
                    

class BusinessContact(BaseContact):
    def __init__(self, telefon_służbowy, stanowisko, nazwa_firmy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telefon_służbowy = telefon_służbowy
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy

    def __str__(self):
        return f'{self.imię} {self.nazwisko} {self.telefon} {self.email} {self.telefon_służbowy} {self.stanowisko} {self.nazwa_firmy}'
    
    def __repr__(self):
        return f"BusinessContact(imię={self.imię}, nazwisko={self.nazwisko}, telefon={self.telefon}, email={self.email}, telefon_służbowy={self.telefon_służbowy}, stanowisko={self.stanowisko}, nazwa_firmy={self.nazwa_firmy})"
    
    def contact(self):
        print(f"Wybieram numer {self.telefon_służbowy} i dzwonię do {self.imię} {self.nazwisko}")


contacts = []


def create_contacts(type, how_many):
    for i in range(how_many):
        if type == "BaseContact":
            contacts.append(BaseContact(
                imię=fake.first_name(),
                nazwisko=fake.last_name(),
                telefon=fake.phone_number(),
                email=fake.email()
            ))
        elif type == "BusinessContact":
            contacts.append(BusinessContact(
                telefon_służbowy=fake.phone_number(),
                stanowisko=fake.job(),
                nazwa_firmy=fake.company(),
                imię=fake.first_name(),
                nazwisko=fake.last_name(),
                telefon=fake.phone_number(),
                email=fake.email()
            ))


create_contacts(type="BusinessContact", how_many=3)
print(contacts)
contact1 = BaseContact(imię="Karol", nazwisko="Salata", telefon=608354611, email="karolsalata@o2.pl")
contact1.contact()

contact1.label_length = len(contact1.imię) + len(contact1.nazwisko)

print(contact1._label_length)


