from screeninfo import get_monitors

# Retrieve and print information about each display
monitors = get_monitors()
for monitor in monitors:
    print(f"Monitor: {monitor.name}")
    print(f"    Width: {monitor.width}")
    print(f"    Height: {monitor.height}")
    print(f"    Position: ({monitor.x}, {monitor.y})")
