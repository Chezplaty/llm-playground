import re

class SimpleTokenizer:
    def __init__(self, vocab: dict):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text) -> list[str]:
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [i for i in preprocessed if i.split()] #no white spaces
        preprocessed = [i if i in self.str_to_int else "<|unk|>" for i in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids: list[int]) -> str:
        text = " ".join([self.int_to_str[num] for num in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text


with open("training_data.txt", 'r', encoding="utf-8") as file:
    raw_text = file.read()

result = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
preprocessed = [i for i in result if i.split()]
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

#assign each unique token an id/number
vocab = {token: i for i, token in enumerate(all_tokens)}

tokenizer = SimpleTokenizer(vocab)
text = "Cheese is cool, but it is way better grilled. <|endoftext|> Hello 8DD"
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))