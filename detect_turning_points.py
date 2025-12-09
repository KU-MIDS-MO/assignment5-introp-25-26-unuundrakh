import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    diff = np.diff(signal)
    
    signs = np.sign(diff)
    
    turning_points=[]
        
    for i in range(len(signs) - 1):
        if signs[i] !=0 and signs[i+1] !=0 and signs[i] !=signs[i+1]:
            turning_points.append(i + 1)
    turning_points = np.array(turning_points, dtype=int)
        
    x = np.arange(len(signal))
    plt.figure(figsize=(7, 4))
    plt.plot(x, signal, marker='o', label="signal")
    plt.scatter(turning_points, signal[turning_points], color="yellow", s=80)
    plt.title("Turning Points")
    plt.xlabel("Index")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
        
    return turning_points

