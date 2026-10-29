from person import Person
from datetime import date

person = Person("Matthew Eduardo Romero", date(2007,10,29))

print(person.initials())

print(person.is_birthday())