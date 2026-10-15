import heapq
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

#counting the frequency of each character in the file and storing it in a dictionary
def get_frequencies(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

#checking which letter is more frequent and building a binary tree based on the frequency of each character
def build_tree(frequencies):
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, Node(char, freq))
        
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        
        merged_freq = left_node.freq + right_node.freq
        parent_node = Node(None, merged_freq)
        parent_node.left = left_node
        parent_node.right = right_node
        
        heapq.heappush(heap, parent_node)
        
    return heapq.heappop(heap)

#generating the binary codes for each character based on the binary tree
def generate_codes(root, current_code, codes_dict):
    if root is None:
        return
    if root.char is not None:
        codes_dict[root.char] = current_code
        return
    generate_codes(root.left, current_code + "0", codes_dict)
    generate_codes(root.right, current_code + "1", codes_dict)

#getting the file path and reading the file content
def read_file(filename):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    exact_file_path = os.path.join(script_directory, filename)
    
    with open(exact_file_path, 'r', encoding='utf-8') as file:
        return file.read()

#writing the compressed binary data to a file
def write_true_binary(filename, bit_string):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    exact_file_path = os.path.join(script_directory, filename)
    
    extra_padding = 8 - (len(bit_string) % 8)
    if extra_padding != 8:
        bit_string += "0" * extra_padding
        
    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte_chunk = bit_string[i:i+8]
        byte_array.append(int(byte_chunk, 2))
        
    # Save as a raw binary file ('wb')
    with open(exact_file_path, 'wb') as file:
        file.write(byte_array)

#main function to execute the Huffman encoding process
if __name__ == "__main__":
    input_filename = input("Enter the name of the file to compress (e.g., my_data.txt): ")
    
    try:
        my_text = read_file(input_filename)
        
        if len(my_text) == 0:
            print("Error: The file is empty. Please add some text and try again.")
        else:
            print(f"\nSuccessfully read {len(my_text)} characters from {input_filename}...")
            
            frequencies = get_frequencies(my_text)
            root_node = build_tree(frequencies)
            
            huffman_codes = {}
            generate_codes(root_node, "", huffman_codes)
            
            compressed_text = "".join(huffman_codes[char] for char in my_text)
            
            base_name = input_filename.split('.')[0]
            binary_filename = f"{base_name}_compressed.bin"
            
            write_true_binary(binary_filename, compressed_text)
            print(f"Success! True binary saved directly to your project folder as: {binary_filename}")
            
            #calculating the size of the original and compressed files and displaying the results
            original_bits = len(my_text) * 8
            compressed_bits = (len(compressed_text) // 8 + (1 if len(compressed_text) % 8 != 0 else 0)) * 8
            
            print(f"\nOriginal File Size: {original_bits} bits")
            print(f"New File Size: {compressed_bits} bits")
            print(f"Space Saved: {100 - (compressed_bits / original_bits * 100):.2f}%")
            
    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'.")