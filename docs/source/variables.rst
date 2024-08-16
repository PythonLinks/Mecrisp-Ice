Variables
=========

This is documenation of the variables in Mecrisp Ice.  It is complimentary to the `glossary <glossary.html>`_. 
If any words or variables are missing, please click on the github link, and file an issue, so that it can be corrected. 

CORE VARIABLES

``base`` determines the
external representation, how the user will see the values.  Common values are 2 (binary), 10 (decimal)
and 16 (hexadecimal).

``constantfoldingpointer`` Is used to calculate the stack depth while the compiler performs constant folding

``disasm-$`` Current position for disassembling.

``disasm-cont`` Continue disassembling up to this position.
 
``dp`` Dictionary Pointer is the next empty address.  As words and data are defined, ``dp`` is incremented, and new 
values are then written to this address. 

``foldability`` -- The flags for constant folding of the word to be compiled.  With constant folding 
the line:: 

     2 4 + 
  
becomes::
  
     6
  
Constant folding can take many values.   For doubles, folding up to 4 is supported. 

``fineforoptimisation`` A flag to denote if the compiler may change (or merge something with) the last instruction written.
  
``forth`` Points to the list (Dictionary) of forth words. Each Forth word includes a pointer 
to the previous word. 

``>in`` -- Offset into the terminal input buffer

``init`` -- Store the xt of your entry point into it for a turnkey application that starts immediately on boot

``lastword`` Pointer to the newest definition, used for adding flags to it afterwards 
and to update the dictionary pointer in ``;``. It really should be callsed ``currentword``, 
but to save space it is called ``lastword``.

``leaves`` The number of leaves to handle in a ``do leave leave ... loop``.

``rO`` No longer used.  Should be deleted in the next release after 2.7. 

``sourceC`` Double variable holding the current source to be interpreted.

``state`` Determines the state of the user intereface.  It could either be compiling or interpreting. 

``thisxt`` Pointer to the start of the executable code of the currently compiled definition, used for recurse and :noname

``tib`` Terminal input buffer










