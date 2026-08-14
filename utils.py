import json 

def load_data(arquivo):
    caminho_completo = open(f"static/data/{arquivo}" , "r")
    return json.load(caminho_completo)

def load_template(arquivo): 
    return  (open(f"static/templates/{arquivo}" , "r")).read()

    
