# class Animal:
#      def __init__(self, specie, an):
#          self.specie = specie
#          self.an = an
#
# Mamifer = Animal("Feline", 3)
# print(Mamifer.specie, Mamifer.an)
#
# class Pisica(Animal):
#     def __init__(self, specie, an, race):
#         self.race = race
#         super().__init__(specie, an)
#
#     def sound(self):
#         self.sound = "miau"
#         return self.sound
#
# pisica = Pisica(specie="felina", an=4, race="nigga")
# print(pisica.specie, pisica.an, pisica.race, pisica.sound())



# class Calculator:
#     def __init__(self, numarul1, numarul2):
#         self.nr1 = numarul1
#         self.nr2 = numarul2
#         try:
#             print(float(numarul1/numarul2))
#         except TypeError:
#             print("Loh ai scris gresit")
#         except ZeroDivisionError:
#             print("Loh ai impartit la 0")
#         else:
#             print("Caroci maladet")
#
# calculator = Calculator(4, 1)


