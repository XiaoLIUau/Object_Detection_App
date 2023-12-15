import os
from flask import Flask
import smtplib
import threading
# # Adjust the path to import main.py
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask App'


@app.route('/notify', methods=['GET'])
def send_notification():
    sender = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASSWORD')
    receiver = 'xiao.liu.contact@gmail.com'# 'xin.chen9@uq.net.au' #

    print(sender)
    print(receiver)
    if not sender or not password:
        return 'Email credentials are not set', 500

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Outlook SMTP server
    server.starttls()

    print("smtp set...")

    try:
        server.login(sender, password)
        print('login working...')
        server.sendmail(sender, receiver, 'Subject: Cap Detected\n\nA cap has been detected by the system.')
    except smtplib.SMTPException as e:
        return f'Failed to send email: {e}', 500
    finally:
        server.quit()

    return 'Notification sent'


if __name__ == '__main__':

    # # Start camera stream in a separate thread
    # threading.Thread(target=main, daemon=True).start()
    app.run(debug=True, host='0.0.0.0')
    # threading.Thread(target=lambda: app.run(debug=True, host='0.0.0.0', port=5000)).start()
    # main()
