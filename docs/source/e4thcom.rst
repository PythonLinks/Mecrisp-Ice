e4thcom Terminal Emulator
=========================

`e4thCom <https://wiki.forth-ev.de/doku.php/en:projects:e4thcom>`_ is a terminal emulator for embedded Forth applications.
As soon as you want to upload a program, 
and not overwhelm the embedded device, you will need it.  It uploads a line at a time, and waits for the response.The Unofficial Mecrisp Stellaris has an `excellent introduction to e4thcom 
<https://mecrisp-stellaris-folkdoc.sourceforge.io/serial-terminals.html#e4thcom>`_. It is also 
`recommended by J1Sc <https://github.com/SteffenReith/J1Sc#a-forth-shellterminal-for-j1sc>`_ (J1 in Scala and SpinalHDL).
E4thcom is for Linux and there is a version for windows.  It did not run on my Apple silicon mac mini. 

There are two things I had to do to make E4thcom work with Mecrisp-Ice.  The first is that we have to run it at half duplex. 
Use the ``--hdm`` flag

``sudo ./e4thcom -d ttyACM1 -b B115200 --hdm -t mecrisp-qs``

The next is to not overwhelm the memory.  The Mecrisp Ice 16 bit single port RAM version assumes 8K words of memory.  The newer Ice40Up5K has even less block RAM.  There are only 30, 
not 32 block RAMs, so that you only have 7680 words of memory. So if your test suites crash, 
then try ``here .`` to make sure that you are not past the 8K word limit.  Then shrink down the program you are uploading. 

Remember to run it from the e4thcom directory. 

And please let me know if anyone else is using it, so that I can report multiple successful users. 
