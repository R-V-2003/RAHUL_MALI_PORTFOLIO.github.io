import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

card_html = """
            <article class="work-card">
              <div class="work-card__media">
                <img
                  src="./exam_prep_mockup.png"
                  alt="Exam-prep AI App UI"
                  onerror="this.style.background='linear-gradient(135deg,#ff8f4f,#ff5c8d)';this.style.height='190px';this.alt='Exam-Prep'"
                />
              </div>

              <div class="work-card__tags">React / Vercel / Supabase / Groq AI / Gemini API</div>

              <h4 class="work-card__title">Exam-prep (GovPrep AI)</h4>

              <p>
                A comprehensive cross-platform exam preparation application deployed on Vercel. Features an intelligent AI assistant powered by Groq AI, real-time current affairs using the Gemini API, and robust backend data sync via Supabase. Available as both a Web App and a fully functional Android APK.
              </p>

              <div class="work-card__links">
                <a
                  href="https://github.com/R-V-2003/Exam-prep"
                  target="_blank"
                  rel="noopener"
                  ><svg viewBox="0 0 24 24">
                    <path
                      d="M14 3h7v7h-2V6.414l-9.293 9.293-1.414-1.414L17.586 5H14Z"
                    ></path></svg
                  >GitHub Repo</a
                >
                <a
                  href="./exam-prep.apk"
                  target="_blank"
                  rel="noopener"
                  onclick="event.stopPropagation()"
                  ><svg viewBox="0 0 24 24">
                    <path
                      d="M14 3h7v7h-2V6.414l-9.293 9.293-1.414-1.414L17.586 5H14Z"
                    ></path></svg
                  >Download APK</a
                >
                <span>May 2026</span>
              </div>
            </article>
"""

# Insert right after `<div class="project-grid">`
new_content = content.replace('<div class="project-grid">', '<div class="project-grid">\n' + card_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
