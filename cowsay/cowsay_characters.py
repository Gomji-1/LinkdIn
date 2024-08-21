import cowsay

# List of characters to use
characters = [
    'cow', 'tux', 'beavis', 'dragon', 'ghostbusters', 'kitty', 'meow', 'stimpy', 'turkey'
]

# Message to display
message = "Hello, World!"

# Iterate over the list of characters and print the message using each character
for character in characters:
    try:
        print(f"Using character: {character}")
        # Call cowsay with the specified character
        getattr(cowsay, character)(message)
    except AttributeError:
        print(f"Character '{character}' not found in cowsay.")
