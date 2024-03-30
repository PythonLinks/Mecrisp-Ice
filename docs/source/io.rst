I/O
===

Mecrisp Ice supports both an I/O ``io@`` and an I/O write ``io!`` command (Forth words). 
The words look much like the memory read :duref:``@`` and memory write ``!`` 
words but they work a better differently.   For memory reads and writes, the 
address really is a 13/16/32/64 bit address.  For I/O reads and writes, the 16 bit I/O address 
really represents one of 16 ports, each represented by a bit.  This I/O model comes from the MSP430 chips.  
If you read the verilog, the :duref:`io_addr` wire really should be called the :duref:`io_port` wire. 
Here are some example of I/O ports. 

::

     Addr  Bit READ            WRITE

     0001  0   PMOD in
     0002  1   PMOD out        PMOD out
     0004  2   PMOD dir        PMOD dir
     0008  3   misc.out        misc.out

     0010  4   header 1 in
     0020  5   header 1 out    header 1 out
     0040  6   header 1 dir    header 1 dir
     0080  7

     0100  8   header 2 in
     0200  9   header 2 out    header 2 out
     0400  10  header 2 dir    header 2 dir
     0800  11
  
     1000  12  UART RX         UART TX
     2000  13  misc.in
     4000  14  ticks           set ticks
     8000  15

Contents of misc.out and misc.in

::
  
   Bitmask Bit  misc.out        misc.in

     0001    0  SPI CS          UART Ready to Transmit
     0002    1  SPI MOSI        UART Character received
     0004    2  SPI SCK         SPI MISO
     0008    3  IrDA-TXD        IrDA-RXD
     0010    4  IrDA-Sleep      RTS
     0020    5  CTS             Random
     0040    6  Green LED
     0080    7  Red LED
     0100    8  Red LED
     0200    9  Red LED
     0400   10  Red LED

Of course the particular port mappings will depend on your specific board.  Please read the 
README file in the directory for the board that you are using. 

It makes sense for the software to be able to set individual bits.  But when there is a transmission protocol, 
such as SPI, this appraoch is based on the Forth software bit banging the outputs.  For example, for SPI, 
even the output clock gets bit banged!      
  
* The IN register gives the current electrical state
* The contents of the OUT registers determine what level the outputs should be
* The DIR register let you switch a pin to be an output by writing an one into

You can set two registers at once if you OR together their addresses.
  255 $440 io! should set all header pins as outputs.

Inputs can be ORed together the same way and give an ORed result.

You can detect short-circuited pins

*  for example if a pin is set to output and low, but shortened to Vcc,
*  then the OUT register will read back low, as set by you, but the
*  IN register will read high for that pin.

Misc.out and misc.in are a mixed back of wires and flags available.

No fear to destroy the IrDA transceiver with too long pulses as it turns off
the IR LED itself when IrDA-TXD is high for more than 50 us.

The UART data register is for both incoming and outgoing data,
a read from it will clear the "Character received" flag
and you should only write to it when "Ready to Transmit" is set.

Ticks contains a 16 bit cycle counter that counts up with 48 MHz and
you can set it to any value you wish by writing to it.

Memory location $0002 is an interrupt vector for the ticks counter overflow.
You can place an opcode there, perhaps ALU Exit ($608C) or a JMP to a handler.
Interrupts can be enabled with eint and disabled with dint.

