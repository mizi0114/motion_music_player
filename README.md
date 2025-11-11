# motion_music_player
Music player using a motion sensor to activate

I created a music player to plays snippets of audio when activated by motion. It will be used for installation during a party or simular by the entrance for when people arrive. 
Uses the PyDub Python module. 

Equipment used 

- Raspberry Pi 4
- PIR Motion Sensor
- External Speaker (MiniRig 2 in my case)

Cron is then used to launch the .sh script upon booting, a 30 second delay when scheduling the .sh file is recommended, to allow the system to boot up properly. 
