"""
COMPREHENSIVE PYTHON EXERCISES
------------------------------
These exercises progress from basic loops to functions, 
classes, and finally to PyGame fundamentals.
"""

# ==================== FOR LOOP EXERCISES ====================

def for_loop_exercises():
    """
    Exercise 1: Print numbers from 1 to 10
    """
    print("\nExercise 1.1: Print numbers from 1 to 10")
    # TODO: Write a for loop to print numbers from 1 to 10
    
    """
    Exercise 1.2: Calculate the sum of numbers from 1 to 100
    """
    print("\nExercise 1.2: Calculate the sum of numbers from 1 to 100")
    total = 0
    # TODO: Write a for loop to calculate the sum of numbers from 1 to 100
    # and store the result in the 'total' variable
    
    print(f"Sum: {total}")  # Expected: 5050
    
    """
    Exercise 1.3: Print all even numbers from 1 to 20
    """
    print("\nExercise 1.3: Print all even numbers from 1 to 20")
    # TODO: Write a for loop to print all even numbers from 1 to 20
    
    """
    Exercise 1.4: Create a multiplication table for a given number
    """
    print("\nExercise 1.4: Create a multiplication table for number 7")
    number = 7
    # TODO: Write a for loop to print the multiplication table for number 7
    # Format should be: "7 x 1 = 7", "7 x 2 = 14", etc.
    
    """
    Exercise 1.5: Iterate through a string and count vowels
    """
    print("\nExercise 1.5: Count vowels in a string")
    message = "Hello, how are you doing today?"
    vowels = "aeiouAEIOU"
    vowel_count = 0
    # TODO: Write a for loop to count the number of vowels in the message
    
    print(f"The message contains {vowel_count} vowels")  # Expected: 11


# ==================== WHILE LOOP EXERCISES ====================

def while_loop_exercises():
    """
    Exercise 2.1: Count down from 10 to 1
    """
    print("\nExercise 2.1: Count down from 10 to 1")
    # TODO: Write a while loop to count down from 10 to 1
    
    """
    Exercise 2.2: Keep asking for user input until they type 'quit'
    """
    print("\nExercise 2.2: Keep asking for input until user types 'quit'")
    # TODO: Write a while loop that asks the user for input
    # and continues until they type 'quit'
    
    """
    Exercise 2.3: Generate random numbers until getting a number > 0.9
    """
    print("\nExercise 2.3: Generate random numbers until getting one > 0.9")
    import random
    attempts = 0
    # TODO: Write a while loop that generates random numbers between 0 and 1
    # until you get a number greater than 0.9. Count how many attempts it takes.
    
    print(f"It took {attempts} attempts to get a number > 0.9")
    
    """
    Exercise 2.4: Implement a simple guessing game
    """
    print("\nExercise 2.4: Number guessing game")
    import random
    target = random.randint(1, 100)
    guesses = 0
    # TODO: Implement a number guessing game where the computer picks a number
    # between 1 and 100, and the user tries to guess it. Give "higher" or "lower" hints.
    # Count how many guesses it takes.


# ==================== FUNCTION EXERCISES ====================

def function_exercises():
    """
    Exercise 3.1: Create a function to check if a number is prime
    """
    print("\nExercise 3.1: Check if a number is prime")
    
    # TODO: Define a function called is_prime that takes a number as input
    # and returns True if it's prime, False otherwise
    
    # Test the function
    test_numbers = [2, 7, 10, 13, 25]
    for num in test_numbers:
        # TODO: Call your is_prime function and print the result
        pass
    
    """
    Exercise 3.2: Create a function to calculate factorial
    """
    print("\nExercise 3.2: Calculate factorial")
    
    # TODO: Define a function called factorial that calculates the factorial of a number
    
    # Test the function
    for num in range(1, 6):
        # TODO: Call your factorial function and print the result
        pass
    
    """
    Exercise 3.3: Create a function that returns the largest element in a list
    """
    print("\nExercise 3.3: Find largest element in a list")
    
    # TODO: Define a function called find_largest that returns the largest element in a list
    
    # Test the function
    test_lists = [
        [1, 5, 8, 3, 2],
        [10, 3, 5, 8],
        [7]
    ]
    for lst in test_lists:
        # TODO: Call your find_largest function and print the result
        pass
    
    """
    Exercise 3.4: Create a function with default parameters
    """
    print("\nExercise 3.4: Function with default parameters")
    
    # TODO: Define a function called greet that takes a name and a greeting
    # Use "Hello" as the default greeting
    
    # Test the function
    # TODO: Call your greet function with different parameters
    
    """
    Exercise 3.5: Create a function to convert temperature
    """
    print("\nExercise 3.5: Temperature conversion function")
    
    # TODO: Define a function called convert_temp that converts between Celsius and Fahrenheit
    # The function should take a temperature and a unit ('C' or 'F')
    # and return the converted temperature
    
    # Test the function
    # TODO: Call your convert_temp function with different temperatures and units


# ==================== CLASS EXERCISES ====================

def class_exercises():
    """
    Exercise 4.1: Create a simple Rectangle class
    """
    print("\nExercise 4.1: Create a Rectangle class")
    
    # TODO: Define a Rectangle class with width and height attributes,
    # and methods to calculate area and perimeter
    
    # Test the Rectangle class
    # TODO: Create Rectangle instances and test the methods
    
    """
    Exercise 4.2: Create a BankAccount class
    """
    print("\nExercise 4.2: Create a BankAccount class")
    
    # TODO: Define a BankAccount class with methods for deposit, withdraw, and check_balance
    
    # Test the BankAccount class
    # TODO: Create a BankAccount instance and test the methods
    
    """
    Exercise 4.3: Create a Student class with inheritance
    """
    print("\nExercise 4.3: Create a Student class with inheritance")
    
    # TODO: Define a Person class with name and age attributes
    
    # TODO: Define a Student class that inherits from Person and adds student_id and courses attributes
    
    # Test the classes
    # TODO: Create Person and Student instances and demonstrate inheritance
    
    """
    Exercise 4.4: Create a class with special methods (__str__, __eq__, etc.)
    """
    print("\nExercise 4.4: Class with special methods")
    
    # TODO: Define a Point class with x and y coordinates and implement:
    # - __init__: Initialize x and y
    # - __str__: Return a string representation like "Point(x, y)"
    # - __eq__: Check if two points are equal
    # - __add__: Add two points together (add their coordinates)
    
    # Test the Point class
    # TODO: Create Point instances and test the special methods


# ==================== PYGAME BASICS EXERCISES ====================

def pygame_exercises():
    """
    Note: These are conceptual exercises. You'll need to install pygame to run them.
    """
    
    """
    Exercise 5.1: Set up a basic Pygame window
    """
    print("\nExercise 5.1: Set up a basic Pygame window")
    
    # TODO: Write code to initialize Pygame and create a window
    # with the title "My First Pygame Window"
    
    """
    Exercise 5.2: Draw shapes and change colors
    """
    print("\nExercise 5.2: Draw shapes and change colors")
    
    # TODO: Write code to:
    # - Create a window
    # - Draw a red rectangle, a blue circle, and a green line
    # - Update the display and add a simple game loop
    
    """
    Exercise 5.3: Make a moving rectangle (basic animation)
    """
    print("\nExercise 5.3: Animate a moving rectangle")
    
    # TODO: Write code to animate a rectangle moving across the screen
    
    """
    Exercise 5.4: Handle keyboard input
    """
    print("\nExercise 5.4: Handle keyboard input")
    
    # TODO: Write code to move a rectangle using arrow keys
    
    """
    Exercise 5.5: Create a simple game: Catch the Square
    """
    print("\nExercise 5.5: Simple 'Catch the Square' game")
    
    # TODO: Create a game where:
    # - A player-controlled rectangle moves with arrow keys
    # - A target square appears at random positions
    # - When the player touches the target, it moves and the score increases


# ==================== SOLUTIONS ====================

def for_loop_solutions():
    """Solutions for For Loop Exercises"""
    
    # Exercise 1.1: Print numbers from 1 to 10
    print("\nSolution 1.1: Print numbers from 1 to 10")
    for i in range(1, 11):
        print(i)
    
    # Exercise 1.2: Calculate the sum of numbers from 1 to 100
    print("\nSolution 1.2: Calculate the sum of numbers from 1 to 100")
    total = 0
    for i in range(1, 101):
        total += i
    print(f"Sum: {total}")
    
    # Exercise 1.3: Print all even numbers from 1 to 20
    print("\nSolution 1.3: Print all even numbers from 1 to 20")
    for i in range(2, 21, 2):
        print(i)
    
    # Alternative solution
    print("Alternative solution:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
    
    # Exercise 1.4: Create a multiplication table for a given number
    print("\nSolution 1.4: Create a multiplication table for number 7")
    number = 7
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    
    # Exercise 1.5: Iterate through a string and count vowels
    print("\nSolution 1.5: Count vowels in a string")
    message = "Hello, how are you doing today?"
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in message:
        if char in vowels:
            vowel_count += 1
    
    print(f"The message contains {vowel_count} vowels")


def while_loop_solutions():
    """Solutions for While Loop Exercises"""
    
    # Exercise 2.1: Count down from 10 to 1
    print("\nSolution 2.1: Count down from 10 to 1")
    count = 10
    while count > 0:
        print(count)
        count -= 1
    
    # Exercise 2.2: Keep asking for user input until they type 'quit'
    print("\nSolution 2.2: Keep asking for input until user types 'quit'")
    # Uncomment to test
    """
    user_input = ""
    while user_input.lower() != "quit":
        user_input = input("Enter something (type 'quit' to exit): ")
        print(f"You entered: {user_input}")
    print("Goodbye!")
    """
    
    # Exercise 2.3: Generate random numbers until getting a number > 0.9
    print("\nSolution 2.3: Generate random numbers until getting one > 0.9")
    import random
    attempts = 0
    random_num = 0
    
    while random_num <= 0.9:
        random_num = random.random()
        attempts += 1
        print(f"Generated: {random_num:.4f}")
    
    print(f"It took {attempts} attempts to get a number > 0.9")
    
    # Exercise 2.4: Implement a simple guessing game
    print("\nSolution 2.4: Number guessing game")
    # Uncomment to test
    """
    import random
    target = random.randint(1, 100)
    guesses = 0
    guess = 0
    
    print("I'm thinking of a number between 1 and 100.")
    while guess != target:
        try:
            guess = int(input("Your guess: "))
            guesses += 1
            
            if guess < target:
                print("Higher!")
            elif guess > target:
                print("Lower!")
            else:
                print(f"Correct! You found the number in {guesses} guesses!")
        except ValueError:
            print("Please enter a valid number.")
    """


def function_solutions():
    """Solutions for Function Exercises"""
    
    # Exercise 3.1: Create a function to check if a number is prime
    print("\nSolution 3.1: Check if a number is prime")
    
    def is_prime(num):
        """Check if a number is prime"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
            
        return True
    
    # Test the function
    test_numbers = [2, 7, 10, 13, 25]
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")
    
    # Exercise 3.2: Create a function to calculate factorial
    print("\nSolution 3.2: Calculate factorial")
    
    def factorial(n):
        """Calculate the factorial of n"""
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n+1):
                result *= i
            return result
    
    # Test the function
    for num in range(1, 6):
        print(f"{num}! = {factorial(num)}")
    
    # Exercise 3.3: Create a function that returns the largest element in a list
    print("\nSolution 3.3: Find largest element in a list")
    
    def find_largest(lst):
        """Find the largest element in a list"""
        if not lst:
            return None
        largest = lst[0]
        for item in lst:
            if item > largest:
                largest = item
        return largest
    
    # Test the function
    test_lists = [
        [1, 5, 8, 3, 2],
        [10, 3, 5, 8],
        [7]
    ]
    for lst in test_lists:
        print(f"Largest in {lst} is {find_largest(lst)}")
    
    # Exercise 3.4: Create a function with default parameters
    print("\nSolution 3.4: Function with default parameters")
    
    def greet(name, greeting="Hello"):
        """Greet a person with a customizable greeting"""
        return f"{greeting}, {name}!"
    
    # Test the function
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    print(greet("Charlie", "Good morning"))
    
    # Exercise 3.5: Create a function to convert temperature
    print("\nSolution 3.5: Temperature conversion function")
    
    def convert_temp(temp, unit):
        """Convert temperature between Celsius and Fahrenheit"""
        if unit.upper() == 'C':
            # Convert Celsius to Fahrenheit
            return (temp * 9/5) + 32
        elif unit.upper() == 'F':
            # Convert Fahrenheit to Celsius
            return (temp - 32) * 5/9
        else:
            return f"Invalid unit: {unit}. Use 'C' or 'F'."
    
    # Test the function
    print(f"32°F = {convert_temp(32, 'F'):.1f}°C")
    print(f"100°C = {convert_temp(100, 'C'):.1f}°F")


def class_solutions():
    """Solutions for Class Exercises"""
    
    # Exercise 4.1: Create a simple Rectangle class
    print("\nSolution 4.1: Create a Rectangle class")
    
    class Rectangle:
        """A simple rectangle class"""
        
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            """Calculate the area of the rectangle"""
            return self.width * self.height
        
        def perimeter(self):
            """Calculate the perimeter of the rectangle"""
            return 2 * (self.width + self.height)
        
        def __str__(self):
            """Return a string representation of the rectangle"""
            return f"Rectangle(width={self.width}, height={self.height})"
    
    # Test the Rectangle class
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 4)
    
    print(f"Rectangle 1: {rect1}")
    print(f"Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")
    
    print(f"Rectangle 2: {rect2}")
    print(f"Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
    
    # Exercise 4.2: Create a BankAccount class
    print("\nSolution 4.2: Create a BankAccount class")
    
    class BankAccount:
        """A simple bank account class"""
        
        def __init__(self, account_number, owner_name, balance=0):
            self.account_number = account_number
            self.owner_name = owner_name
            self.balance = balance
        
        def deposit(self, amount):
            """Deposit money into the account"""
            if amount > 0:
                self.balance += amount
                return f"Deposited ${amount}. New balance: ${self.balance}"
            else:
                return "Deposit amount must be positive"
        
        def withdraw(self, amount):
            """Withdraw money from the account"""
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    return f"Withdrew ${amount}. New balance: ${self.balance}"
                else:
                    return "Insufficient funds"
            else:
                return "Withdrawal amount must be positive"
        
        def check_balance(self):
            """Check the current balance"""
            return f"Account {self.account_number} ({self.owner_name}) balance: ${self.balance}"
        
        def __str__(self):
            """Return a string representation of the account"""
            return f"BankAccount({self.account_number}, {self.owner_name}, ${self.balance})"
    
    # Test the BankAccount class
    account = BankAccount("12345", "John Doe", 100)
    print(account)
    print(account.check_balance())
    print(account.deposit(50))
    print(account.withdraw(30))
    print(account.withdraw(200))
    
    # Exercise 4.3: Create a Student class with inheritance
    print("\nSolution 4.3: Create a Student class with inheritance")
    
    class Person:
        """A simple person class"""
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def introduce(self):
            """Introduce the person"""
            return f"Hi, I'm {self.name} and I'm {self.age} years old."
        
        def __str__(self):
            """Return a string representation of the person"""
            return f"Person({self.name}, {self.age})"
    
    class Student(Person):
        """A student class that inherits from Person"""
        
        def __init__(self, name, age, student_id, courses=None):
            # Call the parent class's __init__ method
            super().__init__(name, age)
            self.student_id = student_id
            self.courses = courses if courses else []
        
        def add_course(self, course):
            """Add a course to the student's course list"""
            self.courses.append(course)
        
        def introduce(self):
            """Override the introduce method to include student information"""
            return f"{super().introduce()} I'm a student with ID {self.student_id}."
        
        def list_courses(self):
            """List all courses the student is enrolled in"""
            if self.courses:
                return f"Enrolled in: {', '.join(self.courses)}"
            else:
                return "Not enrolled in any courses"
        
        def __str__(self):
            """Return a string representation of the student"""
            return f"Student({self.name}, {self.age}, {self.student_id})"
    
    # Test the classes
    person = Person("Alice", 30)
    student = Student("Bob", 20, "S12345")
    
    print(person)
    print(person.introduce())
    
    print(student)
    print(student.introduce())  # Uses overridden method
    
    student.add_course("Python Programming")
    student.add_course("Data Science")
    print(student.list_courses())
    
    # Exercise 4.4: Create a class with special methods
    print("\nSolution 4.4: Class with special methods")
    
    class Point:
        """A 2D point class with special methods"""
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __str__(self):
            """Return a string representation of the point"""
            return f"Point({self.x}, {self.y})"
        
        def __repr__(self):
            """Return a representation of the point for debugging"""
            return f"Point({self.x}, {self.y})"
        
        def __eq__(self, other):
            """Check if two points are equal"""
            if not isinstance(other, Point):
                return False
            return self.x == other.x and self.y == other.y
        
        def __add__(self, other):
            """Add two points together"""
            if isinstance(other, Point):
                return Point(self.x + other.x, self.y + other.y)
            return NotImplemented
        
        def distance(self, other):
            """Calculate the distance between two points"""
            if not isinstance(other, Point):
                raise TypeError("Can only calculate distance to another Point")
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    # Test the Point class
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    p3 = Point(3, 4)  # Same as p1
    
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")
    
    print(f"p1 == p2: {p1 == p2}")  # Should be False
    print(f"p1 == p3: {p1 == p3}")  # Should be True
    
    p4 = p1 + p2
    print(f"p1 + p2 = {p4}")  # Should be Point(4, 6)
    
    distance = p1.distance(p2)
    print(f"Distance between p1 and p2: {distance:.2f}")  # Should be around 2.83


def pygame_solutions():
    """Conceptual solutions for PyGame exercises"""
    
    print("\nPyGame Solutions (conceptual code)")
    
    # Exercise 5.1: Set up a basic Pygame window
    print("\nSolution 5.1: Set up a basic Pygame window")
    print("""
    # This is conceptual code - you need to install pygame to run it
    import pygame
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My First Pygame Window")
    
    # Main game loop
    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    """)
    
    # Exercise 5.2: Draw shapes and change colors
    print("\nSolution 5.2: Draw shapes and change colors")
    print("""
    # This is conceptual code - you need to install pygame to run it
    import pygame
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drawing Shapes")
    
    # Define colors (R, G, B)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    
    # Main game loop
    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw a red rectangle
        rect = pygame.Rect(50, 50, 200, 100)  # (x, y, width, height)
        pygame.draw.rect(screen, RED, rect)
        
        # Draw a blue circle
        circle_center = (400, 300)  # (x, y)
        circle_radius = 50
        pygame.draw.circle(screen, BLUE, circle_center, circle_radius)
        
        # Draw a green line
        line_start = (600, 100)  # (x, y)
        line_end = (700, 500)    # (x, y)
        line_width = 5
        pygame.draw.line(screen, GREEN, line_start, line_end, line_width)
        
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    """)
    
    # Exercise 5.3: Make a moving rectangle (basic animation)
    print("\nSolution 5.3: Animate a moving rectangle")
    print("""
    # This is conceptual code - you need to install pygame to run it
    import pygame
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Moving Rectangle")
    
    # Define colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    # Set up the rectangle
    rect_x = 50
    rect_y = 300
    rect_width = 50
    rect_height = 50
    rect_speed = 5
    
    # Set up the clock
    clock = pygame.time.Clock()
    
    # Main game loop
    running = True
    while running:
        # Limit to 60 FPS
        clock.tick(60)
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Move the rectangle
        rect_x += rect_speed
        
        # If the rectangle reaches the edge, reverse direction
        if rect_x <= 0 or rect_x + rect_width >= 800:
            rect_speed = -rect_speed
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw the rectangle
        pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))
        
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    """)
    
    # Exercise 5.4: Handle keyboard input
    print("\nSolution 5.4: Handle keyboard input")
    print("""
    # This is conceptual code - you need to install pygame to run it
    import pygame
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Keyboard Control")
    
    # Define colors
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    
    # Set up the rectangle
    rect_x = 400
    rect_y = 300
    rect_width = 50
    rect_height = 50
    rect_speed = 5
    
    # Set up the clock
    clock = pygame.time.Clock()
    
    # Main game loop
    running = True
    while running:
        # Limit to 60 FPS
        clock.tick(60)
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get the state of all keyboard keys
        keys = pygame.key.get_pressed()
        
        # Move the rectangle based on arrow key presses
        if keys[pygame.K_LEFT]:
            rect_x -= rect_speed
        if keys[pygame.K_RIGHT]:
            rect_x += rect_speed
        if keys[pygame.K_UP]:
            rect_y -= rect_speed
        if keys[pygame.K_DOWN]:
            rect_y += rect_speed
        
        # Keep the rectangle within the screen bounds
        if rect_x < 0:
            rect_x = 0
        if rect_x + rect_width > 800:
            rect_x = 800 - rect_width
        if rect_y < 0:
            rect_y = 0
        if rect_y + rect_height > 600:
            rect_y = 600 - rect_height
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw the rectangle
        pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
        
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    """)
    
    # Exercise 5.5: Create a simple game: Catch the Square
    print("\nSolution 5.5: Simple 'Catch the Square' game")
    print("""
    # This is conceptual code - you need to install pygame to run it
    import pygame
    import random
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode