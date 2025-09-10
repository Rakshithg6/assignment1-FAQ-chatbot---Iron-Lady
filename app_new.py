from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
try:
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found!")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    # Test the configuration
    print("Testing Gemini API connection...")
    response = model.generate_content("Hi")
    print("Gemini API connection successful!")
    
except Exception as e:
    print(f"Warning: Gemini API configuration failed: {str(e)}")
    model = None

def get_ai_response(query):
    if not model:
        return handle_faq_query(query)
        
    try:
        context = """You are an AI assistant for Iron Lady Leadership Programs. Your role is to provide helpful information about our programs:

Key Programs:
• Executive Leadership Program (6 months)
• Women in Tech Leadership (4 months)
• Early Career Mentorship (3 months)
• Leadership Bootcamp (6 weeks)

Features:
• Hybrid learning (online/offline)
• Industry certificates
• Expert mentors
• Practical training

Be friendly and use emojis and bullet points in responses."""

        prompt = f"{context}\n\nUser Question: {query}\n\nProvide a helpful response:"
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
        return handle_faq_query(query)
        
    except Exception as e:
        print(f"AI Error: {str(e)}")
        return handle_faq_query(query)

def handle_faq_query(query):
    query = query.lower()
    
    if 'program' in query:
        return """📚 Our Leadership Programs:

• Executive Leadership Program (6 months)
  - For senior professionals
  - Advanced leadership skills
  - Strategic focus

• Women in Tech Leadership (4 months)
  - Tech industry focused
  - Specialized mentoring
  - Career growth

• Early Career Mentorship (3 months)
  - For emerging leaders
  - Skill development
  - Career guidance

• Leadership Bootcamp (6 weeks)
  - Intensive training
  - Practical workshops
  - Hands-on experience"""

    elif 'duration' in query:
        return """⏱️ Program Durations:

• Executive Leadership: 6 months
  - Flexible schedule
  - Part-time format
  
• Women in Tech: 4 months
  - Weekend sessions
  - Online modules
  
• Early Career: 3 months
  - Weekly sessions
  - Structured learning
  
• Leadership Bootcamp: 6 weeks
  - Intensive format
  - Daily workshops"""

    elif 'online' in query or 'offline' in query:
        return """🌐 Learning Modes:

• Online Features
  - Live virtual sessions
  - Interactive workshops
  - Digital resources
  - 24/7 access

• Offline Components
  - In-person workshops
  - Networking events
  - Group activities
  - Direct mentoring"""

    elif 'certificate' in query:
        return """🎓 Certification Details:

• Program Certificates
  - Industry-recognized
  - Digital badges
  - Verified credentials

• Additional Benefits
  - Alumni network
  - Career resources
  - Lifetime access"""

    elif 'mentor' in query:
        return """👥 Our Expert Mentors:

• Industry Leaders
  - Fortune 500 executives
  - Tech veterans
  - 10+ years experience

• Specialized Coaches
  - Certified trainers
  - Career experts
  - Leadership specialists"""

    return """👋 Welcome to Iron Lady Leadership Programs!

📚 We offer:
• Executive Leadership Program
• Women in Tech Leadership
• Early Career Mentorship
• Leadership Bootcamp

What would you like to know about our programs?"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json.get('message', '')
        
        # First check for exact FAQ matches
        faq_questions = {
            'what programs does iron lady offer?': handle_faq_query('program'),
            'what is the program duration?': handle_faq_query('duration'),
            'is the program online or offline?': handle_faq_query('online'),
            'are certificates provided?': handle_faq_query('certificate'),
            'who are the mentors?': handle_faq_query('mentor')
        }
        
        if user_message.lower() in faq_questions:
            return jsonify({'response': faq_questions[user_message.lower()]})
        
        # Use AI for other questions
        response = get_ai_response(user_message)
        return jsonify({'response': response})
        
    except Exception as e:
        print(f"Error in ask route: {str(e)}")
        return jsonify({'response': handle_faq_query('')})

if __name__ == '__main__':
    app.run(debug=True)
