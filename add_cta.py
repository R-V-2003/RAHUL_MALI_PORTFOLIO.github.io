import re

with open('case-study-chalo.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_section = """
      <!-- ── CTA Download ── -->
      <section class="cs-section cs-fade-in" style="margin: 60px 0; text-align: center; padding: 40px; background: rgba(14, 107, 255, 0.05); border-radius: 24px; border: 1px solid rgba(14, 107, 255, 0.1);">
        <h2 style="font-size: 28px; margin-bottom: 16px;">Experience Chalo</h2>
        <p style="margin-bottom: 30px;">Download the fully functioning Android APK and see the platform in action.</p>
        <a href="https://raw.githubusercontent.com/R-V-2003/RAHUL_MALI_PORTFOLIO.github.io/main/chalo.apk" style="display: inline-flex; align-items: center; gap: 10px; background: var(--primary); color: white; padding: 14px 32px; border-radius: 999px; text-decoration: none; font-weight: 600; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 10px 20px rgba(14, 107, 255, 0.2);">
          <svg viewBox="0 0 24 24" style="width: 20px; height: 20px; fill: currentColor;"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
          Download APK
        </a>
      </section>

      <!-- ── Reflection ── -->
"""

new_content = content.replace("<!-- ── Reflection ── -->", cta_section)

with open('case-study-chalo.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
