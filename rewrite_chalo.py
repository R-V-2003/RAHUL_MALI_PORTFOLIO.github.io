import re

with open('case-study-chalo.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_main = '''
    <main class="cs-content">
      <div class="container">
        <!-- Hero Section -->
        <section class="cs-hero">
          <div class="cs-hero__text">
            <h1 class="cs-hero__title">CHALO &ndash; The Ride-Hailing Revolution</h1>
            <p class="cs-hero__desc">
              An original, full-stack startup idea designed to bridge the gap between affordable shared transit and premium tech reliability. From deep market research and UI design in Figma, all the way to Node.js backend development and Dockerized deployment on AWS. This isn't a clone; it's a complete product lifecycle.
            </p>
            <div class="cs-hero__meta">
              <span class="meta-tag">Role: Founder, Product Designer &amp; Full-Stack Developer</span>
              <span class="meta-tag">Timeline: Q2 2026</span>
              <span class="meta-tag">Tech Stack: React, Node.js, SQLite, Docker, AWS ECS</span>
            </div>
            <div class="cs-hero__actions">
              <a href="./chalo.apk" class="btn btn--primary">
                <svg viewBox="0 0 24 24"><path d="M14 3h7v7h-2V6.414l-9.293 9.293-1.414-1.414L17.586 5H14Z"></path></svg>
                Download APK
              </a>
            </div>
          </div>
        </section>

        <!-- Image Gallery/Showcase -->
        <section class="cs-showcase">
          <img
            src="./chalo_card_image.png"
            alt="CHALO App Mockups showcasing passenger and driver flows"
            class="cs-hero-img"
          />
        </section>

        <!-- Article Content -->
        <article class="cs-article">
          <div class="cs-article__grid">
            
            <div class="cs-article__main">
              <h2>1. Market Research & Problem Identification</h2>
              <p>
                <strong>The Daily Struggle:</strong> Millions of commuters in Tier-1 and Tier-2 cities travel daily under the hot sun. Public transit schedules are unpredictable, and booking a private cab (like Uber or Ola) daily costs a fortune. The shared transit market (shared autos) operates entirely offline, leaving passengers guessing when their next ride will arrive, while drivers circle empty looking for passengers.
              </p>
              <p>
                <strong>The Opportunity:</strong> There is a massive, unserved middle market. Bridging the "First &amp; Last Mile" gap requires combining the unmatched affordability of offline shared transit with the premium tracking and AI technology of modern ride-hailing apps.
              </p>

              <h2>2. The Solution: CHALO</h2>
              <p>
                Chalo is a full-stack smart shuttle management and ride-hailing platform. It provides:
              </p>
              <ul>
                <li><strong>For Passengers:</strong> A stunning map-based UI providing real-time visualization of shuttles, transparent fixed fares (e.g., ₹10 per stop), and guaranteed rides.</li>
                <li><strong>For Drivers:</strong> A dedicated "Driver Dashboard" helping them select high-demand routes, navigate efficiently, and minimize empty trips (deadhead miles).</li>
              </ul>
              <div class="cs-image-wrapper" style="border: 2px dashed #4ade80; padding: 40px; text-align: center; border-radius: 12px; margin: 2rem 0;">
                <p style="color: #4ade80; margin: 0; font-weight: bold;">[Placeholder for User-Side Flow Screens]</p>
              </div>

              <h2>3. UI/UX Design & User Research</h2>
              <p>
                The interface was meticulously crafted in Figma to prioritize speed and usability. I integrated a giant, gorgeous map right in the center of the experience, because a ride-hailing app needs a map taking up 70% of the screen.
              </p>
              <p>
                <strong>AI Smart Assistant ("Bhaya"):</strong> A floating chat widget powered by AI. Just type "Gurukul to Thaltej?" and Bhaya instantly provides walking directions, ETAs, and suggests the right shuttle to board.
              </p>
              <div class="cs-image-wrapper" style="border: 2px dashed #60a5fa; padding: 40px; text-align: center; border-radius: 12px; margin: 2rem 0;">
                <p style="color: #60a5fa; margin: 0; font-weight: bold;">[Placeholder for Driver-Side Flow Screens]</p>
              </div>

              <h2>4. Full-Stack Development</h2>
              <p>
                Moving from design to code, I architected a robust, scalable system:
              </p>
              <ul>
                <li><strong>Frontend:</strong> React (via Vite) packaged for mobile using Ionic Capacitor. Real-time route animation is powered by the Google Maps JavaScript API.</li>
                <li><strong>True Road-Aligned Pathfinding:</strong> Unlike simple straight lines, the database stores hundreds of intermediate coordinates for each route. The frontend interpolates these coordinates to animate the shuttle icon smoothly along the actual curves of the city roads.</li>
                <li><strong>Backend:</strong> A high-performance Node.js &amp; Express server backed by an SQLite database (<code>better-sqlite3</code>). Authentication is handled securely via JWT and <code>bcryptjs</code>.</li>
              </ul>

              <h2>5. AWS Deployment & DevOps</h2>
              <p>
                Building the app was only half the battle. I implemented a modern CI/CD pipeline to host the application in the cloud:
              </p>
              <p>
                The entire stack is containerized using <strong>Docker</strong> (multi-stage builds). Deployment is fully automated via <strong>GitHub Actions</strong>. Any push to the main branch triggers a workflow that builds the Docker image, pushes it to <strong>Amazon ECR</strong>, and updates an <strong>Amazon ECS</strong> Task Definition to perform a rolling update without downtime.
              </p>
            </div>

            <!-- Sidebar -->
            <aside class="cs-sidebar">
              <div class="cs-sidebar-block">
                <h4>The Verdict</h4>
                <p>
                  Chalo is more than just an app; it's a movement to organize the disorganized transit sector. It proves my capability to take a raw startup idea, conduct user research, design the interface, code the full stack, and deploy it to enterprise-grade AWS infrastructure.
                </p>
              </div>
            </aside>

          </div>
        </article>
      </div>
    </main>
'''

new_content = re.sub(r'<main class="cs-content">.*?</main>', new_main, content, flags=re.DOTALL)

with open('case-study-chalo.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
