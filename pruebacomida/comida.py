import xml.etree.cElementTree as ET
tree = ET.parse('comida.xml')
root = tree.getroot()

menu = {}

for food in root.findall('food'):
    name = (food.find('name').text)
    price = (food.find('price').text)
    menu [name] = price

assert len(menu) == 5
assert isinstance (menu , dict)
for name, price in menu.items():
    print ("Plato: " + name + "\nPrecio: " + price + "\n")
  
