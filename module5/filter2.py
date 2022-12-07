matches = [
    {
    'casa': 'Francia',
    'visitante': 'Korea',
    'casa_score': 0,
    'visitante_score': 2,
    'home_result': 'Win'
    },
    {
    'casa': 'Colombia',
    'visitante': 'Mexico',
    'casa_score': 1,
    'visitante_score': 1,
    'home_result': 'Draw'
    },
    {
    'casa': 'Italia',
    'visitante': 'España',
    'casa_score': 3,
    'visitante_score': 2,
    'home_result': 'Win'
    },
]
new_list =  list(filter(lambda item: item['home_result'] == 'Win', matches))

print(new_list[0]['casa'], new_list[1]['casa'])
print(f'los ganadores hasta el momentos son:')

for i in range(2):
    print(new_list[i]['casa'])