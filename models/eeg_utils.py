import numpy as np
import scipy.io
import h5py
import os
import uuid
import matplotlib
matplotlib.use('Agg')  # For servers without GUI
import matplotlib.pyplot as plt
import pandas as pd

def extract_eeg_features(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    data = None
    if ext == '.mat':
        try:
            try:
                mat = scipy.io.loadmat(filepath)
                # DEBUG: print keys to identify data source
                print("Available keys in .mat file:", mat.keys())

                # Try multiple common keys
                for key in ['data', 'EEG', 'X', 'eeg_data', 'raw_data']:
                    if key in mat:
                        data = mat[key]
                        break

                if data is None:
                    raise ValueError("No valid EEG data key found in .mat file.")
            except NotImplementedError:
                # For MATLAB v7.3
                with h5py.File(filepath, 'r') as f:
                    print("HDF5 keys:", list(f.keys()))
                    if 'data' in f:
                        data = np.array(f['data']).T
                    else:
                        raise ValueError("No 'data' key found in HDF5 .mat file.")
        except Exception as e:
            raise ValueError(f"MAT file error: {e}")

    elif ext == '.csv':
        try:
            df = pd.read_csv(filepath, on_bad_lines='skip')
            data = df.select_dtypes(include=[np.number]).to_numpy()
            if data.shape[0] == 0 or data.shape[1] == 0:
                raise ValueError("No usable numeric EEG data found in CSV.")
        except Exception as e:
            raise ValueError(f"CSV load error: {e}")
    else:
        raise ValueError("Unsupported file format")

    if data is None or data.size == 0:
        raise ValueError("EEG data is empty or invalid.")
    if data.shape[1] < 1:
        raise ValueError("No EEG channels found in data.")

    # 🧠 Feature extraction: first 5 channels
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    max_vals = np.max(data, axis=0)
    min_vals = np.min(data, axis=0)
    median = np.median(data, axis=0)

    features = np.concatenate([
        mean[:5], std[:5], max_vals[:5], min_vals[:5], median[:5]
    ])
    return features

def generate_eeg_plot(filepath, category):
    ext = os.path.splitext(filepath)[1].lower()

    data = None
    if ext == '.mat':
        try:
            try:
                mat = scipy.io.loadmat(filepath)
                for key in ['data', 'EEG', 'X', 'eeg_data', 'raw_data']:
                    if key in mat:
                        data = mat[key]
                        break
                if data is None:
                    raise ValueError("No valid EEG key in .mat file.")
            except NotImplementedError:
                with h5py.File(filepath, 'r') as f:
                    if 'data' in f:
                        data = np.array(f['data']).T
        except:
            return None
    elif ext == '.csv':
        try:
            df = pd.read_csv(filepath)
            data = df.select_dtypes(include=[np.number]).to_numpy()
        except:
            return None
    else:
        return None

    if data is None or data.shape[1] < 1:
        return None

    # ✅ Normalize data for better plotting
    data = data.astype(float)
    data = data / np.max(np.abs(data), axis=0)

    fig, ax = plt.subplots(figsize=(10, 4))
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
    for i in range(min(3, data.shape[1])):
        ax.plot(data[:500, i], label=f'Channel {i+1}', color=colors[i], linewidth=1.5)

    ax.set_title(f"EEG Brainwave Signal - {category.capitalize()}")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Normalized Amplitude")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.3)

    # 📁 Save with unique filename
    output_name = f"eeg_plot_{uuid.uuid4().hex}.png"
    plot_path = os.path.join('static/img', output_name)

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    return output_name
