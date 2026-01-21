from flask import Blueprint, render_template, request, flash
from services.file_reader import read_file
from services.nlp_processor import preprocess_text
from services.ai_service import classify_and_generate_response

email_bp = Blueprint("email_bp", __name__)

@email_bp.route("/", methods=["GET", "POST"])
def index():
    categoria = ""
    resposta = ""
    texto_processado = ""

    try:
        if request.method == "POST":
            texto = request.form.get("email_text", "")

            if "email_file" in request.files:
                arquivo = request.files["email_file"]
                if arquivo.filename != "":
                    texto = read_file(arquivo)

            texto_processado = preprocess_text(texto)

            categoria, resposta = classify_and_generate_response(texto_processado)

    except Exception as e:
        categoria = "Erro no processamento"
        resposta = (
            "Ocorreu um erro ao processar seu email. "
            "Verifique o texto ou tente novamente mais tarde."
        )
        print(f"[Erro no routes/email_routes] {str(e)}")

    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta,
        texto=texto_processado
    )
