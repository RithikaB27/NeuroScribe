from flask import Flask, render_template, request, send_from_directory
import os
import time
from werkzeug.utils import secure_filename
from models.model import generate_text_from_eeg
from models.eeg_utils import generate_eeg_plot

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    output_text = eeg_plot = category = None
    preview_data = rouge = bleu = accuracy = output_time = None

    if request.method == 'POST':
        if 'eegfile' not in request.files:
            return render_template('generate.html', output_text="No file uploaded.")

        eegfile = request.files['eegfile']
        language = request.form.get('language', 'en')

        if eegfile.filename == '':
            return render_template('generate.html', output_text="No selected file.")

        filename = secure_filename(eegfile.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        eegfile.save(filepath)

        try:
            start_time = time.time()
            result = generate_text_from_eeg(filepath, lang=language)

            output_text = result.get("text", "")
            category = result.get("category", "")
            preview_data = result.get("preview_data", [])
            rouge = result.get("rouge", "")
            bleu = result.get("bleu", "")
            accuracy = result.get("accuracy", "")
            output_time = round(time.time() - start_time, 2)

            eeg_plot = generate_eeg_plot(filepath, category)
        except Exception as e:
            output_text = f"Error during generation: {str(e)}"

    return render_template('generate.html',
                           output_text=output_text,
                           eeg_plot=eeg_plot,
                           category=category,
                           preview_data=preview_data or [],
                           rouge=rouge,
                           bleu=bleu,
                           accuracy=accuracy,
                           output_time=output_time)

@app.route('/static/img/<filename>')
def eeg_plot_file(filename):
    return send_from_directory('static/img', filename)

if __name__ == '__main__':
    print("✅ Flask running at http://127.0.0.1:5000")
    app.run(debug=True)
