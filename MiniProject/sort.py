import gradio as gr  # Import the Gradio library

# Define the selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum element with the first element
    return arr

# Define the merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]  # Divide the array elements into two halves
        R = arr[mid:]

        merge_sort(L)  # Sort the first half
        merge_sort(R)  # Sort the second half

        i = j = k = 0  # Initialize indices for merging 

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function to sort an array based on the selected algorithm
def sort_array(array, algorithm):
    array = list(map(int, array.split(',')))  # Convert the input string to a list of integers
    if algorithm == "Selection Sort":
        sorted_array = selection_sort(array)
    elif algorithm == "Merge Sort":
        sorted_array = merge_sort(array)
    return ', '.join(map(str, sorted_array))  # Convert the sorted list back to a comma-separated string

# Define the Gradio interface components
inputs = [
    gr.Textbox(label="Enter array (comma-separated)", placeholder="e.g., [3,1,4,1,5,9]"),  # Input for array
    gr.Dropdown(["Selection Sort", "Merge Sort"], label="Choose Sorting Algorithm")  # Dropdown for algorithm selection
]
outputs = gr.Textbox(label="Sorted Array")  # Output for sorted array

# Custom CSS for styling the interface
css = """
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}
.gradio-container {
    border: 2px solid #333;
    border-radius: 10px;
    padding: 20px;
    max-width: 600px;
    margin: 50px auto;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.gr-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
}
.gr-button:hover {
    background-color: #45a049;
}
"""

# Launch the Gradio interface
gr.Interface(fn=sort_array, inputs=inputs, outputs=outputs, title="Sorting Algorithm Visualizer", css=css).launch()
