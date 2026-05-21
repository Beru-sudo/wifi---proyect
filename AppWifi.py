from flask import Flask, render_template
import qrcode

app = Flask(__name__)

# DATOS DEL WIFI
WIFI_NAME = "ECONOFIBRA_ROCIO"
WIFI_PASSWORD = "##10821082"

# FORMATO WIFI QR
wifi_data = f"WIFI:T:WPA;S:{WIFI_NAME};P:{WIFI_PASSWORD};;"

# GENERAR QR
qr = qrcode.make(wifi_data)
qr.save("static/wifi_qr.png")

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