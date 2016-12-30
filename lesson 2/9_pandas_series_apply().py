import pandas as pd

states = pd.Series([
    'California',
    'OH',
    'Michigan',
    'NY'
])

# I want: 'CA', 'OH', 'MI', 'NY'
def clean_state(state):
    if len(state) == 2:
        return state
    elif state == 'Alabama':
        return 'AL'
    elif state == 'California':
        return 'CA'
    elif state == 'Michigan':
        return 'MI'
        # ...

clean_states = []
for state in states:
    clean_states.append(clean_state(state))

clean_states = pd.Series(clean_states)
clean_states = states.apply(clean_state)

# Change False to True to see what the following block of code does

# Example pandas apply() usage (although this could have been done
# without apply() using vectorized operations)
if True:
    s = pd.Series([1, 2, 3, 4, 5])
    def add_one(x):
        return x + 1
    print s.apply(add_one)

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def reverse_name(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    return last_name + ", " + first_name

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".
    
    Try to use the Pandas apply() function rather than a loop.
    '''
    '''
    reversed_names = []
    for name in names:
        first_name = name.split()[0]
        last_name = name.split()[1]
        name = last_name + ", " + first_name
        reversed_names.append(name)
    return reversed_names
    '''
    return names.apply(reverse_name)

print reverse_names(names)
