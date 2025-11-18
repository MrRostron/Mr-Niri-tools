# Touchpad Toggle Script

A simple Python script to toggle touchpad on/off for the [niri](https://github.com/YaLTeR/niri) compositor.

## Description

This script modifies the niri configuration file (`~/.config/niri/config.kdl`) to toggle the touchpad state by commenting/uncommenting the `off` setting for the touchpad input section.


Your niri config should have a touchpad section that looks like this:
input touchpad {
    // off // toggleOffTouchpad
    // ... other settings
}
This script looks for the specific inline comment // toggleOffTouchpad to identify the line to modify. Make sure this comment exists in your config file.

## Installation
- clone or download the respository
- ensure the script is executable
```bash
chmod +x toucpad_toggle
```

## Usage

1. Make sure you have a niri configuration file at `~/.config/niri/config.kdl`
2. Run the script:
   ```bash
   python touchpad_toggle.py
   ```
3. Or set to a keybinding
