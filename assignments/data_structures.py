# Assignment: Hands on Python Data Structures
# Task 1 - Working with Lists
fruits = ['apple', 'banana', 'cherry', 'date', 'grape'] #Create the list of fruits
print("Original list: " + f"{fruits}")
fruits.append("fig") #Add a fruit
print("After adding a fruit: " + f"{fruits}")
fruits.remove("apple") #Remove a fruit
print("After removing a fruit: " + f"{fruits}")
#Reverse the list of fruits at the end + print it out.
print("Reversed list: " + f"{fruits[::-1]}")

# Task 2 - Exploring Dictionaries
#Creating a dictionary with following keys
profile = {"name": "Nikhil Munagala",
           "age": 21,
           "city": "New Brunswick"}
#Create new favorite color for profile.
profile["favorite color"] = "blue"
#Update the value for the city key.
profile["city"] = "Hoboken"
#Join the keys from profile together.
print("Keys: " + ", ".join(profile.keys()))
#Map each value into a string and then join them together.
print("Values: " + ", ".join(map(str, profile.values())))

# Task 3 - Using Tuples
favorites = ('Extraction', 'Not Like Us', 'To Kill a Mockingbird')
print("Favorite things: " + f"{favorites}")
# Changing one of the elements in tuple
try:
    favorites[0] = 'Inception'
except TypeError:
    print("Oops! Tuples cannot be changed.")
print("Length of tuple: " + f"{len(favorites)}")