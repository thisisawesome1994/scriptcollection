from flask import Flask, request, render_template

app = Flask(__name__)

# Gemiddelde aminozuurinhoud in 100g vlees (in mg)
amino_acid_content_per_100g = {
    'beef': {
        'Histidine': 1000,
        'Isoleucine': 1400,
        'Leucine': 2700,
        'Lysine': 2600,
        'Methionine + Cysteine': 1300,
        'Phenylalanine + Tyrosine': 2200,
        'Threonine': 1200,
        'Tryptophan': 300,
        'Valine': 1800
    },
    'chicken': {
        'Histidine': 850,
        'Isoleucine': 1500,
        'Leucine': 2500,
        'Lysine': 3000,
        'Methionine + Cysteine': 1200,
        'Phenylalanine + Tyrosine': 2000,
        'Threonine': 1100,
        'Tryptophan': 250,
        'Valine': 1600
    }
}

# Essentiële aminozuren per kg lichaamsgewicht (in mg)
essential_amino_acids_per_kg = {
    'Histidine': 10,
    'Isoleucine': 20,
    'Leucine': 39,
    'Lysine': 30,
    'Methionine + Cysteine': 15,
    'Phenylalanine + Tyrosine': 25,
    'Threonine': 15,
    'Tryptophan': 4,
    'Valine': 26
}

def calculate_meat_needed(weight, meat_type):
    total_meat_needed = 0
    for amino_acid, daily_need_per_kg in essential_amino_acids_per_kg.items():
        daily_need = daily_need_per_kg * weight  # in mg
        meat_needed_for_amino_acid = daily_need / (amino_acid_content_per_100g[meat_type][amino_acid] / 100)  # in grams
        if meat_needed_for_amino_acid > total_meat_needed:
            total_meat_needed = meat_needed_for_amino_acid
    return total_meat_needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        beef_needed = calculate_meat_needed(weight, 'beef')
        chicken_needed = calculate_meat_needed(weight, 'chicken')
        return render_template('index.html', beef_needed=beef_needed, chicken_needed=chicken_needed)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9026, debug=False)