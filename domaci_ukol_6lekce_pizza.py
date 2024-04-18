#Domaci ukol Rozvazka Pizzy Jitka Baldwin

class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Objednana {self.name} v cene {self.price} "
    
class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

#Přidává dodatečný atribut: ingredients (slovník, kde klíče jsou názvy ingrediencí a hodnoty jejich množství v gramech).
#mplementujte metodu add_extra pro přidání extra ingrediencí do pizzy. Tato metoda by měla odpovídajícím způsobem
# Napište metodu __str__ tak, aby zahrnovala seznam ingrediencí a celkovou cenu.

    def __str__(self):
        return super().__str__() + f""   
    

#Třída Drink (dědí z Item)

class Drink(Item):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return super().__str__() + f" Napoj {self.name} o objemu {self.volume}"    

margarita = Item("Margarita", 245 )
cola = Drink("Cola", 1.5, 500)
print(margarita)
print(cola)
