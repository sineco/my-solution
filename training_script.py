from datasets import load_dataset
from transformers import AutoTokenizer

data_files = {"train": "updated_train.json",
              "test": "updated_test.json"}

raw_datasets =  load_dataset("json", data_files=data_files )

# Define the label set
label_set = ['O', 'B-PLATFORM', 'I-PLATFORM', 'B-TIME', 'I-TIME', 'B-DATE', 'I-DATE']

# Rename some columns
raw_datasets = raw_datasets.rename_column("ner_tags", "labels")
raw_datasets = raw_datasets.rename_column("tokens", "words")

# Tokenize the model


model_checkpoint = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

print(tokenizer.is_fast)

inputs = tokenizer(raw_datasets["train"][0]["words"], is_split_into_words=True)
print(inputs.tokens())
print(inputs.word_ids())

def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            # Start of a new word!
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            # Special token
            new_labels.append(-100)
        else:
            # Same word as previous token
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels

labels = raw_datasets["train"][0]["labels"]
word_ids = inputs.word_ids()
print(labels)
print(align_labels_with_tokens(labels, word_ids))

#raw_datasets_conll = load_dataset("conll2003")
#print(raw_datasets_conll)

# For the future we could store the data in a remote server
# url = "https://github.com/crux82/squad-it/raw/master/"
#data_files = {
#    "train": url + "SQuAD_it-train.json.gz",
#    "test": url + "SQuAD_it-test.json.gz",
#}
#squad_it_dataset = load_dataset("json", data_files=data_files, field="data")

#print(raw_datasets['test'][0]['test'][0]['tokens'])
# print(raw_datasets['train'][0]['tokens'])
print(raw_datasets['train'][0]['labels'])
# print(raw_datasets['train'].features["ner_tags"])


print('#######################')
#tasets_conll['train'][0])
# example = raw_datasets['train'][0]
# print(example.keys())
# ner_feature = raw_datasets_conll["train"].features["ner_tags"]
# print(ner_feature)
