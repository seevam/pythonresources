# 🎮 Fun with Pygame: Game States & Scoring 🎮


### 🚀 Welcome to Game Development!

Today we're going to learn how to make games that can:
- Keep track of what's happening (Game State)
- Show a "Game Over" screen when you lose (Game Over Window)
- Show a starting screen when you begin (Game Start Window)
- Count your score while you play (Score Update)

We'll be using a fun game where a character jumps to avoid a dragon!

---

## 🧩 Part 1: Understanding Game States (15 minutes)

### What is a Game State? 

A game state is like the "mood" of your game. Is it playing? Is it paused? Is it over?

In our game, we use `game_Active = True` to mean "the game is running" and `game_Active = False` to mean "the game is over".

### 🔍 Let's Find It in Our Code:

```python
game_Active = True  # When our program starts, the game is active!

# Later in our code...
if game_Active:
    # All the code for when the player is playing
else:
    # All the code for when the game is over
```

### 🎯 Exercise 1: Game State Explorer

1. Run the game and play until you hit the dragon
2. What changes on the screen when `game_Active` becomes `False`?
3. Find where in the code the game checks if the player hits the dragon
4. Add a print statement that says "Dragon collision!" when this happens

---

## 🎭 Part 2: Game Windows (15 minutes)

Games show different screens at different times:
- The gameplay screen
- The "Game Over" screen
- The start screen (which we'll add!)

### 🔍 Let's Find the Game Over Screen in Our Code:

```python
# This creates the "Game Over" text
game_over_text = pygame.font.Font(None, 48)
game_over_text_surf = game_over_text.render("Game Over", False, 'Black')
game_over_text_rect = game_over_text_surf.get_rect(center = (300,400))

# This is where the game over screen gets displayed
else:  # when game_Active is False
    display_surf.blit(background,(0,0))
    display_surf.blit(game_over_text_surf, game_over_text_rect)
    display_surf.blit(score_message, (300,400))
```

### 🎯 Exercise 2: Create a Start Screen

Let's add a start screen! We need:
1. A new variable called `game_started = False`
2. Text that says "Press Space to Start!"
3. Code to show this text when the game isn't started yet
4. Code to start the game when space is pressed

Fill in the blanks:
```python
# Add near the top with other variables
game_started = _____

# Add with other text objects
start_text = pygame.font.Font(None, 48)
start_text_surf = start_text.render("_______________", False, 'Blue')
start_text_rect = start_text_surf.get_rect(center = (300, 400))

# Modify the main loop to check game_started
if not game_started:
    display_surf.blit(background, (0,0))
    display_surf.blit(_____, _____)
elif game_Active:
    # Existing gameplay code
```

---

## 🧮 Part 3: Score Tracking (15 minutes)

Our game keeps score based on how long you survive!

### 🔍 Let's Look at the Score Function:

```python
def score_card():
    # Calculate seconds since the game started
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    
    # Create the text showing the time
    score_surface_text = pygame.font.Font(None, 36)
    score_surface = score_surface_text.render(f'{current_time}', False, 'Red')
    
    # Position the text and display it
    score_surface_rect = score_surface.get_rect(center = (300,400))
    display_surf.blit(score_surface, score_surface_rect)
    
    # Return the time so we can use it elsewhere
    return current_time
```

### 🎯 Exercise 3: Improve the Score Display

Let's make our score display more fun! Try these challenges:

1. Move the score to the top-right corner of the screen
2. Change "RED" to your favorite color
3. Add text to say "SCORE: " before the number
4. Make the font bigger for the score

---

## 🔄 Part 4: Game Reset & Flow (10 minutes)

When the game ends, we need a way to restart!

### 🔍 Let's Look at the Restart Code:

```python
# When the game is over and player presses space
elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    game_Active = True
    dragon_rect.left = 500
    start_time = pygame.time.get_ticks()
```

### 🎯 Exercise 4: Add a High Score System

Let's keep track of the highest score:

```python
# Add at the top with other variables
high_score = 0

# Add in the game over section
if score > high_score:
    high_score = score
    
# Display the high score on the game over screen
high_score_text = pygame.font.Font(None, 36)
high_score_surf = high_score_text.render(f"High Score: {high_score}", False, 'Purple')
high_score_rect = high_score_surf.get_rect(center = (300, 450))
display_surf.blit(high_score_surf, high_score_rect)
```

---

## 🚀 Bonus Challenges

If you finish early or want to practice at home:

1. **Color Change Challenge**: Make the background change color based on your score
2. **Speed Demon**: Make the dragon move faster as your score increases
3. **Life System**: Give the player 3 lives before game over
4. **Power-ups**: Add coins the player can collect for extra points

---

## 🎉 What We Learned Today

- **Game States**: How games remember what's happening
- **Game Windows**: How to show different screens (start, play, game over)
- **Score Tracking**: How to count and display points
- **Game Flow**: How games move between different states

Great job! You're on your way to becoming a game developer! 🎮👾🚀
