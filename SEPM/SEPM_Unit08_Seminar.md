# Seminar Preparation: Data Structures

## Task 1:
Select at least two different data structures to hold the data associated with the list of functional and non-functional requirements that you defined for [previous tasks](SEPM/SEPM_Unit03_Activity.md) with justification. 

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

## Task 2: 
Select at least one academic paper, which might be similar to the work of [Abeykoon et al. (2020)](SEPM_Unit08_Reading.pdf).
Use your sourced information to support your data structure choices.





## Reflections
...

<br><br>

---

## Reference
Abeykoon, V. et al. (2020) Data Engineering for HPC with Python. 2020 IEEE/ACM 9th Workshop on Python for High-Performance and Scientific Computing (PyHPC). DOI 10.1109/PyHPC51966.2020.00007

<br><br>

---

[Return to Module 5 Unit 8](SEPM_Unit08.md)
