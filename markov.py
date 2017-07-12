"""Generate Markov text from 2 text files."""

from random import choice
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes string that are file names, opens the files, and turns
    the files' contents into one string of text.
    """

    contents1 = open(file_path1).read()
    contents2 = open(file_path2).read()

    contents = contents1 + contents2

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # split() defaults to splitting at white space
    words = text_string.split()

    # using range turns it into a list of indices to loop through
    # rather than looping over the words, allowing you to access
    # + 1 or +2 for example
    for i in range(len(words)):
        # assigning a tuple to the var 'key', which is the first
        # n words in the list of words. using % allows you to
        # loop around from the end back to the beginning. this won't
        # have an effect until you are at the end of the list
        key = tuple(words[i:n+i % len(words)])

        #if the key isn't in the dictionary:
        if key not in chains:
            #add an empty list as the value
            chains[key] = []
        # add the 3rd word to the value list. this also uses mod
        # to loop over the end of the list
        chains[key].append(words[(i + n) % len(words)])
    # adds None value to the end for a stopping point
    chains[key].append(None)
    # return the filled up dictoinary
    return chains


def make_text(chains, n):
    """Return text from chains."""

    # makes a list of all keys in the dictionary 'chains'
    random_keys = chains.keys()

    while True:
        # chooses a random key from the list of keys
        random_key = choice(random_keys)
        # stores the tuple in a list from beginning to n
        words = list(random_key[:n])
        # if the first word isn't title case, keep trying
        if words[0].istitle() is not True:
            continue
        else:
            break

    while True:
        # checks if the last letter of the last word is any of these chars
        if words[-1][-1] in ('?!.'):
            break
        # checks if the key is in the dictionary yet
        if random_key not in chains:
            break
        # adds the next word randomly
        next_word = choice(chains[random_key])

        # checks if the word is None and ends the markov chain
        if next_word is None:
            words = words[:-1]
            break

        # adds the next word to the markov chain
        words.append(next_word)

        # rebinds the random key
        random_key = (random_key[1:] + (next_word,))
        
    # returns the list of words split by a space
    return " ".join(words)

# takes in the first file to be read
input_path_1 = sys.argv[1]
# takes in the second file to be read
input_path_2 = sys.argv[2]
# converts the 3rd argument to int
n = int(sys.argv[3])

# Open the files and turn them into one long string
input_text = open_and_read_file(input_path_1, input_path_2)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text