"""
Gym Management System - Flask Application
A simple web application for gym management with multiple pages
"""

from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    """Render the home page"""
    return render_template('home.html')

# Route for About Us Page
@app.route('/about')
def about():
    """Render the about us page with team and facilities info"""
    # Sample team data
    team_members = [
        {
            'name': 'John Smith',
            'role': 'Head Trainer',
            'specialty': 'Strength & Conditioning'
        },
        {
            'name': 'Sarah Johnson',
            'role': 'Yoga Instructor',
            'specialty': 'Yoga & Flexibility'
        },
        {
            'name': 'Mike Davis',
            'role': 'Nutrition Expert',
            'specialty': 'Diet & Nutrition Planning'
        },
        {
            'name': 'Emily Brown',
            'role': 'Cardio Specialist',
            'specialty': 'Cardio & Weight Loss'
        }
    ]
    return render_template('about.html', team=team_members)

# Route for Membership Page
@app.route('/membership')
def membership():
    """Render the membership plans page"""
    # Membership plans data
    plans = [
        {
            'name': 'Basic',
            'price': '29',
            'duration': 'month',
            'features': [
                'Access to gym equipment',
                'Locker facility',
                'Free WiFi',
                'Basic workout plan'
            ]
        },
        {
            'name': 'Standard',
            'price': '49',
            'duration': 'month',
            'features': [
                'All Basic features',
                'Group fitness classes',
                'Personal trainer (2 sessions/month)',
                'Nutrition consultation',
                'Steam & Sauna access'
            ],
            'popular': True
        },
        {
            'name': 'Premium',
            'price': '79',
            'duration': 'month',
            'features': [
                'All Standard features',
                'Unlimited personal training',
                'Customized meal plans',
                'Massage therapy (2 sessions/month)',
                'Priority equipment access',
                'Guest passes (5/month)'
            ]
        }
    ]
    return render_template('membership.html', plans=plans)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)