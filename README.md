# NeuroScribe: Turning Thoughts into Words

NeuroScribe is a Brain-Computer Interface (BCI) powered project that transforms EEG brainwave signals into human-readable thoughts across multiple languages (English, Hindi, and Tamil). Built using AI, NLP, and Deep Learning-inspired pipelines, it supports `.mat` EEG files and produces meaningful visualizations, thought generation, and performance metrics.

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

### 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, if cloning from GitHub)

---

### 📁 1. Clone the Repository (if using Git)

```bash
git clone https://github.com/your-username/neuroscribe.git
cd neuroscribe
```

---

### 📦 2. Install Required Libraries

Use the following command to install all dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
Flask
numpy
pandas
scipy
matplotlib
h5py
```

If you're missing pip:

```bash
python -m ensurepip --upgrade
```

---

### 🚀 3. Run the Flask Application

In your terminal:

```bash
python app.py
```

You should see:

```
✅ Flask running at http://127.0.0.1:5000
```

---

### 🌐 4. Access the Web App

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

### 🧪 5. Upload EEG File & Generate Thought

1. Navigate to the **Generate** page.
2. Upload a `.mat` EEG file.
3. Choose a language (English, Hindi, Tamil).
4. Click “Generate Thought”.
5. View the output text, EEG graph, features, and metrics.

---

---

## 💻 Software Requirements

- **Operating System**: Windows 10 / 11, Linux, or macOS
- **Python Version**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended for larger EEG files)
- **Browser**: Chrome, Firefox, or any modern browser
- **MATLAB (optional)**: For inspecting `.mat` EEG files

---

## 🛠️ Tools Used

| Tool / Software        | Purpose                                        |
|------------------------|------------------------------------------------|
| **Visual Studio Code** | Development and debugging                      |
| **Python 3.9+**         | Backend programming language                   |
| **Flask**              | Web application framework                      |
| **Jupyter Notebook**   | Prototyping EEG feature extraction             |
| **Chart.js**           | Browser-based EEG feature graph plotting       |
| **Matplotlib**         | Plot EEG brainwave signal as image             |
| **Git & GitHub**       | Version control and project collaboration      |
| **Canva / Figma**      | (Optional) UI mockups and poster design        |
| **Command Prompt / Terminal** | Running Flask server and scripts       |

---

## 🔮 Future Enhancements

- 🧠 **Integration with Transformer Models**  
  Implement models like **BART** or **T5** to generate open-ended, real-time thoughts from EEG data.

- 🧩 **Semantic Matching Module**  
  Use sentence embeddings (e.g., **SBERT**) to semantically align EEG signals with thought templates.

- 📡 **Real-Time EEG Stream Support**  
  Enable live EEG input using devices like **OpenBCI** or **Muse Headband**.

- 👤 **User Personalization**  
  Collect EEG patterns over time to make the system **adaptive to individual users** through fine-tuned profiles.

- 🗂️ **User Login and History Tracking**  
  Allow users to view previous uploads and results by storing session history securely.

- 📥 **Downloadable PDF Reports**  
  Generate a PDF that includes the EEG signal plot, thought output, language, and accuracy metrics.

- ☁️ **Cloud Deployment**  
  Host the application on platforms like **Render, Heroku, or AWS** for public access.

- 📱 **Mobile-Responsive UI**  
  Redesign the front end to work seamlessly on phones and tablets.

---

## 📚 Dataset Used

- **ZuCo 2.0 Dataset (Zurich Cognitive Language Processing Corpus)**  
  EEG-based eye-tracking and language reading dataset.  
  Used as a reference for EEG data structure and feature modeling.  
  [Link to dataset](https://osf.io/2urht/)

- **Custom `.mat` EEG Files**  
  EEG files in `.mat` (MATLAB) format collected or simulated for test purposes.

---
