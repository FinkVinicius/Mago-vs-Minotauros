import datetime
import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
       self.db_name = db_name
       self.conect = sqlite3.connect(db_name)
       self.conect.execute('''
                            CREATE TABLE IF NOT EXISTS dados(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL)        
                           ''')
    
    # REMOVA o @staticmethod. Use 'self' para acessar o 'self.conect'
    def save(self, name, score):
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        dados_para_salvar = {
            'name': name, 
            'score': score, 
            'date': data_atual
        }
        # Agora o self.conect funciona porque o save pertence à instância
        self.conect.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', dados_para_salvar)
        self.conect.commit()

    def consulta(self) -> list:
        return self.conect.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()
    
    def close(self):
        self.conect.close()