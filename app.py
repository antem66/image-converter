from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    # A simple health check endpoint
    return jsonify({"status": "healthy", "message": "WebP to PNG converter is running."}), 200

@app.route('/convert', methods=['POST'])
def convert_image():
    """
    Converts an uploaded WebP image to PNG or JPEG based on the optional 'output_format' form field.
    Default is PNG.
    """
    if 'image' not in request.files:
        return jsonify({"error": "No 'image' file part in the request"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.content_type.startswith('image/webp'):
        return jsonify({"error": f"File is not a WebP image. Content-Type: {file.content_type}"}), 400

    # Get the desired output format from the form (default to 'png')
    output_format = request.form.get('output_format', 'png').lower()
    if output_format == 'jpg':
        output_format = 'jpeg'
    if output_format not in ['png', 'jpeg']:
        return jsonify({"error": f"Unsupported output format: {output_format}. Only 'png' and 'jpeg' are supported."}), 400

    try:
        input_image_stream = io.BytesIO(file.read())
        img = Image.open(input_image_stream)

        if img.format != 'WEBP':
            return jsonify({"error": f"Uploaded file could not be identified as WebP by Pillow. Detected format: {img.format}"}), 400

        output_image_stream = io.BytesIO()
        img.save(output_image_stream, format=output_format.upper())
        output_image_stream.seek(0)

        # Set mimetype and extension
        if output_format == 'png':
            mimetype = 'image/png'
            ext = 'png'
        else:
            mimetype = 'image/jpeg'
            ext = 'jpg'

        return send_file(
            output_image_stream,
            mimetype=mimetype,
            as_attachment=True,
            download_name=f'converted.{ext}'
        )

    except Exception as e:
        return jsonify({"error": f"An error occurred during image processing: {str(e)}"}), 500

if __name__ == '__main__':
    # Railway provides the PORT environment variable. Default to 8080 if not set.
    port = int(os.environ.get('PORT', 8080))
    # Listen on 0.0.0.0 to be accessible from outside the container
    app.run(host='0.0.0.0', port=port)