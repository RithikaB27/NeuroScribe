import scipy.io
import pandas as pd
import os

def convert_mat_to_csv(mat_path, output_csv_path):
    mat = scipy.io.loadmat(mat_path)
    if 'data' not in mat:
        raise ValueError("No 'data' key found in .mat file.")
    df = pd.DataFrame(mat['data'])
    df.to_csv(output_csv_path, index=False)
    print(f"Saved to: {output_csv_path}")

# Example usage
convert_mat_to_csv("uploads/sample.mat", "converted/sample.csv")
