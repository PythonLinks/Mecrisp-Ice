Cross Compiler
==============

This page documents the Mecrisp-Ice cross compiler.  
Historically cross compilers are most difficult to understand. 

@PythonLinks: the cross compiler is most difficult to understand. 

@Mecrisp: I agree. And this is *after* I commented it.  The one by James Bowman is even harder to read.

The first complexity is that words are defined with both : and ::.  In the cross compiler initially : defines gforth words, then : defines cross compier words, and :: defines downloaded words.   Similarly in the nulcleus.fs files : defines cross comipiler words and :: defines downloaded words.  The header-* commands also define downloaded words. 

The next complexiy is that there are three dictionaries  

1. The main gforth dictionary to which are added a few helpers and tools like #d and #h defined below. 

2. One for the definitions and labels that are available only when the crosscompiler is running, but 
are not downloaded to the FPGA.  These words redefine words that are in gForth, but are only used in cross compiling, not in gForth itself. In order to not break gForth, they are in a spearate dictionary. 
They are not downloaded to the FPGA, to prevent bloat.  There are a lot more named definitions in nucleus.fs than in the dictionaty chain of the final binary image.  They could be added to the final image using the header commands. 

3. One for the words that end up in the final bitstream.  These word definitions start with ::
The dictionary entries defined with the header-... macros are also available in the final crosscompiled nucleus.

Words Added to the GForth Main Dictionary
-----------------------------------------

#d  Interprets the next string as a decimal. 

#h Interprets the next string as a hexadecimal

tcell  ( -- cellsize ) Number of bytes in a word.  2/4/8 for 16/32/64 bit designs.

tbits  ( -- bits ) Number of bits in a word. 

tmask  ( -- mask ) 

tcells ( n -- n*cell ) 

tcell+ ( n -- n+cell ) 

tflash The size of the final image.

_tbranches Stores branch addressess to simplify cross compilation.  Also saved to the build directory. 

tbranches

tdp Target dictionary Pointer.  used by ``here``

org (n -- ) Write to target dictionary pointer.

there ( -- n) Read from target dictionary pointer.

Edit the Memory Area to be copied to Flash
------------------------------------------

tc!      ( c t-addr -- )  Write a character to a memory area to be copied to flash. 
tc@      ( t-addr -- c )  Read a character from the memory area to be copied to flash. 
tw!      ( w t-addr -- )  Write a word to the memory area to be copied to flash. 
tw@      ( t-addr -- w )  Read a word from the memory area to be copied to flash.  Unsigned, as expected for 16 bit target memory contents.

twalign  ( -- )   Make target dictionary pointer even
tc,      ( c -- ) Add byte to target dictionary
tw,      ( w -- ) Add word to target dictionary

target-wordlist
add-order

Cross Compiler  Words
--------------------

First we have gForth words which are included in the cross compiled environment. 

(  Comments
\  Comments

org         Write to target dictionary pointer.
include       
included      
[if]          
[else]       
[then]       

literal Generates a literal defined by the first bit being set to 1.  If the number already has a first bit ste to 1, inverts it, sets the first bit to 1, and then adds the invert command.

tail-call-optimisation If the last word in a definition is a call, then we can just return up another level. 

header  Adds a word to the target dictionary.

header-imm
header-imm-0-foldable

These words add a word to the target dictionary, and mark that it is foldable if that 
many arguments are all literals. 

header-0-foldable

header-1-foldable

header-2-foldable

header-3-foldable

header-4-foldable

:  This defines a new word, but only for the cross-compiler. 

: wordstr ( "name" -- c-addr u )   \ Scan ahead in the input line in order to parse the next word without removing it from the input buffer.
Just for pretty listing file printing, nothing special happens here.


Words Available on the FPGA
---------------------------

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

 
: target    only target-wordlist add-order definitions ;
: ]         target ;
:: meta     forth definitions ;
:: [        forth definitions ;

: t' ( -- t-addr ) bl parse target-wordlist search-wordlist 0= throw >body @ ; \ Tick for target definitions

\ -----------------------------------------------------------------------------
\  Numbers in crosscompilation environment.
\  Unfortunately, it isn't easily possible to rewire the host's number parsing capabilities...
\  Therefore, all numbers for target usage need to be prefixed with an ugly d# or h#
\ -----------------------------------------------------------------------------

: sign>number   ( c-addr1 u1 -- ud2 c-addr2 u2 )
    0. 2swap
    over c@ [char] - = if
        1 /string
        >number
        2swap dnegate 2swap
    else
        >number
    then
;

: base>number   ( caddr u base -- )
    base @ >r base !
    sign>number
    r> base !
    dup 0= if
        2drop drop literal
    else
        1 = swap c@ [char] . = and if
            drop dup literal 16 rshift literal
        else
            -1 abort" Bad number."
        then
    then ;

\ Stack effects for these are "final effects", actually they are writing literal opcodes.

:: d#     ( -- x )    bl parse 10 base>number ;
:: h#     ( -- x )    bl parse 16 base>number ;
:: [']    ( -- addr ) ' >body @ tcell * literal ;
:: [char] ( -- c )    char literal ;

\ -----------------------------------------------------------------------------
\  Control structures for the crosscompiler.
\  This is much more comfortable than using labels and jumps manually.
\ -----------------------------------------------------------------------------

: resolve ( orig -- )
    tdp @ over tbranches ! \ Forward reference from orig to this location
    dup tw@ tdp @ tcell / or swap tw!
;

:: if      tdp @ 0 0branch ;
:: then    resolve ;
:: else    tdp @ 0 ubranch swap resolve ;
:: begin   tdp @ ;
:: again   tcell / ubranch ;
:: until   tcell / 0branch ;
:: while   tdp @ 0 0branch ;
:: repeat  swap tcell / ubranch resolve ;

\ -----------------------------------------------------------------------------
\  A little mess just for handling output file names.
\  Quite unimportant for understanding the crosscompiler.
\ -----------------------------------------------------------------------------

: .trim ( a-addr u ) \ shorten string until it ends with '.'
    begin
        2dup + 1- c@ [char] . <>
    while
        1-
    repeat
;

( Strings                                    JCB 11:57 05/18/12)

: >str ( c-addr u -- str ) \ a new u char string from c-addr
    dup cell+ allocate throw dup >r
    2dup ! cell+    \ write size into first cell
                    ( c-addr u saddr )
    swap cmove r>
;
: str@  dup cell+ swap @ ;
: str! ( str c-addr -- c-addr' ) \ copy str to c-addr
    >r str@ r>
    2dup + >r swap
    cmove r>
;
: +str ( str2 str1 -- str3 )
    over @ over @ + cell+ allocate throw >r
    over @ over @ + r@ !
    r@ cell+ str! str! drop r>
;

: example
    s"  sailor" >str
    s" hello" >str
    +str str@ type
;

next-arg 2dup .trim >str constant prefix.
: .suffix  ( c-addr u -- c-addr u ) \ e.g. "bar" -> "foo.bar"
    >str prefix. +str str@
;
: create-output-file w/o create-file throw ;
: out-suffix ( s -- h ) \ Create an output file h with suffix s
    >str
    prefix. +str
    s" build/" >str +str str@
    create-output-file
;

: prepare-listing ( -- )
    s" lst" out-suffix lst !
;

\ -----------------------------------------------------------------------------
\  Finally, load the source file which shall be crosscompiled.
\ -----------------------------------------------------------------------------

prepare-listing

tcell org

variable insertquit \ This is a hack to backpatch the address of quit.

target included      \ Include the source file of the nucleus to be crosscompiled

[ tdp @ 0 org ] jmp main [ org ]
[ tdp @ insertquit @ org ] jmp quit [ org ]

meta

\ -----------------------------------------------------------------------------
\  Crosscompilation done. Write target binary image to file.
\ -----------------------------------------------------------------------------

decimal

0 value file

: dumpall
    s" hex" out-suffix to file

    hex
    8192 0 do
        i tcell * tw@
        s>d <# tcell 2* 0 do # loop #> file write-line throw
    loop
    file close-file
;

\ -----------------------------------------------------------------------------
\  Wordlist juggling tools to properly switch into and out of the crosscompilation environment.
\ -----------------------------------------------------------------------------

: target    only target-wordlist add-order definitions ;
: ]         target ;
:: meta     forth definitions ;
:: [        forth definitions ;

