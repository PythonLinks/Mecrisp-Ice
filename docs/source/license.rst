License
#######

The original J1, and the more useable, but not maintained SwapForth had  BSD 3-Clause "New" or "Revised" License.
Mecrisp Ice included the same license until it was removed in version 2.6d. 

Of course the software uses gForth, so maybe everything is gpl infected.  
I am not a lawyer, so the following is not legal advice, just my best guess at the status of code.

There are two parts.  Verilog and Forth.  GNU treats c, javascript and images differently.  They do not cross infect, so 
I assume that the forth did not cross infect the verilog.   As for the Forth part, it is processed thougth gForth, so for the 
longest time I thought it was infected, but on reading and documenting the cross compiler, I see that no gnu code was added to the 
emited target executable, so I now believe that the Forth code is still just under the BSD license. 

Of course my advice is do tnot use any mecrisp version past 2.6d, as the legal status is undefined. 

Again I am not a lawyer. 
