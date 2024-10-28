# from transformers import GPT2Tokenizer, GPT2Model

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')
# text = "complete this statement ='hey how are you'"
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)

# print(output)

from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Input text
text = "complete this statement ='hey how are you'"

# Encode the input text
encoded_input = tokenizer(text, return_tensors='pt')

# Generate output
output = model.generate(**encoded_input, max_length=50)  # Adjust max_length as needed

# Decode the output to get the text
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

print(decoded_output)
