Installation
============

To use Mecrisp Ice, You have to do three things:

#. `Download Mecrisp Ice <https://sourceforge.net/projects/mecrisp/files/>`_ and untar it. I recommend the    ``d`` version.  the newer versions lack a license file. If you are developing on the `Pico Ice circuit     board <https://tinyvision.ai/products/pico-ice-fpga-trainer-board>`_, then you are better off 
   downloading `Mecrisp Pi <https://github.com//mecrisp-pi/tree/main>`_.  

#. Download and install the open source Yosys OSS CAD suite `development tools 
   <https:/yosyshq.readthedocs.io/en/latest/install.html>`_.   

#. Download and install `Free Pascal <https://www.freepascal.org/download.html>`_   

#. Download and `install gforth <https://www.gnu.org/software/gforth/>`_ I am running mecrisp ice 2.6e, 
   with gForth 0.7.3.  The mecrisp 2.6e release does not work with the more recent gForth 0.79.   

Now change into the root directory and compile the Miecrisp Ice Forth Emulator. 

::

    cd common-crosscompiler
    fpc -XX -O3 icecreammachine-8kb.pas
    fpc -XX -O3 icecreammachine-16kb.pas
    rm *.o
    cd ..

Then search the root directory for your board, change into that directory read the local readme, and type: 

:: 

    ./compile
    ./compile nucleus

You can now flash the board, although the instructions to do that may well depend on the particular board. 

Simulator
---------
There are also a number of verilator simulators.  Which one should you choose?  Well on Mecrisp Pi, there 
are only two simulators, the two that are relevant for the ICE40 PSRAMs. 

* verilator-16bit
* verilator-16bit-dualport
* verilator-16bit-dualport.tar
* verilator-16bit-quickstore
* verilator-32bit
* verilator-32bit-quickstore
* verilator-32bit-singleport
* verilator-64bit

To run them, first `install Verilator <https://verilator.org/guide/latest/install.html>`_, change into the appropriate directory and type:

::

   ./compile
   ./emulate

And finally visit the `repository for this documentation   <https://github.com/PythonLinks/Mecrisp-Ice/tree/main/docs/source>`_, and create an issue or pull request for anything that you had to do differently.  
