from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Поиск продукта</title>
<h2>Введите название продукта:</h2>
<form action="/search" method="post">
  <input type="text" name="query" placeholder="Например, iPhone 15">
  <input type="submit" value="Сгенерировать ссылку">
</form>
{% if link %}
  <p>Вот ваша ссылка: <a href="{{ link }}" target="_blank">{{ link }}</a></p>
{% endif %}
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML)

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    if not query.strip():
        return redirect("/")
    search_link = "https://www.google.com/search?q=" + "+".join(query.strip().split())
    return render_template_string(HTML, link=search_link)

if __name__ == "__main__":
    app.run(debug=True)

