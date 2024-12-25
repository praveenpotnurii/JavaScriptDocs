import os
from pathlib import Path

def merge_md_files(input_dir):
    # Create Path object for input directory
    input_path = Path(input_dir)
    
    # Extract prefix from directory name and create output filename
    dir_prefix = input_path.name.split('-')[0]  # Get '01' from '01-variables-data-types-docs'
    output_filename = f'part_{dir_prefix}.md'
    output_path = input_path / output_filename
    
    # Get all md files in the directory
    md_files = sorted(input_path.glob('*.md'))
    
    if not md_files:  # Skip if no markdown files found
        print(f"No markdown files found in {input_path}")
        return
    
    # Open output file in write mode
    with open(output_path, 'w', encoding='utf-8') as outfile:
        # Iterate through each md file
        for i, md_file in enumerate(md_files):
            # Read content of current file
            with open(md_file, 'r', encoding='utf-8') as infile:
                # Write filename as header
                outfile.write(f'\n# {md_file.stem}\n\n')
                # Write content
                outfile.write(infile.read())
                # Add separator between files (except for last file)
                if i < len(md_files) - 1:
                    outfile.write('\n\n---\n\n')
    print(f"Created {output_path}")

def process_all_directories():
    # Get current directory
    current_path = Path('.')
    
    # Find all directories that start with a number
    directories = [d for d in current_path.iterdir() 
                  if d.is_dir() and d.name[0:2].isdigit()]
    
    # Sort directories to process them in order
    directories.sort()
    
    # Process each directory
    for directory in directories:
        print(f"\nProcessing directory: {directory}")
        merge_md_files(directory)

# Usage example
if __name__ == '__main__':
    process_all_directories()