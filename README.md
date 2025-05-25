# NeuroScribe: Turning Thoughts into Words

NeuroScribe is a Brain-Computer Interface (BCI) powered project that transforms EEG brainwave signals into human-readable thoughts across multiple languages (English, Hindi, and Tamil). Built using AI, NLP, and Deep Learning-inspired pipelines, it supports `.mat` and `.csv` EEG files and produces meaningful visualizations, thought generation, and performance metrics.

---

## 📌 Project Overview

> “Turning EEG signals into human thoughts using AI, semantic mapping, and visual interpretation.”

- 🧬 Converts EEG brain signals into readable text  
- 🌍 Multilingual output: English, Hindi, and Tamil  
- 📈 Real-time EEG signal graph + top feature visualization  
- 🎯 ROUGE, BLEU, and Accuracy metrics displayed  
- 🕒 Output generation time tracking  
- 🔁 Deterministic: same EEG file always gives same text

---

## 🧰 Technologies Used

### ✅ Frontend
- HTML5 + CSS3 + JavaScript
- Chart.js (for real-time EEG feature graph)
- Dark mode, animations, and typing effect

### ✅ Backend
- Python 3.9+
- Flask (web framework)
- Jinja2 (template rendering)
- NumPy, Pandas (data processing)
- Matplotlib (EEG signal plots)
- SciPy, h5py (for .mat EEG files)
- uuid, hashlib (unique output and consistency)

---

## 🔍 Features

| Feature                  | Description |
|--------------------------|-------------|
| 🧠 Thought Generation     | Converts EEG into coherent multilingual thoughts |
| 📊 EEG Graphs            | Signal and feature visualization |
| 🌐 Multilingual Support  | English, Hindi, Tamil |
| 🎯 Accuracy Metrics      | ROUGE-L, BLEU, and simulated accuracy |
| 🔁 Deterministic Output  | Same file = same text |
| 🕒 Output Timer          | Measures generation duration |

---

## 📁 Supported File Formats

- `.mat` files (MATLAB v7 and v7.3)

---

## 📂 Folder Structure
```
NeuroScribe/
├── app.py
├── models/
│ ├── model.py
│ └── eeg_utils.py
├── templates/
│ ├── index.html
│ ├── generate.html
│ └── about.html
├── static/
│ ├── css/
│ │ └── style.css
│ └── img/
├── uploads/
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Running Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/neuroscribe.git
cd neuroscribe

**### 2. Install Dependencies**
```bash
pip install -r requirements.txt```

**### 3. Run the App**
```bash
python app.py```

Visit http://127.0.0.1:5000 in your browser.

---

**## 🧪 Example Workflow**

1. Go to the Generate page.
2. Upload an EEG file (.mat or .csv).
3. Select output language.
4. Click "Generate Thought".
5. View:
  - Generated multilingual thought
  - EEG signal graph
  - EEG feature chart
  - Accuracy metrics and generation time

---

**## 📦 Software Requirements**

- Python 3.8 or higher
- OS: Windows 10 / Linux / macOS
- RAM: 4GB+ (8GB recommended)
- Browser: Chrome or Firefox

---

**## 🛠 Tools Used**

- Visual Studio Code (VS Code)
- Git & GitHub (for version control)
- Terminal / CMD (for running scripts)

---

**## 🔮 Future Enhancements**

- 🧠 Integrate transformer models like BART/T5 for real-time decoding
- 📊 Semantic Matching using SBERT or CLIP
- 🔄 Real-time EEG streaming from headbands (Muse, OpenBCI)
- 🧍‍♂️ User-specific adaptive output based on personalized brain data
- 🗂️ User login and session history tracking
- 📥 Export results to downloadable PDF
- ☁️ Cloud deployment + mobile support

---

**## 📚 Dataset Used**

- ZuCo 2.0: Zurich Cognitive Language Processing Corpus
(Used for feature structure inspiration. Real-time live EEG streaming not included.)

---

