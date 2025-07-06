import pyodbc  # Libreria per la connessione ODBC a SQL Server

# PARAMETRI DI CONNESSIONE
# Qui dovrai inserire i parametri per connetterti al tuo database locale
# Puoi prendere i valori dal README:
# - Server: MSSQLSERVER
# - Database: 123
# - Driver: ODBC Driver 18 for SQL Server (o quello che hai installato)

SERVER = 'localhost'  # Aggiornato per riflettere la connessione SSMS
DATABASE = '123'        # <--- Inserisci qui il nome del database
DRIVER = 'ODBC Driver 18 for SQL Server'  # <--- Verifica che il driver sia corretto

# STRINGA DI CONNESSIONE
# Qui costruisci la stringa di connessione usando i parametri sopra
# Puoi aggiungere altri parametri come autenticazione, TrustServerCertificate, ecc.
CONNECTION_STRING = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"

# FUNZIONE PER OTTENERE UNA CONNESSIONE
# Questa funzione restituirà una connessione attiva al database
# Puoi usarla in tutte le funzioni che devono interrogare il database

def get_db_connection():
    """
    Restituisce una nuova connessione al database.
    TODO: Puoi aggiungere qui eventuale gestione degli errori o log.
    """
    try:
        return pyodbc.connect(CONNECTION_STRING)
    except Exception as e:
        print(f"Errore di connessione al database: {e}")
        raise

# --- FUNZIONE DI TEST TEMPORANEA ---
# Puoi eseguire questo file direttamente per testare la connessione
if __name__ == "__main__":
    try:
        conn = get_db_connection()
        print("Connessione al database riuscita!")
        conn.close()
    except Exception as e:
        print(f"Errore di connessione al database: {e}")

# Ricordati di rimuovere o commentare questa parte dopo il test!

