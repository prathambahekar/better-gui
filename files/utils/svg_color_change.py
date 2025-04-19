import re

def change_svg_icon_color(svg_data: str, new_color: str) -> str:
    """
    Change the fill color of an SVG icon to the new color.
    """
    return re.sub(r'fill=["\']#[0-9a-fA-F]{3,6}["\']', f'fill="{new_color}"', svg_data)

def load_svg_from_file(file_path: str) -> str:
    """
    Load the content of an SVG file.
    """
    with open(file_path, 'r') as file:
        return file.read()

# Example usage:
file_path = 'path/to/your/icon.svg'
new_color = '#FF5733'

# Load the SVG data
svg_data = load_svg_from_file(file_path)

# Change the SVG icon color
updated_svg_data = change_svg_icon_color(svg_data, new_color)

# You can then save or use the updated SVG data as needed
with open('path/to/your/updated_icon.svg', 'w') as file:
    file.write(updated_svg_data)
