from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# Ensure Data directory exists
if not os.path.exists('Data'):
    os.makedirs('Data')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_student", methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            # Run add_face.py with the provided name
            process = subprocess.Popen(['python', 'add_face.py', name], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            return f"Student added successfully! {stdout.decode()}"
    return render_template("add_student.html")

@app.route("/mark_attendance")
def mark_attendance():
    # Run mark_attendance.py
    process = subprocess.Popen(['python', 'mark_attendance.py'], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return f"Attendance marked! {stdout.decode()}"

@app.route("/check_attendance")
def check_attendance():
    # Run check_attendance.py and get the output
    process = subprocess.Popen(['python', 'check_attendance.py'], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    attendance_data = stdout.decode()
    return render_template("check_attendance.html", attendance_data=attendance_data)

if __name__ == "__main__":
    app.run(debug=True)