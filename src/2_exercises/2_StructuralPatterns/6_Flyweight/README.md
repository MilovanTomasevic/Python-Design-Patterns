## Flyweight Coding Exercise
You are given a class called `Sentence` , which takes a string such as `'hello world'`. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

```py
sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
```