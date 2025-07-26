# Medicine Suggestion App

This is a Streamlit-based AI assistant that suggests **safe, over-the-counter (OTC)** medications for **common minor ailments** (like fever, headache, etc.). It uses Google Generative AI + LangGraph + Pipedream tools.

> ⚠️ This app is for educational purposes only and **does not replace medical advice**.

## Features
- 💊 Suggests medicine based on symptom, age, weight, comorbidities
- 🚫 Avoids unsafe/prescription drugs
- 🛑 Alerts for red-flag symptoms
- 🤖 Powered by LangChain, LangGraph, and Gemini

## Setup

```bash
git clone <repo-url>
cd medical-mcp
python -m venv venv
venv\Scripts\activate     # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
