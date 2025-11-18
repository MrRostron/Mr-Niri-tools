import os
from pathlib import Path


def main() -> None:
    config_path = Path("~/.config/niri/config.kdl").expanduser()
    config, toggle_off_line_num = open_config(config_path)
    config = toggle_on_off(toggle_off_line_num, config)
    write_config(config_path, config)


def open_config(path: Path) -> tuple:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found at location: {path}")
    if not path.is_file():
        raise ValueError(f"File does not exist: {path}")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"No read persmission: {path}")

    contents = []
    toggle_off_line_num = None
    with open(path, "r") as f:
        for line_num, line in enumerate(f):
            if "toggleOffTouchpad" in line:
                toggle_off_line_num = line_num
                contents.append(line)
            else:
                contents.append(line)
    return contents, toggle_off_line_num


def write_config(path: Path, config: list) -> None:
    with open(path, "w") as f:
        for line in config:
            f.write(line)


def toggle_on_off(line_num: int, contents: list) -> list:
    toggle = contents[line_num]
    leading_spaces = len(toggle) - len(toggle.lstrip())
    indent = "" * leading_spaces
    if "// off // toggleOffTouchpad" in toggle:
        toggle = f"{indent}off // toggleOffTouchpad\n"
    else:
        # Disable touchpad: add comment, keep same indentation
        toggle = f"{indent}// off // toggleOffTouchpad\n"

    contents[line_num] = toggle
    return contents


if __name__ == "__main__":
    main()
