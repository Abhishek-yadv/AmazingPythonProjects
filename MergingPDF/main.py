# Create a Sample Pdf file
num_of_pdf = int(input("Enter numer of pdf you want: "))
while num_of_pdf > 0:
    import faker
    import fpdf
    def create_pdf(filename):
        fake = faker.Faker()
        text = fake.text(1000)
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        return pdf.output(filename+".pdf")
    my_file_name = input("Input your pdf file name:")
    create_pdf(my_file_name)
    num_of_pdf -=1
print("Done!")


import PyPDF2
def merge_pdfs(pdf_paths, output_pdf):
    merger = PyPDF2.PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(pdf_path)
    merger.write(output_pdf)

if __name__ == "__main__":
    # List your PDF paths to merge
    pdf_paths = [r"D:\PythonProject\pdf1.pdf", r"D:\PythonProject\pdf2.pdf"] #put your file path
    output_pdf = "merged_pdf.pdf"  # Output PDF file name
    merge_pdfs(pdf_paths, output_pdf)


