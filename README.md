# RAM Monitor Taskbar Icon

The RAM Monitor Taskbar Icon is a Python script that creates a taskbar icon displaying the current memory usage percentage.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the source code.

```bash
git clone https://github.com/Raz-Dahan/MemoryDisplay.git
cd MemoryDisplay
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

   ```powershell
   venv\Scripts\activate
   ```

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

Run the `ram_monitor.py` script to display the taskbar icon:

```bash
python ram_monitor.py
```

The taskbar icon will show the current memory usage percentage.

To exit the program and stop the taskbar icon, right-click on the taskbar icon and select the "Exit" option from the menu.

## Customization

You can customize the appearance of the taskbar icon by modifying the `create_icon()` function in the `ram_monitor.py` script. For example, you can change the icon size, font, colors, or add additional information to display.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The taskbar icon implementation is based on the [pystray](https://github.com/moses-palmer/pystray) library.
