Test Suite
==========

Mecrisp-Ice includes an extensive test suite in ``./testsuite`` It is based on
the HAYES-FORTH test suite, with significatn modifcations for use with mecrisp-ice.
The HAYES-FORTH test suite tests compliance with ANSI Forth 2012.

You can find the Hayes Forth test suite in the directory
``./testsuite/forth2012-test-suite-master``

Here is `the original 
<https://github.com/gerryjackson/forth2012-test-suite/>`_

I recommend that first you read the test suite's README.md in either location. 
  
``./tester.txt`` implements the test program. 

Here are the individual test scripts. 

::
  
    test-core.txt
    test-core-ext.txt
    test-core-plus.txt
    test-double.txt
    test-mecrisp-ice-extras.txt
    test-strings.txt

Those all get merged into a single file called complete-test.txt.
``doubletest.fth`` tests mecrisp doubles, but is not used by the default ./testing program. 
You can read the original documentation in german in
README_DE or in README.pdf

There is a copy protected version translation into English by deepl.com at
enREADME.pdf  

If you want to run the complete tests in simulation, then execute
./testing

That will then call ./compilenucleus, which will compile the various
forth parts into a binary which can be run using the icecreammachine
emulators

  ::
  
    icecreammachine-16kb-speicherkarte
    icecreammachine-16kb-speicherkarte.o
    icecreammachine-16kb-speicherkarte.pas

``speicherkarte`` means "memory card".  I wish I knew why it had that name.

``ungetestet.txt`` means ``untested.txt``. I presume it is the parts of Forth
which were not tested by the test suite.  For example user input can
not be tested by the test suite, and hardware specific things cannot
be tested by the test suite, although they can hopefully be tested on
the verilator emulators.

The filename ``zahlenzauber.*`` filename means ``numbermagic.*`` Again I am
not sure what it does or why it has that name.

You can also run the forth test suites on your favorite verilator simulator.
I just copied the file and pasted it into the simulator terminal.   It all worked fine. 

Testing on the FPGA
-------------------

We could in principal run the test suites on the hardware devicesbut that is more difficult. 
For that it is recommended that you use the e4thcom terminal emulator.  It makes it possible to load the files. 

Original Hayes Forth test suite documentation
---------------------------------------------

Below is part of the original Hayes Forth documentation translated to English by Google Docs. 

In this environment, the (extended) Hayes-Forth tester is executed,
which checks the definitions for their standard-compliant function and
all operators for correct results, whereby trivial cases are also
captured and checked. This Hayes test suite is structured logically,
so that the tests only use primitives that have already been tested
correctly as far as possible.

Matthias adapted and expanded this test suite to the special features
of Mecrisp-Ice.  His changes are in the files in the top level
directory.

After the tests have been run, the emulator checks the memory image
for places that were neither read nor executed and can assign these to
the individual definitions using a rudimentary interpretation of the
dictionary structure. This allows the test coverage to be checked and
completed.

There are some routines in the Forth core that can only be
meaningfully executed when used manually (e.g. pressing the delete key
when typing commands), only in the event of an error (e.g. aborting
the program) or only in real hardware (IO registers, interrupts). and
therefore not captured by the automatic tests. However, these cases
are manageable, can be tried out in real hardware and have been found
to be good.

The entire test suite can also be executed on the logic of the "real"
processor simulated in Verilator. This makes it possible to compare
the test results in the emulator with the actual implementation of the
processor in logic and to exclude errors in the processor source code
itself, at least to the extent that they change its functionality as
covered by the test. However, in Verilator, juggling the memory image
itself is more complicated, so the test coverage sample is performed
in the emulator.
