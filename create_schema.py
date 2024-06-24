import psycopg2

try:
    conn = psycopg2.connect(
        dbname="hochschule_db",
        user="hochschule_user",
        password="password",
        host="localhost",
        port="5432"
    )
except:
    print("Couldn't connect to the database")


cur = conn.cursor()

cur.execute("CREATE SCHEMA IF NOT EXISTS public;")

# Define the schema

create_hochschule_table = """
CREATE TABLE IF NOT EXISTS public.Hochschule (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    JahrGr INTEGER,
    AnzahlStud INTEGER,
    PromR BOOLEAN,
    HabR BOOLEAN,
    Traegerschaft VARCHAR(255),
    Bundesland VARCHAR(255),
    Hochschultyp VARCHAR(255)
);
"""

create_ort_table = """
CREATE TABLE IF NOT EXISTS public.Ort (
    OrtID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    EinwohnerM INTEGER,
    EinwohnerW INTEGER,
    EinwohnerIns INTEGER
);
"""

create_adresse_table = """
CREATE TABLE IF NOT EXISTS public.Adresse (
    HID INTEGER REFERENCES public.Hochschule(ID),
    OrtID INTEGER REFERENCES public.Ort(OrtID),
    Strasse VARCHAR(255),
    Hausnr VARCHAR(50),
    PLZ VARCHAR(20),
    PRIMARY KEY (HID, OrtID)
);
"""

cur.execute(create_hochschule_table)
cur.execute(create_ort_table)
cur.execute(create_adresse_table)

conn.commit()

cur.close()
conn.close()

print("Created schema if it did not already exist")