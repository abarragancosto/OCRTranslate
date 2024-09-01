from transformers import MarianMTModel, MarianTokenizer

class TextTranslator:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-es"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate_text(self, text):
        sentences = self._split_text_into_sentences(text)
        translated_sentences = []
        for sentence in sentences:
            encoded = self.tokenizer(sentence, return_tensors="pt", padding=True, truncation=True, max_length=512)
            generated_tokens = self.model.generate(**encoded)
            translated_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
            translated_sentences.append(translated_text)
        return '. '.join(translated_sentences)

    def _split_text_into_sentences(self, text):
        return text.split('. ')
