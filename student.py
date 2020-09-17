# Ecrire en python des classes qui respectent les conditions suivantes:
# - Un étudiant a un nom
# - Un étudiant a plusieurs notes
# - Une notes a une valeur (integer)
# Ecrire la méthode qui permet de retrouver toutes les notes associées à un étudiants et de faire la moyenne

from datetime import date
from random import *
from statistics import mean


class Student:

    def __init__(self, fname: str, lname: str):
        self.vivant = True
        self.fname = fname
        self.lname = lname        
        self.notes = []
   
    def average(self):
        self.avenote = mean(self.notes)
        print(f"{self.fname} has an average note {self.avenote}")

    def result(self):
        self.realNote = randint(0, 10)
        print(f"{self.fname} has {self.realNote} /10 !")
        self.notes.append(self.realNote)


maxim = Student("Maxim", "Novikov")
print(maxim.__dict__)

maxim.result()
maxim.result()
maxim.result()
maxim.average()
