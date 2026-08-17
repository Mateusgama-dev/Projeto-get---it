import json 
import sqlite3

def load_data():

    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM note")
    dados = cursor.fetchall()

    conexao.close()
    return dados

def load_template(arquivo): 
    return  (open(f"static/templates/{arquivo}" , "r")).read()

    
def init_db():

    conexao = sqlite3.connect("banco.db")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()
