from Cyborg import Cyborg

cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.global_state()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
#cyborg.digest()