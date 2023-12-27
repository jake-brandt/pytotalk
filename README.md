# Jake's MIDI Push-to-Talk aka PyToTalk

This was an uber-quick, no-patterns-followed prototype that I can use
for Push To Talk in Discord voice chat (or any other non-admin application,
to be honest).

## To install

1. Check out this repo somewhere on your computer.
2. Make sure you have Python 3.11.x installed.
3. Either use `pipenv` or `venv` to create a virtual environment if you prefer clean systems like I do; or if you're a wild animal use the system-level Python environment.
4. If using `pipenv`, run `pipenv install` to restore dependencies. If using `venv` or system-level environments, run `pip install -r requirements.txt`.

## To use

Ensure you are in your correct Python environment (or use the pipenv `run` command) and launch `pytotalk.py`. Without any modifications, the script will use the first MIDI device it finds; and the only key mapped is the default note for Drum Pad 8 (last pad) on the Arturia MINILAB mkII, note 43 or G3. Press this key down (or G3 on the main keyboard portion) and keyboard key F24 will be pressed once; and upon release, the simulated F24 keypress will be released. It should not repeat like a physical keyboard.

In Discord, for example, you can now head over to your push-to-talk settings and record this keypress while the script is running.

And there you have it.

## Modifying

You can map as many MIDI notes to as many keycodes as you like by modifying the `midi_to_key` dictionary. You can even get creative and handle other MIDI events - perhaps changing a knob to a volume control, for example.

You may also need to modify the MIDI instrument it binds to, if you happen to have more of a studio setup than I. Someday I hope to have that problem.

Another worthwile change would be the sleep time in the main application event loop; increase this sleep duration to reduce the load on CPU; I haven't tested any values other than the initial so far. Do note that an increase in sleep times will have a proportional increase in maximum latency for keypresses.

## Limitations and Admininistrative Apps (Windows)

I haven't tested this too much yet; other than confirming I can control Discord's push-to-talk with it. In theory it should work for any non-administrator application; **and if elevated to administrator**, should also be able to send events to any administrator-level application. I quickly tested this with Command Prompt and the letter "a" mapped to C5 - pretty thorough test suite if you ask me.

*However*, as generous and generally helpful as the open source community is, one should never blindly run an application as an administrator without first vetting the application as well as its dependencies. 

## License and Warranty Exclusion

Please refer to `COPYING`; it shouldn't get in your way if you're here to learn or use the app for open source or personal reasons :)