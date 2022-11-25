ax = float(input('Введите координаты точки a по оси x: '))
ay = float(input('Введите координаты точки a по оси y: '))
bx = float(input('Введите координаты точки b по оси x: '))
by = float(input('Введите координаты точки b по оси y: '))

distans = round(((ax-bx)**2+(ay-by)**2)**0.5, 2)
print(f'Растояние между точками a и b равно {distans}' )