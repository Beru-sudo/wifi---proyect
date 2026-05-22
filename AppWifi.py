from flask import Flask, render_template

app = Flask(__name__)

# DATOS DEL WIFI
WIFI_NAME = "ECONOFIBRA_ROCIO"
WIFI_PASSWORD = "##10821082"

# PAGINA PRINCIPAL
@app.route("/")
def home():
    return render_template(
        "index.html",
        wifi_name=WIFI_NAME,
        wifi_password=WIFI_PASSWORD
    )

# EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)