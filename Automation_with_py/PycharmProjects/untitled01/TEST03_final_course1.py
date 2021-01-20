def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]
    list = []
    frequencies = {}
    string = ""
    for x in file_contents:
        if x.isalpha():
            string += x
        else:
            string += " "
    split = string.split()

    for xword in split:
        if xword.lower() not in uninteresting_words:
            list.append(xword)

    for nword in list:
        if nword not in frequencies:
            frequencies[nword] = 0
        frequencies[nword] += 1

#    return frequency
    return list
#    return string



file_contents = "The strangest figures we saw were the Slovaks, who were more barbarian than the rest, with their big cow-boy hats, great baggy dirty-white trousers, white linen shirts, and"
x = calculate_frequencies(file_contents)
print(x)


