# Microservices and Microkernels Debate

## Requirement
Read [Biggs et al (2018)](SSD_Unit12_SeminarReference2.pdf) and [Bucchiarone et al (2018)](SSD_Unit12_SeminarReference.pdf) as examples of modern views and approaches to the Monolithic vs. Microservices/ Microkernel debate.

 - Post your team’s stance to the forum along with justifications.
 - Read all the arguments for each position.
 - Choose one team response that disagrees with your team stance and post a message that refutes their argument.
 - During this week’s seminar session, all students will independently vote for which argument they believe was presented most persuasively.
   

## My Stance
I remain firmly convinced that moving away from monolithic architectures is both inevitable and highly beneficial for modern software systems. It is true that monolithic operating systems (OSs) and monolithic application designs initially emerged for convenience and performance considerations. However, as Biggs et al. (2018) argue, the sheer volume of privileged code in large-scale or monolithic OS designs introduces numerous attack vectors and significantly expands the trusted computing base (TCB). Approximately 96% of critical exploits in Linux could be mitigated or entirely eliminated by adopting a microkernel architecture (Biggs et al., 2018). This evidence alone underlines the importance of minimising privileged code and placing vulnerable components (e.g., device drivers or debugging tools) outside the kernel.

Likewise, Bucchiarone et al. (2018) demonstrate that rearchitecting monolithic applications into microservices enhances scalability, maintainability, and resilience. By splitting functionality into smaller, independently deployable services, each team can work on a single component without jeopardising the entire system. Notably, they show that introducing microservices at Danske Bank improved orchestration, containerisation, and DevOps pipelines, leading to more efficient updates and better fault isolation.

Hence, when a microkernel-based OS hosts a microservices-based application, we see a separation of privileges and a clear delineation of responsibilities. This combined approach maximises the benefits of minimal TCB at the operating system level with the advantages of independently deployable, domain-focused services at the application level.

## Reflections
Working through these articles and debates has clarified the distinct but complementary roles of microkernels (focusing on OS-level security and TCB minimisation) and microservices (emphasising modular design and independent deployments at the application layer). When combined, these approaches can offer improved resilience, security, and scalability. Although transitions can be challenging, well-documented success stories (like Danske Bank) suggest strongly that the benefits justify the efforts, particularly for critical domains where security and stability are paramount.

<br><br>

---

## Reference
Biggs, S. Lee, D. & Heiser, G. (2018) The Jury Is In: Monolithic OS Design Is Flawed: Microkernel-based Designs Improve Security. Proceedings of the 9th Asia-Pacific Workshop on Systems (APSys '18). ACM 16:1–7.

Bucchiarone, A. Dragoni, N. Dustdar, S. Larsen, S.T. & Mazzara, M. (2018) From Monolithic to Microservices: An Experience Report from the Banking Domain. IEEE Software 35 (3):50-55.

<br><br>

---

[Return to Module 6 Unit 12](SSD_Unit12.md)
