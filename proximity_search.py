#!/usr/bin/env python3
import os
import re
import argparse
from collections import defaultdict
from pathlib import Path

def find_keyword_proximity(directory, keywords, window_size=100):
    """
    Search for keywords in markdown files within a specified proximity.
    
    Args:
        directory (str): Path to directory containing markdown files
        keywords (list): List of keywords to search for
        window_size (int): Number of characters to consider as proximity window
    """
    # Convert keywords to lowercase for case-insensitive search
    keywords = [k.lower() for k in keywords]
    keyword_pattern = re.compile('|'.join(map(re.escape, keywords)), re.IGNORECASE)
    
    results = defaultdict(list)
    
    # Get all markdown files in the directory
    md_files = list(Path(directory).glob('*.md'))
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find all keyword matches with their positions
            matches = []
            for match in keyword_pattern.finditer(content):
                matches.append((match.group().lower(), match.start()))
            
            # Check for keywords in proximity
            for i in range(len(matches)):
                current_word, current_pos = matches[i]
                context_start = max(0, current_pos - 50)
                context_end = min(len(content), current_pos + 50)
                context = content[context_start:context_end]
                
                # Find other keywords in the proximity window
                for j in range(max(0, i-5), min(len(matches), i+6)):
                    if i == j:
                        continue
                    
                    other_word, other_pos = matches[j]
                    if abs(current_pos - other_pos) <= window_size:
                        # Get a window of text around both keywords
                        start = min(current_pos, other_pos)
                        end = max(current_pos + len(current_word), 
                                other_pos + len(other_word))
                        
                        # Expand the window for better context
                        context_start = max(0, start - 100)
                        context_end = min(len(content), end + 100)
                        
                        # Get the surrounding text
                        context = content[context_start:context_end]
                        
                        # Highlight the keywords in the context
                        context = context.replace(current_word, f'**{current_word.upper()}**')
                        context = context.replace(other_word, f'**{other_word.upper()}**')
                        
                        results[md_file.name].append({
                            'keywords': (current_word, other_word),
                            'context': context,
                            'positions': (current_pos, other_pos)
                        })
                        
        except Exception as e:
            print(f"Error processing {md_file}: {str(e)}")
    
    return results

def print_results(results, directory):
    """Print the search results in a readable format.
    
    Args:
        results (dict): Dictionary of search results
        directory (str): Base directory where files are located
    """
    for filename, matches in results.items():
        full_path = os.path.abspath(os.path.join(directory, filename))
        print(f"\n{'='*80}")
        print(f"FILE: {filename}")
        print(f"PATH: {full_path}")
        print(f"Found {len(matches)} proximity matches")
        print(f"{'='*80}")
        
        for i, match in enumerate(matches, 1):
            kw1, kw2 = match['keywords']
            print(f"\nMatch {i}: '{kw1.upper()}' near '{kw2.upper()}'")
            print(f"Context: ...{match['context']}...")
            print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description='Search for keywords in proximity within markdown files.')
    parser.add_argument('keywords', nargs='+', help='Keywords to search for')
    parser.add_argument('--dir', default='user_analyses_md', 
                       help='Directory containing markdown files (default: user_analyses_md)')
    parser.add_argument('--window', type=int, default=100,
                       help='Proximity window size in characters (default: 100)')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"Error: Directory '{args.dir}' not found.")
        return
    
    print(f"Searching for keywords: {', '.join(args.keywords)}")
    print(f"In directory: {os.path.abspath(args.dir)}")
    print(f"Proximity window: {args.window} characters")
    print("-" * 80)
    
    results = find_keyword_proximity(args.dir, args.keywords, args.window)
    
    if results:
        print_results(results, args.dir)
        print(f"\nFound {sum(len(v) for v in results.values())} total matches across {len(results)} files.")
    else:
        print("No proximity matches found.")

if __name__ == "__main__":
    main()
