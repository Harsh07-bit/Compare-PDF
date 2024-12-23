import fitz  # PyMuPDF
import difflib


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text("text")  # Extract text from page
    return text


# Function to compare text of two PDFs
def compare_pdfs(pdf1_path, pdf2_path):
    # Extract text from both PDFs
    pdf1_text = extract_text_from_pdf(pdf1_path)
    pdf2_text = extract_text_from_pdf(pdf2_path)

    # Use difflib to compare texts
    diff = difflib.ndiff(pdf1_text.splitlines(), pdf2_text.splitlines())
    delta = '\n'.join(x for x in diff if x.startswith('+ ') or x.startswith('- '))

    if delta:
        print("Differences found:")
        print(delta)
    else:
        print("The PDFs are identical.")


# Get input PDF paths from the user
pdf1_path = input("Enter the path for the first PDF file: ")
pdf2_path = input("Enter the path for the second PDF file: ")

# Compare the two PDFs
compare_pdfs(pdf1_path, pdf2_path)
