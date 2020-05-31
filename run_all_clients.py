"""
Run clients with a single file.
Depending on number of players on the map add another interfaces.
Don´t forget to run server.py in another command line.

For devel purposes.
"""
import pyglet

import client_receiver
import client_welcome_board

hostname = input("Type server's hostname: ")

client_welcome_board.create_client(hostname)
client_receiver.create_client(hostname)

pyglet.app.run()
