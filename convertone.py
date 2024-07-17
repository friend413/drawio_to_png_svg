import subprocess

def convert_drawio(drawio_path, output_path, output_format='png'):
    # Define the command to run draw.io CLI
    # Ensure the path to the drawio application is correct
    drawio_executable = 'drawio'  # Keep the executable name as just 'drawio'
    command = [
        'xvfb-run',  '--auto-servernum', '--server-num=1', # This command precedes the actual drawio command
        drawio_executable,
        '--export',  # Command to export
        '--format', output_format,  # Define format: png or svg
        '--output', output_path,  # Define output file path
        drawio_path  # Input .drawio file
    ]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"File converted successfully: {output_path}")

# Example usage
convert_drawio('example.drawio', 'output.png', 'png')
convert_drawio('example.drawio', 'output.svg', 'svg')
