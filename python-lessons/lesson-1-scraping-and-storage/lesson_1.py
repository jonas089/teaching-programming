# this lesson is about reading from,- and writing to files in Python


'''
    open your console and run 'pip3 install pickle' before trying to run this program
    'picke' is a dependency (code written by someone else) that you can import using 'pip'.
    pip ist the standard python package manager
    import os, pickle
'''

import os


# create file if it doesn't exist
path_to_file = "data/data.dat"
'''
if not os.path.exists(path_to_file):
    open(path_to_file, "x")
    print("File was created!")
else:
    print("File already exists!")


# write text to file
text = "Hi, I am Jonas :D"

with open(path_to_file, "w") as my_file:
    my_file.write(text)
    print("Text was written to file!")

# read the text from the file
with open(path_to_file, "r") as my_file:
    content = my_file.read()
    print("The content of the file is: ", content)
'''

# introduction to dictionaries (or a hashmap)
'''
    a dictionary is a datastructure to store key,- value pairs.
'''
dog_ages = {}
# molly is 1.5 years old
dog_ages['molly'] = 1.5
dog_ages['django'] = 7
#print(dog_ages)

mollys_age = dog_ages['molly']
#print("Molly is {} years old".format(mollys_age))

# dog_ages datastructure was created and filled with 2 data entries (molly's age and django's age)

# next we want to save our dictionary to the data.dat file
# for that purpose, we will use the 'pickle' library
import pickle
'''
pickle is used to serialize and deserialize data (convert a dictionary or other data structures to bytes)
'''
with open(path_to_file, "wb") as my_file:
    pickle.dump(dog_ages, my_file)


'''
read the dictionary (dog_ages) from the file and deserialize it to obtain values
'''
with open(path_to_file, "rb") as my_file:
    dog_ages = pickle.load(my_file)
    print("Molly's age: ", dog_ages['molly'])


# Example of a more complex dictionary for a real world API
preise = {"cardano": {"usd": 0.23, "euro": 0.21}}

cardano_preis_usd = preise["cardano"]["usd"]
cardano_preis_euro = preise["cardano"]["euro"]

print("Cardano preis USD: ", cardano_preis_usd)
print("Cardano preis EUR: ", cardano_preis_euro)

# Use the 'requests' library to query the API for the price of Bitcoin
import requests, time, json
api = "https://api.coingecko.com/api/v3/simple/price"
timeout = 10

'''
start_time = time.time()
runtime = 100
while time.time() < start_time + runtime:
    dictionary_as_string = requests.get("{}?ids=bitcoin&vs_currencies=usd".format(api)).text    # the .text grabs the text response 
                                                                                    #(if you don't do this you'll instead get the status code of the request)
    actual_dictionary_object = json.loads(dictionary_as_string)
    print("Bitcoin price: ", actual_dictionary_object["bitcoin"]["usd"], "$")
    time.sleep(timeout)
'''
