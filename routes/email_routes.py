from flask import Blueprint, render_template, request
from services.file_reader import read_file
from services.nlp_processor import preprocess_text
from services.ai_service import classify_and_generate_response

email_bp = Blueprint("email_bp", __name__)

@email_bp.route("/", methods=["GET", "POST"])
def index():
    categoria = None
    resposta = None
    texto_email = None

    arquivo = None  # ✅

    if request.method == "POST":
        texto_email = request.form.get("email_text")

        if "arquivo" in request.files and request.files["arquivo"].filename != "":
            arquivo = request.files["arquivo"]
            texto_email = read_file(arquivo)

        if texto_email:
            texto_processado = preprocess_text(texto_email)
            categoria, resposta = classify_and_generate_response(texto_processado)

    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta,
        texto_email=texto_email
    )
