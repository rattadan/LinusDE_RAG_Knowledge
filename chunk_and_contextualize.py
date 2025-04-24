import os
import re
import requests
from pathlib import Path

def split_into_chunks(text, chunk_size=5, overlap=2):
    # Split text into sentences using regex
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    i = 0
    while i < len(sentences):
        chunk = sentences[i:i+chunk_size]
        if len(chunk) < chunk_size:
            break
        chunks.append(' '.join(chunk))
        i += chunk_size - overlap
    return chunks

def query_ollama(chunk, model="llama3.2:1b", host="http://localhost:11434"):
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": chunk,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except Exception as e:
        print(f"Error querying Ollama: {e}")
        return "[Error from LLM]"

def save_markdown(chunk, llm_output, out_dir, idx):
    md_content = f"## Chunk {idx+1}\n\n**Original Text:**\n\n{chunk}\n\n---\n\n**LLM Contextual Output:**\n\n{llm_output}\n"
    out_path = os.path.join(out_dir, f"chunk_{idx+1}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)

def main(txt_path, out_dir):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = split_into_chunks(text)
    for idx, chunk in enumerate(chunks):
        llm_output = query_ollama(chunk)
        save_markdown(chunk, llm_output, out_dir, idx)
    print(f"Processed {len(chunks)} chunks. Markdown files saved to {out_dir}.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chunk .txt file and contextualize with Ollama LLM.")
    parser.add_argument("txt_path", help="Path to the input .txt file.")
    parser.add_argument("out_dir", help="Directory to save .md files.")
    args = parser.parse_args()
    main(args.txt_path, args.out_dir)
