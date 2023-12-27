"""
Jake's MIDI Push-to-Talk aka PyToTalk - Use your MIDI device for push-to-talk in Discord, Zoom, etc.
Copyright (C) 2023  Jake Brandt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time
import mido
from pynput.keyboard import Controller, Key, KeyCode

# List available MIDI ports
print("Available MIDI ports:")
print(mido.get_input_names())

# Select an input port (Jake's Arturia Minilab MKII is on 0 generally)
inport_name = mido.get_input_names()[0]

# Define a mapping from MIDI notes to keyboard keys
midi_to_key = {
    43: Key.f24,    # G3 or last drum pad on Arturia Minilab MKII
    72: 'a'         # C5 (I think?) to test a visible key ("a")
}

keyboard = Controller()

def press_keys(keys):
    if isinstance(keys, tuple):
        for key in keys:
            keyboard.press(KeyCode.from_char(key) if isinstance(key, str) else key)
    else:
        keyboard.press(KeyCode.from_char(keys) if isinstance(keys, str) else keys)

def release_keys(keys):
    if isinstance(keys, tuple):
        for key in keys:
            keyboard.release(KeyCode.from_char(key) if isinstance(key, str) else key)
    else:
        keyboard.release(KeyCode.from_char(keys) if isinstance(keys, str) else keys)

try:
    with mido.open_input(inport_name) as inport:
        while True:
            for msg in inport.iter_pending():  # Non-blocking
                if msg.type in ['note_on', 'note_off']:
                    note = msg.note
                    velocity = msg.velocity

                    if note in midi_to_key:
                        key = midi_to_key[note]
                        if msg.type == 'note_on' and velocity > 0:
                            press_keys(key)
                        elif msg.type == 'note_off' or (msg.type == 'note_on' and velocity == 0):
                            release_keys(key)
                    else:
                        print('Note not mapped:', note)

            time.sleep(0.01)  # Short sleep, _God save the CPU_
except KeyboardInterrupt:
    print("Exiting PyToTalk...")
