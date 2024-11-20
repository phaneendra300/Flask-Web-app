from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            items.append(item)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    if request.method == 'POST':
        updated_item = request.form.get('item')
        if updated_item:
            items[index] = updated_item
        return redirect(url_for('index'))
    return render_template('update.html', item=items[index], index=index)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

