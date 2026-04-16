# Bad Apple!! Terminal Player

A Windows command-line player that renders the *Bad Apple!!* music video as ASCII art directly in the console, with synchronized audio playback.

---

## Requirements

- **OS:** Windows (uses `winsound`, `ctypes`, Windows console APIs)
- **Python:** 3.10+ (uses `match` statements)
- **Dependencies:**
  - [Pillow](https://pypi.org/project/Pillow/) — `pip install Pillow`
- **Assets (must be present in the same directory):**
  - `Bad Apple!!.wav` — audio file
  - `frames/` — folder containing JPEG frames named `BA-00000.jpg` through `BA-06572.jpg`

---

## File Structure

```
├── frames/                  # JPEG frames (BA-00000.jpg ... BA-06572.jpg)
├── BA_custom_config.py      # Interactive configuration editor
├── BA_incheck.py            # Input validation utilities
├── BA_main.py               # Entry point
├── BA_menu.py               # Main menu and preset configuration
├── BA_player.py             # Playback engine
├── Bad Apple!!.exe          # (optional standalone executable)
├── Bad Apple!!.mp4          # Source video (reference)
├── Bad Apple!!.wav          # Audio file (required)
└── README.txt
```

---

## Usage

Run the player with:

```bash
python BA_main.py
```

On launch you will be prompted to press `ENTER` to continue or `0` to exit. You will then be taken to the configuration/preset menu.

---

## Configuration Menu

| Option | Description |
|--------|-------------|
| `1` | Recommended — 160×120, winsetcursor, Raster Font size 6 |
| `2` | Reduced Size — 120×90, winsetcursor, Raster Font size 6 |
| `3` | Miniplayer — 60×45, winsetcursor, Raster Font size 6 |
| `4` | Edit custom configuration |
| `5` | Play with current custom configuration |
| `0` | Exit |

Selecting a preset (1–3) immediately launches playback with those settings. Use option `4` to tweak individual settings, then `5` to play.

---

## Custom Configuration Options

| # | Setting | Description | Example values |
|---|---------|-------------|----------------|
| 1 | **Resolution** | Number of character columns × rows | `160 120`, `120 90`, `60 45` |
| 2 | **Window margin** | Right and bottom console padding | `3 3`, `4 5` |
| 3 | **Cleaning mode** | How the screen is cleared between frames | `winsetcursor`, `wincls`, `newline 84` |
| 4 | **Cleaning delay** | Delay between frames in milliseconds | `0`, `33`, `1000` |
| 5 | **Play music** | Enable or disable audio | `y` / `n` |
| 6 | **Countdown** | Seconds to wait before starting | `0`, `3`, `5` |
| 7 | **Starting frame** | Frame number to start from (max: 6572) | `0`, `824` |
| 8 | **Custom font** | Console font to use during playback | `none`, `raster, 6`, `Consolas, 8` |

### Cleaning Modes

- `winsetcursor` — moves the console cursor back to the top and overwrites the previous frame. Smoothest playback.
- `wincls` — runs `cls` between frames. More flicker, but compatible with all terminals.
- `newline <n>` — prints `n` blank lines between frames (e.g. `newline 84`).

### Custom Font

Fonts are loaded from `C:\Windows\Fonts`. Options:

- `none` — keep the current console font unchanged
- `raster` — use Windows Raster Fonts 8×8 at size 6 (recommended)
- `<font name>` — use a named installed font at default size 6
- `<font name>, <size>` — use a named installed font at a specific size

> **Note:** The recommended font is included in the project directory. Install it before running for best results.

---

## Pixel Mapping

Each video pixel is mapped to one of four ASCII characters based on brightness:

| Brightness | Character | Meaning |
|------------|-----------|---------|
| ≥ 235 | `o` | White |
| 157–234 | `x` | Light gray |
| 81–156 | `+` | Dark gray |
| ≤ 80 | ` ` (space) | Black |

---

## Modules

### `BA_main.py`
Entry point. Calls the menu, collects configuration, and starts playback.

### `BA_menu.py`
Displays the startup message and the preset/configuration selection menu. Returns the final configuration dictionary to `BA_main`.

### `BA_custom_config.py`
Interactive settings editor. Receives the current configuration dictionary, allows editing individual fields, and returns the updated configuration.

### `BA_player.py`
Core playback engine. Handles font setup, window sizing, countdown, audio, frame rendering, and console clearing. Reads JPEG frames from the `frames/` directory using Pillow and prints them as ASCII art.

### `BA_incheck.py`
Input validation helper. Provides `inputcheck(user_input, type)` which returns `True` if the input can be cast to the specified type (`"int"`, `"float"`, `"str"`).

---

## Known Limitations

- **Windows only** — relies on `winsound` and Windows console APIs (`ctypes.windll`).
- Frame filenames are hardcoded to the `BA-XXXXX.jpg` format with a max of frame 6572.
- The `starting_frame` option offsets playback but audio always starts from the beginning.
