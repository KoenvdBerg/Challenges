#! /usr/env/bin python3

class Word:
    def __init__(self, word):
        self.word = word
        self.subwords = [word[0:i] for i in range(len(word)+1)]
        
class AutoComplete:
    def __init__(self):
        self.data = []
        self.result = []

    def build(self, inputwords):
        for word in inputwords:
            self.data.append(Word(word))

    def find(self, inputsubword):
        for w in self.data:
            if inputsubword in w.subwords:
                self.result.append(w.word)

        


if __name__ == "__main__":
    input = ["hello", "help", "hooray", "foo", "bar", "falcon"]

    test = AutoComplete()
    test.build(input)
    test.find("h")
    print(test.result)
    