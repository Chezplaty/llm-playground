import re

with open("training_data.txt", 'r', encoding="utf-8") as file:
    raw_text = file.read()

result = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
result = [i for i in result if i.split()]
print(len(result))
print(result[:30])