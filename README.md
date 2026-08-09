# Rahul Mali's Unfiltered Portfolio

Welcome to the source code of my personal portfolio. If you're looking for standard corporate jargon and boring layouts, you're in the wrong place. 

## 🚀 Live Demo
[View the Live Portfolio](https://r-v-2003.github.io/RAHUL_MALI_PORTFOLIO.github.io/)

## 🛠️ What's Inside?
- **HTML5 & CSS3**: Hand-crafted layouts built to perfection without relying on a massive framework.
- **Glassmorphism UI**: Keeping things trendy and shiny.
- **Sarcastic Case Studies**: Real talk about what it actually takes to build UI/UX (mostly fighting with divs and convincing stakeholders).

## 📁 Repository Structure
- `index.html`: The main landing page, filled with all the unfiltered truths.
- `case-study-ptenote.html`: A deep dive into the PTENote redesign.
- `case-study-detnote.html`: The story behind the DetNote exam booking platform.
- `case-study-chalo.html`: The journey of building the CHALO app.
- `case-study-examprep.html`: The case study for GovPrep AI (BCI-Prep).
- `chalo.apk`: **[Download the Chalo APK here](https://raw.githubusercontent.com/R-V-2003/RAHUL_MALI_PORTFOLIO.github.io/main/chalo.apk)**.
- `exam-prep.apk`: **[Download the BCI-Prep APK here](https://raw.githubusercontent.com/R-V-2003/RAHUL_MALI_PORTFOLIO.github.io/main/exam-prep.apk)**.
- `Rahul Mali _ Portfolio_files/`: Assorted assets and official brand icons for AI tools.

## 🎛️ Static CMS Dashboard & Cryptographic Security

I built a completely serverless, client-side Content Management System (`dashboard.html`) to manage my portfolio's journey timeline, project grid, achievements, and media gallery directly from any browser (desktop or mobile).

### 🔒 How Security is Maintained on a Static Site
Normally, static sites on GitHub Pages cannot securely store private credentials (like GitHub API tokens) because all front-end code is public. To solve this securely without paying for or maintaining backend servers:
- **AES-256 Client-Side Encryption:** The GitHub Personal Access Token (PAT) is encrypted using a **Master Admin Password** using the standard AES-256 algorithm.
- **Zero Raw Tokens in Git:** Only the encrypted ciphertext string is checked into this public repository. Without the Master Password, it is cryptographically impossible for anyone to decrypt and steal the token.
- **Transient Memory Authentication:** When logging into the dashboard, the token is decrypted locally in the browser's volatile memory and is used in-memory to call GitHub APIs. It is never sent to any external server.
- **Stealth Access (Easter Egg):** The admin dashboard does not have a visible link anywhere on the site. Instead, there is a **hidden Easter Egg trigger** in the navigation header that redirects to the login panel, keeping the dashboard completely hidden from casual visitors and recruiters.

---
*Created by [Rahul Mali](https://r-v-2003.github.io/RAHUL_MALI_PORTFOLIO.github.io/)*
