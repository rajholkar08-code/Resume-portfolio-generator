import os
import json
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read Resume
with open("uploads/resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

# Prompt
prompt = f"""
Analyze the following resume.

Generate a professional 2-3 line summary.

Return ONLY valid JSON.

{{
  "name":"",
  "headline":"",
  "summary":"MUST NOT BE EMPTY",
  "skills":[],
  "education":[],
  "projects":[],
  "achievements":[],
  "contact": {{
      "email":"",
      "github":"",
      "linkedin":""
  }}
}}

Resume:

{resume_text}
"""

# Gemini Call
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print("===== GEMINI RESPONSE =====")
print(response.text)

# Clean Response
json_text = response.text.strip()
json_text = json_text.replace("```json", "")
json_text = json_text.replace("```", "")
json_text = json_text.strip()

# Save JSON
with open("resume_data.json", "w", encoding="utf-8") as file:
    file.write(json_text)

print("JSON Saved Successfully!")

# Read JSON
with open("resume_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Read Template
with open("template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Basic Info
name = data.get("name", "")
headline = data.get("headline", "")
summary = data.get("summary", "")

# Skills
skills_html = ""

for skill in data.get("skills", []):
    skills_html += f'<span class="skill">{skill}</span> '

# Projects
projects_html = ""

for project in data.get("projects", []):
    projects_html += f"""
    <div class="project-card">
        <h4>🚀 {project}</h4>
        <p>Project completed successfully.</p>
    </div>
    """

# Education
education_html = "<ul>"

for edu in data.get("education", []):
    education_html += f"<li>{edu}</li>"

education_html += "</ul>"

# Achievements
achievements_html = "<ul>"

for achievement in data.get("achievements", []):
    achievements_html += f"<li>{achievement}</li>"

achievements_html += "</ul>"

# Contact
contact = data.get("contact", {})

contact_html = f"""
<p>
<b>Email:</b>
<a href="mailto:{contact.get('email','')}">
{contact.get('email','')}
</a>
</p>

<p>
<b>GitHub:</b>
<a href="https://{contact.get('github','')}" target="_blank">
{contact.get('github','')}
</a>
</p>

<p>
<b>LinkedIn:</b>
<a href="https://{contact.get('linkedin','')}" target="_blank">
{contact.get('linkedin','')}
</a>
</p>
"""

# Replace Template Variables
template = template.replace("{{name}}", name)
template = template.replace("{{headline}}", headline)
template = template.replace("{{summary}}", summary)
template = template.replace("{{skills}}", skills_html)
template = template.replace("{{projects}}", projects_html)
template = template.replace("{{education}}", education_html)
template = template.replace("{{achievements}}", achievements_html)
template = template.replace("{{contact}}", contact_html)

# Save Portfolio
with open("templates/portfolio.html", "w", encoding="utf-8") as file:
    file.write(template)

print("Portfolio Generated Successfully!")