from flask import Flask, render_template, request

app = Flask(__name__)

def get_companies(date):
    print(f"Date: {date}")
    # This is a placeholder. Implement the actual logic or method call here.
    return ["Company1", "Company2", "Company3"]  # Example response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        event = request.form['event']
        date = request.form['date']
        names = get_companies(date)
        return render_template('response.html', names=names, event=event)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
