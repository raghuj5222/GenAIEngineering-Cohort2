import os 
from dotenv import load_dotenv 
from groq import Groq 
  
 # Load environment variables from .env 
load_dotenv() 
api_key = os.getenv("GROQ_API_KEY") 
print("API Key Loaded:", bool(api_key)) 
  
 # Configure the Groq API 
try: 
          
    client = Groq(api_key=api_key) 
    print("API Configured Successfully") 
except Exception as e: 
     print("Configuration Error:", str(e)) 
  
# Make a test API call 
try: 
     
    chat_completion = client.chat.completions.create( 
        messages=[{"role": "user", "content": "Hello, Groq! Confirm this API key is working."}], 
        model="llama3-8b-8192" 
    ) 
    print("Response Text:", 
    chat_completion.choices[0].message.content) 
except Exception as e: 
    print("API Call Error:", str(e)) 