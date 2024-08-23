Instruction set
==============

This page documents the instructions supported by the J1a, Mecrisp Ice J1a and the Hana 1 hardware.  
All of the other words, documented in the `glossary <glossary.html>`_  are built using these instructions. 

Here are the abbreviations used on this page. 

::

   a address of 16 bit value
   c address of 8 bit value (usually a character)
   d is a double number
   n means a number
   u means unsigned number
   x anything
   ud unsigned double
   xd double anything
   true 1111_1111_1111_1111
   false 0000_0000_0000_0000
   | or as in u|n

::

 noop     No Operation.  Nothing changes.
 +       ( u1|n1 u2|n2 -- u3|n3 ) Addition
 -       ( u1|n1 u2|n2 -- u3|n3 ) Subtraction
 xor     ( x1 x2 -- x3 ) Bitwise Exclusive-OR
 and     ( x1 x2 -- x3 ) Bitwise AND
 or      ( x1 x2 -- x3 ) Bitwise OR
 invert  ( x1 -- x2 )   Invert all bits
 =       ( x1 x2 -- flag )   Test for Equality
 <       ( n1 n2 -- flag )
 u<      ( u1 u2 -- flag )
 swap    ( x1 x2 -- x2 x1 )
 dup     ( x -- x x )
 drop    ( x -- )
 over    ( x1 x2 -- x1 x2 x1 )
 nip     ( x1 x2 -- x2 )
 >r      ( x -- ) (R: -- x )
 r>      ( -- x ) (R: x -- )
 r@      ( -- x ) (R: x -- x )
 !       ( u|n a-addr -- ) Stores single number in memory
 io!     ( x c-addr -- ) Stores  into IO register
 2/     ( n1 -- n2 ) Arithmetric right-shift
 2*     ( n1 -- n2 ) Arithmetric  left-shift
 exit
 hack  ( addr data  -- addr) \ writes data to io

Elided Words
------------

For more advanced users, the J1 includes elided, which execute two or more ANSI words in one clock cycle. 
You can read more at the bottom of `this page <https://github.com/jamesbowman/swapforth/blob/master/j1a/basewords.fs>`_
All of the J1 elided words are available in the cross compiled nucleus. 

Mecrisp Ice 
-----------

Mecrisp Ice adds the following words to the J1a insruction set. 


::

  1-       ( u1|n1 -- u2|n2 ) Subtracts one, optimized         
  1+       ( u1|n1 -- u2|n2 ) Adds one, optimized    
  io@      ( c-addr -- x ) Fetches from IO register    
  @        ( a-addr -- u|n ) Fetches single number from memory
  lshift   (x1 u -- x2 ) Logical  left-shift of u bit-places
  rshift   ( x1 u -- x2 ) Logical right-shift of u bit-places
  dint     ( -- ) Disable interrupt
  eint     ( -- ) Enable ticks counter overflow interrupt
  arshift  ( x1 u -- x2 ) Arithmetric right-shift of u bit-places
  rdepth   ( -- +n ) return stack depth.    
  um*low   ( u1 u2 -- ud )  16bit * 16bit = 32 bit multiplication low bits
  um*high  ( u1 u2 -- ud )  16bit * 16bit = 32 bit multiplication high bits
 
You can read the list of elided words for Mecrisp Ice in the repository.  
I am not sure if the two sets of elided words differ or not.           
But only those elided words listed in the nucleus-\*.fs file are included in the cross compiled code. 

Hana 1
------
          
The Hana 1 has 3 additional commands for controlling the SPI bus.  

::

  spi@   ( -- data )   Read a 16 bit value from SPI.    
  spi!  ( data addr -- )  Write a 16 bit value to SPI.       
  cs-   ( -- )  Turn off chip select for the FLASH. 

Flash chip select is turned on automatically when writing to FLASH. 
       
