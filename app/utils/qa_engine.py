import os
import requests

class QAEngine:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model  = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self,name,question):
        headers = {
            "Authorization" : f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        prompt = f"""
                    You are an AI assistant with reliable knowledge about well-known public figures and celebrities.

                    Your task is to answer the question about **{name}** clearly, concisely, and accurately.

                    Guidelines:
                    - Provide only factually correct and widely accepted information.
                    - Keep the answer short and to the point.
                    - If the information is uncertain or not publicly available, clearly state that.

                    Question:
                    {question}
                """

        
        payload  = {
            "model" : self.model,
            "messages" : [{"role" : "user" , "content" : prompt}],
            "temperature" :  0.5,
            "max_tokens" : 512
        }

        response = requests.post(self.api_url , headers=headers , json=payload)

        if response.status_code==200:
            return response.json()['choices'][0]['message']['content']
        
        return "Sorry I couldn't find the answer"



