import pandas as pd
import re


def get_brand(product_name):
    if pd.isna(product_name):
        return "Unknown"
    text = str(product_name).lower()
    brands = ['aorus','asus','apple','gigabyte','hp','acer','msi','altyk']
    found_brand = None
    for brand in brands:
        if brand in text:
            return brand
    return 'Other'

def get_CPU(product_name):

    if pd.isna(product_name):
        return "Unknown"
    text = str(product_name).upper()
    
    match_intel_ultra = re.search(r'CORE\s*ULTRA\s*(\d+)',text)
    if match_intel_ultra:
        tier = match_intel_ultra.group(1)
        return f"Intel Core Ultra {tier}"
    
    match_intel_core = re.search(r'CORE\s*(?:I|\s)*(\d+)', text)
    if match_intel_core:
        tier = match_intel_core.group(1)
        return f"Intel Core i{tier}"


    match_amd_ai = re.search(r'RYZEN\s*AI\s*(\d+)',text)
    if match_amd_ai:
        tier = match_amd_ai.group(1)
        return f"AMD Ryzen AI {tier}"

    match_amd = re.search(r'RYZEN\s*(\d+)',text)
    if match_amd:
        tier = match_amd.group(1)
        return f"AMD Ryzen {tier}"
    
    
    if 'APPLE' in text or 'MACBOOK' in text:
        match_apple = re.search(r'\bM(\d+)', text) 
        if match_apple:
            return f"Apple M{match_apple.group(1)}"
        
    return 'Other'

def get_RAM(product_name):
    if pd.isna(product_name):
        return "Unknown"
    text = str(product_name).upper()

    match = re.search(r'RAM\s*(\d+)\s*GO',text)
    if match:
        tier = int(match.group(1))
        return tier
    return 'Other'
    
def get_ssd(product_name):
    if pd.isna(product_name):
        return "Unknown"
    text = str(product_name).upper()

    pattern = r'SSD\s*(\d+)\s*(GO|TO)'
    match = re.search(pattern,text)
    try:
            num = int(match.group(1)) 
            unit = match.group(2)    
            
            if unit in ['TO', 'TB']:
                return num * 1024
            else:
                return num 
    except:
            return 'other'
            
    return 'other'


#Create new columns in the CSV file.
df = pd.read_csv('D:/Full projet/laptop-price-intelligence/data/laptops_processed.csv')
df['Brand'] = df['Name'].apply(get_brand)
df['CPU_Type'] = df['Detail'].apply(get_CPU)
df['RAM_GB'] = df['Detail'].apply(get_RAM)
df['SSD_GB'] = df['Detail'].apply(get_ssd)
print(df.head)

# Save data
df.to_csv('D:/Full projet/laptop-price-intelligence/data/laptops_final.csv', index=False, encoding='utf-8-sig')
print("The file was saved at: laptops_final.csv")

