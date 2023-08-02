import psutil
import pystray
from PIL import Image, ImageDraw, ImageFont
import time
import threading

# Function to get memory usage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Global variable to control the program's state
running = True

# Function to exit the program and stop the icon
def exit_program(icon, _item):
    global running
    running = False

# Update the icon thread with the new exit behavior
def update_icon_thread(icon):
    while running:
        memory_usage = get_memory_usage()
        icon.title = f"Memory Usage: {memory_usage:.0f}%"
        icon.icon = create_icon(memory_usage)
        time.sleep(0.5)

def create_icon(memory_usage):
    icon_size = 100  # Increase the icon size here
    image = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font_size = int(0.75 * icon_size)

    # Use the font name directly (assuming "Segoe UI" is available on your system)
    font = ImageFont.truetype("segoeui.ttf", font_size)

    # Draw the memory percentage
    memory_percentage = f"{memory_usage:.0f}"

    # Get the size of the text using draw.textbbox()
    bbox = draw.textbbox((0, 0), memory_percentage, font=font)
    percentage_width = bbox[2] - bbox[0]
    percentage_height = bbox[3] - bbox[1]

    # Calculate the center (x, y) of the icon
    icon_center_x = icon_size / 2
    icon_center_y = icon_size / 2

    # Calculate the top-left corner (x, y) of the text to position it slightly below the center of the icon
    percentage_x = icon_center_x - (percentage_width / 2)
    percentage_y = icon_center_y - (int(percentage_height / 1.05))

    draw.text((percentage_x, percentage_y), memory_percentage, font=font, fill=(0, 0, 0))

    return image

# Function to exit the program and stop the icon
def exit_program(icon, _item):
    icon.stop()

# Create the taskbar icon
def create_taskbar_icon():
    memory_usage = get_memory_usage()
    menu = (pystray.MenuItem('Exit', exit_program),)
    icon = pystray.Icon("Memory Usage", create_icon(memory_usage), "Memory Usage", menu)

    # Start the icon update thread
    update_thread = threading.Thread(target=update_icon_thread, args=[icon], daemon=True)
    update_thread.start()

    # Run the taskbar icon
    icon.run()


if __name__ == "__main__":
    create_taskbar_icon()
