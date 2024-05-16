from core.__init__ import *

print('SPECIES SEARCH \n')

#get species'
print('WHITING')
print(Species(species='whiting', debug=True, extensive_info=True).species_search())

# extensive_search
# print('\n\n Wombat (extensive)')
# print(Species(species='wombat', debug=True, extensive_search=True).species_search())

# # search for a grass hopper
# print('\n\n Agaricus bisporus (different kingdom)')
# print(Species(kingdom='fungi', species='Agaricus bisporus', family='Agaricaceae', debug=True).get_species())


# print('\n\n list all fish species')
# print(Species(debug=True, species="fish").species_search())

# print('\n\n SURVEYS \n')

# print(Surveys(projids=1, debug=True).get_surveys())