
GLOSSARY
========

This is the list of Forth words supported by Mecrisp Ice.
**View it with fixed-width font !**
This provides short descriptions of all currently included words:
To figure out exaclty what each word does, you have to read the code.
Search for ": word" to find where the word is defined. 

::

  grep -ri ": word"

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

And now we have the word definitions. 

Terminal-IO
-----------
                      
::
                             
        emit?           ( -- Flag ) Ready to send a character ?
        key?            ( -- Flag ) Checks if a key is waiting
        key             ( -- Char ) Waits for and fetches the pressed key
        emit            ( Char -- ) Emits a character.
        alu.            ( Opcode -- ) ( If this opcode is from an one-opcode
 	                     definition, it gets named. This way inlined
		    	            ALUs get a proper description. )
			  
 
Stack Jugglers
--------------
                             
Single-Jugglers
---------------                             

::     

        drop            ( x -- )
        dup             ( x -- x x )
        nip             ( x1 x2 -- x2 )
        swap            ( x1 x2 -- x2 x1 ) 
        tuck            ( x1 x2 -- x2 x1 x2 )
        over            ( x1 x2 -- x1 x2 x1 )
        rot             ( x1 x2 x3 -- x2 x3 x1 )
        -rot            ( x1 x2 x3 -- x3 x1 x2 )
        ?dup            ( x -- 0 | x x ) if true dup
        3rd             (x1 x2 x3 -- x1 x2 x3 x1)

        depth           ( -- +n ) Stack depth. Doubles  count twice.

Return Stack Operations
-----------------------

::

        rdepth          ( -- +n ) return stack depth. 
        >r              ( x -- ) (R: -- x )
        r>              ( -- x ) (R: x -- )
        r@              ( -- x ) (R: x -- x )
        rdrop           (  --  ) (R: x -- )
	
Double-Jugglers:        They perform the same for double numbers.
-----------------------------------------------------------------
                             
::     
                             
        2drop           ( x1 x2 -- )
        2droprdrop      ( x1 x2 -- )	(R: x -- )
        2swap           ( x1 x2 x3 x4 -- x3 x4 x1 x2 )
        2over           ( x1 x2 x3 x4 -- x1 x2 x3 x4 x1 x2 )
        2dup            ( x1 x2 -- x1 x2 x1 x2 )

 
                             
Logic
-----

::     

        arshift         ( x1 u -- x2 ) Arithmetric right-shift of u bit-places
        rshift          ( x1 u -- x2 ) Logical right-shift of u bit-places
        lshift          ( x1 u -- x2 ) Logical  left-shift of u bit-places
        invert          ( x1 -- x2 )   Invert all bits
        not             ( x1 -- x2 )   Invert all bits = Bitwise not
        xor             ( x1 x2 -- x3 ) Bitwise Exclusive-OR
        or              ( x1 x2 -- x3 ) Bitwise OR
        and             ( x1 x2 -- x3 ) Bitwise AND
        false           ( --  0 ) False-Flag
        true            ( -- -1 ) True-Flag 16 bits of ones


Arithmetic for single numbers
-----------------------------

::        

        /mod            ( n1 n2 -- n3 n4 ) n1 / n2 = n4 rem n3
        mod             ( n1 n2 -- n3 ) n1 / n2 = remainder n3
        /               ( n1 n2 -- n3 ) n1 / n2 = n3
        *               ( u1|n1 u2|n2 -- u3|n3 ) 16 low order bits from a 16 bit
	                                         by 16 bit multiply.  No sign.
        min             ( n1 n2 -- n1|n2 ) Keeps smaller of top two items
        max             ( n1 n2 -- n1|n2 ) Keeps greater of top two items
        umin            ( u1 u2 -- u1|u2 ) Keeps unsigned smaller
        umax            ( u1 u2 -- u1|u2 ) Keeps unsigned greater
        1-              ( u1|n1 -- u2|n2 ) Subtracts one, optimized
        1+              ( u1|n1 -- u2|n2 ) Adds one, optimized

        2*              ( n1 -- n2 ) Arithmetric  left-shift
        2/              ( n1 -- n2 ) Arithmetric right-shift
        abs             ( n -- u ) Absolute value
        negate          ( n1 -- n2 ) Negate
        sgn             ( u1 n1 -- n2 ) Give u1 the sign of n2
        -               ( u1|n1 u2|n2 -- u3|n3 ) Subtraction
        +               ( u1|n1 u2|n2 -- u3|n3 ) Addition


Arithmetic involving double numbers
-----------------------------------

::

        um*             ( u1 u2 -- ud )  16bit * 16bit = 32 bit multiplication

        um/mod          ( ud u1 -- u2 u3 ) ud / u1 = u3 remainder u2

        m+              ( d1 n -- d2 ) Addition of a double with a single
        m*              ( n1 n2 -- d )     n1 * n2 = d
        fm/mod          ( d n1 -- n2 n3 )  d / n1 = n3 remainder r2 floored
        sm/rem          ( d n1 -- n2 n3 )  d / n1 = n3 remainder r2 symmetric

        */              ( n1 n2 n3 -- n4 )     n1 * n2 / n3 = n4
        */mod           ( n1 n2 n3 -- n4 n5 )  n1 * n2 / n3 = n5 remainder n4

        d2*             ( d1 -- d2 ) Arithmetric  left-shift

        dabs            ( d -- ud ) Absolute value
        dnegate         ( d1 -- d2 ) Negate
        d-              ( ud1|d1 ud2|d2 -- ud3|d3 ) Subtraction
        d+              ( ud1|d1 ud2|d2 -- ud3|d3 ) Addition
        s>d             ( n -- d ) Makes a signed single number double length


Comparisons  
-----------

Checks if the TOS is ___ than the NOS

::
                             
        u<=             ( u1 u2 -- flag )   Unsigned comparisons
        u>=             ( u1 u2 -- flag )
        u>              ( u1 u2 -- flag )
        u<              ( u1 u2 -- flag )
        <=              ( n1 n2 -- flag )   Signed comparisons
        >=              ( n1 n2 -- flag )
        >               ( n1 n2 -- flag ) 
        <               ( n1 n2 -- flag )
        0>              ( n -- flag )       Positive ?
        0<              ( n -- flag )       Negative ?
        0<>             ( x -- flag )
        0=              ( x -- flag )
        <>              ( x1 x2 -- flag ) = invert
        =               ( x1 x2 -- flag )   Test for Equality

        d0=             ( d -- flag )

        within          ( x1 x2 x3 -- ? )   Check if x1 is within x2 and x3.


Extension for double and s15.16 fixpoint numbers
------------------------------------------------

::     

        2constant name  ( ud|d -- ) Makes a double constant.
        2variable name  ( ud|d -- ) Makes an initialized double variable

        du<=            ( ud1 ud2 -- flag )   Unsigned double comparisons
        du>=            ( ud1 ud2 -- flag )
        du>             ( ud1 ud2 -- flag )
        du<             ( ud1 ud2 -- flag )

        d<=             ( d1 d2 -- flag )     Signed double comparisons
        d>=             ( d1 d2 -- flag )
        d>              ( d1 d2 -- flag )
        d<              ( d1 d2 -- flag )
        d=              ( xd1 xd2 -- flag )   equal
        d<>             ( xd1 xd2 -- flag )   not equal
	
        d0<             ( d -- flag )         Negative ?

        dmax            ( d1 d2 -- d1|d2 ) Keeps smaller of top two items
        dmin            ( d1 d2 -- d1|d2 ) Keeps greater of top two items

        2rot            ( xd1 xd2 xd3 -- xd2 xd3 xd1 )
        2nip            ( xd1 xd2 -- xd2 )

        2xor            ( xd1 xd2 -- xd3 ) Bitwise Exclusive-OR
        2or             ( xd1 xd2 -- xd3 ) Bitwise OR
        2and            ( xd1 xd2 -- xd3 ) Bitwise AND

        d2/             ( d1 -- d2 )   Arithmetric right-shift
        dshr            ( xd1 -- xd2 ) Logic right-shift

        2arshift        ( xd1 u -- xd2 ) Arithmetric right-shift of u bit-places
        2rshift         ( xd1 u -- xd2 ) Logical right-shift of u bit-places
        2lshift         ( xd1 u -- xd2 ) Logical  left-shift of u bit-places

        ud/mod          ( ud1 ud2 -- ud3 ud4 ) 32/32 = 32 rem 32 Division
                                               ud1 / ud2 = ud4 remainder ud3

Fixpoint numbers are stored ( n-comma n-whole ) and can be handled
like signed double numbers.

::      

        s>f             ( n -- df ) Single integer to s15.16 fixpoint

        f/              ( df1 df2 -- df3 ) Division of two fixpoint numbers
        f*              ( df1 df2 -- df3 ) Multiplication

        hold<           ( char -- )
                        Adds character to pictured number output buffer
                        from behind.
        f#              ( n-comma1 -- n-comma2 )
                        Adds one comma-digit to number output
        f.              ( df -- )
                        Prints a fixpoint number with 16 fractional digits
        f.n             ( df n -- )
                        Prints a fixpoint number with n fractional digits

For internal usage:

::      

        (ud/mod)        ( -- ) Common part of ud/mod and f/
        divisor         ( -- a-addr ) Double variable
        shift           ( -- a-addr ) Double variable
        dividend        ( -- a-addr ) Double variable


Tools for number input and output 
---------------------------------

::      

        number          ( c-addr len -- 0 )
                                     -- n 1 )
                                     -- n-low n-high 2 )
                        Tries to convert a string to a number.
        d. ( d -- )
        Display d in free field format.


Number base
----------- 

::

        binary          ( -- ) Sets base to 2
        decimal         ( -- ) Sets base to 10
        hex             ( -- ) Sets base to 16
        base            ( -- a-addr ) Base variable address

Memory access
-------------- 
**WARNING**: Mecrisp Ice is based on a 13 ½ bit memory model.  The hardware can access 8K = (2\ :sup:`13`) sixteen bit words by dropping the lowest bit, and using the next 13 bits as the address.  The software can access either byte in a 16 bit word using that lowest bit and left or right shifts.  So reading and writing usually accesses every second address, the lowest bit gets dropped.  For those Forth words that operate on bytes, the lowest bit is used, but dropped when actually reading or writing the 16 bit word.  You can read the code for reading characters c@, and the more complex code for writing characters c! to see how this works.  Basically they first look at the byte address on the top of stack, and then based on whether it is odd or even, do different things when accessing the 16 bit word.  

::

        cmove           ( c-addr1 c-addr2 u -- ) Moves backward
        cmove>          ( c-addr1 c-addr2 u -- ) Moves forward
        move            ( c-addr1 c-addr2 u -- ) Moves u Bytes in Memory
        fill            ( c-addr u c ) Fill u Bytes of Memory with value c

        constant  name  ( u|n -- )  Makes a single constant.
        variable  name  ( u|n -- )  Makes an initialized single variable

        2@              ( a-addr -- ud|d ) Fetches two words from memory.  Often used
                        with double numbers. 
        2!              ( ud|d a-addr -- ) Stores two words in memory.  Often used
                        with double numbers. 
        @               ( a-addr -- u|n ) Fetches single number from memory
        !               ( u|n a-addr -- ) Stores single number in memory
        +!              ( u|n a-addr -- ) Add to memory location

        c@              ( c-addr -- char ) Fetches byte from memory
        c!              ( char c-addr ) Stores byte in memory

IO memory area
--------------

::

        io@             ( c-addr -- x ) Fetches from IO register
        io!             ( x c-addr -- ) Stores  into IO register

        xor!            ( mask c-addr -- ) Toggle bits
        bic!            ( mask c-addr -- ) Clear BIts
        bis!            ( mask c-addr -- ) Set BIts


Strings and beautiful output
----------------------------

String routines
---------------

::

        type            ( c-addr length -- )
                        Prints a string.

        rtype           ( c-addr length u -- )
                        Prints a string in a field u characters wide.

        s" Hello"       Compiles a string and
                        ( -- c-addr length )
                        gives back its address and length when executed.

        ." Hello"       Compiles a string and
                        ( -- )
                        prints it when executed.

        ( Comment )     Ignore Comment
        \ Comment       Comment to end of line

        cr              ( -- ) Emits line feed
        bl              ( -- 32 ) ASCII code for Space
        space           ( -- ) Emits space
        spaces          ( n -- ) Emits n spaces if n is positive

        accept          ( c-addr maxlength -- length ) Read input into a string.

Counted string routines:

::

        count           ( cstr-addr -- c-addr length )
                        Convert counted string into addr-length string

Pictured numerical output
--------------------------

Read about `pictured numerical output <https://gforth.org/manual/Formatted-numeric-output.html>`_


::
	
        [char] *        Compiles code of following char
                        ( -- char ) when executed

        char *          ( -- char ) gives code of following char
        hold            ( char -- ) Adds character to pictured number
                                    output buffer from the front.

        sign            ( n -- ) Add a minus sign to pictured number
                                 output buffer, if n is negative

        #S              ( ud1|d1 -- 0 0 ) Add all remaining digits
                        from the double length number to output buffer
        #               ( ud1|d1 -- ud2|d2 ) Add one digit from the
                        double length number to output buffer
        #>              ( ud|d -- c-addr len )
                        Drops double-length number and finishes
                        pictured numeric output ready for type
        <#              ( -- ) Prepare pictured number output buffer
        u.              ( u -- ) Print unsigned single number
        .               ( n -- ) Print single number
        ud.             ( ud -- ) Print unsigned double number
        d.              ( d -- ) Print double number

        u.r             ( u width -- ) Print      unsigned right aligned
         .r             ( n width -- ) Print        signed right aligned
        d.r             ( d width -- ) Print double signed right aligned

        buf0            ( -- a-addr ) Start of number output buffer
        buf             ( -- a-addr ) End   of number output buffer
        hld             ( -- a-addr ) Variable with current position

Deep insights
-------------

::

        words           ( -- ) Prints list of defined words.
        .x2             ( c -- ) Prints  8 bit unsigned in hex base
        .x              ( u -- ) Prints 16 bit unsigned in hex base
                                 This is independent of number subsystem.

User input and its interpretation
________________________________

::

        tib             ( -- c-addr ) Input buffer
        pad             ( -- c-addr ) Location to hold temporary data

        refill          ( -- ? ) Refill input buffer, return true if successful
        source!         ( c-addr len -- ) Change source
        source          ( -- c-addr len ) Current source
        >in             ( -- addr ) Variable with current offset into source

        /string         ( c-addr1 u1 n -- c-addr2 u2 ) Cut n leading characters
	                                  (u1 is the original number of
					  characters, u2 the new number)
        parse-name      ( -- c-addr len ) Get next token from input buffer
        parse           ( char -- c-addr len )
                        Cuts anything delimited by char out of input buffer

        evaluate        ( any addr len -- any ) Interpret given string
        quit            ( many -- ) (R: many -- ) Resets Stacks
        abort           ( many -- ) (R: many -- ) Print ? and quit


Dictionary expansion
-------------------- 

::

        align           ( -- ) Aligns dictionary pointer
        aligned         ( c-addr -- a-addr ) Advances to next aligned address
        cell+           ( x -- x+2 ) Add size of one cell
        cells           ( n -- 2*n ) Calculate size of n cells

        allot           ( n -- ) Tries to advance Dictionary Pointer by n bytes
        here            ( -- a-addr|c-addr )
                        Gives current position in Dictionary

        ,               ( u|n -- ) Appends a single 16 bit number to dictionary
        c,              ( char -- ) Appends an 8 bit byte to the dictionary

        unused          ( -- u ) How many free space is still available ? Assumes  
                        hex 4000 address space. 

        cornerstone name    Create a permanent dictionary wayback point
        new                 Core wayback point.


Dictionary expansion  (more internal)
-------------------------------------

::

        s,              ( c-addr len -- ) Inserts a string with a maximum
                                          of 255 characters without runtime
        sliteral        ( c-addr len -- ) Insert a string with runtime

        literal         ( u|n -- ) Compiles a literal

        compile,        ( a-addr -- ) Compiles a call to a subroutine

        forth           ( -- a-addr ) Variable with entry point for dictionary

        ahead           ( -- a-addr ) Prepare a forward jump


Flags and inventory
-------------------

::

        immediate       ( -- ) Makes current definition immediate.
        foldable        ( n -- ) Current word becomes foldable with n constants

        sfind           ( c-addr len -- c-addr len 0 | a-addr flags )
                               Searches for a string in Dictionary.


Compiler essentials
-------------------

::

        execute         ( a-addr -- ) Calls subroutine
        recurse         ( -- ) Lets the current definition call itself
        ' name          ( -- a-addr ) Tries to find name in dictionary
                                      gives back executable address
        ['] name        ( -- a-addr)  Tick that compiles the executable address
                                      of found word as literal
        postpone name   ( -- ) Helps compiling immediate words.
        does>           ( -- ) executes: ( -- a-addr )
                               Gives address to where you have stored data.
        create name     ( -- ) Create a definition with default action
        >body           ( a-addr -- a-addr ) Address of data field after create
        state           ( -- a-addr ) Address of state variable
        ]               ( -- ) Switch to compile state
        [               ( -- ) Switch to execute state
        ;               ( -- ) Ends a new word definition
        : name          ( -- ) Starts a new word definition
        :noname         ( -- a-addr ) Starts a new word definition for a machine
	                              instruciton defined in hardware. 


Control structures
------------------ 

Decisions:

                         
::

    flag if ... then
    flag if ... else ... then

        then            ( -- )           This is the common
        else            ( -- )           flag if ... [else ...] then
        if              ( flag -- )      structure.

    Case:

    n case
       m1   of ... endof
       m2   .. ... .....
       all others
    endcase

        case            ( n -- n )       Begins case structure
        of              ( m -- )         Compares m with n, choose this if n=m
        endof           ( -- )           End of one possibility
        endcase         ( n -- )         Ends case structure, discards n

Indefinite Loops
----------------                         

::           

    begin ... again
    begin ... flag until
    begin ... flag while ... repeat

    repeat          ( -- ) Finish of a middle-flag-checking loop.

    while           ( flag -- ) Check a flag in the middle of a loop

    until           ( flag -- ) begin ... flag until
                                    loops until flag is true
    again           ( -- )  begin ... again
                                is an endless loop
    begin           ( -- )


Definite Loops
--------------                     

::                     
                     
    limit index   do ... [one or more leave(s)] ... loop
             ?do ... [one or more leave(s)] ... loop
              do ... [one or more leave(s)] ... n +loop
             ?do ... [one or more leave(s)] ... n +loop


        j               ( -- u|n ) Gives second loop index
        i               ( -- u|n ) Gives innermost loop index


        unloop          (R: old-limit old-index -- )
                        Drops innermost loop structure,
                        pops back old loop structures to loop registers

        exit            ( -- ) Returns from current definition.

        leave           ( -- ) (R: old-limit old-index -- )
                        Leaves current innermost loop promptly

        +loop           ( u|n -- )
                        (R: unchanged | old-limit old-index -- )
                        Adds number to current loop index register
                        and checks whether to continue or not

        loop            ( -- )
                        (R: unchanged | old-limit old-index -- )
                        Increments current loop index register by one
                        and checks whether to continue or not.

        ?do             ( Limit Index -- )
                        (R: unchanged | -- old-limit old-index )
                        Begins a loop if limit and index are not equal

        do              ( Limit Index -- )
                        (R: -- old-limit old-index )
                        Begins a loop

        bounds          ( addr len -- limit index )
                        Calculate values to loop over a string

 
SPI and low-level flash memory access
------------------------------------- 

::      

        spix            ( c1 -- c2 ) Exchange one byte on SPI
        >spi            ( c -- ) Send one byte to SPI
        spi>            ( -- c ) Receive one byte from SPI
        idle            ( -- ) Set SPI flash to idle state
        spiwe           ( -- ) Write enable on SPI flash
        waitspi         ( -- ) Wait for write or erase to finish


Memory images
-------------

Sectors from 1 to 63. Sector 1 is automatically loaded after Reset.

::       

        load            ( sector# -- ) Loads an image
        save            ( sector# -- ) Saves an image
        erase           ( sector# -- ) Erase an image

        init            ( -- a-addr ) Variable containing either zero
                                      or the address of a turnkey definition
                                      which is executed automatically

 
Misc hardware
-------------

::       
        delay: (u -- ) Wait so many clock ticks.
        now ( -- ) set the timer to 0.
        ticks           ( -- u ) Read current ticks.  
        ms              ( u -- ) Wait u milliseconds.  Check the clock frequency. 
        nextirq         ( u -- ) Trigger next interrupt u cycles
                                 after the last one

        randombit       ( -- 0 | 1 ) Gives a random bit
        random          ( -- x ) Gives a random number

        eint?           ( -- ? ) Are interrupts enabled ?
        eint            ( -- ) Enable ticks counter overflow interrupt
        dint            ( -- ) Disable interrupt

 
Insight tools that are gone after NEW in targets with 8 kb only
--------------------------------------------------------------- 

::       

        .s              ( many -- many ) Prints stack contents

        dump            ( addr len -- ) Dump memory contents

        insight         ( -- ) Complete printout of dictionary structure

        name.           ( a-addr -- ) If this is the code-start of a definition,
                                      try to print its name.
        memstamp        ( a-addr -- ) Show memory location nicely
        disasm-$        ( -- a-addr ) Variable for current disasm position
        disasm-cont     ( -- a-addr ) Variable: Continue up to this position
        disasm-step     ( -- ) Disassemble one more instruction

        seec            ( -- ) Continue to see at disasm-$
        see name        ( -- ) See the definition

Additional Words
----------------

Here are words that are in the gateware, but not previously listed in this glossary.   I mention them here, 
but I am not sure what they do, nor where they belong.  If you read their code, and 
are confident of what they do, please post an issue, so that I can update this glossary.  Or better yet, issue a pull request. 

::

    buffer: ( u "<name>" -- ; -- addr )

    digit
    digit?
    link@
    nop  ( -- )  No operation.  Does nothing. 
    pause
    welcome  ( -- ) display a welcome message
    
