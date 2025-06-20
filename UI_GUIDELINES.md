# UI Guidelines

## Creating a New Page
1. In `files/gui/pages/`, create a new file for your page.
2. Inherit from `QWidget` or a base page class (see `settings_base.py`).
3. Use components from `widget/` and styles from `theme.py`.

## Adding a New Widget
1. Add your widget to `files/gui/widget/`.
2. Import style constants from `files/gui/theme.py`.
3. Document its usage in the docstring and add it to the UI Showcase page (`ui_showcase.py`).

## Styling
- Use only constants from `theme.py` for colors, fonts, etc.
- Avoid hardcoding style values in widgets/pages.

## UI Showcase
- See `ui_showcase.py` for examples of all available widgets and their usage.

## Naming and Structure
- Use descriptive, consistent names for files, classes, and variables.
- Group related files logically (widgets, pages, icons, etc.).

## Example: Using a Themed Button
```python
from files.gui.widget.xbutton import xButton
btn = xButton("Click Me")
``` 