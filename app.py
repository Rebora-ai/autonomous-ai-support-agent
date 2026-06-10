import os
import json

# Имитируем базу знаний компании (например, правила возврата товаров интернет-магазина США)
COMPANY_KNOWLEDGE = """
ReboraShop Policy:
1. Returns are accepted within 30 days of purchase.
2. Items must be unworn and in original packaging.
3. Shipping for returns is FREE for US customers.
4. Refunds take 5-7 business days to process.
"""

def generate_ai_response(client_question):
    # Используем библиотеку ollama для отправки запроса локальной модели Llama 3
    import ollama
    
    # Формируем жесткую системную инструкцию по принципу Форда — только факты
    system_prompt = f"You are an AI Support Agent. Answer the customer using ONLY this policy: {COMPANY_KNOWLEDGE}. Be concise and polite."
    
    try:
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': client_question}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error connecting to local LLM: {e}. Make sure Ollama is running."

if __name__ == "__main__":
    print("[*] Запуск конвейера Rebora.ai...")
    test_question = "Hi! Can I return my shoes? I bought them 2 weeks ago, but they don't fit. Do I need to pay for shipping?"
    
    print(f"\n[Входящий тикет клиента]: {test_question}")
    print("[*] ИИ анализирует базу знаний...")
    
    ai_reply = generate_ai_response(test_question)
    print(f"\n[Автоматический ответ ИИ]:\n{ai_reply}")
