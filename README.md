# fleaway
FreeWay Simulator

This project needs the adafruit interface.
The interface uses dma on the pwm gpio 18 (pin 12). This is not clear on the instructions since it uses a breakout board and doesn't explain it.
Since the pi runs at 3.3 volts it's best to use a voltage translator for the neopixel input.
For the pi 3 the gpio 18 is used for the sound pcm that attaches to the local sound hardware.
This needs to be disabled


* Disabling the local snd driver (hdmi or usb sound can still be used)
  * `sudo vi /etc/modprobe.d/blacklist-rgb-matrix.conf`
  * add the following lines:

    * `blacklist snd_bcm2835`
    * `blacklist snd_pc`
    * `blacklist snd_timer`
    * `blacklist snd_pcsp`
    * `blacklist snd`

  * Save the file and quit vi
  * `sudo update-initramfs -u`
  * reboot and confirm no "snd" modules are running by executing the command "lsmod"
* instructions for the rasp pi driver at adafruit
  * https://learn.adafruit.com/neopixels-on-raspberry-pi/overview
