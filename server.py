from flask import Flask, render_template, url_for, request, jsonify, redirect
import csv

app = Flask(__name__) #Created an instance of the Flask framework, created an app
print(__name__)

@app.route("/") # root directory website
def home():
    return render_template('index.html') #look for templates html file, and then run the given html file


print("Testing")

@app.route("/thankyou.html") # root directory website
def thankyou():
    return render_template('thankyou.html')

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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
        #return 'Thanks!'
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!!'


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)  # Function to save data to CSV
#             return jsonify({'message': 'Thanks for your submission!'}), 200
#         except Exception as e:
#             print(f"Error saving to database: {e}")  # Log the error
#             return jsonify({'message': 'Did not save to database.'}), 500
#     return jsonify({'message': 'Something went wrong. Try again!'}), 400




if __name__ == '__main__':
    app.run(debug=True)