# Installing Pygame on Windows

## Step 1: Install Python  
Before installing Pygame, ensure Python is installed on your system. Check by running:
```sh
python --version
```
If Python is not installed, download and install it from the official website:
[Python Official Website](https://www.python.org/downloads/)

**Important:** During installation, check the box **"Add Python to PATH"**.

---

## Step 2: Upgrade `pip`  
Upgrade `pip` (Python's package manager) to ensure a smooth installation:
```sh
python -m pip install --upgrade pip
```

---

## Step 3: Install Pygame  
Now install Pygame using `pip`:
```sh
pip install pygame
```
If you want to install the latest **Pygame Community Edition (pygame-ce)**:
```sh
pip install pygame-ce
```

---

## Step 4: Verify Installation  
To check if Pygame was installed successfully, run:
```sh
python -m pygame.examples.aliens
```
This should open a simple Pygame demo window.

---

## Troubleshooting Issues  
### 1. Command Not Found?
- Restart your computer and try again.
- Ensure Python is added to the system PATH (reinstall Python if necessary, checking the "Add to PATH" box).

### 2. Pygame Not Found?
- Try installing with:
  ```sh
  pip install pygame --user
  ```

### 3. Using an Older Python Version?
- Pygame requires **Python 3.7 or later**. Check your version:
  ```sh
  python --version
  ```
  If you have an older version, update Python from the official website.

---

## Additional Resources
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Downloads](https://www.python.org/downloads/)

If you encounter issues, feel free to ask for help! 🚀
