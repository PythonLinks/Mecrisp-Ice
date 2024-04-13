e4thcom Terminal Emulator
=========================

`e4thCom <https://wiki.forth-ev.de/doku.php/en:projects:e4thcom>`_ is a terminal emulator for embedded Forth applications.
As soon as you want to upload a program, 
and not overwhelm the embedded device, you will need it.  It uploads a line at a time, and waits for the response.The Unofficial Mecrisp Stellaris has an `excellent introduction to e4thcom 
<https://mecrisp-stellaris-folkdoc.sourceforge.io/serial-terminals.html#e4thcom>`_. It is also 
`recommended by J1Sc <https://github.com/SteffenReith/J1Sc#a-forth-shellterminal-for-j1sc>`_ (J1 in Scala and SpinalHDL).
E4thcom is for Linux and there is a version for windows.  It did not run on my Apple silicon mac mini. 

Here is the basic command.  

``sudo ./e4thcom -d ttyACM1 -b B115200 --hdm -t mecrisp``

There are three different possible choices for the -t option.  ``mecrisp``,    ``mecrisp-qs`` and  ``mecrisp-st``.  The e4thcom author recommends that you use the ``-t mecrisp`` version for 16 bit systems and the  ``-t mecrisp-st`` for 32 bit versions.  

The ``--hdm`` option tells it to run at half duplex.   The problem is that on my 12 Mhz pico-ice board it would only accept about 34 characters per line, before having a problem. In half duplex, e4thcom waits, after sending a char, until an echo is received.   With faster clocks you should be able to drop the ``--hdm`` option.  The pico-ice also runs at 48Mhz.  

The next challenge is to not overwhelm the memory.  The Mecrisp Ice 16 bit single port RAM version assumes 8K words of memory.  The newer Ice40Up5K has even less block RAM.  There are only 30, 
not 32 block RAMs, so that you only have 7680 words of memory. So if your test suites crash, 
then try ``here .`` to make sure that you are not past the 8K word limit.  Then shrink down the program you are uploading. 

Remember to run it from the e4thcom directory. 

And please let me know if anyone else is using it, so that I can report multiple successful users. 

If you have problems, you can run it  like this

``  ./e4thcom -t test (your -p and -b option ...) | tee test-merisp-ice.txt
``

And post the ``test-mecrisp-ice.txt`` as an issue on the github repository, linked in the upper right hand corner of this page.  

In the process of debugging it, the e4thcom author wrote a brilliant email. 

  On 12.04.24 

    If I type this line, the cursor hovers over the last l,
    : char+ ( u -- u+1 ) 1+ ; 1 foldable

  A timing problem. B115200 seams to be a bit to fast for the target. The target missed the last two chars and the trailing CR, that was added by the Enter key.  Because of the missing CR the target was still waiting for input.
         
    If I hit return it crashes.

  Crashes is a bit misleading here. Return/Enter did send a CR to the target, that was still waiting for input. The CR made the target interpret its TIB [: char+ ( u -- u+1 ) 1+ ; 1 foldab] and return an error message because foldab was not a valid name.

    If I type these two lines

    : char+ ( u -- u+1 ) 1+ ;

    1 foldable

    I get the ok.

  That makes clear, that it is a timing problem. The target misses chars when more than ~ 34 are send.

  So there is no protocol missmatch with the command line communication.

    The magic is if I type this line.

    : char+ ( u -- u+1 ) 1+ ; 1 foldable

    And do not hit the enter.  Remember the cursor is hovering over the last l.  

    If I then type "le" <enter> It works fine.

  This is, because the target waits for the chars (leCR) that got lost.
  So the problem is that it is dropping the last "le".
  I think it needs to pause after the ";"

  No, no pause needed there. Nothing is interpreted until the CR is received.

  B115200 is simply to fast for the target (as it is now). If you want or must stay with B115200 you can try to circumvent the problem by starting e4thcom with the --hdm option (halve duplex mode). Then e4thcom waits, after sending a char, until an echo is received. This should solve the timing problem here.Please be aware that trying to upload files with e4thcom although the command line communication is not working properly, is a waste of time and energy. It will not work because the protocol for uploading is more complicated than that for the command line communication.

  e.g.: The above recording creates questions that will disappear when the command line communication words. So don't care.

  When the command line communication works (which does not require any -t option) try to use -t mecrisp for a 16 Bit mecrisp-ice ore mecrisp-st for a 32 bit mecrisp-ice to test uploading files. I expect the plug-ins will work without modifications.
