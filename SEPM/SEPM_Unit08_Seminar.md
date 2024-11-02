# Seminar Preparation: Data Structures

## Below two different data structures to hold the data associated with the list of functional and non-functional requirements in [previous tasks](SEPM_Unit03_Activity.md) with justification. 

### Queue
 - **Functional Requirements:**
    - **Playlist Management:** Queues handle song order, allowing users to play, skip, or replay songs seamlessly.
    - **Navigation:** Supports "Next" and "Previous" song functionalities efficiently.
   
   **Justification:** Queues are ideal for maintaining the order of songs, allowing easy access to the "Next" and "Previous" functionalities. This aligns perfectly with the playlist's sequential nature.
   
 - **Non-Functional Requirements:**
    - **Performance:** Ensures smooth playback with minimal delay when transitioning between songs.
    - **Scalability:** Can manage large playlists without performance degradation.

   **Justification:** Queues provide efficient operations for adding and removing songs in a playlist, ensuring smooth transitions with minimal delay.  Moreover, as playlists grow, a queue can handle an increasing number of songs without significant performance loss.
      
### Hash Table
 - **Functional Requirements:**
   - **Fast Lookups:** Quickly retrieves song, artist, or album data when searching or selecting.
   - **Efficient Metadata Access:** Provides immediate access to song details for playback and recommendations.
  
   **Justification:** Hash tables enable quick retrieval of song, artist, or album data, which is crucial for search and selection features.

   
 - **Non-Functional Requirements:**
   - **Efficiency:** Offers constant time complexity for search operations, ensuring rapid response times.
   - **Reliability:** Consistently retrieves accurate data, enhancing user trust and experience.

   **Justification:** With average O(1) time complexity for lookups, hash tables ensure rapid access to large music catalogs.  Moreover, They provide consistent performance, ensuring users receive accurate data swiftly, enhancing user satisfaction.

## Below the key points of selected articles:

### Key Points from Abeykoon et al. (2020)
**1. Data Engineering for HPC:**
 - Emphasizes efficient data handling for large-scale systems.
 - Uses high-performance compute kernels and distributed memory execution.

**2. Use of Tables and Efficient Data Structures:**
 - Highlights the importance of fast data access and manipulation.
 - Discusses the integration of efficient data structures like tables for quick data retrieval.

**3. Scalability and Performance:**
 - Focuses on optimizing systems for large datasets.
 - Demonstrates the necessity of scalable solutions to handle increasing data loads effectively.

### Key Points from Dicheva & Hodge (2018)
**1. Educational Focus on Data Structures:**
 - Uses games to improve understanding of data structures, specifically stacks.
 - Highlights the importance of selecting appropriate data structures for problem-solving.

**2. Active Learning and Conceptual Understanding:**
 - Encourages hands-on activities for better grasp of abstract data types.
 - Demonstrates how practical applications can enhance understanding of data structures’ roles.


## How These Articles Support my Data Structure Choices
### Queue
 - **Abeykoon et al. (2020)** supports the use of queues through its focus on efficient data processing and scalability. The paper's emphasis on high-performance systems aligns with queues' ability to manage large playlists efficiently.
 - **Dicheva & Hodge (2018)**, while focusing on stacks, underscores the value of appropriate data structures for managing operations, similar to how queues manage song order and navigation in playlists.

### Hash Table
 - **Abeykoon et al. (2020)** highlights the need for fast data retrieval and efficient data handling, supporting the use of hash tables for quick access to song metadata and search functionalities.
 - **Dicheva & Hodge (2018)**, by illustrating the importance of understanding data structures, indirectly supports hash tables' role in providing efficient and reliable data access, crucial for maintaining user satisfaction in applications like music services.


## Reflections
Through this assignment, I learned how crucial data structures like queues and hash tables are for efficient system design. Queues help manage playlists by keeping song order smooth and performance high. Hash tables allow quick access to song details, enhancing user experience. Insights from the articles showed the importance of scalability and performance in handling large datasets. In future projects, I'll apply these structures to optimize backend operations and improve user interactions. This experience also emphasized the value of active learning in understanding complex concepts.

<br><br>

---

## Reference
Abeykoon, V. et al. (2020) Data Engineering for HPC with Python. 2020 IEEE/ACM 9th Workshop on Python for High-Performance and Scientific Computing (PyHPC). DOI 10.1109/PyHPC51966.2020.00007

Dicheva, D., & Hodge, A. (2018). 'Active learning through game play in a data structures course', SIGCSE '18: Proceedings of the 49th ACM Technical Symposium on Computer Science Education. Baltimore, MD, USA, 21-24 February 2018. ACM. 834–839. DOI: https://doi.org/10.1145/3159450.3159605

<br><br>

---

[Return to Module 5 Unit 8](SEPM_Unit08.md)
