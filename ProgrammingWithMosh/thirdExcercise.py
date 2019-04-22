# Find the most repeated character in a sentence or a phrase

sentence = """This is a common interview question
Who is your father?
What is your occupation?
Where do you live?
How do you assess your skills?
"""


def MostRepeatedChar(phrase):

    table = dict()
    for ch in phrase:
        if ch in table:
            table[ch] += 1
        else:
            table[ch] = 1

    char_frequency = sorted(
        table.items(),
        key=lambda key_value: key_value[1],
        reverse=True)

    return (char_frequency[0])

print(MostRepeatedChar(sentence))
