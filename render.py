import markdown
import sys

def markdown_to_html(md_filepath, html_filepath):
    # Read the Markdown file
    with open(md_filepath, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML output to a file
    with open(html_filepath, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Example usage: python script.py README.md output.html
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_markdown_file> <output_html_file>")
        sys.exit(1)

    md_filepath = sys.argv[1]
    html_filepath = sys.argv[2]
    markdown_to_html(README.md, render.html)
