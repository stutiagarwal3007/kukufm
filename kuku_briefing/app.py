from flask import Flask, render_template, request, abort
from .models import get_user
from .ai_pipeline import create_daily_briefing

app = Flask(__name__)

@app.route('/')
def index():
    # In a real app, user_id would come from login session
    user_ids = ["user123", "user456", "user789"]
    return render_template('index.html', user_ids=user_ids)

@app.route('/get_briefing', methods=['POST'])
def get_briefing_route():
    user_id = request.form.get('user_id')
    if not user_id:
        abort(400, "User ID is required.")

    user = get_user(user_id)
    if not user:
        abort(404, f"User '{user_id}' not found.")

    # Run the simulated AI pipeline
    briefing_output = create_daily_briefing(user)

    return render_template('index.html', briefing=briefing_output, selected_user_id=user_id, user_ids=["user123", "user456", "user789"])

if __name__ == '__main__':
    # Use a different port if 5000 is occupied
    app.run(debug=True, port=5000)
