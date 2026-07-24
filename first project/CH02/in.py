print('P' in 'Python')
print('x' not in 'Python')
print(1 in [1, 2, 3])
print(2 not in [1, 2, 3])
print('.....')
import decimal
x = 2.5 ; y = 2.5
print(id(x), id(y))
print(x is y, x == y)
z = decimal.Decimal('2.5')
print(id(z))
print(z is x, z == x)