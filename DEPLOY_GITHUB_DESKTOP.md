# Publicera Processkartan via GitHub Desktop + Streamlit Community Cloud

## 1. Lägg projektet i GitHub Desktop
1. Packa upp ZIP-filen `Processkartan_GitHub_v0.1.zip`.
2. Öppna GitHub Desktop.
3. Välj **File > Add local repository**.
4. Om GitHub Desktop säger att mappen inte är ett Git-repository, välj **create a repository** i samma mapp.
5. Repository name: `processkartan`.
6. Gör första commit, exempelvis `Initial Processkartan Streamlit prototype`.
7. Klicka **Publish repository**.

## 2. Publicera till Streamlit Community Cloud
1. Gå till Streamlit Community Cloud och logga in med GitHub.
2. Välj **Create app**.
3. Repository: ditt GitHub-konto / `processkartan`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Önskat appnamn: `processkartan` om namnet är ledigt.
7. Deploy.

Därefter får appen normalt en adress i stil med:
`https://processkartan.streamlit.app`

Den exakta adressen kan inte fastställas förrän Streamlit har accepterat appnamnet och deploymenten är skapad.

## 3. Arbetsflöde efteråt
När kod uppdateras:
1. Ersätt/uppdatera filerna lokalt.
2. Kontrollera ändringarna i GitHub Desktop.
3. Commit.
4. Push origin.
5. Streamlit bygger om appen automatiskt från GitHub.
