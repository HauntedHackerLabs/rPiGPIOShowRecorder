# rPiGPIOShowRecorder

This program is written to allow the recording and playback of animatronic shows on Raspberry Pi.

The concept of this programm is to:

1. Play and audio file.
2. Allow the puppeteer to control servos via an attached joystick.
3. Record those servo movements for playback in an animatronic show.


Right now it is in its absolute infancy.  It is currently writing the show to a new .py that is named during a user input.  My next goal is to write the show to MongoDB.  

My ultimate dream for this program is to have a webapp that you run to record the show on a central controller device.  The central controller app will likely be written in Djanho.  Each animatronic in a show will download its show parts from this central controller.  Using MQTT or some other messaging protocol the animatronics in the show will trigger events for other animatronics to play.  Ie someone triggers a motion detector on animatronic A and it says "Hey Bob someone is coming your way."  Animatronic B "Bob" will receive the message and respond with "Okay let me get the chainsaw started!" 