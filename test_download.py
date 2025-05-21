import requests
import argparse
import os

# Supported output formats for Pillow: PNG, JPEG, BMP, TIFF, GIF, etc.
# The API must support these (currently only PNG is implemented in app.py)
SUPPORTED_FORMATS = ['png', 'jpeg', 'jpg']

def test_convert_webp_to_image(webp_path, api_url, output_format, output_file):
    # Normalize jpg to jpeg
    if output_format == 'jpg':
        output_format = 'jpeg'
    with open(webp_path, 'rb') as f:
        files = {'image': (os.path.basename(webp_path), f, 'image/webp')}
        data = {'output_format': output_format}
        response = requests.post(api_url, files=files, data=data)
        assert response.status_code == 200, f"Status code: {response.status_code}, Body: {response.text}"
        expected_mime = f"image/{output_format}"
        assert expected_mime in response.headers['Content-Type'], f"Content-Type: {response.headers['Content-Type']}"
        # Set output file extension if not provided
        if not output_file.lower().endswith(f'.{output_format}'):
            output_file = os.path.splitext(output_file)[0] + f'.{output_format}'
        with open(output_file, 'wb') as out:
            out.write(response.content)
        print(f"Image file saved as {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test WebP to image API.')
    parser.add_argument('--webp', default='test.webp', help='Path to input WebP file')
    parser.add_argument('--url', default='http://localhost:8080/convert', help='API endpoint URL')
    parser.add_argument('--format', default='png', choices=SUPPORTED_FORMATS, help="Desired output format: 'png', 'jpeg', or 'jpg'")
    parser.add_argument('--output', default='test_converted.png', help='Output file name')
    args = parser.parse_args()
    test_convert_webp_to_image(args.webp, args.url, args.format, args.output)

# Suggestions for further improvements:
# - Add support for specifying output format to the API (e.g., as a query parameter or form field)
# - Add tests for error cases (bad file, wrong format, etc.)
# - Add image validation (open with Pillow, check dimensions, etc.)
# - Add CLI option for verbose/debug output
# - Add support for remote URLs as input

    test_convert_webp_to_png()
