import google.generativeai as genai

genai.configure(api_key="api_key")

try:
    models = genai.list_models()
    print("可用模型:", [model.name for model in models])
except Exception as e:
    print("API Key 可能无效:", e)