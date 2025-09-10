# Iron Lady Leadership Programs Chatbot

A Flask-based chatbot that provides information about Iron Lady's leadership development programs. The chatbot uses both predefined FAQs and AI-powered responses to answer user queries about programs, duration, mode of delivery, certifications, and mentors.

## Features

- 🤖 Interactive chatbot interface
- 📚 Comprehensive program information
- 💬 AI-powered responses using Google's Gemini API
- 📱 Responsive design
- ❓ Quick-access FAQ buttons

## Programs Offered

- Executive Leadership Program (6 months)
- Women in Tech Leadership (4 months)
- Early Career Mentorship (3 months)
- Leadership Bootcamp (6 weeks)

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd iron_lady_chatbot
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `.env` file
- Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

## Technologies Used

- Python/Flask
- Google Gemini AI
- HTML/CSS
- JavaScript

## Note

Make sure to keep your API keys confidential and never commit them to the repository.
