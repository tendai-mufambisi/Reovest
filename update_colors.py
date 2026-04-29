#!/usr/bin/env python3
import os

files_to_update = ['3DPlans.html', 'townplanning.html']

for filename in files_to_update:
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace colors
        content = content.replace('#0A2342', '#000000')
        content = content.replace('#FFB300', '#FFFFFF')
        content = content.replace('#1C3D6A', '#333333')
        content = content.replace('#FFE194', '#F5F5F5')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"{filename} colors updated successfully")
    else:
        print(f"{filename} not found")
