import subprocess
import os

def convert_drawio(drawio_path, output_path, output_format='png'):
    # Define the command to run draw.io CLI
    command = [
        'xvfb-run', '--auto-servernum', '--server-num=1',
        'drawio',
        '--export',
        '--format', output_format,
        '--output', output_path,
        drawio_path
    ]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"File converted successfully: {output_path}")

def convert_all_drawio_in_folder(folder_path, output_format='png'):
    # List all files in the given folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".drawio"):
            drawio_path = os.path.join(folder_path, filename)
            # Create an output file path with the same base name but different extension
            output_filename = f"{os.path.splitext(filename)[0]}.{output_format}"
            output_path = os.path.join(folder_path, output_filename)
            # Convert the file
            convert_drawio(drawio_path, output_path, output_format)
            print(f"Converted {drawio_path} to {output_path}")

# Usage example: converting all .drawio files in the 'drawio_files' directory to PNG
convert_all_drawio_in_folder('./drawio/files', 'png')
convert_all_drawio_in_folder('./drawio/files', 'svg')
