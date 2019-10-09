#If the number of rails is greater than the length of the message then it will break down into plaintext and could easily be seen.
#If the number of rails divides evenly into the message length then the message will have spaces in the columns and would be harder to break.
def wordPop(text, n):
    nwords = []

    words = text.split()

    for word in words:

        if (len(word) == n):
            nwords.append(word)

    return (nwords)
w = 'This is a test for a length of words of different sizes'
print(wordPop(w.lower(), 5))
