import psutil
import pystray
from PIL import Image, ImageDraw, ImageFont
import time
import threading

# Function to get memory usage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=None, percpu=False)

# Global variables to control the program's state, text color, and display mode
running = True
text_color = (0, 0, 0)  # Default color: black
display_mode_memory = True  # Default display mode is memory usage

# Function to exit the program and stop the icon
def exit_program(icon, _item):
    global running
    running = False
    icon.stop()

# Function to toggle the text color between white and black
def toggle_text_color(icon, _item):
    global text_color
    if text_color == (0, 0, 0):  # Current color is black, change to white
        text_color = (255, 255, 255)
    else:  # Current color is white, change to black
        text_color = (0, 0, 0)

# Function to toggle between displaying memory usage and CPU usage
def toggle_display_mode(icon, _item):
    global display_mode_memory
    display_mode_memory = not display_mode_memory

# Update the icon thread with the new exit behavior
def update_icon_thread(icon):
    while running:
        if display_mode_memory:
            usage_percentage = get_memory_usage()
            icon.title = f"Memory Usage: {usage_percentage:.0f}%"
        else:
            usage_percentage = get_cpu_usage()
            icon.title = f"CPU Usage: {usage_percentage:.0f}%"

        icon.icon = create_icon(usage_percentage)
        time.sleep(0.5)

def create_icon(usage_percentage):
    icon_size = 100  # Increase the icon size here
    image = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font_size = int(0.75 * icon_size)

    # Use the font name directly (assuming "Segoe UI" is available on your system)
    font = ImageFont.truetype("segoeui.ttf", font_size)

    # Draw the percentage
    usage_text = f"{usage_percentage:.0f}"

    # Get the size of the text using draw.textbbox()
    bbox = draw.textbbox((0, 0), usage_text, font=font)
    usage_width = bbox[2] - bbox[0]
    usage_height = bbox[3] - bbox[1]

    # Calculate the center (x, y) of the icon
    icon_center_x = icon_size / 2
    icon_center_y = icon_size / 2

    # Calculate the top-left corner (x, y) of the text to position it slightly below the center of the icon
    usage_x = icon_center_x - (usage_width / 2)
    usage_y = icon_center_y - (int(usage_height / 1.05))

    draw.text((usage_x, usage_y), usage_text, font=font, fill=text_color)

    return image

# Create the taskbar icon
def create_taskbar_icon():
    usage_percentage = get_memory_usage()

    # Create the menu with the "Toggle Text Color", "Toggle Display Mode", and "Exit" options
    menu = (pystray.MenuItem('Toggle Text Color', toggle_text_color),
            pystray.MenuItem('Toggle Display Mode', toggle_display_mode),
            pystray.MenuItem('Exit', exit_program))

    icon = pystray.Icon("Usage Display", create_icon(usage_percentage), "Usage Display", menu)

    # Start the icon update thread
    update_thread = threading.Thread(target=update_icon_thread, args=[icon], daemon=True)
    update_thread.start()

    # Run the taskbar icon
    icon.run()


if __name__ == "__main__":
    create_taskbar_icon()
