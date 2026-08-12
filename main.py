import os
import json

from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

# ==========================
# GEMINI
# ==========================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================
# READ RESUME
# ==========================

resume_text = ""

files = os.listdir("uploads")

if not files:
    raise Exception("No resume uploaded")

resume_file = os.path.join(
    "uploads",
    files[0]
)

# PDF
if resume_file.lower().endswith(".pdf"):

    reader = PdfReader(
        resume_file
    )

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text + "\n"

# TXT
elif resume_file.lower().endswith(".txt"):

    with open(
        resume_file,
        "r",
        encoding="utf-8"
    ) as file:

        resume_text = file.read()

else:

    raise Exception(
        "Only PDF and TXT files are supported."
    )

# ==========================
# PROMPT
# ==========================

prompt = f"""
Analyze the following resume.

Return ONLY valid JSON.

Required format:

{{
"name":"",
"headline":"",
"summary":"",
"skills":[],
"education":[],
"projects":[],
"achievements":[],
"contact":
{{
"email":"",
"github":"",
"linkedin":""
}}
}}

Generate a professional 2-3 line summary.

Resume:

{resume_text}
"""

# ==========================
# GEMINI
# ==========================

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

json_text = response.text.strip()

json_text = json_text.replace(
    "```json",
    ""
)

json_text = json_text.replace(
    "```",
    ""
)

json_text = json_text.strip()

# ==========================
# SAVE JSON
# ==========================

with open(
    "resume_data.json",
    "w",
    encoding="utf-8"
) as file:

    file.write(json_text)

# ==========================
# LOAD JSON
# ==========================

with open(
    "resume_data.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

# ==========================
# TEMPLATE
# ==========================

with open(
    "templates/template.html",
    "r",
    encoding="utf-8"
) as file:

    template = file.read()

# ==========================
# DATA
# ==========================

name = data.get("name", "")
headline = data.get("headline", "")
summary = data.get("summary", "")

# Skills

skills_html = ""

for skill in data.get("skills", []):

    skills_html += (
        f'<span class="skill">'
        f'{skill}'
        f'</span>'
    )

# Projects

projects_html = ""

for project in data.get(
    "projects",
    []
):

    projects_html += f"""
    <div class="project-card">
        <h4>{project}</h4>
    </div>
    """

# Education

education_html = "<ul>"

for edu in data.get(
    "education",
    []
):

    education_html += (
        f"<li>{edu}</li>"
    )

education_html += "</ul>"

# Achievements

achievements_html = "<ul>"

for item in data.get(
    "achievements",
    []
):

    achievements_html += (
        f"<li>{item}</li>"
    )

achievements_html += "</ul>"

# Contact

contact = data.get(
    "contact",
    {}
)

contact_html = f"""
<p>Email: {contact.get('email','')}</p>
<p>Github: {contact.get('github','')}</p>
<p>LinkedIn: {contact.get('linkedin','')}</p>
"""

# ==========================
# REPLACE
# ==========================

template = template.replace(
    "{{name}}",
    name
)

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

# ==========================
# SAVE PORTFOLIO
# ==========================

with open(
    "templates/portfolio.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(template)

print("Portfolio Generated Successfully")