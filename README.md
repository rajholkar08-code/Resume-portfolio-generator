# AI-Assisted Resume Portfolio Generator

🌐 **Live Demo:**
https://resume-portfolio-generator-quiu.onrender.com/

📂 **GitHub Repository:**
https://github.com/rajholkar08-code/Resume-portfolio-generator

---

## Overview

AI-Assisted Resume Portfolio Generator is a web application that transforms a resume into a professional portfolio website using Google Gemini AI. Users can upload their resume and profile photo, and the system automatically extracts relevant information to generate a personalized portfolio.

The project was developed as part of a Summer Bootcamp focused on AI, APIs, databases, and full-stack web development.

---

## Features

* Upload Resume (PDF/TXT)
* Upload Profile Photo
* AI-Powered Resume Analysis
* Automatic Information Extraction
* Dynamic Portfolio Generation
* Professional Portfolio Layout
* Multiple Theme Selection Options
* Responsive User Interface
* Structured JSON Data Generation
* Real-Time Portfolio Preview

---

## Live Website

Visit the deployed project:

https://resume-portfolio-generator-quiu.onrender.com/

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI Integration

* Google Gemini API

### Data Processing

* JSON
* PyPDF

### Development Tools

* VS Code
* GitHub

### Deployment

* Render

---

## Project Workflow

```text
Resume Upload
      ↓
Resume Text Extraction
      ↓
Gemini AI Processing
      ↓
Structured JSON Generation
      ↓
HTML Template Population
      ↓
Theme Selection
      ↓
Portfolio Generation
      ↓
Portfolio Display
```

---

## Project Structure

```text
Resume-portfolio-generator/
│
├── app.py
├── main.py
├── requirements.txt
├── resume_data.json
│
├── templates/
│   ├── index.html
│   ├── template.html
│   └── portfolio.html
│
├── static/
│   ├── style.css
│   └── profile.jpg
│
├── uploads/
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rajholkar08-code/Resume-portfolio-generator.git
cd Resume-portfolio-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variable

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a resume and optional profile photo.
2. Resume content is extracted from the uploaded file.
3. Gemini AI analyzes the resume.
4. AI generates structured JSON data.
5. Flask processes the JSON response.
6. Portfolio data is inserted into the HTML template.
7. Selected theme is applied.
8. Final portfolio is generated and displayed.

---

## Sample Portfolio Sections

The generated portfolio includes:

* Personal Information
* Professional Headline
* About Me / Summary
* Skills
* Projects
* Education
* Achievements
* Contact Details

---

## AI Model Used

**Google Gemini Flash**

The Gemini model is used to:

* Extract resume information
* Generate structured JSON
* Organize profile details
* Create portfolio-ready content

---

## Future Enhancements

* PDF Portfolio Export
* DOCX Resume Support
* Portfolio Template Library
* Supabase Database Integration
* Custom Portfolio URLs
* Advanced Theme Customization
* Portfolio Analytics Dashboard

---

## Learning Outcomes

Through this project, we gained practical experience in:

* AI Integration
* Prompt Engineering
* Flask Development
* JSON Processing
* API Usage
* Frontend Development
* Deployment on Render
* GitHub Version Control

---

## Author

**Raju Singh**

B.Tech Computer Science Engineering (AI & ML)
GLA University, Mathura

GitHub:
https://github.com/rajholkar08-code

LinkedIn:
https://www.linkedin.com/in/raju-singh-57a941383/

---

## License

This project is created for educational and learning purposes as part of a Summer Bootcamp project.
