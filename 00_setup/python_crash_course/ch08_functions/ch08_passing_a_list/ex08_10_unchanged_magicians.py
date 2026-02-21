def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """
    Return a NEW list where each name has 'the Great' added, without modifying the original list.
    """
    great_magicians = []
    for magician in magicians:
        great_magicians.append(f"{magician} the Great")
    return great_magicians

magicians = ['Marcelo','Marcio','Angel']
# Note: This copy will point to a different memory location
# Make a "great" copy
great_magicians = make_great(magicians[:])

print("Original list:")
show_magicians(magicians)

print("\nGreat list (copy):")
show_magicians(great_magicians)