from utils import load_data, load_template
import json
import sqlite3

def index():

    note_template = load_template('components/note.html')
    
    notes_li = [

        note_template.format(id = i, title=title, details=content)
        for i ,title , content in load_data()
    ]


    notes = '\n'.join(notes_li)
    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (titulo, detalhes)
    )

    conexao.commit()
    conexao.close()
    
        

    

