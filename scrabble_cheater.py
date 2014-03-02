import sys
from scrabble import wordlist, scores

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >>sys.stderr, "Usage: scrabble.py [RACK]"
        sys.exit(1)

    rack = set(sys.argv[1].lower()) #Constant time membership checking
    valid_words = []
    un = sys.argv[1].count('?')

    for word in wordlist:
        # Make a copy of the rack for every new word, so we can manipulate it
        # without compromising the original rack.
        available_letters = set(rack)
        unknowns = un

        for letter in word.lower():
            if letter not in available_letters and unknowns == 0:
                break
            if unknowns != 0 and letter not in available_letters:
                unknowns -= 1
            else:
       	        available_letters.remove(letter)
        else:
            # Calculate the Scrabble score.
            score = 0
            for letter in word:
                score = score + scores[letter]
            valid_words.append((score, word))

    for play in sorted(valid_words, reverse=True):
        print play[0], play[1]
