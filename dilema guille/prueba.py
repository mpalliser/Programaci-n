def fix_machine(escombrera, producto):
    mensajeError = "Give me something that's not useless next time."
    
    posicion = 0
 
    
    while posicion <= len(producto):
        if escombrera.find(producto[posicion]) == -1:
            return mensajeError
        elif posicion == len(producto)-1:       
            return producto
        posicion +=1




# TEST CASES funcion fix_machine
print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
print("Test case 5: ", fix_machine('matrix reloaded', 'dedo mixta lordo') == 'dedo mixta lordo')