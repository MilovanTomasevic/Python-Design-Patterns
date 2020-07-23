# Python Design Patterns

## Description

- This repository contains an overview of the Gang of Four (GoF) design patterns with modern-day variations, adjustments, and discussions in Python.

## Learning Objectives

- SOLID Design Principles:
  - [Single Responsibility Principle](/src/1_patterns/1_SOLIDDesignPrinciples/1_SingleResponsibility/srp.py)
  - [Open-Closed Principle](/src/1_patterns/1_SOLIDDesignPrinciples/2_Open-Closed/ocp.py)
  - [Liskov Substitution Principle](/src/1_patterns/1_SOLIDDesignPrinciples/3_LiskovSubstitution/lsp.py)
  - [Interface Segregation Principle](/src/1_patterns/1_SOLIDDesignPrinciples/4_InterfaceSegregation/isp.py)
  - [Dependency Inversion Principle](/src/1_patterns/1_SOLIDDesignPrinciples/5_DependencyInversion/dip.py)
- Creational Design Patterns:
  - [Builder](/src/1_patterns/2_CreationalPatterns/1_Builder/)
    - A builder is a separate component for building an object
    - Can either give builder an initializer or return it via a static function
    - To make builder fluent, return self
    - Different facets of an object can be built with different builders working in tandem via a base class
  - [Factories (Factory Method and Abstract Factory)](/src/1_patterns/2_CreationalPatterns/2_Factories/)
    - A factory method is a static method that creates object
    - A factory is an entity that can take care of object creation
    - A factory can be external or reside inside the object as an inner class
    - Hierarchies of factories can be used to create related objects
  - [Prototype](/src/1_patterns/2_CreationalPatterns/3_Prototype/)
    - To implement a prototype, partially construct an object and store it somewhere
    - Deep copy the prototype
    - Customize the resulting instance
    - A factory provides a convenient API for using prototypes
  - [Singleton](/src/1_patterns/2_CreationalPatterns/4_Singleton/)
    - Different realizations of Singleton: custom allocator, decorator, metaclass
    - Laziness is easy, just init on first request
    - Monostate variation
    - Testability issues
- Structural Design Patterns:
  - [Adapter](/src/1_patterns/3_StructuralPatterns/1_Adapter/)
    - Implementing an Adapter is easy
    - Determine the API you have and the API you need
    - Create a component which aggregates (has a reference to, ...) the adaptee
    - Intermediate representations can pile up: use caching and other optimizations
  - [Bridge](/src/1_patterns/3_StructuralPatterns/2_Bridge/1_bridge.py)
    - Decouple abstraction from implementation
    - Both can exist as hierarchies
    - A stronger form of encapsulation
  - [Composite](/src/1_patterns/3_StructuralPatterns/3_Composite/)
    - Objects can use other objects via inheritance/composition
    - Some composed and singular objects need similar/identical behaviors
    - Composite design pattern lets us treat both types of objects uniformly
    - Python supports iteration with \_\_iter\_\_ and Iterable ABC
    - A single object can itself iterable by yielding self from \_\_iter\_\_
  - [Decorator](/src/1_patterns/3_StructuralPatterns/4_Decorator/)
    - A decorator keeps the reference to the decorated object(s)
    - Adds utility attributes and methods to augment the object's features
    - May or may not forward calls to the underlying object
    - Proxying of underlying calls can be done dynamically
    - Python's functional decorators wrap functions; no direct relation to the GoF Decorator Pattern
  - [Façade](/src/1_patterns/3_StructuralPatterns/5_Facade/1_facade.py/)
    - Build a Facade to provide a simplified API over a set of classes
    - May wish to (optionally) expose internals through the facade
    - May allow users to 'escalate' to use more complex API
  - [Flyweight](/src/1_patterns/3_StructuralPatterns/6_Flyweight/)
    - Store common data externally
    - Specify an index or a reference into the external data store
    - Define the idea of 'ranges' on homogeneuous collections and store data related to those ranges
  - [Proxy](/src/1_patterns/3_StructuralPatterns/7_Proxy/)
    - A proxy has the same interface as underlying object
    - To create a proxy, simple replicate the existing interface of an object
    - Add relevant functionality to the redefined member functions
    - Different proxies (communications, logging, caching, etc.) have completely different behaviors
- Behavioral Design Patterns
  - [Chain of Responsibility](/src/1_patterns/4_BehavioralPatterns/1_ChainOfResponsibility/)
    - Chain of responsibility can be implemented as a chain of references or
      a centralized construct
    - Enlist objects in the chain, possibly controlling their order
    - Object removal from chain (e.g., \_\_exit\_\_)
  - [Command](/src/1_patterns/4_BehavioralPatterns/2_Command/)
    - Encapsulate all details of an operation in a separate object
    - Define instruction for applything the command (either in the command itself, or elsewhere)
    - Optionally define instructions for undoing the command
    - Can create composite commands (a.k.a. macros)
  - [Interpreter](/src/1_patterns/4_BehavioralPatterns/3_Interpreter/)
    - Barring simple cases, an interpreter acts in two stages
    - Lexing turns text into a set of tokens
    - Parsing tokens into meaningful construct
  - [Iterator](/src/1_patterns/4_BehavioralPatterns/4_Iterator/)
    - An iterator specified how you can traverse an object
    - Stateful iterators cannot be recursive
    - yield allows for much more succinct iteration
  - [Mediator](/src/1_patterns/4_BehavioralPatterns/5_Mediator/)
    - Create the mediator and have each object in the system refer to it
      - E.g., in a property
    - Mediator engages in bidirectional communication with its connected components
    - Mediator has functions the components can call
    - Components have functions the mediator can call
    - Event processing (e.g., Rx) libraries make communication easier to implement
  - [Memento](/src/1_patterns/4_BehavioralPatterns/6_Memento/)
    - Mementos are used to roll back states arbitrarily
    - A memento is simply a token/handle class with typically no function of its own
    - A memento is not required to expose directly the state(s) to which it reverts the system
    - Can be used to implement undo/redo
  - [Observer](/src/1_patterns/4_BehavioralPatterns/7_Observer/)
    - Observer is an intrusive approach: an observable must provide an event to subscribe to
    - Subsciption and unsubscription with additional/removal of items in list
    - Property notifications are easy: dependent property notifications are tricky
  - [State](/src/1_patterns/4_BehavioralPatterns/8_State/)
    - Given sufficient complexity, it pays to formally define possible states and events/triggers
    - Can define
      - State entry/exit behaviors
      - Action when a particular event causes a transition
      - Guard conditions enabling/disabling a transition
      - Default action when no transitions are found for an event
  - [Strategy](/src/1_patterns/4_BehavioralPatterns/9_Strategy/1_strategy.py/)
    - Define an algorithm at a high level
    - Define the interface you expect each strategy to follow
    - Provide for dynamic composition of strategies in the resulting object
  - [Template](/src/1_patterns/4_BehavioralPatterns/10_Template/1_template_method.py/)
    - Define an algorithm at a high level in parent class
    - Define constituent parts as abstract methods/properties
    - Inherit the algorthm class, providing the necessary ovverides
  - [Visitor](/src/1_patterns/4_BehavioralPatterns/11_Visitor/)
    - OOP double-dispatch approach is not necessary in Python
    - Make a visitor, decorating each 'overload' with @visitor
    - Call visit() and the entire structure gets traversed


## My TOP #11 Methods of Patterns

|  No |                                                  Name                                                 |                                                           Exercise                                                           |                                                        Test                                                        |                                                                                                                  Description                                                                                                                 |
|:---:|:-----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  1. | [ Adapter](/src/1_patterns/3_StructuralPatterns/1_Adapter/)                                           | [ Text and Exercise for Adapter](/src/2_exercises/2_StructuralPatterns/1_Adapter/)                                           | [Test Adapter](/tests/2_StructuralPatterns/1_Adapter/test_adapter.py/)                                             | Allows objects with incompatible interfaces to collaborate.                                                                                                                                                                                  |
|  2. | [ Builder](/src/1_patterns/2_CreationalPatterns/1_Builder/)                                           | [ Text and Exercise for Builder](/src/2_exercises/1_CreationalPatterns/1_Builder/)                                           | [Test Builder](/tests/1_CreationalPatterns/1_Builder/test_builder.py/)                                             | Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.                                                                        |
|  3. | [ Command](/src/1_patterns/4_BehavioralPatterns/2_Command/)                                           | [ Text and Exercise for Command](/src/2_exercises/3_BehavioralPatterns/2_Command/)                                           | [Test Command](/tests/3_BehavioralPatterns/2_Command/test_command.py/)                                             | Turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operations. |
|  4. | [ Decorator](/src/1_patterns/3_StructuralPatterns/4_Decorator/)                                       | [ Text and Exercise for Decorator](/src/2_exercises/2_StructuralPatterns/4_Decorator/)                                       | [Test Decorator](tests/2_StructuralPatterns/4_Decorator/test_decorator.py/)                                        | Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.                                                                                                                 |
|  5. | [ Factories (Factory Method and Abstract Factory)](/src/1_patterns/2_CreationalPatterns/2_Factories/) | [ Text and Exercise for Factories (Factory Method and Abstract Factory)](/src/2_exercises/1_CreationalPatterns/2_Factories/) | [Test Factories (Factory Method and Abstract Factory)](/tests/1_CreationalPatterns/2_Factories/test_factories.py/) | Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. Abstract - Lets you produce families of related objects without specifying their concrete classes.      |
|  6. | [ Iterator](/src/1_patterns/4_BehavioralPatterns/4_Iterator/)                                         | [ Text and Exercise for Iterator](/src/2_exercises/3_BehavioralPatterns/4_Iterator/)                                         | [Test Iterator](/tests/3_BehavioralPatterns/4_Iterator/test_iterator.py/)                                          | Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).                                                                                                                         |
|  7. | [ Observer](/src/1_patterns/4_BehavioralPatterns/7_Observer/)                                         | [ Text and Exercise for Observer](/src/2_exercises/3_BehavioralPatterns/7_Observer/)                                         | [Test Observer](/tests/3_BehavioralPatterns/7_Observer/test_observer.py/)                                          | Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.                                                                                                            |
|  8. | [ Prototype](/src/1_patterns/2_CreationalPatterns/3_Prototype/)                                       | [ Textand Exercise for Prototype](/src/2_exercises/1_CreationalPatterns/3_Prototype/)                                        | [Test Prototype](/tests/1_CreationalPatterns/3_Prototype/test_prototype.py/)                                       | Lets you copy existing objects without making your code dependent on their classes.                                                                                                                                                          |
|  9. | [ Singleton](/src/1_patterns/2_CreationalPatterns/4_Singleton/)                                       | [ Textand Exercise for Singleton](/src/2_exercises/1_CreationalPatterns/4_Singleton/)                                        | [Test Singleton](/tests/1_CreationalPatterns/4_Singleton/test_singleton.py/)                                       | Lets you ensure that a class has only one instance, while providing a global access point to this instance.                                                                                                                                  |
| 10. | [ Strategy](/src/1_patterns/4_BehavioralPatterns/9_Strategy/1_strategy.py/)                           | [ Text and Exercise for Strategy](/src/2_exercises/3_BehavioralPatterns/9_Strategy/)                                         | [Test Strategy](tests/3_BehavioralPatterns/9_Strategy/test_strategy.py/)                                           | Lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.                                                                                                                      |
| 11. | [ Template](/src/1_patterns/4_BehavioralPatterns/10_Template/1_template_method.py/)                   | [ Text and Exercise for Template](/src/2_exercises/3_BehavioralPatterns/10_Template/)                                        | [Test Template](/tests/3_BehavioralPatterns/10_Template/test_template_method.py/)                                  | Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.                                                                                          |

## Awknowledgements

- Dmitri Nesteruk's course "Design Patterns in Python" on Udemy.com

## Author

- **MT** - [milovantomasevic.com](https://milovantomasevic.com)

- Certificate of Completion – Udemy - [See credential](https://www.udemy.com/certificate/UC-c9139435-41e7-4038-aa8b-1a2573b5de98/)

![Certificate of Completion – Udemy](/cert/cert.jpg)
