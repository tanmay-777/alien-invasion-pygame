# Alien Invaders

A 2D arcade shoot 'em up built with Python and Pygame. Defend against descending cyan alien fleets across escalating waves, dodge incoming enemy fire, and compete for the high score against a procedurally generated deep-space starfield.

---

## Features

- **Difficulty Selection:** Choose between Easy, Medium, and Hard modes right from the launch screen.
- **Progressive Wave Scaling:** Dynamic scaling increases fleet movement speed, alien projectile frequency, and point values each time a wave is cleared.
- **Procedural Starfield:** Pre-rendered pitch-black space background populated with randomized star scales, coordinate jitter, and low-frequency metallic flare stars.
- **Full Audio Integration:** High-energy background soundtrack paired with responsive sound effects for laser fire and ship explosions.
- **Retro Arcade HUD:** Neon-green telemetry tracking live score, all-time session high score, current wave level, and remaining lives.
- **Standalone Windows Build:** Packaged via PyInstaller (`--onedir`) for instant startup with zero Python installation required.

---

## Controls

| Input | Action |
| :--- | :--- |
| `Left Arrow` | Move Ship Left |
| `Right Arrow` | Move Ship Right |
| `Spacebar` | Fire Lasers |
| `Mouse Click` | Select Difficulty to Start |
| `Q` | Quit Game |

---

## Quick Start (Windows Executable)

No Python installation or setup is required to play the standalone release:

1. Navigate to the **[Releases](../../releases)** page of this repository.
2. Download **`Alien_Invaders-v1.0.0-Windows.zip`** from the latest release assets.
3. Extract the `.zip` archive to any folder on your PC.
4. Open the extracted folder and run **`Alien_Invaders.exe`**.

---

## Running from Source

### Prerequisites
- Python 3.10+
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tanmay-777/Alien_Invaders.git
   cd Alien_Invaders
   ```

2. **Create and activate a virtual environment (optional):**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install Pygame:**
   ```bash
   pip install pygame
   ```

4. **Launch the game:**
   ```bash
   python alien_invasion.py
   ```

---

## Project Structure

```text
Alien_Invaders/
├── fonts/               # Retro arcade TrueType font files
├── images/              # Sprites (red player ship, cyan alien UFOs, dual star layers)
├── sounds/              # Background OST and laser/explosion WAV effects
├── alien.py             # Alien sprite logic, fleet boundaries, and movement
├── alien_invasion.py    # Core game engine, main loop, collision & event handling
├── bullet.py            # Player and alien projectile management
├── button.py            # Difficulty selection UI buttons
├── game_stats.py        # Session state, life counters, and score tracking
├── scoreboard.py        # Neon-green HUD rendering and title screen credits
├── settings.py          # Game constants, difficulty multipliers, and color palettes
├── ship.py              # Player ship movement and screen boundary logic
└── stars.py             # Procedural starfield sprite initialization
```

---

## Building the Executable

To bundle the source code into a standalone Windows directory yourself using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconsole --onedir --name "Alien_Invaders" --add-data "fonts;fonts" --add-data "images;images" --add-data "sounds;sounds" alien_invasion.py
```

> **Note:** Ensure the `fonts/`, `images/`, and `sounds/` folders are placed directly alongside `Alien_Invaders.exe` inside `dist/Alien_Invaders/` for relative asset paths to resolve properly.

---

## Credits

- **Developer:** [Tanmay-777](https://github.com/Tanmay-777)
- **Soundtrack:** *"CORE"* composed by Toby Fox (*UNDERTALE* OST)
