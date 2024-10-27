# Unit 12: The Great Tanenbaum-Torvalds Debate Revisited

Welcome to Week 12 where we will revisit (and recreate in our own small way) the Tanenbaum-Torvalds debate of the early nineties.

At the time of the original debate, Andrew Tanenbaum was a university lecturer who had created Minix – a small, microkernel-based operating system that he used as a teaching tool. Linus Torvalds was a master's student who had completed a module in operating systems design. Anecdotally, Torvalds claimed he was just trying to create his own OS kernel that he could use with GNU and would make best use of his new (at the time) 386 based PC. He used Minix as the theoretical basis of his new system.

The world of computing was very different in 1992. Processor speeds were in the MHz, not GHz range. There was no multi-core x86 CPU available – and certainly not in desktop systems. Therefore, the decisions about how OSes should be designed – the trade-offs between single address space systems versus user-kernel memory splits, and the concerns about context switch times were much more acute in those days.

Today we live in a web scale world: workloads run in virtual clouds with supposedly unlimited capacity for expansion – both for RAM and CPU. Malevolent intention is everywhere – barely a day goes by without another announcement of a critical exploit or vulnerability in one system or another – and sometimes in the underlying hardware as well!

All these things should be borne in mind when considering the validity of both Tanenbaum’s and Torvalds’ arguments nearly thirty years on: is a monolithic kernel still the best approach in a mostly distributed world? Does the use of microservices equate to a need for microkernels? And how does the shadow of incessant cyber-attacks impact these decisions? Hopefully this debate will help us all to re-evaluate our opinions on the best approach to take.

In this unit we shall:
 - Review journals and articles about monoliths, microkernels and microservices.
 - Engage in a debate about the above.
 - Explore some of the advances in secure programming.

### Learning Outcomes
On completion of this unit you will be able to:
 - Recommend a strategy around which methodology to adopt: monolithic or microservices.
 - Provide evidence to support your recommendation.
 - Explain how faceted data approaches work.

This session summarises the module and asks you to think about current trends in system design and development and the two opposing approaches: monolithic or microservice/ modular designs.

### Artefacts and Collaborative Discussion 
As part of my e-portfolio, I have completed the following activities which are documented in the provided link:

[Microservices and Microkernels Debate](SSD_Unit12_Seminar.md) <br><br>

### Reflections
During this unit, I gained valuable insights into xxx

### Action Plan
I'm planning to enhance my understanding of xxx

<br><br>

--- 

[Return to Module 6 Main Page](SSD_main.md)
