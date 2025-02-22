# FREE-LLM-APIS  

**FREE-LLM-APIS** provides an easy and hassle-free way to access **Gemini Pro, OpenAI GPT-4, and DeepSeek**—without digging through intensive  documentation (because who has time for that?).  

⚡ **Note:** These are basic sample notebooks. For in-depth details, check the linked docs below.  

---

## Quick Setup Guide  

### 🔹 1. Install Dependencies & Set Up Virtual Environment  

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 🔹 2. Install Ollama for Local Models  

If you want to run models **locally**, install **Ollama** and pull the required models.  

```bash
pip install ollama
ollama pull <model_name>
```

Now you can use models like `deepseek-r1:8b`.  

🔗 **Useful guide:** [Running DeepSeek R1 Locally with Ollama & Docker](https://blog.xeynergy.com/running-deepseek-r1-locally-with-ollama-and-docker-9b2b7d05607a)  

---

### 🔹 3. Using Gemini API (Google AI)  

To access **Gemini Pro**, you’ll need an API key. If you don’t have one yet, grab it from **Google AI Studio**:  

🔗 [Get Your API Key](https://aistudio.google.com/app/apikey)  

📖 **Documentation:** [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs?_gl=1*c9jjq1*_ga*OTcwMTA3NzY1LjE3Mzg2ODYwNjY.*_ga_P1DBVKWT6V*MTc0MDIxMjcwOC43LjEuMTc0MDIxMzc5Mi42MC4wLjEwNTU3OTI0MTA.)  

---

### 🔹 4. Using OpenAI APIs (GPT-4 Turbo, Whisper, DALL·E)  

To use OpenAI’s models, authenticate with a **GitHub personal access token**:  

1. Go to **GitHub Settings → Developer Settings → Personal Access Tokens**  
2. Generate a new token  
3. Use it to authenticate OpenAI API requests  

**Note:** If you hit the rate limit, you’ll need to upgrade your plan.  

---

## 📂 Repository Overview  

- `deepseek.py` → Code for interacting with **DeepSeek LLM**  
- `gemini-pro.py` → API client for **Google Gemini Pro**  
- `openai-models.py` → Scripts for using **OpenAI models (GPT-4, Whisper, DALL·E)**  
- `.env.example` → Template for API keys & environment variables  
- `requirements.txt` → Dependencies to install  
- `README.md` → This guide  

---
