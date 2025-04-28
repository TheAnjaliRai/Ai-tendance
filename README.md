# Ai-tendance 🎓

**Ai-tendance** is a smart, AI-powered attendance system that automates the process of marking attendance using facial recognition. This application ensures accuracy, saves time, and simplifies attendance tracking for educational institutions and organizations.

## 🧪 Features

- **Facial Recognition**: Uses advanced facial recognition technology for reliable identification.
- **Automated Attendance**: Records attendance in real-time upon successful recognition.
- **User Management**: Allows the addition of new users by capturing their facial data.
- **Attendance Logs**: Maintains attendance records for future analysis and review.

## 🔧 Technologies Used

- **Python**: The primary programming language.
- **OpenCV**: For image processing and facial recognition.
- **Flask**: Web framework to manage server-side logic and routes.
- **HTML/CSS**: For designing the user interface.

## 📁 Project Structure

```
Ai-tendance/
├── app.py
├── add_face.py
├── check_attendance.py
├── mark_attendance.py
├── utils/
│   └── [utility scripts]
├── static/
│   └── [static files like CSS, JS, images]
├── templates/
│   └── [HTML templates]
├── requirements.txt
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher.
- Conda installed on your system.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TheAnjaliRai/Ai-tendance.git
   cd Ai-tendance
   ```

2. **Create a Conda environment**:

   ```bash
   conda create --name aienv python=3.10
   conda activate aienv
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## 📸 Usage

1. **Adding a New User**:

   Run the `add_face.py` script to capture and store a new user’s facial data.

   ```bash
   python add_face.py
   ```

2. **Marking Attendance**:

   Use the `mark_attendance.py` script to initiate facial recognition and mark attendance.

   ```bash
   python mark_attendance.py
   ```

3. **Checking Attendance Records**:

   Execute the `check_attendance.py` script to view stored attendance logs.

   ```bash
   python check_attendance.py
   ```
## 📸 Screenshots

Below are some screenshots of the application in action:

1. **Home Page**  
   ![Image](https://github.com/user-attachments/assets/354510b6-e77f-4598-a688-a58150d12bad)

2. **Facial Recognition in Action**  
   ![Facial Recognition](images/recognition_screenshot.png)

3. **Attendance Logs**  
   ![Attendance Logs](images/attendance_logs_screenshot.png)

   
## 📃 License

This project is licensed under the [MIT License](LICENSE).

## 👩‍💻 Author

**Anjali Rai**

- GitHub: [@TheAnjaliRai](https://github.com/TheAnjaliRai)
- Email: anjalirai0004@gmail.com

