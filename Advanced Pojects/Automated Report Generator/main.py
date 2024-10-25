# This project generates reports in PDF format from provided data.
# Implement the code here

import os
from fpdf import FPDF

def create_report(report_data, report_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in report_data:
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(report_file)

if __name__ == "__main__":
    report_data = ["Report Title", "Data point 1", "Data point 2", "Conclusion"]
    report_file = "report.pdf"
    create_report(report_data, report_file)
    print(f"Report generated: {report_file}")
