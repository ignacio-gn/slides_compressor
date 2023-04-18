# Slides Compressor
*Remove superfluous slides in PDF presentations with multiple pages per slide*

## Description
This python based tool is used to compress presentations exported as PDFs, where many pages might represent a single slide. Often it is the case that slide n+1 contains the same text and elements as slide n, but adds a new article/image/element. With this tool, the slide n would be removed. That way, the output PDF contains no redundat information and less slides.

## Dependencies
- Python 3.11.0 or later
- PyPDF2 3.0.1

## Usage
Execute the main file and follow the instructions. This tool accesses the filesystem through user input.

