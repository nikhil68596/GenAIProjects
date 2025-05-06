# Assignment: Exploring String Methods

# Task 1: String Slicing and Indexing
string = "Python is amazing!"

# Derive the results below
print("First word: " + string[:6]) # First 6 characters of the string
print("Amazing part: " + string.split()[-1]) # The word amazing
print("Amazing part: " + string[::-1]) # Reversed string

# Task 2: String Methods
new_string = " hello, python world! "
# Performing each operation separately.
print("Stripped string ->" + new_string.strip())
#Secon task -> Capitalizing the first letter of the string
capita_string = new_string #Store the original value of new string
#Find the first alphabet character.
for i in range(len(capita_string)):
    if capita_string[i].isalpha():
        #New string = chars before + current char to uppercase + chars after
        capita_string = capita_string[0:i] + capita_string[i].capitalize() + capita_string[i+1:]
        break
print("Capitalized string ->" + capita_string)
print("String when replacing world with universe ->" + new_string.replace("world", "universe")) 
print("Uppercase string ->" + new_string.upper()) 

# Task 3: Check for Palindromes
word = input("Please enter a word: ")
# Check to see if the word is the same word when read backwards.
result = f"Yes, {word} is a palindrome!" if word == word[::-1] else f"No, {word} is not a palindrome!"
print(result)