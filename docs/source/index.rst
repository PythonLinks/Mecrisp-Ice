=====================================
Mecrisp Ice Unofficial Documentation!
=====================================

**Mecrisp Ice** is a family of 16, 32 and 64 bit soft core forth
processors written in Verilog and based on the J1 stack machine. Mecrisp Ice supports the following
boards.


.. csv-table:: Supported Boards 

    "blackice2",    "hx8k-32bit",  "tinyfpga-bx"
    "fomu",         "icebreaker",  "ulx3s"
    "fomu-ledcomm", "mch2022",     "ulx3s-usb-experimental"
    "hx1k",         "mystorm",     "hx8k" 
    "nandland",     "`Pico-Ice <https://sourceforge.net/p/mecrisp/discussion/general/thread/350a65f919/>`_"
 


This repository includes:

* ready-to-fly versions of the J1 for many boards. Search for your board name in the root
  directory change into that directory, read the local README,
  and type "./compile". That will generate the bitstream (also called gateware ) for that board.
  How to download it to your board will depend on the specific board and operating system.

* Verilog definitions for the various processors, as well as additional useful
  modules in ./common-verilog.

* Ready-to-emulate verilator simulators for the different versions in ./verilator*

* Cross compilers for the different versions, and the definitions of the various instructions sets are located in ./common-crosscompiler.

* An extended version of the Hayes-Forth test suite is located in
  ./testsuite. The original documentation is in German and computer generated translations are available in English. 

* Pascal simulators are also in ./common-crosscompiler.

* A easy-to-use starting point for defining your own board can be found in
  ./skeletalstructure and

If you have any questions, please post them on `our discussion board
<https://sourceforge.net/p/mecrisp/discussion/general/>`_

.. note::

Posting issues and pull requests is most welcome.   

I completed my master's thesis in September 2024.  I built a single port stack machine, based on Mecrisp Ice, running on the Pice-Ice circuit board, on a Lattice  ICE40 UP5K FPGA. 

Contents
--------

.. toctree::


   api
   contact
   cross-compiler
   e4thcom
   flashing
   glossary
   instruction-set
   io
   license
   links
   pseudo-dual-port
   test-suite
   tool-chain
   usage
   variables
