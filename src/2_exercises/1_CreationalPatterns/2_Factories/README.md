## Factory Coding Exercise
You are given a class called `Person` . The person has two attributes: `id` , and `name` .

Please implement a  `PersonFactory` that has a non-static  `create_person()`  method that takes a person's name and return a person initialized with this name and an id.

The `id` of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.