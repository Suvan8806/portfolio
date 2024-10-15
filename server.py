from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

app = Flask(__name__) #Created an instance of the Flask framework, created an app
print(__name__)

@app.route("/") # root directory website
def home():
    return render_template('index.html') #look for templates html file, and then run the given html file




def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
  with open('database.csv', mode='a', newline='') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#       try:
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/thankyou.html')
#         #return 'Thanks!'
#       except:
#         return 'did not save to database'
#     else:
#       return 'something went wrong. Try again!!'


    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "*********@gmail.com"  # Enter your address
    receiver_email = "********@gmail.com"  # Enter receiver address
    password = "**********"

    # Retrieve data from the form
    sender= request.form['sender_email']
    subject = request.form['subject']
    message = request.form['message']


    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # Attach the message text
    body = f"Message from: {sender}\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))
    
    
    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Sent!")

    return redirect('/thankyou.html')


print("Testing")

@app.route("/thankyou.html") # root directory website
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
