# How to Install Pygame on macOS

Follow these steps to install Pygame on your macOS system from scratch.

## 1. Verify Python Installation
Ensure Python is installed on your system:
```bash
python3 --version
```

If Python is not installed, install it using [Homebrew](https://brew.sh/):
```bash
brew install python
```
Or download and install it from [python.org](https://www.python.org/downloads/).

---

## 2. Install Pygame
### **Option 1: Use a Virtual Environment (Recommended)**
1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv pygame_env
   ```
   
   This creates a virtual environment named `pygame_env` in your current directory.

2. **Activate the Virtual Environment:**
   ```bash
   source pygame_env/bin/activate
   ```
   After activating, your terminal prompt will change to indicate you are in the virtual environment.

3. **Install Pygame:**
   ```bash
   pip install pygame
   ```

4. **Test Installation:**
   ```bash
   python -m pygame.examples.aliens
   ```
   If the game runs, Pygame is installed successfully.

5. **Deactivate the Virtual Environment:**
   To exit the virtual environment:
   ```bash
   deactivate
   ```

---

### **Option 2: Use `--break-system-packages` (Not Recommended)**
If you prefer to install Pygame globally and override macOS restrictions:

1. Run the following command:
   ```bash
   pip3 install pygame --break-system-packages
   ```

This might cause system-level conflicts, so proceed with caution.

---

### **Option 3: Use `pipx` for Isolation**
1. **Install `pipx`:**
   ```bash
   brew install pipx
   pipx ensurepath
   ```

2. **Install Pygame:**
   ```bash
   pipx install pygame
   ```

3. **Run Pygame from the Isolated Environment:**
   ```bash
   pipx run pygame
   ```

---

### **Option 4: Add `--user` Flag**
Install Pygame in the user’s local directory:
```bash
pip3 install pygame --user
```

---

## 3. Verify Installation
To confirm Pygame is installed:
1. Open a Python interactive shell:
   ```bash
   python3
   ```

2. Run the following commands:
   ```python
   import pygame
   print(pygame.__version__)
   ```
   If no errors occur and the version is displayed, Pygame is installed correctly.

---

## Troubleshooting
- If `pip3` isn’t found, update your PATH or reinstall Python.
- For permission errors, use the `--user` flag.
- For system-level issues, consider using a virtual environment as the safest approach.
