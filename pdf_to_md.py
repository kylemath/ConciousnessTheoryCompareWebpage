#!/usr/bin/env python3
"""
Convert PDF to Markdown using PyMuPDF
"""
import fitz  # PyMuPDF
import sys

def pdf_to_markdown(pdf_path, output_path):
    """Convert PDF file to Markdown format"""
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Extract markdown content from all pages
        markdown_content = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            # Get markdown content from the page
            # This preserves formatting, tables, headings, etc.
            markdown_text = page.get_markdown()
            
            # Add page separator (optional, helps identify page breaks)
            if page_num > 0:
                markdown_content.append("\n---\n")
            
            markdown_content.append(markdown_text)
        
        # Join all pages
        full_markdown = "\n".join(markdown_content)
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_markdown)
        
        print(f"Successfully converted {pdf_path} to {output_path}")
        print(f"Total pages: {len(doc)}")
        
        doc.close()
        return True
        
    except Exception as e:
        print(f"Error converting PDF: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    pdf_file = "1.pdf"
    md_file = "1.md"
    
    pdf_to_markdown(pdf_file, md_file)

