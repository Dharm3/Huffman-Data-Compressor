# Huffman Data Compress
A lossless data compression tool built in Python. This algorithm reads standard ASCII text files, calculates character frequencies, and builds a mathematical Huffman Tree to generate optimal, prefix-free binary codes.

##  Features
* **Frequency Analysis:** Utilizes dictionaries to count character occurrences.
* **Tree Construction:** Implements a Min Heap (`heapq`) to dynamically build the Huffman Tree from the bottom up.
* **Prefix-Free Codes:** Recursively goes through the binary tree to generate unique bit strings for every character.
* **True Binary File I/O:** Converts mathematical string representations of 1s and 0s into raw byte arrays to shrink file size.

##  Technical Concepts Demonstrated
* **Data Structures:** Binary Trees, Priority Queues and Hash Maps.
* **Algorithms:** Greedy Algorithms, Depth First Search for tree traversal.
* **Low-Level Operations:** Bitwise padding, base 2 string-to-integer conversion, and binary file writing (`wb`).

##  Usage
1. Clone the repository and navigate to the project folder.
2. Ensure you have a standard text file (e.g., `data.txt`) in the same directory.
3. Run the script:
   ```bash
   python huffman.py
