# Reverse Engineering

Challenge Name : Reversing-2

# Solution

- Unzip upx.zip 

![[Pasted image 20210818124152.png]]

- Open the program and clik Run till we got into here.

![[Pasted image 20210818162556.png]]

- View on the right bottom and look for the sentence we have .

![[Pasted image 20210818162848.png]]

- Copy the address and go to that address with (CTRL + G).

![[Pasted image 20210818162925.png]]

- Right Click -> Search For -> All referenced text strings

![[Pasted image 20210818163021.png]]

- Found like a partial flag. Also sentence that we have never seen before.

![[Pasted image 20210818163103.png]]

- Double click on any of the sentence to go to the address. Looking inside the address we found out 2 possible output.

1. Part 1

![[Pasted image 20210818163622.png]]

2. Part 2

![[Pasted image 20210818163604.png]]

- On Part 2 we found out an interesting function which is **GetCommandLineA function**. More reference can be read in here :

https://docs.microsoft.com/en-us/windows/win32/api/processenv/nf-processenv-getcommandlinea

- Also there is a string **"-pl34se-give-me-th3-k3y"**. Might be we need to give an argument to the program with the string we found. Let's try it!

![[Pasted image 20210818164039.png]]

- Alright nice! But where is the flag? Looking back at the address of Part 1. We know that there is a check of **IsDebuggerPresent** and there is OutputDebugStringA. Get the address of the debugger checker and set a breakpoint on it using (F2). Rerun the program by giving the argument by going to Debug -> Arguments.

![[Pasted image 20210818164702.png]]

- Run and use F7 and F8 to go into here.

![[Pasted image 20210818165432.png]]

- Change the EAX to 0 

![[Pasted image 20210818165730.png]]

- Set breakpoint to OutputDebugStringA and we will get the flag once we run it again.

# Flag

![[Pasted image 20210818165946.png]]

# References

- https://github.com/ctfs/write-ups-2015/blob/master/nullcon-hackim-2015/reversing-2