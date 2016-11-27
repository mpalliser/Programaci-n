
dinero = int (input("Introduce una cantidad de dinero "))

billete_100 = dinero // 100
dinero = dinero % 100

billete_50 = dinero // 50
dinero = dinero % 50
        
billete_20 = dinero // 20
dinero = dinero % 20
        
billete_10 = dinero // 10
dinero = dinero % 10

billete_5 = dinero // 5
dinero = dinero % 5

billete_1 = dinero // 1
dinero = dinero % 1

print (billete_100, billete_50, billete_20, billete_10, billete_5, billete_1)
