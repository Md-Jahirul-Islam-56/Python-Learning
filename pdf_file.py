import PyPDF2

#___________________READING_________________

# Open the PDF file in binary mode:

# with open('L.pdf', 'rb') as pdf_file:
#     # Create a PDF reader object
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     # Get the total number of pages
#     num_pages = len(pdf_reader.pages)
    
#     # Extract text from the first page
#     page = pdf_reader.pages[0]
#     text = page.extract_text()
    
#     print(text)


#___________________MERGING_________________


# # Create a PDF merger object
# merger = PyPDF2.PdfMerger()

# # Append the first PDF file
# with open("1.pdf", "rb") as pdf_file1:
#     merger.append(pdf_file1)

# # Append the second PDF file
# with open("2.pdf", "rb") as pdf_file2:
#     merger.append(pdf_file2)
# with open("3.pdf", "rb") as pdf_file3:
#     merger.append(pdf_file3)

# with open("4.pdf", "rb") as pdf_file4:
#     merger.append(pdf_file4)

# with open("5.pdf", "rb") as pdf_file5:
#     merger.append(pdf_file5)

# with open("6.pdf", "rb") as pdf_file6:
#     merger.append(pdf_file6)

# # Write the output to a new file
# with open("bl.pdf", "wb") as merged_file:
#     merger.write(merged_file)

# merger.close() #The merger object is different from regular file objects that are automatically closed when exiting a with block. So we should close it.


#____________SPLITTING PDF OR EXTRACTING PAGES_____________


# # Open the PDF
# with open('Course_Specification_EEE_2301_Spring_2024_MLH.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     # Create a PDF writer object
#     pdf_writer = PyPDF2.PdfWriter()

#     # Extract a specific page (e.g., page 2)
#     page = pdf_reader.pages[1]  # Index starts from 0
#     pdf_writer.add_page(page)
    
#     # Save the extracted page as a new PDF
#     with open('extracted_page.pdf', 'wb') as output_file:
#         pdf_writer.write(output_file)

#___________________ROTATING_________________

# Open the PDF in read-binary mode
# with open('extracted_page.pdf', 'rb') as pdf_file:
#     # Create a PDF reader object
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     # Get the page to rotate (e.g., the first page)
#     page = pdf_reader.pages[0]
    
#     # Rotate the page clockwise by 90 degrees (returns a new rotated page)
#     rotated_page = page.rotate(90)
    
#     # Create a PDF writer object and add the rotated page
#     pdf_writer = PyPDF2.PdfWriter()
#     pdf_writer.add_page(rotated_page)
    
#     # Save the rotated page as a new PDF
#     with open('rotated.pdf', 'wb') as output_file:
#         pdf_writer.write(output_file)

#___________________ADDING WATERMARK_________________

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.colors import Color

# # Create a PDF with a transparent watermark
# output = 'transparent_watermark.pdf'
# c = canvas.Canvas(output, pagesize=letter)
# width, height = letter

# # Set transparency
# c.setFillColor(Color(0, 0, 0, alpha=0.3))  # Black with 30% opacity

# # Draw the watermark
# c.setFont("Helvetica", 60)
# c.drawCentredString(width / 2, height / 2, "CONFIDENTIAL")

# # Save the PDF
# c.save()


# # Open the PDF and the watermark PDF in read-binary mode
# with open('merged.pdf', 'rb') as pdf_file, open('transparent_watermark.pdf', 'rb') as watermark_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     watermark_reader = PyPDF2.PdfReader(watermark_file)
    
#     # Get the watermark page (assuming it's a single-page PDF)
#     watermark_page = watermark_reader.pages[0]
    
#     # Create a PDF writer object
#     pdf_writer = PyPDF2.PdfWriter()
    
#     # Loop through each page in the PDF and apply the watermark
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         page.merge_page(watermark_page)  # Apply the watermark
#         pdf_writer.add_page(page)
    
#     # Save the watermarked PDF
#     with open('watermarked.pdf', 'wb') as output_file:
#         pdf_writer.write(output_file)



#  pymupdf,pdfminer ---> these modules can be used to extract pictures from the pdf
