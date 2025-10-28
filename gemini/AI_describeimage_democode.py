
import google.generativeai as genai
import PIL.Image

# Set Google Gemini API key
genai.configure(api_key="YourKeyHere")
 
# Specify which Gemini model to use
model = genai.GenerativeModel('gemini-1.5-pro')

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


# define default language to work with the AI model 
slang = "en-EN"

# Main function  
def main():
    global today, openaitts, model, chat, slang, gf, safety_settings 

    sample_file = PIL.Image.open('firefighter.jpg')

    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([sample_file, "Describe this image."])
    print(response.text)

 
if __name__ == "__main__":
    main()










