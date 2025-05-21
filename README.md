# WebP to PNG Image Converter API

A simple Flask-based API for converting WebP images to PNG format. Designed to be containerized and easily deployed to platforms like [Railway](https://railway.app/).

---

## Features
- **POST /convert**: Accepts a WebP image and returns a PNG image.
- **GET /**: Health check endpoint.

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

### Convert WebP to PNG
```bash
curl -X POST -F "image=@your_image.webp" http://localhost:8080/convert --output converted.png
```

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
└── README.md         # This file
```

---

## Troubleshooting
- Ensure that Railway sets the `PORT` environment variable (it does by default).
- If you get a `ModuleNotFoundError`, make sure all dependencies are installed.
- For CORS or production security, consider using a production WSGI server (e.g., Gunicorn) and/or a reverse proxy.

---

## License
MIT
