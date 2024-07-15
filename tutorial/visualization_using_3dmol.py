def generate_html_with_3dmol(pdb_data):
    js_code = f'''
    <html>
    <head>
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <div id="viewer" style="width: 800px; height: 600px;"></div>
        <script>
            var pdb_data = `
{pdb_data}
            `;
            var viewer = $3Dmol.createViewer($('#viewer'));
            viewer.addModel(pdb_data, 'pdb');
            viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
            viewer.zoomTo();
            viewer.render();
        </script>
    </body>
    </html>
    '''
    return js_code

pdb_data = '''
ATOM      1  N   ALA A   1       5.564  29.130  14.207  1.00 13.77           N
ATOM      2  CA  ALA A   1       4.647  28.033  14.588  1.00 12.67           C
ATOM      3  C   ALA A   1       5.087  26.677  14.069  1.00 12.31           C
ATOM      4  O   ALA A   1       6.073  26.627  13.345  1.00 12.38           O
ATOM      5  CB  ALA A   1       4.739  27.792  16.091  1.00 12.60           C
ATOM      6  N   CYS A   2       4.356  25.599  14.498  1.00 11.63           N
ATOM      7  CA  CYS A   2       4.624  24.269  14.073  1.00 11.65           C
ATOM      8  C   CYS A   2       5.701  24.186  12.997  1.00 11.46           C
ATOM      9  O   CYS A   2       5.729  23.141  12.356  1.00 11.75           O
ATOM     10  CB  CYS A   2       3.302  23.608  13.743  1.00 11.79           C
ATOM     11  SG  CYS A   2       1.965  23.896  15.032  1.00 12.29           S
'''

with open('mol_viewer.html', 'w') as f:
    html_content = generate_html_with_3dmol(pdb_data.strip())
    f.write(html_content)
