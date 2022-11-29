#Dictionary.py
#author:amy
#date:08.11.22


dictionary_1 = {"V344LDA":2000,
                "J245DWE":6350,
                "K265QWS":500}

print(dictionary_1)

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
    }

cities ={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonvile'
    }

cities['NY']= 'New York'
cities['OR'] = 'Portland'

print(cities)
print('-' * 10)
print(cities['NY'])

print('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
    print("{0} has the city {1}".format(abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("{0} state is abbreciated {1} and has city {2}".format(state, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

    city = cities.get('TX', 'Does Not Exist')
    print("The city for the state 'TX' is: {0}".format(city))
    
