# WebP to PNG/JPEG Image Converter API

A simple Flask-based API for converting WebP images to PNG or JPEG (JPG) format. Designed for easy containerization and deployment (e.g., Railway, Docker, local).

---

## Features
- **POST /convert**: Accepts a WebP image, returns a PNG or JPEG image (selectable).
- **GET /**: Health check endpoint.
- **Test script**: Download and verify conversion results automatically.

---

## Requirements
- Python 3.9+
- [Flask](https://flask.palletsprojects.com/)
- [Pillow](https://python-pillow.org/)

All dependencies are listed in `requirements.txt`.

---

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd image-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:8080` by default.

---

## Usage

### Health Check
```bash
curl http://localhost:8080/
```

### Convert WebP to PNG or JPEG
#### PNG output (default):
```bash
curl -X POST -F "image=@your_image.webp;type=image/webp" http://localhost:8080/convert --output converted.png
```

#### JPEG output:
```bash
curl -X POST -F "image=@your_image.webp;type=image/webp" -F "output_format=jpeg" http://localhost:8080/convert --output converted.jpg
```
- You can use `output_format=jpeg` or `output_format=jpg` (both work).
- The response will be the converted image file.

---

## Docker

1. **Build the Docker image**
   ```bash
   docker build -t image-converter .
   ```
2. **Run the Docker container**
   ```bash
   docker run -p 8080:8080 image-converter
   ```

---

## Deploying to Railway

1. [Create a new project on Railway](https://railway.app/new).
2. Connect your GitHub repository or upload your code.
3. Railway will auto-detect the `Dockerfile` and build the image.
4. The app will listen on the port defined by the `PORT` environment variable (default is 8080).
5. Once deployed, use the `/convert` endpoint as described above.

---

## File Structure
```
.
├── app.py            # Main Flask app
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container build instructions
├── .dockerignore     # Files to ignore in Docker builds
├── .gitignore        # Git ignore rules
├── .gitattributes    # Git attributes for line endings/binaries
├── test_download.py  # Script to test and download conversion results
└── README.md         # This file
```

---

## Automated Testing

You can use the included test script to verify the API and download results automatically:

```bash
python3 test_download.py --webp test.webp --format png --output result.png
python3 test_download.py --webp test.webp --format jpeg --output result.jpg
```
- The script uploads your WebP image, requests the desired output format, and saves the result.
- See `test_download.py` for more options.

---

## Troubleshooting
- Ensure that Railway sets the `PORT` environment variable (it does by default).
- If you get a `ModuleNotFoundError`, make sure all dependencies are installed.
- For CORS or production security, consider using a production WSGI server (e.g., Gunicorn) and/or a reverse proxy.
- For JPEG output, transparency will be lost (JPEG does not support alpha channel).
- For any API errors, check the returned JSON for details.

---

## Git & GitHub Workflow

1. Initialize git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Add your remote:
   ```bash
   git remote add origin https://github.com/yourusername/image-converter.git
   git branch -M main
   git push -u origin main
   ```
3. Make changes, commit, and push as needed.

---

## License
MIT
