from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def web():

    return render_template('first_task.html')

@app.route('/process', methods=['POST'])
def process():
    string1 = request.form['word_for_reverse']
    string2 = request.form['word_for_uppercase']

    reverse_result = string1[::-1]
    uppercase_result = string2.upper()

    return render_template('first_task.html', reverse_result=reverse_result, uppercase_result=uppercase_result)
    
if __name__ == '__main__':
    app.run(debug=True)
