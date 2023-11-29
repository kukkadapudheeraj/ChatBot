from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

model_name = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

class Chitchat:

    def __init__(self):
        pass

    def chat(message):
        user_input = message
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response

