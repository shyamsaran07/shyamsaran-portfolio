<!DOCTYPE html>
<html lang="en">
<!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>N. Shyamsaran | Data Analyst Portfolio</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f8f7ff;
            color: #24213b;
            line-height: 1.7;
        }

        header {
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: white;
            position: sticky;
            top: 0;
            z-index: 10;
            box-shadow: 0 2px 10px #ddd;
        }

        header h2 {
            color: #7655e8;
        }

        nav a {
            text-decoration: none;
            color: #24213b;
            margin-left: 18px;
            font-size: 14px;
        }

        nav a:hover {
            color: #7655e8;
        }

        section {
            padding: 65px 8%;
        }

        .hero {
            min-height: 75vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
        }

        .tag {
            color: #7655e8;
            font-weight: bold;
            letter-spacing: 2px;
            font-size: 13px;
        }

        h1 {
            font-size: clamp(38px, 7vw, 68px);
            line-height: 1.15;
            margin: 18px 0;
        }

        h1 span {
            color: #7655e8;
        }

        h2 {
            font-size: 32px;
            margin: 12px 0 25px;
        }

        p {
            color: #65627a;
            max-width: 700px;
        }

        .button {
            display: inline-block;
            margin-top: 25px;
            padding: 12px 22px;
            background: #7655e8;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }

        .button:hover {
            background: #5c3bc5;
        }

        .light {
            background: white;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 22px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 22px #e9e5f5;
            transition: 0.2s;
        }

        .card:hover {
            transform: translateY(-4px);
        }

        .light .card {
            background: #f8f7ff;
        }

        .number {
            color: #7655e8;
            font-weight: bold;
        }

        .card h3 {
            margin: 10px 0;
        }

        .tags {
            margin: 15px 0;
        }

        .tags span {
            display: inline-block;
            background: #eae4ff;
            color: #6745d0;
            padding: 4px 9px;
            margin: 4px 3px 0 0;
            border-radius: 5px;
            font-size: 12px;
        }

        .project-link {
            display: inline-block;
            color: #7655e8;
            text-decoration: none;
            font-weight: bold;
            margin-top: 8px;
        }

        .project-link:hover {
            text-decoration: underline;
        }

        .footnote {
            font-size: 13px;
            margin-top: 20px;
        }

        footer {
            padding: 25px 8%;
            background: #24213b;
            color: white;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }

        footer a {
            color: white;
        }

        @media (max-width: 650px) {
            header {
                flex-direction: column;
                gap: 12px;
            }

            nav a {
                margin: 5px;
                font-size: 12px;
            }

            section {
                padding: 45px 6%;
            }

            h2 {
                font-size: 27px;
            }
        }
    </style>
</head>

<body>

<header>
    <h2>Shyamsaran.</h2>

    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<main>

    <section class="hero" id="home">
        <p class="tag">WELCOME TO MY PORTFOLIO</p>

        <h1>Hi, I'm <span>N. Shyamsaran</span></h1>

        <h2>Aspiring Data Analyst</h2>

        <p>
            I am an AI & Data Science student interested in data analysis,
            Python, data visualization, and solving real-world problems
            using data. I am currently learning and building my skills.
        </p>

        <a href="#projects" class="button">Explore My Projects ↗</a>
    </section>

    <section class="light" id="about">
        <p class="tag">GET TO KNOW ME</p>

        <h2>About Me</h2>

        <p>
            I am currently pursuing my studies in Artificial Intelligence
            and Data Science. I enjoy learning new technologies and
            understanding how data can help people make better decisions.
            My current goal is to develop practical data analysis skills
            and build projects for my portfolio.
        </p>
    </section>

    <section id="skills">
        <p class="tag">WHAT I'M LEARNING</p>

        <h2>My Skills</h2>

        <div class="grid">
            <article class="card">
                <h3>Python</h3>
                <p>Learning programming fundamentals and data analysis.</p>
            </article>

            <article class="card">
                <h3>Data Analysis</h3>
                <p>Learning to explore data and identify useful patterns.</p>
            </article>

            <article class="card">
                <h3>Pandas</h3>
                <p>Working with tables, datasets, and calculations.</p>
            </article>

            <article class="card">
                <h3>Data Visualization</h3>
                <p>Learning to present data through charts and graphs.</p>
            </article>
        </div>
    </section>

    <section class="light" id="projects">
        <p class="tag">MY WORK</p>

        <h2>Selected Projects</h2>

        <div class="grid">

            <article class="card">
                <span class="number">01</span>

                <h3>Sales Data Analysis</h3>

                <p>
                    Analyzed sample sales data using Python to calculate
                    revenue, compare product sales, and explore monthly
                    sales trends.
                </p>

                <div class="tags">
                    <span>Python</span>
                    <span>Pandas</span>
                    <span>Matplotlib</span>
                </div>

                <a href="sales_report.csv"
                   class="project-link"
                   download>
                    Download Sales Report ↓
                </a>

                <br>

                <a href="product_sales.png"
                   class="project-link"
                   target="_blank">
                    View Sales Chart ↗
                </a>
            </article>

            <article class="card">
                <span class="number">02</span>

                <h3>Customer Insights</h3>

                <p>
                    A future project idea to explore customer data,
                    discover patterns, and understand customer behaviour.
                </p>

                <div class="tags">
                    <span>Python</span>
                    <span>Data Analysis</span>
                </div>
            </article>

            <article class="card">
                <span class="number">03</span>

                <h3>Interactive Dashboard</h3>

                <p>
                    A future project idea to display important business
                    information through charts and visual reports.
                </p>

                <div class="tags">
                    <span>Power BI</span>
                    <span>Visualization</span>
                </div>
            </article>

        </div>

        <p class="footnote">
            Note: Sales Data Analysis uses sample data.
            Customer Insights and Interactive Dashboard are future project ideas.
        </p>
    </section>

    <section id="contact">
        <p class="tag">LET'S CONNECT</p>

        <h2>Contact Me</h2>

        <p>
            I am interested in learning, collaborating on projects,
            and exploring opportunities in data analysis.
        </p>

        <a href="mailto:your.email@example.com" class="button">
            Send Me an Email ↗
        </a>

        <p class="footnote">
            Replace your.email@example.com with your own email address
            when you are ready.
        </p>
    </section>

</main>

<footer>
    <span>© 2026 N. Shyamsaran</span>
    <span>Made with curiosity ♡</span>
    <a href="#home">Back to top ↑</a>
</footer>

</body>
</html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shyamsaran | Portfolio</title><style>
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:Arial,sans-serif;background:#0b1020;color:#fff;line-height:1.7}
header{background:#151b32;padding:18px 7%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.logo{font-size:24px;color:#a99aff;font-weight:bold}
nav{display:flex;flex-wrap:wrap;gap:14px}
nav a{color:white;text-decoration:none;font-size:14px}
nav a:hover{color:#a99aff}
section{padding:65px 8%;scroll-margin-top:20px}
.hero{min-height:80vh;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,#11172e,#292052)}
.tag{color:#b4a5ff;letter-spacing:3px;font-size:13px}
h1{font-size:clamp(38px,7vw,65px);line-height:1.2;margin:15px 0}
h1 span{color:#a99aff}
h2{font-size:30px;margin:12px 0 22px}
p{color:#c8cce0}
.hero p{max-width:650px}
.btn{display:inline-block;background:#8872ff;color:white;padding:11px 18px;border-radius:8px;text-decoration:none;margin:18px 10px 0 0}
.btn:hover{background:#6e57ed}
.secondary{background:transparent;border:1px solid #8872ff}
.light{background:#11172b}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.card{background:#191f39;border:1px solid #303653;padding:22px;border-radius:13px}
.card h3{margin-bottom:8px}
.card p{font-size:14px}
.badge{display:inline-block;background:#302752;color:#d0c7ff;padding:4px 9px;border-radius:5px;margin:10px 5px 0 0;font-size:12px}
.link{display:inline-block;color:#b5a7ff;text-decoration:none;margin-top:12px}
footer{padding:22px 8%;background:#070a14;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
footer a{color:#b5a7ff}
@media(max-width:600px){header{flex-direction:column}nav{justify-content:center;gap:10px}section{padding:45px 6%}}
</style></head><body><header>
<div class="logo">Shyamsaran.</div>
<nav>
<a href="#home">Home</a>
<a href="#about">About</a>
<a href="#education">Education</a>
<a href="#skills">Skills</a>
<a href="#projects">Projects</a>
<a href="#research">Interests</a>
<a href="#certificates">Certificates</a>
<a href="#resume">Resume</a>
<a href="#contact">Contact</a>
</nav>
</header><section class="hero" id="home">
<p class="tag">WELCOME TO MY PORTFOLIO</p>
<h1>Hi, I'm <span>Shyamsaran</span></h1>
<h2>Aspiring Data Analyst</h2>
<p>I am a final-year Artificial Intelligence and Data Science student learning Python, data analysis, and data visualization. I enjoy exploring data and finding useful insights.</p>
<a class="btn" href="#projects">Explore My Projects ↓</a>
<a class="btn secondary" href="#contact">Contact Me</a>
</section><section id="about" class="light">
<p class="tag">ABOUT ME</p>
<h2>Who Am I?</h2>
<p>I am a B.Tech Artificial Intelligence and Data Science student at Mahendra College of Engineering. I am developing my technical knowledge through practice and small projects. My career interest is data analytics, and I want to use data to understand problems and support better decisions.</p>
</section><section id="education">
<p class="tag">MY ACADEMIC JOURNEY</p>
<h2>Education</h2>
<div class="grid">
<div class="card">
<h3>Mahendra College of Engineering</h3>
<p>B.Tech — Artificial Intelligence and Data Science</p>
<p>Currently pursuing 4th Year</p>
<span class="badge">AI & Data Science</span>
</div>
</div>
</section><section id="skills" class="light">
<p class="tag">WHAT I'M LEARNING</p>
<h2>Technical Skills</h2>
<div class="grid">
<div class="card"><h3>Python</h3><p>Programming fundamentals and basic data processing.</p></div>
<div class="card"><h3>Data Analysis</h3><p>Exploring data and finding patterns.</p></div>
<div class="card"><h3>Pandas</h3><p>Working with tables and datasets.</p></div>
<div class="card"><h3>Matplotlib</h3><p>Creating charts and visual reports.</p></div>
</div>
</section><section id="projects">
<p class="tag">MY WORK</p>
<h2>Projects</h2>
<div class="grid">
<div class="card">
<h3>Sales Data Analysis</h3>
<p>Analyzed sample sales data using Python to explore product sales and revenue trends.</p>
<span class="badge">Python</span><span class="badge">Pandas</span><span class="badge">Matplotlib</span>
<br><a class="link" href="sales_report.csv" download>Download Sales Report ↓</a>
<br><a class="link" href="product_sales.png" target="_blank">View Sales Chart ↗</a>
</div>
<div class="card">
<h3>Customer Insights</h3>
<p>Future project idea: explore customer data and discover behaviour patterns.</p>
<span class="badge">Python</span><span class="badge">Analytics</span>
</div>
<div class="card">
<h3>Interactive Dashboard</h3>
<p>Future project idea: build a dashboard to display useful business information.</p>
<span class="badge">Power BI</span><span class="badge">Visualization</span>
</div>
</div>
<p style="margin-top:18px">Note: Sales Data Analysis is a sample-data project. The other two are planned projects.</p>
</section><section id="research" class="light">
<p class="tag">AREAS OF INTEREST</p>
<h2>Research Interests</h2>
<div class="grid">
<div class="card"><h3>Data Analytics</h3><p>Finding patterns and useful insights in data.</p></div>
<div class="card"><h3>Artificial Intelligence</h3><p>Exploring AI methods for solving practical problems.</p></div>
<div class="card"><h3>Data Visualization</h3><p>Presenting data through clear charts and dashboards.</p></div>
</div>
</section><section id="certificates">
<p class="tag">MY ACHIEVEMENTS</p>
<h2>Certificates</h2>
<div class="grid">
<div class="card">
<h3>Certificate 01</h3>
<p>Add the title of a course or training certificate you have completed.</p>
</div>
<div class="card">
<h3>Certificate 02</h3>
<p>Add another genuine certificate or workshop achievement here.</p>
</div>
<div class="card">
<h3>Certificate 03</h3>
<p>You can add more certificates when you have the files ready.</p>
</div>
</div>
<p style="margin-top:18px">These are placeholders, not actual certificates. Replace them with your real achievements.</p>
</section><section id="resume" class="light">
<p class="tag">MY RESUME</p>
<h2>Resume</h2>
<p>My resume will be available to view or download after I upload my PDF file.</p>
<a class="btn" href="resume.pdf" download>Download My Resume ↓</a>
<p style="margin-top:12px;font-size:13px">Upload your PDF with the filename resume.pdf for this button to work.</p>
</section><section id="contact">
<p class="tag">LET'S CONNECT</p>
<h2>Contact Me</h2>
<p>I'm interested in learning, collaborating on projects, and exploring opportunities in data analytics.</p>
<a class="btn" href="mailto:your.email@example.com">Send Me an Email ↗</a>
<p style="margin-top:12px;font-size:13px">Replace this sample email address with your actual email address.</p>
</section><footer>
<span>© 2026 Shyamsaran</span>
<span>Learning • Building • Growing</span>
<a href="#home">Back to Top ↑</a>
</footer></body>
</html>
