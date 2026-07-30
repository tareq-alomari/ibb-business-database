#!/usr/bin/env python3
"""Generate 22-phase analysis files for 10 sub-sectors in Ibb Governorate."""
import os

BASE = "/home/tareq/cs/projects/idea analysis/IBB/ibb-business-database/التحليلات"

SECTORS = [
    "الترجمة", "التسويق_الرقمي", "التصميم", "التصوير", "التطريز",
    "التكييف", "التنظيف", "الجمعيات_الخيرية", "الحدائق", "الحدادة",
]

PHASES = [
    "01_Project_Discovery", "02_Research", "03_Business_Analysis",
    "04_Market_Analysis", "05_Competitor_Analysis", "06_Stakeholders",
    "07_User_Research", "08_Functional_Analysis", "09_Non_Functional_Requirements",
    "10_Information_Architecture", "11_UX", "12_UI_Design",
    "13_Database_Design", "14_API_Design", "15_Software_Architecture",
    "16_Technical_Stack", "17_Security", "18_SEO", "19_Dashboard",
    "20_Project_Planning", "21_Documentation", "22_Final_Deliverables",
]

PHASE_NAMES_AR = [
    "Project Discovery", "Research", "Business Analysis",
    "Market Analysis", "Competitor Analysis", "Stakeholders",
    "User Research", "Functional Analysis", "Non-Functional Requirements",
    "Information Architecture", "UX", "UI Design",
    "Database Design", "API Design", "Software Architecture",
    "Technical Stack", "Security", "SEO", "Dashboard",
    "Project Planning", "Documentation", "Final Deliverables",
]

PHASE_NUMS = [
    "الأولى", "الثانية", "الثالثة", "الرابعة", "الخامسة",
    "السادسة", "السابعة", "الثامنة", "التاسعة", "العاشرة",
    "الحادية عشرة", "الثانية عشرة", "الثالثة عشرة", "الرابعة عشرة",
    "الخامسة عشرة", "السادسة عشرة", "السابعة عشرة", "الثامنة عشرة",
    "التاسعة عشرة", "العشرون", "الحادية والعشرون", "الثانية والعشرون",
]

# Import sector data from module
import importlib.util
spec = importlib.util.spec_from_file_location("sector_data", os.path.join(os.path.dirname(__file__), "sector_data.py"))
sector_data = importlib.util.module_from_spec(spec)

def main():
    # We need to dynamically load the data
    exec(open(os.path.join(os.path.dirname(__file__), "sector_data.py")).read(), sector_data.__dict__)
    
    total_files = 0
    total_lines = 0
    
    for sector in SECTORS:
        sector_dir = os.path.join(BASE, sector)
        if not os.path.isdir(sector_dir):
            print(f"⚠ Skipping {sector}: directory not found")
            continue
        
        meta = sector_data.SECTOR_META[sector]
        sector_files = 0
        sector_lines = 0
        
        for idx, phase in enumerate(PHASES):
            phase_dir = os.path.join(sector_dir, phase)
            os.makedirs(phase_dir, exist_ok=True)
            
            content = generate_phase_content(sector, meta, idx)
            
            filepath = os.path.join(phase_dir, f"{phase}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            lines = content.count("\n") + 1
            total_files += 1
            total_lines += lines
            sector_files += 1
            sector_lines += lines
        
        print(f"  ✓ {sector}: {sector_files} files, {sector_lines} lines")
    
    print(f"\n{'='*60}")
    print(f"Total: {total_files} files, {total_lines} lines")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
