# Introduction to Python Functions! 🐍
## A Beginner's Guide

### 1. What Are Functions? (30 minutes)
#### The Big Idea
Imagine you have to make your bed every morning. The steps are always the same:
1. Fix the sheets
2. Arrange the pillows
3. Straighten the blanket

Instead of telling someone all these steps every time, wouldn't it be nice to just say "make the bed"?

That's exactly what functions do in Python! They're like magic shortcuts that hold a bunch of instructions.

#### Your First Function
Let's write the simplest function ever:
```python
def say_hello():
    print("Hi there!")

# To use our function, we write:
say_hello()
```

Let's break this down:
- `def` tells Python "I'm creating a function!"
- `say_hello` is the name we gave our function
- The `()` are like empty hands - ready to receive stuff (we'll learn about this soon)
- `:` tells Python "here come the instructions!"
- Everything indented after the `:` is what the function will do

**Try It Yourself #1:**
```python
# Can you create a function that prints three different emoji?
def print_emoji():
    print("😊")
    print("🌟")
    print("🎈")

# Now use it!
print_emoji()
```

**Fun Challenge #1:**
```python
# Make a function that prints out your favorite movie title
# and why you love it!
def my_favorite_movie():
    print("My favorite movie is _____")
    print("I love it because _____")
```

### 2. Functions with Input (Parameters) (40 minutes)
#### The Big Idea
Remember our "make the bed" example? What if we want to make different beds? We need to tell the function WHICH bed to make!

In Python, we can give information to our functions. These are called parameters.

#### Simple Parameter Example
```python
def greet_friend(friend_name):
    print(f"Hi {friend_name}!")
    print(f"I hope you're having an awesome day, {friend_name}!")

# Now we can greet different friends:
greet_friend("Alex")  # Will say hi to Alex
greet_friend("Taylor")  # Will say hi to Taylor
```

Think of `friend_name` as a special box that holds whatever name we give it.

**Try It Yourself #2:**
```python
# Let's make a function that can make any animal sound!
def animal_sound(animal):
    if animal == "cat":
        print("Meow!")
    elif animal == "dog":
        print("Woof!")
    elif animal == "duck":
        print("Quack!")
    else:
        print("I don't know that animal's sound!")

# Try it with different animals:
animal_sound("cat")
animal_sound("dog")
animal_sound("elephant")
```

#### Multiple Parameters
We can give our functions more than one piece of information:

```python
def build_sandwich(bread, filling):
    print(f"1. Get two slices of {bread} bread")
    print(f"2. Add {filling} in the middle")
    print("3. Put the slices together")
    print(f"Yummy! Your {filling} sandwich is ready!")

# Make different sandwiches:
build_sandwich("wheat", "cheese")
build_sandwich("white", "peanut butter")
```

**Fun Challenge #2:**
```python
# Create a function that makes a superhero introduction
def introduce_superhero(hero_name, superpower):
    print(f"Behold! I am {hero_name}!")
    print(f"My superpower is {superpower}!")

# Try making some superheroes:
introduce_superhero("Lightning Girl", "super speed")
introduce_superhero("Captain Code", "debugging")
```

### 3. Understanding Scope (30 minutes)
#### The Big Idea
Imagine you have a toy in your bedroom. Your friend in their house can't play with it unless you bring it to them!

Variables in functions work the same way. Variables created inside a function can only be used inside that function.

```python
def my_game_room():
    # This toy only exists inside the function
    toy = "teddy bear"
    print(f"Inside the room, I can play with my {toy}")

my_game_room()
# This will cause an error:
# print(f"Outside the room, I can't find the {toy}")
```

**Try It Yourself #3:**
```python
# Let's see how scope works:
def magic_number():
    secret = 42
    print(f"Inside function: The secret number is {secret}")

magic_number()
# Try to print secret here - what happens?
# print(secret)  # This will give an error!
```

### 4. Fun with Return Values (30 minutes)
#### The Big Idea
Sometimes we want our functions to not just do something, but give us back a result!

Think of it like a sandwich-making machine:
- We put in bread and filling (parameters)
- It makes the sandwich (does the work)
- It gives us back the finished sandwich (return value)

```python
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Now we can save the result:
answer = add_numbers(5, 3)
print(f"5 + 3 = {answer}")
```

**Try It Yourself #4:**
```python
# Make a function that returns a personalized message
def create_greeting(name):
    message = f"Welcome to Python, {name}!"
    return message

# Save the greeting and print it
my_greeting = create_greeting("Alex")
print(my_greeting)
```

### 5. Super Simple Lambda Functions (20 minutes)
#### The Big Idea
Lambda functions are like tiny one-line functions. Think of them as function shortcuts!

```python
# Normal function
def add_five(number):
    return number + 5

# Same thing as a lambda
add_five_lambda = lambda number: number + 5

# Both do the same thing:
print(add_five(10))       # Prints 15
print(add_five_lambda(10)) # Also prints 15
```

**Try It Yourself #5:**
```python
# Create some simple lambda functions
double = lambda x: x * 2
add_exclamation = lambda text: text + "!"

# Try them out
print(double(7))
print(add_exclamation("Wow"))
```

### Fun Projects to Try

#### 1. The Friendly Chatbot
```python
def chatbot():
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    age = input("How old are you? ")
    print(f"Wow! {age} is a great age!")
    
    hobby = input("What's your favorite hobby? ")
    print(f"That's cool! I love {hobby} too!")

# Run your chatbot
chatbot()
```

#### 2. The Math Helper
```python
def math_helper(num1, num2):
    print(f"Looking at numbers {num1} and {num2}:")
    print(f"Sum: {num1 + num2}")
    print(f"Difference: {num1 - num2}")
    print(f"Product: {num1 * num2}")
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Can't divide by zero!")

# Try it out:
math_helper(10, 5)
```

#### 3. The Weather Outfit Helper
```python
def suggest_outfit(temperature):
    if temperature > 25:
        return "It's hot! Wear shorts and a t-shirt!"
    elif temperature > 15:
        return "It's nice! Wear a light jacket!"
    else:
        return "It's cold! Wear a warm coat!"

# Try different temperatures
print(suggest_outfit(30))
print(suggest_outfit(20))
print(suggest_outfit(10))
```

### Practice Exercises
1. Create a function that takes your name and favorite color and prints "Hi, I'm [name] and I love [color]!"
2. Make a function that takes a number and returns whether it's positive or negative
3. Create a function that prints out a square made of stars (take the size as input)
4. Make a function that converts dog years to human years (multiply by 7)

### Remember:
- Functions are like your own custom commands
- Parameters are like boxes that hold information your function needs
- Return values are like getting an answer back from your function
- Always test your functions with different inputs
- Don't worry about making mistakes - they help you learn!

### Extra Tips for Learning:
1. Type out every example yourself - don't just copy-paste
2. Try to predict what each function will do before you run it
3. Experiment! Change the code and see what happens
4. Draw pictures if it helps you understand better
5. Keep practicing - you're doing great! 🌟
