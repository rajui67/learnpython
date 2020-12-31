demo = { "__name": 'Raju', 'place': 'Winchester'}
after_dexp = {k:v for k,v in demo.items() if not k.startswith('__')}
print(f'demo = {demo},\nafter_dexp = {after_dexp}')