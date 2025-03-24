from flask import Flask, render_template, request
import random

app = Flask(__name__)
gizli_sayi = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def tahmin_oyunu():
    global gizli_sayi
    mesaj = None
    tahmin = None

    if request.method == "POST":
        try:
            tahmin = int(request.form.get("tahmin"))
            if tahmin < gizli_sayi:
                mesaj = {"text": f"{tahmin} sayısı, tuttuğum sayıdan düşük! Daha yüksek bir sayı deneyin.", "color": "red"}
            elif tahmin > gizli_sayi:
                mesaj = {"text": f"{tahmin} sayısı, tuttuğum sayıdan yüksek! Daha düşük bir sayı deneyin.", "color": "red"}
            else:
                mesaj = {"text": "Tebrikler! Doğru tahmin ettiniz. 🎉", "color": "green"}
                gizli_sayi = random.randint(1, 100)  # Yeni sayı belirleniyor.
        except ValueError:
            mesaj = {"text": "Lütfen geçerli bir sayı girin!", "color": "red"}

    return render_template("index.html", mesaj=mesaj)

if __name__ == "__main__":
    app.run(debug=True)
