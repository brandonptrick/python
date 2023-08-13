

def add_dog():
    dogs = ['Marley','Chewy','Ginger']
    print('The current list is: ')
    print(*dogs, sep = ', ')
    add_name = input('Add a dogs name: ')
    new_dog = {'new':add_name}
    return new_dog

def new_list(new):
    dogs = ['Marley','Chewy','Ginger']
    dogs.append(new)
    print(f'Youve added "{new}" to the list! The new list is: ')
    return dogs

user_dog = add_dog()
result = new_list(user_dog['new'])
print(*result, sep = ', ')



