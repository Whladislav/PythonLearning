def info(name='unknown', color='white', price=0):
    print('Object:', name, sep='\t')
    print('Color:', color, sep='\t')
    print('Price:', price, sep='\t')
    print()


info('pen', 'blue', 1)

info(color='red', name='pen', price=2)

info('pen', price=1, color='blue')

info('pen')
