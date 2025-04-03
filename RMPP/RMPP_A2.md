### Assignment 2: Research Proposal Presentation
###  - [Presentation](RMPP_A2_Presentation.pdf)
###  - [Transcript](RMPP_A2_Transcript.pdf)

---

### Slide 1: Opening
<img src="RMPP_A2_Presentation_01.jpg" alt="Slide 1" width="700"/>
<br>

Hello everyone, My name is Helen, Siu Oi Lam
Today, I will be presenting my research proposal titled “A Framework for Mitigating Data Breach Risk – A Case Study and Solution for SMEs in Hong Kong.”

---

### Slide 2: Agenda
<img src="RMPP_A2_Presentation_02.jpg" alt="Slide 2" width="700"/>
<br>

This presentation will outline the significance of my research, the research questions, aims and objectives, key literature, methodology and ethical considerations, as well as a description of the artefact I plan to develop, the project timeline, and expected outcomes.

---

### Slide 3: Significance and Research Problem
<img src="RMPP_A2_Presentation_03.jpg" alt="Slide 3" width="700"/>
<br>

In recent years, there has been a concerning rise in cyber risks and data breaches affecting organisations of all sizes in Hong Kong (HKCERT, 2025; PCPD, 2025).

Surveys indicate that small and medium-sized enterprises, commonly referred to as SMEs, are increasingly adopting technology but remain largely unaware of the associated cyber risks (Yeung, 2020). This lack of awareness leaves them particularly vulnerable.

Many SMEs, however, struggle to meet these requirements due to limited resources and technical expertise (QBE, 2025).

Additionally, compliance requirements under the Personal Data (Privacy) Ordinance, hereafter referred to as PDPO, have been recently reviewed by the Office of the Privacy Commissioner for Personal Data Hong Kong, also known as PCPD, to address these evolving risks (DLA Piper, 2025; Lau, 2025; Legislative Council, 2024).

This research aims to bridge this gap by developing a practical and resource-efficient framework that SMEs can adopt to better protect themselves against data breaches.


---

### Slide 4: Challenges and EDC’s Complaints
<img src="RMPP_A2_Presentation_04.jpg" alt="Slide 4" width="700"/>
<br>

During the project, we faced several challenges across different areas:
1.	Storage System: Our engineering department couldn't produce a solid-state storage solution, leading us to adopt Synful's internal cartridge system, which doesn't meet industry standards.
2.	Design Shift: We shifted focus from a portable form factor to a desktop unit with a built-in keyboard due to production constraints and cost considerations, affecting market appeal.
3.	Technical Issues: EM interference, from the floppy or cartridge drive motors caused system instability and reliability concerns.
4.	Software Limitations: The HBConv application, designed to convert existing EB programs for use on the Synputer, successfully converted only about 60% of programs.
5.	Marketing Requirements: Marketing research indicated that users expected more advanced graphics, better sound quality, and a GUI-based operating system, features our current system doesn't fully provide.

<ins>EDC’s feedback</ins> <br>

In February 1984, EDC provided detailed feedback highlighting several shortcomings affecting the Synputer's suitability for professional use:
1.	Lack of an Industry-Standard Operating System: EDC requires a stable, widely adopted OS for compatibility and ease of use.
2.	Absence of an External Keyboard: The built-in keyboard doesn't meet EDC’s requirements and limits workstation flexibility.
3.	Insufficient Memory: The current RAM capacity is inadequate, hindering performance for demanding applications.
4.	Non-Standard Removable Media: The proprietary cartridge system doesn't align with industry-standard storage media, causing compatibility issues.
5.	Lack of Expandability: The absence of expansion capabilities limits the system's utility in a professional environment.
6.	Underpowered CPU: The 68008 CPU doesn't meet performance expectations, especially for future developments.
7.	System Instability: Regular system crashes are unacceptable in a professional setting where reliability is critical.
To address EDC’s concerns, we plan to update the requirements, aiming to ship the updated units to EDC by July 1984.

---

### Slide 5: Updated Requirement
<img src="RMPP_A2_Presentation_05.jpg" alt="Slide 5" width="700"/>
<br>

To address EDC's feedback and align with market demands, we've updated the Synputer specifications. Here is a summary of the key requirements and justifications for these changes:
1.	Industry-standard OS: We will port CP/M-68K to the Synputer, providing EDC with a stable and widely recognized OS. Additionally, we'll offer MccOS as an optional upgrade for users seeking enhanced features.
2.	External keyboard and connector: We will redesign the system to include a detachable keyboard, addressing both usability and enterprise preferences.
3.	512KB of RAM: To support advanced applications and future-proof the system, we will increase the RAM to 512KB, meeting EDC’s and market demands.
4.	Industry-standard removable media: Alongside our cartridge system, we will integrate a 3.5-inch floppy drive, ensuring compatibility with widely used media formats.
5.	SCSI expansion capability: We will add a SCSI port to allow for expandability, including support for external storage and peripheral devices.
6.	Upgrade CPU: The CPU will be upgraded from the 68008 to the 68000, offering greater performance and an upgrade path for power users.
7.	GUI readiness: We will make the system GUI-ready, supporting GEM graphical and PTR/E pointer environments, meeting the growing demand for GUI-based systems.
8.	Advanced graphics and sound: The system will feature 512 colors at a resolution of 1024x768, along with 3-channel sound to meet gaming and multimedia demands.
9.	Stability improvements: We will resolve the EM interference issues by redesigning the power supply and adding improved shielding to the components.
10.	EB Converter: We propose a licensing deal with the vendor to supply EB for OS at a cost of £25 per machine to mitigate the challenge raised by the HBConv application.
Assuming there will be no conflict with the upgrade option of MccOS, these updated requirements reflect both EDC’s needs and the expectations of the broader consumer market.

---

### Slide 6: Updated Plan and Budget
<img src="RMPP_A2_Presentation_06.jpg" alt="Slide 6" width="700"/>
<br>

To implement the updated requirements, we have developed a costed project plan for the modified Synputer system.

The table here details the components and their associated costs. 
The total material cost is £161 per machine.

Other key costs include:
1.	Software Development of PTR/E & GUI - cost £20,000 for 16-week coding, 8-week design.
2.	Licensing Fees of EduPC - £25 per machine.
3.	SCSI Expansion Board: £15 per unit which is optional and not considered in the budget.
The total estimated budget for the first 2,000 units is £599,385, representing a 20% increase from the original budget.

<ins>Financing the Budget Increase</ins> <br>
Despite the increase, we have strategies to cover the additional costs:
1.	Pre-Orders: With 3,000 existing pre-orders and potential for more due to enhanced features, we can secure additional funding upfront.
2.	Economies of Scale: By producing a unified system for both EDC and the general market, we can reduce per-unit costs.
3.	Cost-Saving Measures: Streamlining production and negotiating for bulk discounts will help manage the budget.
We are confident that these financial adjustments are manageable and will result in a superior product that meets our stakeholders' expectations while ensuring profitability.

---

### Slide 7: Updated Timeline
<img src="RMPP_A2_Presentation_07.jpg" alt="Slide 7" width="700"/>
<br>

To implement the changes, we've adjusted our project timeline. 
1.	Component Sourcing (Weeks 1–4):
    - During the first four weeks following approval, we'll source all necessary components, including the upgraded 68000 CPU, additional RAM modules, and the SCSI expansion boards.
2.	Prototype Development (Weeks 5–12):
    - Over the next eight weeks, we'll develop and assemble prototypes of the updated Synputer.
    - These prototypes will incorporate all the new features, allowing us to test and refine the design.
    - We'll conduct thorough prototype testing, unit and integration testing, and full system testing at various stages to identify and resolve any technical issues.   (Beizer, 1984; Camburn et al., 2017; Hartman, 2005).
3.	Testing and User Acceptance Testing (Weeks 13–16):
    - User acceptance testing will involve select customer from EDC and our consumer base to gather feedback.
    - Feedback will be analyzed and incorporated into the final design where feasible.
4.	Full Production (Weeks 17–24):
    - Full-scale production will commence in June 1984, starting in Week 17.
5.	Delivery to EDC (July 1984):
    - 2,000 units will be delivered to EDC by July 1984, fulfilling our contractual obligations and addressing their urgent needs.
6.	Delivery to Pre-Order Customers (September 1984):
    - The 3,000 pre-ordered units will be delivered to our customers by September 1984.
    - This timeline allows for any final adjustments post-EDC delivery and ensures we meet consumer expectations.
By continuing to use Agile Scrum methodology, carefully managing each sprint in the software development lifecycle, and maintaining open communication with our teams and stakeholders (Nagl, 2023; Negi, 2019), we aim to deliver a high-quality product within the revised schedule.

---

### Slide 8: Updated Marketing Strategy
<img src="RMPP_A2_Presentation_08.jpg" alt="Slide 8" width="700"/>
<br>

Given the different requirements from EDC and the existing user base, we have considered two options:
1.	Create Two Separate Systems:
    - Synputer Base Model focused on home users and hobbyists with minor upgrades.
And,
    - EDC Enterprise Model with higher-spec machine with 68000 CPU, 512KB RAM, external keyboard, and SCSI support.
Or,
2.	One Unified System:
    - A single system meeting both EDC’s and consumer requirements, branded differently for each market segment.

After reviewing the costs and the complexity of managing two product lines, we recommend producing one unified system that meets the needs of both markets, with the benefits of:
1.	Cost Savings: Economies of scale help reduce per-unit costs, as explained in the previous slide regarding budget, and 
2.	Simplified Production: Streamlines manufacturing and reduces logistical overheads.
Creating one unified system ensures we meet both EDC’s enterprise needs and the broader consumer market’s desire for a competitive home computing machine.

<ins>Pricing Strategy</ins> <br>
Our goal is to remain competitive while ensuring profitability. We propose the following pricing:
1.	Standard Price: Maintain at £399.99 for the consumer market.
2.	Enterprise Package: Offer an enterprise package at a 10% premium, £439.99, including additional software licenses, extended support, and other enterprise-specific services.  
3.	Optional Upgrades: We also provide software and peripheral upgrades that customers can purchase based on their needs.
This pricing strategy allows us to meet both consumer and enterprise demands while maintaining profitability.  

---

### Slide 9: Conclusion and Next Step
<img src="RMPP_A2_Presentation_09.jpg" alt="Slide 9" width="700"/>
<br>

We have outlined a comprehensive plan to address EDC's concerns and align the Synputer with current market demands. Next steps:
1.	Finalize the design and begin component sourcing
    - We'll complete the final design adjustments promptly and initiate the sourcing of all necessary components.
2.	Develop prototypes and conduct UAT by May 1984
    - Then develop prototypes with enhancements. 
    - We'll conduct rigorous User Acceptance Testing, involving stakeholders from EDC and select consumer representatives.
3.	Commence Full Production (June 1984)
     - We'll begin full-scale production in June 1984 to meet our delivery commitments.
     - Processes will be monitored closely to maintain quality and adhere to the timeline.
We are confident that the updated Synputer will meet the needs of both EDC and the consumer market. As our logo indicates, Synputer aims to provide a SUPER user experience.

---

### Slide 10: Closing and List of Reference
<img src="RMPP_A2_Presentation_10.jpg" alt="Slide 10" width="700"/>
<br>

That concludes our presentation for today. We've covered the current status of the Synputer project, the challenges we've faced, our proposed solutions, and the updated plan to move forward.

We will continue to monitor the project closely and remain committed to transparency and regular communication with all stakeholders. Your feedback and support are invaluable as we work to bring the Synputer to market successfully.

We're now open for any questions you may have, or if you prefer, you can also contact us after the meeting for any further inquiries.

Thank you all for your time and attention. We look forward to your continued partnership as we progress on this exciting journey.

---

### Slide 11: Closing and List of Reference
<img src="RMPP_A2_Presentation_11.jpg" alt="Slide 11" width="700"/>
<br>

That concludes our presentation for today. We've covered the current status of the Synputer project, the challenges we've faced, our proposed solutions, and the updated plan to move forward.

We will continue to monitor the project closely and remain committed to transparency and regular communication with all stakeholders. Your feedback and support are invaluable as we work to bring the Synputer to market successfully.

We're now open for any questions you may have, or if you prefer, you can also contact us after the meeting for any further inquiries.

Thank you all for your time and attention. We look forward to your continued partnership as we progress on this exciting journey.

---

### Slide 12: Closing and List of Reference
<img src="RMPP_A2_Presentation_12.jpg" alt="Slide 12" width="700"/>
<br>

That concludes our presentation for today. We've covered the current status of the Synputer project, the challenges we've faced, our proposed solutions, and the updated plan to move forward.

We will continue to monitor the project closely and remain committed to transparency and regular communication with all stakeholders. Your feedback and support are invaluable as we work to bring the Synputer to market successfully.

We're now open for any questions you may have, or if you prefer, you can also contact us after the meeting for any further inquiries.

Thank you all for your time and attention. We look forward to your continued partnership as we progress on this exciting journey.

---

### Slide 13: Closing and List of Reference
<img src="RMPP_A2_Presentation_13.jpg" alt="Slide 13" width="700"/>
<br>

That concludes our presentation for today. We've covered the current status of the Synputer project, the challenges we've faced, our proposed solutions, and the updated plan to move forward.

We will continue to monitor the project closely and remain committed to transparency and regular communication with all stakeholders. Your feedback and support are invaluable as we work to bring the Synputer to market successfully.

We're now open for any questions you may have, or if you prefer, you can also contact us after the meeting for any further inquiries.

Thank you all for your time and attention. We look forward to your continued partnership as we progress on this exciting journey.

---

#### References
Beizer, B. (1984) Software system testing and quality assurance. London: Van Nostrand Reinhold.

Burek, J. (2024) How to Build a PC: The Ultimate Beginner’s Guide. PCMag. Available from: https://www.pcmag.com/how-to/how-to-build-a-pc-the-ultimate-beginners-guide [Accessed 1 October 2024]
 
Camburn, B., Viswanathan, V., Linsey, J., Anderson, D., Jensen, D., Crawford, R., Otto, K. & Wood, K. (2017)  Design prototyping methods: state of the art in strategies, techniques, and guidelines. Design Science, (3): 1-13.

Cohen, D., Lindvall, M. & Costa, P. (2004) An introduction to agile methods. Advances in Computers, 62(3): 1-66.
 
Hartman, A. (2005) Software and hardware testing using combinatorial covering suites. In Graph Theory, Combinatorics and Algorithms: Interdisciplinary Applications (237-266). Boston, MA: Springer US.

Jones, C. (2004) Software project management practices: Failure versus success. CrossTalk: The Journal of Defense Software Engineering, 17(10): 5-9 

Leung, H.K. & White, L. (1990) A study of integration testing and software regression at the integration level. In Proceedings. Conference on Software Maintenance 1990, (290-301). IEEE.
  
Micron Technology. (N.D.) How to build your own PC. Crucial. Available from: https://www.crucial.com/articles/pc-builders/how-to-build-a-computer [Accessed 1 October 2024]

Nagl, S. (2023). 5 Benefits of Agile Project Management. School of Professional Studies at Wake Forest University. Available at: https://sps.wfu.edu/articles/benefits-agile-project-management [Accessed 18 August 2024]

Negi, K. (2019) The Scrum Software Development Process. Available from: https://medium.com/@kunalnegi0003/the-scrum-software-development-process-6e48bb021d9f [Accessed 17 August 2024]

Schwaber, K. (1997) Scrum development process. Business object design and implementation. In 10th Annual Conference on Object Oriented Programming Systems, Languages, and Applications Addendum to the Proceedings. ACM/SIGPLAN October (117-134).

<br><br>

---

[Return to Module 7 Main Page](RMPP_main.md)
