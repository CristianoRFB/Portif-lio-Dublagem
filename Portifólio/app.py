from flask import Flask, render_template
app = Flask(__name__)

dublagens = [
    {
        "personagem": "Makoto Naegi",
        "obra": "Danganronpa",
        "data": "2025-05-01",
        "link": "https://drive.google.com/file/d/19LZqqdwna7MaQdmPszZ5CHw5LmQfqQ9u/view",
        "thumb": "https://drive.google.com/thumbnail?id=19LZqqdwna7MaQdmPszZ5CHw5LmQfqQ9u"
    },
    {
        "personagem": "Personagem B",
        "obra": "Naruto",
        "data": "2025-01-20",
        "link": "https://drive.google.com/...",
        "thumb": "https://via.placeholder.com/200x150"
    }
]

@app.route("/dublagens")
def dublagens_view():
    return render_template("dublagens.html", dublagens=dublagens)

# ESTA PARTE FAZ O FLASK RODAR
if __name__ == "__main__":
    app.run(debug=True)
