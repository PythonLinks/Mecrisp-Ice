Cross Compiler
###############

This page documents the Mecrisp-Ice cross compiler.  The cross compiler runs on the desktop,  takes an instruction set, and a  nucleus file and generates a hexadecimal file which verilog can load into the FPGA.  In mecrisp-ice that hex file is merged on the desktop with mecrisp libraries and your applicaiton program before being downloaded in the FPGA bitstream.  The cross compiler suports both `code folding <https://mecrisp-stellaris-folkdoc.sourceforge.io/folding.html>`_, and inlining.

@PythonLinks: "the cross compiler is most difficult to understand." 

@Mecrisp: "I agree. And this is **after** I commented it.  The one by James Bowman is even harder to read."

So ``???`` denotes the parts that I still do not understand.


The cross compiler files are in ``./common-crosscompiler``.
The cross compiler itself is in ``cross-*.fs`` where the ``*`` denotes which architecture it works on. 
In that directory you will also find the ``instructionsset-*.fs`` files which define the words provided by the hardware. 

Usage
-----

:: 

   gforth cross.fs <instructionset*.fs> <nucleus-*.fs>

  Where ``instructionset-*.fs`` defines the Forth words provided by the hardware.
  and ``nucleus-*.fs`` brings up a useable system.

How does it all work?  First you load the instructions into the cross compiler.  That defines words that the hardware supports, as well as the bits that get set for each instruction.  Then you load the nucleus.  That controls which hardware words are available on the target device, and enables program compilation. Then you load Mecrisp libraries and your application. 


The first complexiy is that there are three dictionaries.  What gForth calls ``word lists``.   

1. The main gforth dictionary to which are added a few helpers and tools as listed below.  

2. The cross compiler dictionary for the definitions and labels that are available only when the crosscompiler is running, but are not downloaded to the FPGA.  This prevents bloat.  These words redefine words that are in gForth, but are only used in cross compiling, not in gForth itself. In order to not break gForth, they are in a spearate dictionary. This dictionary is initially populated by the cross-compiler, and additional words are added by ``instructionset-\*.fs``.  There are a lot more named definitions in the cross compiler dictionary than in the target FPGA's dictionary.

3. The target dictionary for words that are downloaded to the target FPGA.  

The next complexity is that words are defined with  ``:``, ``::`` and ``header-* ``.
Depending on the target word list, ``:`` either adds word to the base gForth word list, or to the 
cross compiler word list.  ``::`` adds words to the cross compiler word list, and ``header-*``
adds them from the cross-compiler word list to the target word list.  Later, when loading Mecrisp libraries and application files, 
``:`` adds words to the target word list.  Did you get that?  It is all quite confusing. More importantly did I get that right?  

In gForth, when searching for a word,  there is a ``search-order`` for the word lists (dictionaries).  In gForth,  there is also a curent word list.  When compiling a word, it gets added to the current word list.  You can switch between current word lists with the following commands. 

target   

]         target 

meta     forth definitions 

[        forth definitions ;


Words Added to the gForth Main Dictionary
*****************************************

tcell  ( -- cellsize ) Number of bytes in a word.  2/4/8 for 16/32/64 bit designs.

tbits  ( -- bits ) Number of bits in a word. 

tmask  ( -- mask ) Adds one to the number of tbits.  ??? What is this used for?

tcells ( n -- n*cell )  Total amount of FPGA RAM to be initialized.

tcell+ ( n -- n+cell ) Adds n to the amount of RAM to be initialized. 

tflash The size of the final image.

_tbranches Stores branch addressess to simplify cross compilation.  Also saved to the build directory. 

tbranches ???

tdp Target dictionary Pointer.  used by the next three words.

org (n -- ) Write to target dictionary pointer.

there ( -- n) Read from target dictionary pointer.

twalign  ( -- )   Make target dictionary pointer even

Edit the Memory Area to be copied to Flash
------------------------------------------

tc!      ( c t-addr -- )  Write a byte/character to a memory area to be copied to flash. 

tc@      ( t-addr -- c )  Read a byte/character from the memory area to be copied to flash. 

tw!      ( w t-addr -- )  Write a word to the memory area to be copied to flash. 

tw@      ( t-addr -- w )  Read a word from the memory area to be copied to flash.  Unsigned, as expected for 16 bit target memory contents.

tc,      ( c -- ) Add byte/character to target dictionary

tw,      ( w -- ) Add word to target dictionary


add-order  ???

target-wordlist This is the list of words to be written to the FPGA's RAM. 

Numbers in crosscompilation environment
---------------------------------------

Unfortunately, it isn't easily possible to rewire the host's number parsing capabilities...
Therefore, all numbers for target usage need to be prefixed with an ugly d# or h#

sign>number   ( c-addr1 u1 -- ud2 c-addr2 u2 )

Stack effects for these are "final effects", actually they are writing literal opcodes.
 
d#     ( -- x )    Interprets the next string as a decimal. 


h#     ( -- x )    DInterprets the next string as a hexadecimal

[']    ( -- addr ) pushes the address of a word onto the stack.

[char] ( -- c )    char literal ;

[if]         ???  

[else]        ???

[then]        ???

literal Generates a literal instruction defined by the first bit being set to 1.  If the number already has a first bit set to 1, inverts it, sets the now zero first bit to 1, and then adds the invert command to the emitted Forth. 

tail-call-optimisation If the last word in a definition is a call, then we can just return up another level. 

header  Adds a word to the target dictionary.

header-imm  Adds an immediate word to the target dictionary. 

The following words add a word to the target dictionary, and mark that it is foldable if that 
many arguments are all literals.  For example 2 3 + just generaes a 5, and ``+`` is called 2 foldable. 
This reduces the required memory. 

header-imm-0-foldable Adds an immediate foldable word to the target dictionary. 

header-0-foldable

header-1-foldable

header-2-foldable

header-3-foldable

header-4-foldable

Words for Generating he Output File
-----------------------------------
example

resolve ( orig -- ) Forward reference from orig to this location

.trim ( a-addr u )  shorten string until it ends with '.'

.suffix  ( c-addr u -- c-addr u ) e.g. "bar" -> "foo.bar"

create-output-file w/o create-file throw ;

out-suffix ( s -- h ) \ Create an output file h with suffix s
   
prepare-listing ( -- )
 
dumpall Saves the memory, and also the word index. 


Cross Compiler Words
********************

Hre are gForth words which are included in the cross compiled environment.  

(  Comments

\  Comments

org         Write to target dictionary pointer.

include     includes words from a Forth file. 

included     ???

if       

then     

else     

begin    

again    

until   

while      

repeat   

:  Half way through the ``cross-compiler-*.fs``, ``:`` is redefined.  It still defines a new word, but only for the cross-compiler. There are commands to switch between using the cross-compiler dictionary and the target dictionary. 

wordstr ( "name" -- c-addr u )   Scan ahead in the input line in order to parse the next word without removing it from the input buffer.  Just for pretty listing file printing, nothing special happens here.

String Functions
----------------

>str ( c-addr u -- str ) A new u char string from c-addr.

str@  (  c-addr -- str ) Read string from c-addr.

str! ( str c-addr -- c-addr' ) Copy str to c-addr.

+str ( str2 str1 -- str3 ) Concatenate two strings. 

base>number   ( caddr u base -- )
 

:noname   ( -- ) ; \ This is doing nothing. Just syntactical sugar for the human in order to have a matching pair for ;

;fallthru ( -- ) ; \ Syntactical sugar, too.

, ( w -- ) \ Add a word to target dictionary, this time visible from within the crosscompilation environment.

allot ( u -- ) \ "Allot" space in the target dictionary by filling in zeros.

; \ End a word definition

jmp ( "name" -- )  Add jump opcode to destination label
jz  ( "name" -- ) Add conditional opcode to destination label

create ( "name" -- ) Create allows the creation of named memory locations.
They are named in host only during crosscompilation.
For target usage, they just write a literal into the binary image.

inline: ( "name" -- )  The idea of inline: is to parse the next definition, 
which needs to be a single opcode routine,
and to append that opcode to the target dictionary when executed.
Replaces the variable with an inline fetch using a high-call. Usage "<variable> @i"
Generates a call to the next location. The following part of the definition is thus executed twice.

@i ( addr -- x ) \ Effect similar to @ on final execution ( -- ) on compilation. Replaces the variable with an inline fetch using a high-call. Usage "<variable> @i"

DOUBLE ( -- )  Generates a call to the next location. The following part of the definition is thus executed twice.

Wordlist juggling tools to properly switch into and out of the crosscompilation environment.
--------------------------------------------------------------------------------------------

    

t' ( -- t-addr )  Tick for target definitions




QUESTIONS
*********

This is where I ask the questions I am not yet sure about. 

Why are we doing

tflash      1024 32 * tcell * erase

_tbranches  1024 64 * tcell * erase

I thought it should be 8K 16 tcell * * erase

And what is this? 

: tbranches cells _tbranches + ;

What is a high call?

what is the -8kb stuff.  I thought all of the J1 16 bits architectures could only access 8 kb. 

wordlist constant target-wordlist
: add-order ( wid -- ) >r get-order r> swap 1+ set-order ;
: :: get-current >r target-wordlist set-current : r> set-current ;

