from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'secret.key.hui'

@app.route('/')
def home():
    """Main page route"""
    language = session.get('language', 'en')  # Default to English
    return render_template('index.html', language=language)

@app.route('/projects')
def projects():
    """Projects page route"""
    language = session.get('language', 'en')
    return render_template('projects.html', language=language)

@app.route('/set_language/<language>')
def set_language(language):
    """Language switching route"""
    if language in ['en', 'ru']:
        session['language'] = language
    # Redirect back to previous page or home
    return redirect(request.referrer or '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
