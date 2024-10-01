Flashing the Bitstream
======================

Once you have the gateware, it needs to be downloaded to the device. 
On the Pico-Ice the easy way to do this is with the `dfu-util` command.
::
   dfu-util -a 1 -D gateware.bin

Where `gateware.bin` is the name of the gateware you are trying to download to the pico-ice. 

If That Fails
-------------

Sometimes this does not work.  `Here is why <https://github.com/FPGAwars/apio/issues/377>`_.  
In that case a different approach is needed.  The solution is to first convert the binary to a  
`UF2 file format <https://github.com/microsoft/uf2>`_.
::
    bin2uf2 -o gateware.uf2 gateware.bin

You can inspect it with uf2dump. 
:: 
    uf2dump gateware.uf2 > inspect.txt
    more inspect.txt

Then put the pico-ice RP chip in a state to receive new gateware. 
::
   On Linux:
   sudo picocom --baud 1200 /dev/ttyACM0

   On Mac:
    Flashing gateware to the Pico-Ice is not currently working on Mac OS.

If needed, delete the previous gateware.
::
   rm -f /media/devel/pico-ice/gateware.uf2

And now you can install your new gateware by copying to the pico-ice usb drive. 
::
  cp gateware.uf2 /media/devel/pico-ice/

Another Approach
----------------

Another person uses this approach.  
::
   sudo picocom --baud 1200 /dev/ttyACM0
   picotool uf2 convert <file>.bin <file>.uf2
   picotool load <file>.uf2
   picotool verify <file>.uf2
   picotool reboot
