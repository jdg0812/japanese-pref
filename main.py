from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    # Example: Read an Excel file or some other data to determine the color
    df = pd.read_excel('Untitled spreadsheet.xlsx')

    # Logic to decide the color (e.g., if ID is 'yes', set color to red)
    visited = df[df['HAVE_BEEN'] == 'YES']['ID'].tolist()
    # Convert the dataframe to a dictionary
    id_title_map = df.set_index('ID')['TITLE'].to_dict()

    return render_template('index.html', visited=visited, id_title_map=id_title_map)


if __name__ == '__main__':
    app.run(debug=True)