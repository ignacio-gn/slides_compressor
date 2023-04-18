import PyPDF2
import helpers as lib

if __name__ == '__main__':
    sourcefile = open(lib.get_input("Enter path to the source file: "), "rb")
    reader = PyPDF2.PdfReader(sourcefile)
    writer = PyPDF2.PdfWriter()

    # Read pages
    for page_nr in range(len(reader.pages)-1):
        page = reader.pages[page_nr]
        content_local = page.extract_text()
        content_next = reader.pages[page_nr + 1].extract_text()
        if lib.is_contained(content_local, content_next):
            print(f"Equivalent content found at page {page_nr}")
        else:
            writer.add_page(page)
    writer.add_page(reader.pages[-1])

    writer.write(lib.get_input("Enter output path: "))
