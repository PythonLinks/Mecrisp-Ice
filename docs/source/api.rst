Word List 
=========

Here is the sorted word list for version 2.6e followed by the shell script which generated it.  

! # #> #s ' ( (d.) (ud/mod) * / /mod + +! +loop , - -rot . ." .digit .r .s .x .x2 / /mod /string 0< 0<> 0= 0> 1+ 1- 2! 2 2/ 2@ 2and 2arshift 2constant 2drop 2drop 2droprdrop 2dup 2lshift 2nip 2or 2over 2rot 2rshift 2swap 2variable 2xor 3rd : :noname ; < <# <= <> = > >= >body >in >r ?do ?dup @ BUF BUF0 [ ['] [char] \ ] abort abs accept again ahead align aligned allot alu. and arshift base begin bic! binary bis! bl bounds buffer: c! c, c@ case cell+ cells char cmove cmove> compile, constant cornerstone count cr create d+ d- d. d.r d0< d0= d2 d2/ d< d<= d<> d= d> d>= dabs decimal delay depth digit dint disasm-$ disasm-cont disasm-step dividend divisor dmax dmin dnegate do does> drop dshr du< du<= du> du>= dump dup eint eint? else emit emit? endcase endof evaluate execute exit f# f f. f.n f/ false fill fm/mod foldable forth here hex hld hold hold< i if immediate init insight invert io! io@ j key key? leave link@ literal loop lshift m m+ max memstamp min mod move name. negate new nip nop not now number of or over pad parse parse-name pause postpone quit r> r@ rdepth rdrop recurse refill repeat rot rshift rtype s" s, s>d s>f see seec sfind sgn shift sign sliteral sm/rem source space spaces state swap then tib ticks true tuck type u. u.r u< u<= u> u>= ud. ud/mod um* um/mod umax umin unloop until unused variable welcome while within words xor xor!

To generate this wordlist, first run the emulator,

./emulate

then type the "words" command and saved it to a file called junk,
then run the following bash shell script.
cat junk | tr " " "\n" | sort | tr "\n" " 

.. autosummary::
   :toctree: generated

   Mecrisp-Ice
