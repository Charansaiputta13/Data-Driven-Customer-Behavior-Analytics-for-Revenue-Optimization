import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os
from src.data_loader import get_data
from src.analytics import calculate_kpis, get_revenue_by_category

class PDFReport(FPDF):
    def header(self):
        # Logo placeholder (if you had one)
        # self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Customer Behavior Analytics Report', 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 5, body)
        self.ln()

def generate_charts(df):
    """Generates and saves charts for the report."""
    if not os.path.exists('temp_charts'):
        os.makedirs('temp_charts')
    
    # Chart 1: Revenue by Category
    plt.figure(figsize=(10, 6))
    rev_by_cat = get_revenue_by_category(df).sort_values(ascending=True)
    rev_by_cat.plot(kind='barh', color='#F63366')
    plt.title('Total Revenue by Product Category')
    plt.xlabel('Revenue (USD)')
    plt.tight_layout()
    plt.savefig('temp_charts/revenue_by_category.png')
    plt.close()

    # Chart 2: Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=20, kde=True, color='#F63366')
    plt.title('Customer Age Distribution')
    plt.tight_layout()
    plt.savefig('temp_charts/age_distribution.png')
    plt.close()

def create_pdf_report():
    df = get_data()
    kpis = calculate_kpis(df)
    generate_charts(df)

    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Title Page
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 40, 'Executive Insights Report', 0, 1, 'C')
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, 'Data-Driven Customer Behavior Analytics', 0, 1, 'C')
    pdf.ln(20)
    
    # Executive Summary (KPIs)
    pdf.chapter_title('Executive Summary')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Total Revenue: ${kpis['Total Revenue']:,.2f}", 0, 1)
    pdf.cell(0, 10, f"Average Purchase Value: ${kpis['Avg Purchase Value']:.2f}", 0, 1)
    pdf.cell(0, 10, f"Total Customers: {kpis['Total Customers']:,}", 0, 1)
    pdf.cell(0, 10, f"Average Customer Rating: {kpis['Avg Rating']:.2f}", 0, 1)
    pdf.ln(10)

    # Visual Insights
    pdf.chapter_title('Visual Insights')
    pdf.chapter_body("The following charts provide a visual breakdown of revenue sources and customer demographics.")
    
    pdf.image('temp_charts/revenue_by_category.png', x=10, w=180)
    pdf.ln(5)
    pdf.chapter_body("Figure 1: Revenue distribution across different product categories. Identify high-performing sectors.")
    
    pdf.add_page()
    pdf.image('temp_charts/age_distribution.png', x=10, w=180)
    pdf.ln(5)
    pdf.chapter_body("Figure 2: Distribution of customer ages. This helps in targeting marketing campaigns to the right demographic.")

    # Recommendations
    pdf.add_page()
    pdf.chapter_title('Strategic Recommendations')
    recommendations = """
    1. Focus marketing efforts on high-revenue categories identified in Figure 1.
    2. Tailor campaigns to the dominant age groups shown in Figure 2.
    3. Leverage the Market Basket Analysis (available in the dashboard) to create bundle offers.
    4. Implement loyalty programs for high-CLV customers to maximize retention.
    """
    pdf.chapter_body(recommendations)

    pdf.output('Premium_Customer_Insights_Report.pdf', 'F')
    print("PDF Report Generated Successfully!")

if __name__ == "__main__":
    create_pdf_report()
