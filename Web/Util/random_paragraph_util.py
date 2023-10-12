import random

class RandomParagraphGenerator:
    def __init__(self, num_paragraphs=3, min_sentences=3, max_sentences=7, min_words=5, max_words=15):
        self.num_paragraphs = num_paragraphs
        self.min_sentences = min_sentences
        self.max_sentences = max_sentences
        self.min_words = min_words
        self.max_words = max_words

        # Define sample words to generate sentences
        self.words = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"]

    def generate_sentence(self):
        num_words = random.randint(self.min_words, self.max_words)
        sentence = " ".join(random.sample(self.words, num_words))
        return sentence

    def generate_paragraph(self):
        num_sentences = random.randint(self.min_sentences, self.max_sentences)
        paragraph = " ".join(self.generate_sentence() for _ in range(num_sentences))
        return paragraph

    def generate_paragraphs(self):
        paragraphs = [self.generate_paragraph() for _ in range(self.num_paragraphs)]
        return paragraphs
