from string import punctuation

sample = input("Enter a sentence: ")
sample = sample.title().replace(" ", "")

hash_list = [i for i in sample if i not in punctuation]

print(f"Your hashtag is {"#" + "".join(hash_list)[:140]}")