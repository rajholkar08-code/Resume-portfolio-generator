import os
import json
from dotenv import load_dotenv
from google import genai

# ==========================================
# LOAD API KEY
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================
# READ UPLOADED RESUME
# ==========================================

with open("uploads/resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()


# ==========================================
# GEMINI PROMPT
# ==========================================

prompt = f"""
Analyze the following resume.

Return ONLY valid JSON.

Required format:

{{
    "name": "",
    "headline": "",
    "summary": "",
    "skills": [],
    "education": [],
    "projects": [],
    "achievements": [],
    "contact": {{
        "email": "",
        "github": "",
        "linkedin": ""
    }}
}}

Generate a professional 2-3 line summary about the candidate.

Resume:

{resume_text}
"""


# ==========================================
# GEMINI API CALL
# ==========================================

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print("===== GEMINI RESPONSE =====")
print(response.text)


# ==========================================
# CLEAN GEMINI RESPONSE
# ==========================================

json_text = response.text.strip()

if json_text.startswith("```json"):
    json_text = json_text[7:]

if json_text.startswith("```"):
    json_text = json_text[3:]

if json_text.endswith("```"):
    json_text = json_text[:-3]

json_text = json_text.strip()


# ==========================================
# SAVE JSON
# ==========================================

with open("resume_data.json", "w", encoding="utf-8") as file:
    file.write(json_text)

print("JSON Saved Successfully!")


# ==========================================
# READ JSON
# ==========================================

with open("resume_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("===== JSON DATA =====")
print(data)


# ==========================================
# IMPORTANT:
# READ TEMPLATE FROM templates FOLDER
# ==========================================

with open(
    "templates/template.html",
    "r",
    encoding="utf-8"
) as file:
    template = file.read()


# ==========================================
# BASIC INFORMATION
# ==========================================

name = data.get("name", "")
headline = data.get("headline", "")
summary = data.get("summary", "")


# ==========================================
# SKILLS
# ==========================================

skills_html = ""

for skill in data.get("skills", []):
    skills_html += f'<span class="skill">{skill}</span>'


# ==========================================
# PROJECTS
# ==========================================

projects_html = ""

for project in data.get("projects", []):

    projects_html += f"""
    <div class="project-card">
        <h4>{project}</h4>
    </div>
    """


# ==========================================
# EDUCATION
# ==========================================

education_html = "<ul>"

for edu in data.get("education", []):
    education_html += f"<li>{edu}</li>"

education_html += "</ul>"


# ==========================================
# ACHIEVEMENTS
# ==========================================

achievements_html = "<ul>"

for achievement in data.get("achievements", []):
    achievements_html += f"<li>{achievement}</li>"

achievements_html += "</ul>"


# ==========================================
# CONTACT
# ==========================================

contact = data.get("contact", {})

email = contact.get("email", "")
github = contact.get("github", "")
linkedin = contact.get("linkedin", "")

contact_html = f"""
<p>
    <strong>Email:</strong>
    <a href="mailto:{email}">
        {email}
    </a>
</p>

<p>
    <strong>GitHub:</strong>
    <a href="https://{github}" target="_blank">
        {github}
    </a>
</p>

<p>
    <strong>LinkedIn:</strong>
    <a href="https://{linkedin}" target="_blank">
        {linkedin}
    </a>
</p>
"""


# ==========================================
# REPLACE TEMPLATE VARIABLES
# ==========================================

template = template.replace("{{name}}", name)

template = template.replace(
    "{{headline}}",
    headline
)

template = template.replace(
    "{{summary}}",
    summary
)

template = template.replace(
    "{{skills}}",
    skills_html
)

template = template.replace(
    "{{projects}}",
    projects_html
)

template = template.replace(
    "{{education}}",
    education_html
)

template = template.replace(
    "{{achievements}}",
    achievements_html
)

template = template.replace(
    "{{contact}}",
    contact_html
)


# ==========================================
# SAVE GENERATED PORTFOLIO
# ==========================================

with open(
    "templates/portfolio.html",
    "w",
    encoding="utf-8"
) as file:
    file.write(template)


print("================================")
print("Portfolio Generated Successfully!")
print("================================")