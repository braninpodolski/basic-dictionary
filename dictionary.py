import json
from difflib import get_close_matches

def main(word):
    # Load JSON file into dict
    dictionary = json.load(open('data.json', 'r'))
    
    # If word exists, return defintion(s)
    if word in dictionary:
        return('\n'.join(dictionary[word]))

    # If proper noun, return defition(s)
    elif word.title() in dictionary:
        return('\n'.join(dictionary[word.title()]))

    # If acronym, return defition(s)
    elif word.upper() in dictionary:
        return('\n'.join(dictionary[word.upper()]))

    # Check if word is misspelled and correct it
    elif len(get_close_matches(word, dictionary.keys(), 1, 0.8)) > 0:
        corrected = get_close_matches(word, dictionary.keys(), 1, 0.8)[0]

        # Ask for user confirmation and recursively run the function if accepted
        ask = input('Did you mean %s? Enter Y if yes, or N if no: ' % corrected).lower()
        if ask == 'y':
            return('\n'.join(dictionary[corrected]))
        elif ask == 'n':
            return('Word does not exist. Please check word.')
        else:
            return("We didn't understand your entry")

    # If word does not exist (and doesn't meet similarity threshold), return error
    else:
        return('Word does not exist. Please check word.')

# Ask for user input and run function
word = input('Enter Word: ').lower()
print(main(word))