## Memento Coding Exercise
A `TokenMachine`  is in charge of keeping tokens. Each `Token`  is a reference type with a single numerical value. The machine supports adding tokens and, when it does, it returns a memento representing the state of that system _at that given time_.

You are asked to fill in the gaps and implement the Memento design pattern for this scenario. Pay close attention to the situation where a token is fed in as a reference and its value is subsequently changed on that reference - you still need to return the correct system snapshot!