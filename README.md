# Log File Processor API

This project is a FastAPI-based application that enables users to upload `.txt` log files and retrieve the last `n` lines from the file. It is designed for efficient log analysis and includes robust error handling to ensure seamless functionality.

---

## **Getting Started**

### **Prerequisites**
Ensure the following are installed on your system:
- Python 3.7 or higher
- pip (Python package manager)

---

### **1. Clone the Repository**
To begin, clone the repository to your local machine:
```bash
git clone https://github.com/seemachhunga/log_file_processor.git
cd log_file_processor

2. Set Up the Virtual Environment
It is recommended to create a virtual environment to manage dependencies:
python -m venv env
.\env\Scripts\activate

3. Install Dependencies
Install the required Python packages using:
pip install -r requirements.txt

4. Run the Application
Start the application using Uvicorn:
uvicorn app:app --reload

The application will run locally at:
API Documentation: http://127.0.0.1:8000/docs
Root Endpoint: http://127.0.0.1:8000/

log_file_processor/
├── app.py             # Main application file
├── requirements.txt   # List of dependencies
├── README.md          # Documentation
└── uploads/           # Directory for uploaded files

Key Notes
Only .txt files are supported for upload.
Use the interactive API documentation available at http://127.0.0.1:8000/docs for testing and exploring the endpoints.


