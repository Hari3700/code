from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem (for development)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def chat():
    # Initialize session chat history if not present
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        query = request.form.get('query', '').lower()
        response = ""

        # Rule-based responses
        if 'odop' in query:
            response = '''
                <strong>ODOP (One District One Product):</strong> A government initiative aimed at promoting the unique products of each district in India. The idea is to focus on a specific product from each district and enhance its production, marketing, and export potential, thereby boosting the local economy.
            '''
        elif 'business' in query:
            response = '<a href="https://diupmsme.upsdc.gov.in/login/Registration_Login" target="_blank">Visit Business Registration Portal</a>'
        else:
            response = "Sorry, I couldn't understand your query. Please try again."

        # Append to chat history
        session['chat_history'].append({'role': 'user', 'text': query})
        session['chat_history'].append({'role': 'bot', 'text': response})
        session.modified = True  # Mark session as modified

    return render_template('index.html', chat_history=session.get('chat_history', []))

if __name__ == '__main__':
    app.run(debug=True)
