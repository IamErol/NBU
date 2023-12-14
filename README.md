# Running Django Application Locally
This guide will walk you through the steps required to run the Django application on your local machine.

### Prerequisites
-Python installed on your system
-pip (Python package installer)
-Virtual environment (recommended)

### Installation and Setup

1. **Clone the repository**:

   ```
   git clone https://github.com/IamErol/NBU.git
   ```

2. **Navigate to the project directory**:

   ```
   cd NBU
   ```

3. **Create and Activate a Virtual Environment**:

   ```
   python -m venv venv

   On Windows:
   .\venv\Scripts\activate
   
   On Unix or MacOS:
   source venv/bin/activate
   ```
4. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```
   
5. **To load these variables, you can use python-dotenv package. In your Django settings, do:**:

   ```
   import os
   from dotenv import load_dotenv
    
   load_dotenv()
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
   ```

6. **Finally, start the Django development server:**:
   ```
   python manage.py runserver
   ```

   Open your web browser and go to [http://localhost:8000](http://localhost:8000) to access the application.


## Usage

1. **Upload 2 excel files.**

2. **Click upload and merge.**

3. **Download merged file.**






