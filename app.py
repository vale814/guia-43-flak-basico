from flask import Flask, render_template, request
app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar_persona", methods=["POST"])
def agregar_persona():
    if (request.method=='POST'):
        documento=request.form['documento']
        nombre=request.form['nombre']
        edad=request.form['edad']
        
        personaIngresada={
            "documento":documento,
            "nombre":nombre,
            "edad":edad,
        }
        
        datos="\n<<<<DATOS>>>>\n"
        datos+=f"Documento: {documento}\n"
        datos+=f"Nombre: {nombre}\n"
        datos+=f"Edad: {edad}\n"
        print(datos)

        return render_template('index.html', data=personaIngresada)
   

if __name__ == "__main__":
    app.run(debug=True, port=5000)