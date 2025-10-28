

import google.generativeai as genai
from datetime import date

# Set up API key
genai.configure(api_key="YourKeyHere")

today = str(date.today())
 
# Specify GenAI Model
model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

# Set up the Gemini Pro model
gf = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 128,
    } 

safety_settings=[
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]


# Specify language
slang = "en-EN"

# Main function  
def main():
    global today, openaitts, model, chat, slang, gf, safety_settings 
    

    request = '''Explain how AI can assist in daily tasks'''
    response = chat.send_message(request)   
 
    print(response)
 
if __name__ == "__main__":
    main()










