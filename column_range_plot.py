import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    
    A = np.asarray(A) 
    
    column_ranges = A.max(axis=0) - A.min(axis=0)
    
    plt.figure(figsize=(8, 4))
    plt.bar(np.arange(len(column_ranges)), column_ranges)
    plt.xlabel("Column Index")
    plt.ylabel("Range (max - min)")
    plt.tight_layout()
    
    plt.savefig(filename)
    plt.close()
    
    return column_ranges 

# plt.figure(figsize=(4, 8)) - if not specified, matplotlib uses a 
#                              default size (usually around 6x4 inches)
#                              cleaner PDF output
#                              better proportions for bar plots

# plt.tight_layout() - adjusts spacing between elements of the plot