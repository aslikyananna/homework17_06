# homework17_06
Write a Python program that takes a string as input and counts the frequency of each word in the string. The program should store the word frequencies in a dictionary and display the result.

Here are the steps to follow:

Prompt the user to enter a sentence or a paragraph.

Remove any punctuation marks from the input string (e.g., commas, periods, exclamation marks).

Convert the string to lowercase to make the word frequency case-insensitive.

Split the string into a list of words using the split() method.

Create an empty dictionary to store the word frequencies.

Iterate over the list of words and update the dictionary with the frequency of each word. If a word is already in the dictionary, increment its count by 1. If it’s not in the dictionary, add it as a new key with a value of 1.

Display the word frequencies in alphabetical order, along with their corresponding counts.

Example : 
Input : "This is a sample sentence. This sentence is a sample."
Output: 
a: 2
is: 2
sample: 2
sentence: 2
this: 2


Create a phone book program that allows users to store and retrieve contact information. The program should use dictionaries and lists to store the data.

Implement a menu-based system that provides the following options:

Add a new contact: Prompt the user to enter a name and phone number, and add them to the phone book dictionary as a key-value pair.

Search for a contact: Prompt the user to enter a name, and display the corresponding phone number from the phone book dictionary.

List all contacts: Display all the contacts in the phone book, showing both the names and phone numbers.

Exit the program: Terminate the program.

Continuously prompt the user for their choice until they choose to exit the program.

Phone Book Program
------------------
1. Add a new contact
2. Search for a contact
3. List all contacts
4. Exit

Enter your choice: 1

Enter name: James
Enter phone number: 123456789

Contact added successfully!

Enter your choice: 2

Enter name: James
Phone number: 123456789

Enter your choice: 3

Contacts:
James: 123456789

Enter your choice: 4

Goodbye!



















