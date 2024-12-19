# Understanding Code Structure with Pygame! 🎮
**Lesson Duration**: 45-60 minutes

## Learning Objectives 🎯
By the end of this lesson, students will be able to:
- Distinguish between modules, functions, and methods
- Understand dot notation in Python
- Read and interpret Pygame code structure
- Use built-in Python tools to explore code

## 1. Introduction: The Building Blocks 🧱

### Opening Activity (5 minutes)
Let's organize a digital art studio!
```
Digital Art Studio
├── Drawing Tools Department
│   ├── Pencil Tool
│   └── Brush Tool
├── Colors Department
│   ├── Color Mixer
│   └── Color Picker
└── Canvas Department
    ├── New Canvas
    └── Save Canvas
```

This is just like how Python organizes code:
```python
pygame              # The whole art studio
├── display        # Drawing Tools Department
│   ├── set_mode() # New Canvas
│   └── update()   # Refresh Canvas
├── draw           # Colors Department
│   ├── rect()     # Draw Rectangle
│   └── circle()   # Draw Circle
```

## 2. The Three Building Blocks 🏗️

### 1. Modules 📦
- Like departments in our art studio
- Contains related tools and functions
- Example: `pygame.display`

### 2. Functions 🔧
- Like specific tools that anyone can use
- They do specific jobs
- Example: `pygame.init()`

### 3. Methods 🛠️
- Like tools that belong to specific things
- Need their "owner" to work
- Example: `surface.blit()`

## 3. Hands-on Investigation! 🔍

### Activity 1: Code Detective
```python
import pygame

# Let's investigate!
print("What is pygame?", type(pygame))
print("What is pygame.display?", type(pygame.display))
print("What is pygame.init?", type(pygame.init))
```

### Activity 2: Directory Explorer
```python
import pygame

# Let's look inside pygame.display!
print("\nThings in pygame.display:")
for item in dir(pygame.display):
    if not item.startswith('_'):
        print(item)
```

## 4. Fun Exercises! 🎯

### Exercise 1: Module Explorer
Create a program that:
1. Prints all modules in pygame
2. Lets you pick a module to explore
3. Shows what's inside that module

```python
import pygame

pygame.init()

# Get all modules
modules = [item for item in dir(pygame) if not item.startswith('_')]
print("Available modules:", modules)

# Let user pick one
module_name = input("Which module would you like to explore? ")
if module_name in modules:
    module = getattr(pygame, module_name)
    print(f"\nThings in pygame.{module_name}:")
    for item in dir(module):
        if not item.startswith('_'):
            print(item)
```

### Exercise 2: Code Structure Game
Create a simple matching game:
```python
def is_it_a_module(thing):
    """
    Your code here!
    Check if 'thing' is a module
    """
    pass

# Test cases
test_items = [
    pygame.display,    # Module
    pygame.init,       # Function
    pygame.quit,       # Function
    pygame.image,      # Module
]

for item in test_items:
    if is_it_a_module(item):
        print(f"{item} is a module!")
    else:
        print(f"{item} is not a module!")
```

## 5. Practice Problems 📝

1. **Module vs Function Challenge**
   ```python
   # List 3 modules and 3 functions from pygame
   modules = [
       # Your answer here
   ]
   
   functions = [
       # Your answer here
   ]
   ```

2. **Code Reading Challenge**
   ```python
   pygame.display.set_mode((800, 600))
   ```
   - What's the module?
   - What's the function?
   - What are the parameters?

## 6. Wrap-Up Quiz! 🎉

Quick verbal quiz:
1. If I can import it, it's probably a _____ (module)
2. If it has () and does something, it's probably a _____ (function)
3. pygame.display is a _____ (module)
4. pygame.init() is a _____ (function)

## Extension Activities 🚀

For students who finish early:
1. Create a "module explorer" tool
2. Map out the pygame library structure
3. Create a quiz game about modules vs functions

## Common Mistakes to Watch For ⚠️

1. Confusing modules and functions
2. Forgetting parentheses for functions
3. Trying to call modules like functions

Remember: The best way to learn is by doing! Let's start exploring! 🎮
