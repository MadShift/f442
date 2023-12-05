import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/down/<path:filename>', methods=['GET', 'POST'])
def download(filename):    
    downloads = os.path(app.root_path)
    
    return send_from_directory(directory=downloads, filename=filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8229)