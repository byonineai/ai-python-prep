# 8-9. Magicians: Make a list of magician’s names .
# Pass the list to a function called show_magicians(),
# which prints the name of each magician in the list .

# For All elements in S, print(m)

def show_magicians(names):
    for name in names:
        print(name)

def make_great(magicians):
    '''
    Modify the list in place by adding 'the Great" to each magician's name
    '''
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"

magicians = ['Marcelo','Marcio','Angel']

make_great(magicians)

show_magicians(magicians)
