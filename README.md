# Maze by Christopher Manson

Website version of Christopher Manson's 1985 book, *Maze: Solve the World's Most Challenging Puzzle*.

The website is based on [inventwithpython.com/mazewebsite](https://inventwithpython.com/mazewebsite/) by Al Sweigart.

## Play online

**[v1staz.github.io/Maze-by-ChristopherManson/](https://v1staz.github.io/Maze-by-ChristopherManson/)**

## How to play offline

### Option 1 — Double-click

Open `cover.html` directly in your browser.

### Option 2 — Launch script

- **Windows**: double-click `launch.bat`
- **Mac / Linux**: run `./launch.sh`

### Option 3 — Local server

```bash
python launcher.py
```

Starts a local HTTP server and opens the browser automatically.

### Option 4 — Build standalone EXE

```bash
pip install pyinstaller
pyinstaller --onefile --add-data ".:." --name Maze launcher.py
```

The resulting `dist/Maze.exe` (or `dist/Maze` on Linux) is a single self-contained executable.

---

This unofficial website is not affiliated with Christopher Manson or Henry Holt and Company.
