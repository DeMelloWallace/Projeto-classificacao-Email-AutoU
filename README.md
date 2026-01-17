# Classificação Inteligente de Emails com IA

Aplicação web desenvolvida em **Python (Flask)** que utiliza **Inteligência Artificial** para classificar emails e sugerir respostas automáticas, com o objetivo de reduzir o trabalho manual de equipes que lidam com alto volume de mensagens diariamente.

---

## Objetivo do Projeto

Este projeto foi desenvolvido como **desafio técnico para um processo seletivo**, simulando um cenário real de uma **empresa do setor financeiro** que recebe milhares de emails por dia.

A solução busca:

- Classificar emails como **Produtivos** ou **Improdutivos**
- Sugerir respostas automáticas adequadas
- Automatizar tarefas repetitivas
- Liberar tempo da equipe para atividades estratégicas

---

##  Categorias de Classificação

| Categoria     | Descrição |
|--------------|----------|
| **Produtivo** | Emails que exigem ação ou resposta (ex: solicitações, dúvidas, status de requisição) |
| **Improdutivo** | Emails sem necessidade de ação imediata (ex: agradecimentos, felicitações) |

---

## Funcionalidades

- Upload de arquivos `.txt` ou `.pdf`
- Inserção direta de texto do email
- Processamento de linguagem natural (NLP)
- Classificação automática via IA
- Geração de resposta automática
- Fallback local em caso de falha da API
- Interface web simples e intuitiva

---

## Tecnologias Utilizadas

### Backend
- Python 3
- Flask
- NLTK (Processamento de Linguagem Natural)
- OpenAI API (Classificação e geração de resposta)
- Gunicorn

### Frontend
- HTML5
- CSS3
- Bootstrap

### Infraestrutura
- Render.com (Deploy)
- GitHub

---

Observações Importantes

Limites de cota da OpenAI podem causar falhas se excedidos.
Em caso de erro da API, a aplicação retorna respostas simuladas (fallback).
Ideal para testes rápidos sem necessidade de criar conta na OpenAI.

---

## Arquitetura do Projeto

```text
Projeto-classificacao-Email-AutoU/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── routes/
│   └── email_routes.py
│
├── services/
│   ├── file_reader.py
│   ├── nlp_processor.py
│   └── ai_service.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
