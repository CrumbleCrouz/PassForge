import keyboard


def on_key_event(e):
    print(f"name:  {e.name}\ncode: {e.scan_code}")


keyboard.hook(on_key_event)
keyboard.wait("esc")
