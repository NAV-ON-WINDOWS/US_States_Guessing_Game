# 🇺🇸 US States Guessing Game

Think you know all 50 states? Prove it.

**US States Guessing Game** is an interactive geography quiz built with Python and Turtle. Type in as many US states as you can — each correct answer appears on an interactive map. No timer, no pressure. Just you vs. all 50 states.

---

## 🎮 How to Play

1. Run the game (see [Getting Started](#getting-started) below)
2. A map of the United States will appear on screen
3. Type the name of any US state into the prompt
4. Each correct answer is marked directly on the map
5. When you're done, type **exit** to end the game
6. Any states you missed will be revealed at the end — study up for next time!

---

## ✨ Features

- 🗺️ **Interactive map** — correct guesses are plotted live on a US map using Turtle
- 📊 **Score tracking** — see how many states you've named as you go
- 🔍 **Answer reveal** — missed states are shown at the end so you can learn from them
- 📁 **CSV-powered** — state data managed cleanly with Pandas

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core game logic |
| Turtle | Map rendering and graphics |
| Pandas | Reading and managing state data from CSV |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Required libraries: `pandas`

Install dependencies with:

```bash
pip install pandas
```

> **Note:** `turtle` comes built into Python's standard library — no installation needed.

### Running the Game

```bash
python main.py
```

---

## 📁 Project Structure

```
US_States_Guessing_Game/
├── main.py               # Main game logic
├── 50_states.csv         # State names and map coordinates
├── blank_states_img.gif  # US map image used by Turtle
└── README.md
```

---

## 🙌 Acknowledgements

- Map layout and game concept inspired by [Sporcle's US States Quiz](https://www.sporcle.com/games/g/states)
- Built as a Python learning project exploring Turtle graphics and Pandas
