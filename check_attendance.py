import pandas as pd
from datetime import datetime
import os

def check_attendance():
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"Data/Attendance_{date}.csv"
    
    if not os.path.exists(filename):
        return f"No attendance record found for {date}"
    
    try:
        df = pd.read_csv(filename)
        if df.empty:
            return "Attendance file is empty"
        
        # Format the output
        output = f"Attendance for {date}:\n"
        output += df.to_string(index=False)
        return output
    except Exception as e:
        return f"Error reading attendance file: {str(e)}"

if __name__ == "__main__":
    print(check_attendance())