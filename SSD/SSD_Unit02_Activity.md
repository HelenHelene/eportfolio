# e-Portfolio Activity: Data Structures Reflection

## Requirement
Read [Dicheva & Hodge (2018)](SSD_Unit03_Reading.pdf). Think about an online system which you use on a daily basis. 
Consider how it might operate at the back-end using data structures. 

## Introduction
When thinking about an online system I use daily, I'll consider YouTube Music, a music and video streaming service. To understand how YouTube Music might operate at the back-end using data structures, we can break down the application into its core functionalities and identify which data structures are likely used to support each feature. Dicheva & Hodge (2018) focus on the educational benefits of using games to teach data structures, especially stacks. While the paper is specific to teaching stacks, the core idea of using data structures to manage complex operations is highly relevant to YouTube Music as well.

Here are some examples of how YouTube Music might use different data structures for its operations:

## 1. Playlists and Queues
One of the most common features of YouTube Music is the ability to create and manage playlists. A playlist is essentially a collection of songs that can be played in sequence or shuffled.
#### Data Structure: Queue
 - **Reason:** A queue would be a good data structure for handling the "Next" and "Previous" song functionalities. When a song is played, it is dequeued from the front of the queue, and the next song can be played automatically.
 - **Example:** When you hit "Next," the system dequeues the current song and enqueues it to a history list , or a stack.

## 2. Recently Played Songs
YouTube Music often allows users to re-listen to recently played songs or navigate back to a previously played song.
#### Data Structure: Stack
 - **Reason:** A stack is naturally suited for handling the "Last In, First Out" (LIFO) behavior of a history of played songs. When a user navigates to the previous song, the current song is pushed onto the stack, and the last song is popped from the stack to be played again.
 - **Example:** If you hit the "Back" button, the current song is pushed to the stack, and the last song becomes the top of the stack, which can then be played.

## 3. Recommendations and Search Results
YouTube Music’s recommendation engine might use several advanced algorithms to recommend songs based on user preferences, listening history, and trending content. However, efficient recommendations and search results rely on optimized data structures.
#### Data Structure: Trie (Prefix Tree)
 - **Reason:** A Trie is often used for auto-complete and search functionalities. YouTube Music might use a trie to efficiently retrieve songs or artists as a user types in the search bar. This allows fast lookups based on prefixes, which is crucial for real-time search results.
 - **Example:** When you start typing "Ed Sheeran" into the search bar, the system traverses the trie to suggest completions such as "Ed Sheeran - Shape of You."
#### Data Structure: Hash Table
 - **Reason:** For fast lookups of songs, artists, or albums by ID or name, YouTube Music might use hash tables. Hash tables provide average O(1) time complexity for search, insert, and delete operations, which is ideal for managing large amounts of data like music catalogs.
 - **Example:** When you click on a song, the hash table is queried to retrieve the song's metadata, including its URL and other relevant information.

## 4. Personalized Recommendations
Personalized recommendations are a key feature of YouTube Music, and these recommendations are often based on complex algorithms that factor in user behavior, preferences, and trends.
#### Data Structure: Graph
 - **Reason:** A graph data structure could be used to model relationships between users and songs, as well as between songs themselves. For example, a graph could represent the similarity between songs based on genres, artists, or user interactions with those songs.
 - **Example:** If you listen to a particular artist frequently, the graph would track this relationship, reinforcing the likelihood of recommending similar artists or genres.

## 5. Managing User Sessions
YouTube Music needs to manage multiple active sessions across different devices, keeping track of where a user left off in a playlist or what song they are currently listening to.
#### Data Structure: Hash Map with Linked List
 - **Reason:** A combination of a hash map and doubly linked list could be used to implement a Least Recently Used (LRU) cache. This would allow YouTube Music to quickly retrieve the state of a user's session, such as the song they were last playing or their current playlist, while also efficiently managing memory by removing the least recently used sessions.
 - **Example:** If you switch from your phone to your laptop, YouTube Music retrieves your last session using the hash map and linked list.

## 6. Playback Buffering and Streaming
When streaming music, YouTube Music needs to buffer a portion of the song in advance to ensure smooth playback, even if there is a temporary network issue.
#### Data Structure: Circular Queue
 - **Reason:** A circular queue is an ideal data structure for buffering. It allows continuous overwriting of old data while buffering new parts of the song without ever needing to resize the buffer.
 - **Example:** As a song is played, the player continuously buffers the next few seconds of the song into a circular queue, and as the song progresses, the oldest buffered data is overwritten.

## 7. Handling Concurrent Requests
YouTube Music is a large-scale service, handling requests from millions of users concurrently. Efficient and reliable management of these requests is crucial for smooth operation.
#### Data Structure: Priority Queue (Heap)
 - **Reason:** A priority queue could be used to manage incoming requests, assigning higher priorities to more critical requests such as pausing or switching songs, while lower-priority requests (like background updates) are handled later.
 - **Example:** If you press "Pause" while a song is playing, the system prioritizes this request over other non-urgent tasks, ensuring immediate response.

## 8. Dynamic Playlists
When a user selects a dynamic playlist (such as "Your Mix" or "Discover Weekly"), YouTube Music may dynamically generate a list of songs based on the user’s listening habits.
#### Data Structure: Dynamic Array or Linked List
 - **Reason:** A dynamic array or linked list could be used to store a playlist that is generated on-the-fly. Dynamic arrays allow resizing as songs are added to the playlist, while linked lists allow efficient insertion and deletion if the playlist needs to be modified.
 - **Example:** As you listen to recommended songs, the dynamic playlist can grow or shrink depending on your actions (e.g., skipping a song or adding a new one).

## Conclusion
YouTube Music relies heavily on a variety of data structures behind the scenes to efficiently manage its large-scale operations. From queues and stacks for playlist management to hash maps and tries for fast lookups, each data structure plays a critical role in ensuring the platform's smooth operation. As highlighted in the Dicheva & Hodge (2018) paper, understanding these data structures is essential not only for software development but also for creating interactive learning tools such as educational games that help students grasp these abstract concepts. In the context of YouTube Music, mastering data structures is key to building scalable, efficient systems.

## Reflections
Reflecting on this e-Portfolio activity, I learned how data structures like queues, stacks, and graphs are vital for YouTube Music's backend operations. These structures manage playlists, search functionalities, and personalized recommendations. Understanding their role, as emphasized by Dicheva & Hodge (2018), highlights the importance of data structures in creating efficient systems. I can apply this knowledge in future projects to build scalable applications and enhance user experiences. Mastering these concepts also equips me to develop educational tools that simplify learning complex data structures, making them more accessible to others.
<br><br>

---

## Reference
Anderson, C. (2019). Using Deep Neural Networks to make YouTube Recommendations. Medium. Available from: https://towardsdatascience.com/using-deep-neural-networks-to-make-youtube-recommendations-dfc0a1a13d1e

Covington, P., Adams, J., & Sargin, E. (2016). 'Deep neural networks for YouTube recommendations', RecSys '16: Proceedings of the 10th ACM Conference on Recommender Systems. Massachusetts, Boston, USA, 15-19 September 2016. ACM. 191-198. DOI: https://doi.org/10.1145/2959100.2959190

Dicheva, D., & Hodge, A. (2018). 'Active learning through game play in a data structures course', SIGCSE '18: Proceedings of the 49th ACM Technical Symposium on Computer Science Education. Baltimore, MD, USA, 21-24 February 2018. ACM. 834–839. DOI: https://doi.org/10.1145/3159450.3159605

JamWise (2024). Music Recommendation Algorithms: How They Work and What We Can Learn From Them. Available from: https://www.jamwise.org/p/music-recommendation-algorithms-how

Knuth, D. E. (1997). The art of computer programming, volume 1: Fundamental algorithms. 3rd ed. CA: Addison-Wesley.

Laaksonen, A. (2024). Guide to competitive programming: Learning and improving algorithms through contests. 3rd ed. Springer Cham.

Okeke, C. (2023). Introduction to Data Structures with Real World Examples. Medium. Available from: https://medium.com/@DevChy/introduction-to-data-structures-with-real-world-examples-15063e4adbad

Tarjan, R. (1972). Depth-first search and linear graph algorithms. SIAM Journal on Computing 1(2): 146–160. DOI: https://doi.org/10.1137/0201010

Zhou, Y, Wilkinson, D, Schreiber, R & Pan, R (2008). 'Large-scale parallel collaborative filtering for the Netflix Prize', AAIM: International Conference on Algorithmic Aspects in Information and Management. Shanghai, China, 23-25 June 2008.  Springer. 337–348. DOI: 10.1007/978-3-540-68880-8_32.

<br><br>

---

[Return to Module 6 Unit 2](SSD_Unit02.md)
