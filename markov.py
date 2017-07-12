"""Generate Markov text from 2 text files."""

from random import choice
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
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
    #n = 5
    words = text_string.split()
    #split() defaults to splitting at white space

    for i in range(len(words)):
    # using range turns it into a list of indices to loop through
    # rather than looping over the words, allowing you to access
    # + 1 or +2 for example
        key = tuple(words[i:n+i % len(words)])
        #key = (words[i], words[(i + 1) % len(words)])
        # assigning a tuple to the var 'key', which is the first
        # two words in the list of words. using % allows you to
        # loop around from the end back to the beginning. this won't
        # have an effect until you are at the end of the list i.e.
        # 5 % len(words) =
        if key not in chains:
        #if the key isn't in the dictionary:
            chains[key] = []
            #add an empty list as the value
        chains[key].append(words[(i + n) % len(words)])
        # add the 3rd word to the value list. this also uses mod
        # to loop over the end of the list
    chains[key].append(None)

    return chains


def make_text(chains, n):
    """Return text from chains."""

    random_keys = chains.keys()
    #makes a list of all keys in the dictionary 'chains'
    #n = 5
    while True:

        random_key = choice(random_keys)
        #chooses a random key from the list of keys

        words = list(random_key[:n])

        #stores the tuple in a list
        if words[0].istitle() is not True:
        #if the first word isn't title case, keep trying
            continue
        else:
            break

    while True:
        if words[-1][-1] in ('?!.'):
            break
        if random_key not in chains:
            break
        third_word = choice(chains[random_key])

        if third_word is None:
            words = words[:-1]
            break

        words.append(third_word)


        random_key = (random_key[1:] + (third_word,))

    return " ".join(words)


input_path_1 = sys.argv[1]
input_path_2 = sys.argv[2]
input_path_3 = sys.argv[3]
n = 4

# Open the files and turn them into one long string
input_text = open_and_read_file(input_path_1, input_path_2)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text

#still need to change n from being hard coded!