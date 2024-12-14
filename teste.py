import pandas as pd

# Preencher a matriz com o texto "EJC-PMJP" e números de 1 a 300
num = 1
vet = []
for i in range(30):
    linha = []
    for j in range(10):
        linha.append(f"EJC-PMJP<br><br><strong style='font-size: 30px;'>{num}<strong/>")
        num += 1
    vet.append(linha)

df = pd.DataFrame(vet)

# Convert DataFrame to HTML with CSS for cell width and height
html = df.to_html(index=False, header=None, escape=False)

# Add CSS for cell width and height and ensure print styles
html_with_style = f"""
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    td {{
        width: 3cm;
        height: 3cm;
        border: 0px solid black;
        text-align: center;
        vertical-align: middle;
    }}
    @media print {{
        body {{
            margin: 0;
        }}
        table, tr, td {{
            page-break-inside: avoid;
        }}
    }}
</style>
{html}
"""

# Save HTML content to a file
with open("rifa.html", "w") as file:
    file.write(html_with_style)
