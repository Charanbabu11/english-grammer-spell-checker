from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Spell correction route for text input
@app.route('/spell', methods=['POST'])
def spell():
    text = request.form.get('text')
    if text:
        corrected_text = spell_checker_module.correct_spell(text)
        corrected_grammar = spell_checker_module.correct_grammar(text)
        return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)
    return render_template('index.html', error="Please enter text for spell check.")

# Grammar correction route for file upload
@app.route('/grammar', methods=['POST'])
def grammar():
    file = request.files.get('file')
    if file:
        readable_file = file.read().decode('utf-8', errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        corrected_file_grammar = spell_checker_module.correct_grammar(readable_file)
        return render_template(
            'index.html', 
            corrected_file_text=corrected_file_text, 
            corrected_file_grammar=corrected_file_grammar
        )
    return render_template('index.html', error="Please upload a file for grammar check.")

# Main function
if __name__ == "__main__":
    app.run(debug=True)
