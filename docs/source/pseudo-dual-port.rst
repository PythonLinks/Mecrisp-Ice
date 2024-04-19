Mecrisp Ice on Psuedo Dual Port RAM
###################################

The Ice 40 family of FPGA's has pseudo-dual port RAM.  One can read and write to memory at the same time, 
but one cannot do two 
reads, nor two writes simultaneously.  But the J1 reads an instruction every clock cycle, leading to a memory access conflict. 
The solution to this problem, adopted by the origingal J1a, and by Mecrisp's j1-universal-16kn is notoriously difficult to understand. 
The problem is that in order to minimize circuit size, different registers are reused.  
  
Two cycles are required to read data from a single read port memory.   There is a flag called fetch, 
which tells you if this is the second part of the read cycle.  To save registers, that flag is basically set 
  in the program counter.  Remember that the default J1, is a 16 bit cpu, but ony has a 13 bit address space. 
Those three higher bits can be used for something else, and indeed pc[14] is the flag for the second stage of a read cycle.  
A 13 bit instruction address could be stored in pc[12:0] So why not use pc[13]?  Well because actually pc[0]
is used to store interrupts on the mecrisp ice.  
  
In the first cycle, of a two cycle data read process, there is no read data available.  
The address to be read from has to be sent to the memory.   In the meantime, you cannot fully execute the read 
instruction, since there is no data.  So it gets stored on the return stack.  Also during the first cycle, 
we have to set the flags that the next cycle should take the instruction from the return stack 
``pc[14] = TRUE``. 

And since interrupts are flagged on pc[0], the program counter has to be incremened by 2 each clock cycle rather than by 1. 

Of course this whole process is further complicated by having to deal with interrupts.   If there is an interrupt, 
do not fetch, push the instruction on the return stack, and process the interrupt. ??? (I think)

I fully understand that the market wants the smallest stack machine possible.   
That is the perspective of the electrical engineers.  But boy does it make the cpu 
difficult to understand.  I suspect that interrupts could be moved to a higher order bit in the program counter. 
  
When building a version of the J1 for single port memory, something similar has to be done for writing to memory.   
The write instruction arrives.  The address and data are sent to the memory.  At the next positive clock edge the data is written
written.  In the next clock cycle,  the memory is then handed the address for the next instruction, while the rest of the cpu waits for the next 
instruction to arrive. 




