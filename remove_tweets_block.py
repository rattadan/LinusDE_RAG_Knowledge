#!/usr/bin/env python3
import os
import re
from pathlib import Path

def remove_tweets_block(content):
    # More flexible pattern to match the block with varying whitespace and formatting
    pattern = r'##\s*Original\s*Tweets/Messages[\s\S]*?<details[\s\S]*?</details>\s*'
    return re.sub(pattern, '', content, flags=re.IGNORECASE)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = remove_tweets_block(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Find all .md files in the current directory and subdirectories
    md_files = list(script_dir.glob('**/*.md'))
    
    if not md_files:
        print("No markdown files found in the current directory and subdirectories.")
        return
    
    print(f"Found {len(md_files)} markdown files. Processing...")
    
    modified_count = 0
    for file_path in md_files:
        if process_file(file_path):
            print(f"Modified: {file_path}")
            modified_count += 1
    
    print(f"\nProcessing complete. Modified {modified_count} out of {len(md_files)} files.")

if __name__ == "__main__":
    main()
