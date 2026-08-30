import re

with open("training_data.txt", 'r', encoding="utf-8") as file:
    raw_text = file.read()

result = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
preprocessed = [i for i in result if i.split()]
all_words = sorted(list(set(preprocessed)))

#assign each unique token an id/number
vocab = {token: i for i, token in enumerate(all_words)}
