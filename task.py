# Create a public function, which would generate a dictionary with 10 random key, value pairs. 
# Keys have to be a random letter. They can't repeat themselves.
# A value must be a random number. They can't repeat themselves.
# Return: A key with largest value.


from email.contentmanager import raw_data_manager
import random, string



# def dict_generator():
#     size = 10
#     keys = random.sample(string.ascii_lowercase, size)
#     value = [random.randint(1, 30) for _ in range(size)]
#     result = dict(zip(keys, value))
#     return result


# print(dict_generator())
    

def dict_generator():
    my_dictionary = {}
    while True:
        random_letter = random.choice(string.ascii_lowercase)
        random_number = random.randint(1, 30)
        if random_number not in my_dictionary.values():
            my_dictionary[random_letter] = random_number
        
        if len(my_dictionary) >= 10:
            break   
    print(my_dictionary)
    return max(my_dictionary, key=my_dictionary.get)


print(dict_generator())


    
    
    
    # random_keys = []
    # random_values = []
    # for _ in range (0, 10):
    #     n = random.randint(1, 100)
    #     random_values.append(n)

    # for _ in range (0, 10):
    #     n = string.ascii_letters
    #     random_values.append(n)

    


