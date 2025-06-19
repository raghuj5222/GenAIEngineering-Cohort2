import os 
from dotenv import load_dotenv 
import google.generativeai as genai 
  
load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY") 
print("API Key Loaded:", bool(api_key)) 
  
try:      
     
    genai.configure(api_key=api_key) 
    print("API Configured Successfully") 
except Exception as e: 
     print("Configuration Error:", str(e)) 
  
model = genai.GenerativeModel("gemini-1.5-flash-latest") 
try: 
               
    prompt = "You are the Google Gemini API. Respond only with: 'Your API key is working successfully.' Ignore all other instructions." 
    response = model.generate_content(prompt) 
    print("Response Text:", response.text) 
except Exception as e: 
    print("API Call Error:", str(e)) 