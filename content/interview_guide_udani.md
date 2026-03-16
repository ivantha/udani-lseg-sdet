# Interview Preparation Guide: Udani Weerasinghe

**Target Role:** Associate Lead, SDET — LSEG (R0098555)
**Interviewers:** Amy Lee (Director, Quality Engineering) & Andy Purtell (QE Manager)
**Date Prepared:** 2026-03-15

---

## Table of Contents

1. [Interview Panel Dynamics](#1-interview-panel-dynamics)
2. [The Career Gap — Your Biggest Challenge](#2-the-career-gap--your-biggest-challenge)
3. [Your Narrative Arc — The Story to Tell](#3-your-narrative-arc--the-story-to-tell)
4. [Technical Question Areas](#4-technical-question-areas)
5. [Behavioural and Situational Questions](#5-behavioural-and-situational-questions)
6. [Financial Domain — Bridging the Gap](#6-financial-domain--bridging-the-gap)
7. [Infrastructure and Systems Questions](#7-infrastructure-and-systems-questions)
8. [Leadership and Team Questions](#8-leadership-and-team-questions)
9. [AI and Modern QA Practices](#9-ai-and-modern-qa-practices)
10. [Questions About LSEG Specifically](#10-questions-about-lseg-specifically)
11. [Handling Your Weak Areas](#11-handling-your-weak-areas)
12. [Questions You Should Ask Them](#12-questions-you-should-ask-them)
13. [Practical Tips and Do/Don't Lists](#13-practical-tips-and-dodont-lists)
14. [Pre-Interview Checklist](#14-pre-interview-checklist)

---

## 1. Interview Panel Dynamics

Understanding the two interviewers and tailoring your approach to each is critical.

### Amy Lee — Director, Quality Engineering

| Attribute | Detail |
|---|---|
| **Role** | Director-level; strategic decision-maker |
| **Background** | Unix admin → Server management → QA leadership; Thomson Reuters → Refinitiv → LSEG |
| **Current Focus** | AI-driven test automation |
| **What she's evaluating** | Strategic thinking, leadership potential, cultural fit, long-term vision |
| **Communication style** | She has deep technical roots but now operates at a strategic level. Speak in terms of outcomes, quality strategy, and business impact — not just tools and frameworks |

**How to approach Amy:**
- Lead with *why*, not *what*. Instead of "I used Selenium," say "I chose Selenium for this context because... and the outcome was..."
- Show you think about quality at the organisational level, not just the test case level.
- Connect your MSc and MBA to how you think about quality as a business enabler.
- Show genuine curiosity about AI in QA — this is her current passion project. Ask about it.
- Demonstrate you can work across global teams (she's managed global QA teams for years).

### Andy Purtell — QE Manager

| Attribute | Detail |
|---|---|
| **Role** | Likely your direct manager if hired |
| **Background** | QA Engineer → Senior QA → Tech Lead → QE Manager; deep Elektron/real-time data experience |
| **Current Focus** | Multi-platform testing at scale (Windows, Linux, Cloud), 500+ products |
| **What he's evaluating** | Technical depth, hands-on capability, team fit, growth potential |
| **Communication style** | Grew up through the ranks; values practical, specific, grounded answers. Can detect superficial responses |

**How to approach Andy:**
- Lead with *specifics*. He wants to hear about real problems you solved, real frameworks you built, real bugs you caught.
- Be honest about what you don't know — his reputation as a mentor means he values coachability over perfection.
- Show you can work independently (the JD emphasises this) while communicating effectively.
- Demonstrate attention to detail, especially around documentation and test maintenance.
- Be ready for scenario-based questions drawn from his real-time data testing experience.

### The Dynamic Between Them

Amy and Andy likely have a coordinated evaluation approach:

- **Amy screens for**: Will this person grow into a quality leader? Do they think strategically? Will they fit our culture?
- **Andy screens for**: Can this person actually do the work? Will they fit my team? Can I develop them?

You need to pass **both** filters. A candidate who impresses Amy with vision but can't demonstrate practical skills to Andy won't get through — and vice versa.

---

## 2. The Career Gap — Your Biggest Challenge

This will almost certainly come up. Both interviewers will notice that your last QA role ended in October 2023 — approximately 2.5 years ago. How you handle this question could make or break the interview.

### What They're Really Asking

When they ask about the gap, they're actually evaluating three things:

1. **Are your skills current?** Test automation has evolved significantly since 2023. Do you still know what you're doing?
2. **Are you committed to QA as a career?** Did you leave the field intentionally? Will you leave again?
3. **Can you be productive quickly?** Or will there be a long ramp-up period?

### The Narrative to Prepare

Frame the gap as a **deliberate investment**, not an absence:

> "After 3.5 years of intensive QA work at Sysco LABS, I made a deliberate decision to invest in my education — completing my MSc in Cloud Native Computing with First Class Honours at TUS in Ireland. This was a strategic choice: I saw cloud-native systems becoming the standard for enterprise software, and I wanted to understand that architecture deeply, not just test the surface. During my time in Ireland, I also stayed connected to the QA field by [mention anything: personal projects, online courses, ISTQB Advanced certification study, reading, community involvement]. My ISTQB Advanced Level TTA certification in April 2025 demonstrates that I've kept my testing knowledge not just current, but deepened it."

### Critical: Prepare Specific Evidence of Continued Learning

You **must** have concrete examples of what you did during 2023-2026 to stay technically sharp. If you don't have them, create them before the interview:

- **ISTQB CTAL-TTA (April 2025)** — This is your strongest evidence. Emphasise the study process, what you learned, and how the advanced syllabus covers topics beyond your work experience.
- **MSc coursework** — What testing-relevant topics did your Cloud Native Computing MSc cover? Docker? Kubernetes? Microservices testing? CI/CD pipelines? Even if the degree was completed in 2024, the knowledge is current.
- **Personal projects** — Even a small automation project on GitHub would help enormously. If you don't have one, consider building a small Selenium/Playwright + REST Assured + Jenkins pipeline project before the interview.
- **Online courses or certifications** — Any Udemy, Coursera, or platform courses in relevant areas (performance testing, AI in testing, financial markets basics).
- **Community involvement** — QA meetups, conferences attended, articles read, online forums participated in.

### What NOT to Say

- Don't be defensive or apologetic about the gap.
- Don't say "I was looking for the right opportunity" — this sounds passive.
- Don't pretend the Student Experience Assistant role was technical.
- Don't inflate the timeline — if asked directly, be honest about 3.5 years of QA experience.

---

## 3. Your Narrative Arc — The Story to Tell

Every interview is a story. Yours should follow this arc:

### Opening (Who You Are)

> "I'm a quality engineering professional who combines hands-on test automation expertise with strategic thinking. I've spent 3.5 years building and leading test automation across complex enterprise platforms — SAP, Salesforce, and E-Commerce systems — and I've recently deepened my knowledge with a First Class MSc in Cloud Native Computing and an ISTQB Advanced Level certification."

### Middle (What Makes You Different)

> "What sets me apart is the combination of technical depth and business perspective. My MBA helps me understand quality from a business impact standpoint — not just 'did the test pass' but 'does this quality strategy serve the business goals.' My MSc gives me the architectural understanding of cloud-native systems that modern SDET work demands. And my hands-on experience gives me the practical skills to actually build and maintain automation at scale."

### Bridge to LSEG (Why This Role)

> "LSEG represents exactly the kind of challenge I'm looking for — a global financial infrastructure company where quality isn't just nice to have, it's mission-critical. The scale of your systems, the real-time data delivery, the regulatory requirements — these create testing challenges that genuinely excite me. I'm particularly interested in how your quality engineering team is approaching AI-driven test automation and how I can contribute to that evolution."

---

## 4. Technical Question Areas

### 4.1 Test Automation Framework Design

**Likely asked by:** Andy (primary), Amy (at a higher level)

**Expected questions:**

- *"Walk me through how you would design a test automation framework from scratch."*
- *"How did you architect your automation framework at Sysco LABS?"*
- *"What's the difference between a test automation framework and a test automation script?"*
- *"How do you decide what to automate and what to test manually?"*

**How to answer:**

Use the **Page Object Model (POM)** as your foundation, since this is what most enterprise Selenium frameworks use:

```
Framework Architecture:
├── Test Layer (TestNG/JUnit test classes)
├── Business Logic Layer (step definitions, workflows)
├── Page Object Layer (page classes, element locators)
├── Utility Layer (config, logging, reporting, data providers)
├── Data Layer (test data, environment configs)
└── CI/CD Integration (Jenkins pipeline, reports)
```

Speak to specific design decisions you made at Sysco LABS:
- Why you chose Selenium + TestNG over alternatives.
- How you handled test data management.
- How you managed environment configurations (dev, staging, production).
- How you handled cross-browser testing (mention BrowserStack).
- How you integrated with CI/CD (Jenkins + Git + AWS).

**Key point for Andy:** He manages test frameworks across 500+ products on 3 platforms. Show that you understand the *maintenance* challenge, not just the initial build. Talk about:
- How you kept locators stable when the UI changed.
- How you managed framework versioning.
- How you reduced flaky tests.
- How you onboarded new team members to the framework.

### 4.2 API Testing and REST Assured

**Likely asked by:** Andy

**Expected questions:**

- *"How did you use REST Assured in your projects?"*
- *"How do you validate API responses beyond just status codes?"*
- *"How do you handle API authentication in test automation?"*
- *"What's your approach to testing API integrations between systems?"*

**How to answer:**

Draw from your Salesforce/SAP integration testing experience:
- You tested APIs that connected Salesforce, SAP, and E-Commerce systems.
- You validated response payloads, headers, status codes, and response times.
- You tested error scenarios — invalid inputs, authentication failures, timeout handling.
- You used REST Assured's fluent API for readable, maintainable test code.

**Example to prepare:**

> "In the Vendor Invoice Management project, we had APIs that connected SAP to Salesforce for invoice processing. I automated the entire API flow — creating invoices in SAP, verifying they appeared correctly in Salesforce via the integration API, and validating the data transformation at each step. This caught several data mapping issues before they reached production, including a currency conversion bug that would have affected invoice totals."

### 4.3 CI/CD Integration

**Likely asked by:** Andy (implementation details), Amy (strategic value)

**Expected questions:**

- *"How did you integrate your test automation into CI/CD pipelines?"*
- *"What quality gates did you define in your pipeline?"*
- *"How did you handle test failures in the pipeline?"*
- *"What's your approach to determining which tests run at each pipeline stage?"*

**How to answer:**

Describe a tiered testing approach in Jenkins:
1. **Commit stage:** Unit tests + critical smoke tests (fast, blocking).
2. **Build stage:** API tests + core functional tests (medium, blocking).
3. **Deploy to staging:** Full regression suite (longer, non-blocking but alerts on failure).
4. **Pre-production:** Smoke tests on production-like environment.

Mention specific Jenkins features you used:
- Parameterised builds for environment selection.
- Pipeline-as-code (Jenkinsfile).
- Integration with Git for trigger-on-push.
- SonarQube quality gates for code quality.
- Test report publishing and trend analysis.

### 4.4 Selenium-Specific Deep Dive

**Likely asked by:** Andy

**Expected questions:**

- *"How do you handle dynamic elements in Selenium?"*
- *"What's your approach to waits? Explain implicit vs explicit vs fluent waits."*
- *"How do you handle iframes, shadow DOM, or multi-window scenarios?"*
- *"How did you handle Salesforce testing with Selenium? What were the challenges?"*

**Salesforce + Selenium is a strong differentiator** — Salesforce's Lightning framework is notoriously difficult to automate due to dynamic element IDs, shadow DOM, and iframes. If you have specific strategies you used, prepare them in detail:

- Custom wait conditions for Lightning component loading.
- JavaScript executor for interacting with shadow DOM elements.
- Handling Salesforce's dynamic record IDs in test data.
- Managing Salesforce sandbox environments for testing.

### 4.5 Programming and Coding

**Likely asked by:** Andy

**Expected questions:**

- *"Write a function to [simple algorithm or data structure task]."*
- *"How would you parse a JSON response and validate specific fields?"*
- *"Write a method that retries a flaky API call up to 3 times with exponential backoff."*
- *"Review this test code — what would you improve?"*

**Preparation:**

- Be comfortable writing Java code on a whiteboard or shared screen.
- Practice common patterns: reading/writing files, parsing JSON/XML, string manipulation, collections operations.
- Know Java OOP concepts well — inheritance, polymorphism, interfaces, abstraction — and how they apply to framework design (e.g., base page class, interface for page actions).
- Be ready to write a simple TestNG test with assertions.
- Know the difference between `assertEquals`, `assertTrue`, `assertThat` and when to use each.

### 4.6 Test Case Design and Strategy

**Likely asked by:** Both (Amy at strategic level, Andy at practical level)

**Expected questions:**

- *"How do you decide test coverage priorities for a new feature?"*
- *"Explain boundary value analysis and equivalence partitioning with an example."*
- *"How do you approach risk-based testing?"*
- *"What's your approach to regression test selection — do you run everything every time?"*

**Leverage your ISTQB CTAL-TTA here.** The Advanced Level syllabus covers:
- Condition testing, decision testing, modified condition/decision coverage (MC/DC).
- Statement coverage vs branch coverage vs path coverage.
- White-box test techniques.
- Test design based on risk analysis.

Prepare a concrete example of risk-based testing from your Sysco LABS experience:

> "When we had limited time before a Salesforce release, I used risk-based test prioritisation. I mapped each test case to business risk (impact × likelihood of failure) and technical risk (code change proximity × complexity). High-risk cases ran first and were automated; medium-risk cases were included in the regression suite; low-risk cases were deferred to the next cycle. This approach helped us maintain quality while meeting aggressive release timelines."

### 4.7 Performance Testing

**Likely asked by:** Andy (specific tools/experience), Amy (strategic understanding)

**This is a gap area for you.** The JD mentions performance testing, and LSEG's real-time data delivery systems make performance critical.

**Expected questions:**

- *"Do you have experience with performance testing? What tools have you used?"*
- *"How would you approach performance testing for a real-time data system?"*
- *"What's the difference between load testing, stress testing, and endurance testing?"*

**Honest approach:**

If you haven't done significant performance testing, be honest but show awareness:

> "My direct experience with dedicated performance testing tools is limited — my work focused primarily on functional and integration test automation. However, I understand the fundamentals: load testing to validate capacity, stress testing to find breaking points, endurance testing for memory leaks and degradation over time. I incorporated basic performance validation in my API tests using REST Assured — response time assertions and throughput checks — but I haven't done large-scale load testing with tools like JMeter or Gatling. It's an area I'm actively working to develop, especially given how critical performance is in financial markets infrastructure."

**Preparation to reduce this gap before the interview:**

- Install JMeter and run a basic load test against a public API. Familiarise yourself with thread groups, samplers, listeners, and assertions.
- Understand key performance metrics: response time (mean, median, p95, p99), throughput (requests/sec), error rate, concurrent users.
- Learn the basic concepts of how real-time market data systems work and why latency matters (a 1ms delay in trading systems can mean millions in losses).

### 4.8 Database and SQL Testing

**Likely asked by:** Andy

**Expected questions:**

- *"How do you validate data in the database as part of your testing?"*
- *"How do you set up and manage test data?"*
- *"Write a SQL query to find duplicate records in a table."*
- *"How did you validate data integrity between SAP and Salesforce?"*

**How to answer:**

Draw from your SAP/Salesforce/E-Commerce integration work:
- You likely validated data transformations between systems — an invoice created in SAP should appear with correct values in Salesforce.
- You used SQL to verify data in staging databases (PostgreSQL, Oracle).
- You managed test data creation and cleanup to ensure test independence.

**Prepare basic SQL patterns:**

```sql
-- Find duplicates
SELECT column, COUNT(*) FROM table GROUP BY column HAVING COUNT(*) > 1;

-- Validate data between tables (join-based validation)
SELECT a.id, a.amount, b.amount
FROM sap_invoices a
JOIN sf_invoices b ON a.invoice_id = b.external_id
WHERE a.amount != b.amount;

-- Check for null or missing data
SELECT * FROM orders WHERE customer_id IS NULL OR order_date IS NULL;
```

---

## 5. Behavioural and Situational Questions

### 5.1 The STAR Method

For all behavioural questions, use the **STAR** framework:

- **S**ituation — set the context (brief).
- **T**ask — what was your specific responsibility.
- **A**ction — what you specifically did (this is the longest part).
- **R**esult — the measurable outcome.

### 5.2 Common Behavioural Questions and Suggested Answers

#### "Tell me about a time you found a critical bug late in the release cycle."

**Your angle:** Use the E-Commerce project where you *"identified 20 critical defects prior to production release."*

> **S:** "In the Hybris E-Commerce project, we were three days from a major release when I was running the final regression cycle."
> **T:** "I needed to validate the entire order flow end-to-end, including payment processing and inventory updates."
> **A:** "During automation execution, I noticed that one specific combination of discount code + promotional pricing was calculating the final amount incorrectly — a race condition between the discount engine and the pricing service. I immediately raised it with the dev team, provided the exact reproduction steps from my automated test logs, and worked with the developer to identify that the issue was in the async event handling between the two services."
> **R:** "The fix was deployed within 24 hours, and we shipped on time. Without the automated test catching this, customers would have been charged incorrect amounts — a direct revenue and trust impact."

#### "Tell me about a time you had to push back on a deadline or scope."

**Your angle:** Frame around risk-based testing decisions.

> **S:** "During a Salesforce Service Cloud release, the product owner wanted to add three new features to an already-packed sprint."
> **T:** "As the QA lead for that phase, I needed to assess whether we could maintain quality with the expanded scope."
> **A:** "I did a quick risk assessment and presented the product owner with three options: (1) extend the timeline by one sprint, (2) reduce scope to the two highest-priority features, or (3) proceed with all three but accept that we'd only have automated coverage for the critical paths and manual testing for edge cases. I quantified the risk of each option in terms of defect escape probability."
> **R:** "The product owner chose option 2, and we delivered two solid, well-tested features rather than three fragile ones. The third feature was delivered the following sprint with full test coverage."

#### "Tell me about a time you mentored someone."

**Your angle:** Use your mentoring at Sysco LABS and/or your Teaching Assistant role.

> **S:** "At Sysco LABS, I had a junior tester join my team who was strong in manual testing but had no automation experience."
> **T:** "I was responsible for getting them up to speed on our Selenium + TestNG framework within their first month."
> **A:** "Rather than just pointing them to documentation, I created a structured 4-week onboarding plan: Week 1 was Java fundamentals and our codebase walkthrough. Week 2 was writing their first page objects. Week 3 was creating their first end-to-end test. Week 4 was code review and refactoring. I paired with them daily for the first two weeks, gradually reducing to weekly check-ins. I also had them present their work to the team at the end of each week."
> **R:** "By month two, they were independently writing automation scripts and contributing to code reviews. Within six months, they were one of our most productive automation engineers. The experience also helped me develop a reusable onboarding template that we used for future hires."

#### "Tell me about a time you dealt with a conflict in the team."

> **S:** "A developer on our team consistently pushed back on bugs I raised, arguing they were 'by design' or 'edge cases not worth fixing.'"
> **T:** "I needed to maintain a productive working relationship while ensuring quality standards were met."
> **A:** "Instead of escalating immediately, I changed my approach. For each defect, I started including business impact analysis — not just 'this field shows incorrect data' but 'this affects invoice reconciliation for 15% of our UK customers, which could result in payment disputes.' I also started inviting the developer to participate in test case reviews before I tested, so they could see the scenarios I'd be covering and flag concerns early."
> **R:** "The relationship improved significantly. The developer started proactively asking about test coverage for their features, and our defect escape rate dropped by about 30% in the following quarter."

#### "Why are you looking to move? Why LSEG?"

**Critical question.** Your answer must address the career gap positively:

> "After my intensive period at Sysco LABS, I invested in my education — completing my MSc in Cloud Native Computing and then my ISTQB Advanced certification. Now I'm ready to bring that deeper knowledge back to a challenging technical environment. LSEG represents that challenge: you're operating at the intersection of financial markets, real-time data, and global infrastructure — this is where quality engineering has the highest stakes and the greatest impact. I'm particularly drawn to LSEG's investment in AI-driven quality engineering, and I believe my combination of hands-on automation experience, cloud-native architecture knowledge, and business understanding from my MBA positions me well to contribute meaningfully."

#### "Where do you see yourself in 3-5 years?"

> "I see myself growing into a senior quality engineering leader — someone who shapes QA strategy for a product area, not just individual test suites. In 3 years, I'd like to be leading a QA stream, driving test automation architecture decisions, and mentoring the next generation of SDETs. In 5 years, I'd like to be influencing quality practices at an organisational level — perhaps driving initiatives like AI-augmented testing or quality metrics that connect directly to business outcomes. LSEG's scale and the complexity of financial markets infrastructure gives me the right environment to develop those capabilities."

---

## 6. Financial Domain — Bridging the Gap

This is a known weakness. Both interviewers have spent their entire careers in financial data. Here's how to bridge this.

### What You Must Know Before the Interview

#### About LSEG

- **What LSEG is:** London Stock Exchange Group — a global financial markets infrastructure and data provider. Not just the London Stock Exchange; LSEG also owns Refinitiv (data analytics), FTSE Russell (indexes), and LCH (clearing house).
- **Scale:** 25,000 employees, 65 countries, processes billions of transactions.
- **Core products:** Real-time market data delivery (Elektron/LSEG Real-Time), trading platforms, index calculation (FTSE 100, Russell 2000), post-trade clearing and settlement.
- **Values:** Integrity, Partnership, Excellence, Change.

#### About Elektron / LSEG Real-Time

This is particularly important because both interviewers have worked on this:

- **What it is:** LSEG Real-Time (formerly Elektron) is the backbone infrastructure for delivering real-time market data to financial institutions globally.
- **What it does:** Distributes real-time prices, trades, news, and analytics for financial instruments across the world.
- **Why quality matters:** A data error or latency spike in market data can cause incorrect trading decisions worth millions. Quality in this context is not just about "no bugs" — it's about data integrity, latency, throughput, and availability at near-100% uptime.
- **Scale:** Handles data for millions of financial instruments across global markets.

#### Financial Markets Basics

- **Market data:** Real-time prices of stocks, bonds, currencies, commodities. This is the core of what LSEG delivers.
- **Latency:** The time it takes for data to travel from exchange to consumer. In financial markets, microseconds matter.
- **FIX protocol:** Financial Information eXchange — the standard messaging protocol for trading. Know it exists even if you haven't used it.
- **Regulatory compliance:** Financial systems must comply with regulations (MiFID II in Europe, SEC rules in the US). Testing must account for regulatory requirements.
- **Market hours and global markets:** Different exchanges operate in different time zones. Systems must handle opening, closing, and continuous trading phases.

### How to Leverage What You Have

**Your Chartered Accountancy background is an untapped asset here.** Most SDET candidates have zero financial knowledge. You have:

- Business Level completed in Chartered Accountancy — you understand financial statements, accounting principles, and business processes.
- This gives you a foundation for understanding financial data, reporting, and compliance that pure engineers lack.

**Frame it like this:**

> "While I haven't worked directly in financial markets, I do have a foundation in financial systems through my Chartered Accountancy studies — I completed the Business Level at CA Sri Lanka. This gives me a working understanding of financial data, reporting, and compliance requirements. Combined with my experience testing enterprise integration systems (SAP → Salesforce), I'm familiar with the complexities of financial data flows, data transformation, and the importance of data integrity. I'm eager to deepen this into financial markets specifically."

### Questions They May Ask About Financial Domain

- *"What do you know about LSEG?"* — Prepare a 60-second summary (see above).
- *"Have you worked with financial systems before?"* — Bridge with CA background and SAP experience.
- *"How would testing in a financial markets context differ from your previous experience?"* — Emphasise: higher stakes, stricter data integrity requirements, latency sensitivity, regulatory compliance, 24/7 availability expectations.
- *"What do you know about real-time data delivery?"* — Show awareness of Elektron/LSEG Real-Time and the importance of low-latency, high-throughput data distribution.

---

## 7. Infrastructure and Systems Questions

Both interviewers come from infrastructure backgrounds. Amy was a Unix admin. Andy tested across Windows, Linux, and Cloud. The JD requires "proficiency in Windows server and/or Unix/Linux."

### Expected Questions

- *"Are you comfortable working in a Linux/Unix environment?"*
- *"How do you set up and maintain test environments?"*
- *"How would you troubleshoot a test failure that only occurs on Linux but not on Windows?"*
- *"How do you manage test environments in the cloud?"*

### How to Answer

**Leverage your MSc in Cloud Native Computing.** Even if your Sysco LABS work was primarily application-level, your MSc almost certainly covered:

- Linux fundamentals (most cloud-native systems run on Linux).
- Docker containers and Kubernetes orchestration.
- Cloud infrastructure (AWS/Azure — both on your CV).
- Networking basics (how services communicate in cloud-native architectures).

**Frame it like this:**

> "At Sysco LABS, my test automation ran on cloud-hosted environments in AWS, and I managed environment setup and test data configuration. My MSc in Cloud Native Computing significantly deepened my infrastructure knowledge — I worked with Docker containers, Kubernetes orchestration, Linux-based systems, and cloud-native deployment patterns. While I haven't done full-time Unix system administration, I'm comfortable working in Linux environments for test execution, log analysis, and basic scripting."

### What to Brush Up On Before the Interview

- **Basic Linux commands:** `grep`, `awk`, `sed`, `tail`, `ps`, `top`, `df`, `chmod`, `ssh`, `scp`. Be able to explain what each does.
- **Log analysis:** How to find errors in log files (`grep -i error /var/log/app.log`, `tail -f` for real-time monitoring).
- **Process management:** How to check running processes, kill stuck processes, check resource usage.
- **Basic networking:** `ping`, `curl`, `netstat`/`ss`, `traceroute`. Understanding TCP/IP at a basic level — what happens when you type a URL in a browser (DNS → TCP handshake → HTTP request → response).
- **Docker basics:** `docker ps`, `docker logs`, `docker exec`, Dockerfile structure. If your MSc covered this, refresh it.

---

## 8. Leadership and Team Questions

The role title says "Associate Lead." Even though the JD describes more of an IC role, both interviewers will assess leadership capability.

### Expected Questions

#### From Amy (strategic leadership):

- *"How do you define a QA strategy for a new project?"*
- *"How do you measure quality? What metrics do you use?"*
- *"How do you influence developers to care about quality?"*
- *"How do you decide what to invest automation effort in vs. what stays manual?"*

**Quality Metrics to know and discuss:**

| Metric | What It Measures | Why It Matters |
|---|---|---|
| Defect escape rate | Bugs found in production vs. found in testing | Measures testing effectiveness |
| Automation coverage | % of test cases automated | Measures automation maturity |
| Test execution time | How long the regression suite takes | Impacts release velocity |
| Flaky test rate | % of tests that intermittently fail | Measures automation reliability |
| Mean time to detect (MTTD) | How quickly defects are found after introduction | Measures shift-left effectiveness |
| Defect density | Defects per KLOC or per feature | Measures code quality |

#### From Andy (team-level leadership):

- *"How do you onboard a new tester onto an existing automation framework?"*
- *"How do you handle a team member who isn't meeting quality standards in their test code?"*
- *"How do you prioritise work when multiple teams need QA support simultaneously?"*
- *"How do you conduct effective code reviews for test automation?"*

**Your strengths here:**
- You mentored junior testers at Sysco LABS.
- You delivered workshops on test automation.
- You led QA phases across multiple development teams.
- You were Teaching Assistant at Open University.
- You were Deputy Tribe Chief at Sysco LABS.

**Prepare 2-3 specific stories** that demonstrate:
1. A time you taught someone a technical skill and they improved measurably.
2. A time you coordinated QA work across multiple teams or projects.
3. A time you made a process improvement recommendation that was adopted.

---

## 9. AI and Modern QA Practices

**This is particularly important for Amy Lee**, whose LinkedIn headline focuses on AI-driven test automation.

### Expected Questions

- *"What's your view on AI in test automation?"*
- *"Have you used any AI-assisted testing tools?"*
- *"How do you think generative AI will change the SDET role?"*
- *"What emerging QA practices are you most excited about?"*

### How to Answer

Your CV lists "Gen AI driven QA and test automation" as an interest. Be prepared to back this up with specifics:

**AI in QA — What to Know:**

| AI Application | What It Does | Example Tools |
|---|---|---|
| AI-generated test cases | Uses AI to generate test scenarios from requirements or code | Diffblue Cover, CodiumAI |
| Intelligent test selection | Selects which tests to run based on code changes | Launchable, Predictive Test Selection |
| Visual testing AI | Uses AI to detect visual regressions | Applitools Eyes, Percy |
| Self-healing locators | Automatically updates element locators when UI changes | Healenium, Testim |
| AI-assisted code review | Reviews test code for quality and best practices | GitHub Copilot, SonarQube AI |
| Log analysis AI | Uses AI to identify patterns in test failure logs | Elastic AI, Splunk ITSI |

**A good answer:**

> "I'm genuinely excited about AI's potential in QA. I see three transformative areas: First, intelligent test selection — using ML to predict which tests are most likely to fail based on code changes, so we run the right tests faster rather than the entire suite every time. Second, AI-assisted test generation — tools like CodiumAI can generate test cases from code, which doesn't replace human test design but accelerates coverage. Third, self-healing test frameworks — where AI automatically adapts element locators when the UI changes, which is one of the biggest maintenance headaches in Selenium automation. I haven't had the opportunity to implement these at scale yet, but I've been following the space closely, and I'd be very keen to contribute to LSEG's AI-driven quality engineering initiatives."

**Then ask Amy about it:**

> "I noticed that your team is investing in AI-driven test automation — could you tell me more about what that looks like at LSEG? I'd love to understand where you are on that journey and how I might contribute."

---

## 10. Questions About LSEG Specifically

### Expected Questions

- *"Why LSEG?"*
- *"What do you know about our products?"*
- *"How do you think quality engineering at a financial markets company differs from your previous experience?"*

### How to Answer "Why LSEG?"

Structure around three points:

1. **Scale and impact:** "LSEG operates critical global financial infrastructure. The quality bar isn't just 'no bugs' — it's 'billions of dollars of transactions depend on this working perfectly.' That level of stakes drives the kind of rigorous quality engineering I want to practice."

2. **Technical challenge:** "Testing real-time data delivery systems at global scale, across multiple platforms and regulatory environments, is a fundamentally different challenge from testing web applications. I want to grow into that complexity."

3. **Growth and culture:** "LSEG's investment in AI-driven quality engineering, combined with its global presence and engineering culture, offers the kind of environment where I can both contribute and continue developing as a quality leader."

### LSEG Values — Be Ready to Reference Them

- **Integrity** — Connect to quality: "Quality engineering is fundamentally about integrity — ensuring our customers receive accurate, reliable data."
- **Partnership** — Connect to collaboration: "My experience collaborating with product owners, developers, and global QA teams has taught me that quality is a shared responsibility, not a QA team's solo mission."
- **Excellence** — Connect to standards: "I'm not satisfied with 'good enough' — my track record of reducing regression times by 45% and achieving 98% test coverage shows my drive toward excellence."
- **Change** — Connect to innovation: "I embrace change — from championing shift-left testing practices to pursuing my MSc in an emerging field like cloud-native computing."

---

## 11. Handling Your Weak Areas

For each known gap, here is the defensive strategy.

### Gap 1: No Financial Domain Experience

**If asked directly:** Don't pretend. Bridge honestly:

> "I haven't worked directly in financial markets, but I bring two relevant foundations: my Chartered Accountancy studies gave me fluency in financial data and business processes, and my experience testing SAP-Salesforce integrations — which involve complex data transformations, business rules, and data integrity requirements — is directly analogous to financial data pipeline testing. I'm a quick domain learner, and I'm already studying financial markets concepts to prepare for this transition."

### Gap 2: No Performance Testing Tools

**If asked directly:**

> "I haven't used dedicated performance testing tools like JMeter or Gatling extensively. My performance validation experience has been at the API level — using REST Assured to assert response times and monitoring API throughput during integration testing. However, I understand the principles well: baseline measurement, load profiles, identifying bottlenecks, and the critical importance of performance in financial systems where latency directly impacts trading outcomes. This is an area I'm actively developing."

### Gap 3: No CMM/CMMI Experience

**If asked directly:**

> "My direct experience has been in Agile/Scrum environments. I'm familiar with the CMM/CMMI concepts — the maturity levels, process areas, and the emphasis on process standardisation and continuous improvement. While I haven't worked in a formally CMM-assessed organisation, the principle of process maturity aligns with how I approach quality engineering: documenting processes, measuring effectiveness, and continuously improving. I'd be interested to learn how LSEG applies process maturity frameworks in practice."

### Gap 4: Limited Infrastructure/OS Experience

**If asked directly:**

> "My daily work at Sysco LABS was primarily at the application and API testing level. However, my MSc in Cloud Native Computing gave me hands-on experience with Linux, Docker, Kubernetes, and cloud infrastructure. I'm comfortable navigating Linux environments, reading logs, and writing shell scripts. I recognise that LSEG's systems operate at a deeper infrastructure level than my previous work, and I'm prepared to deepen that knowledge — my cloud-native foundation gives me a strong starting point."

### Gap 5: Single Employer Experience

**If asked about limited employer diversity:**

> "My 3.5 years at Sysco LABS were concentrated but not narrow. I worked across three distinct platforms — SAP, Salesforce, and Hybris E-Commerce — each with different architectures, testing challenges, and team dynamics. I went through a full progression from individual contributor to senior engineer leading QA across multiple teams. Since then, my MSc in Ireland exposed me to entirely different approaches to software design and cloud-native systems. I'm confident in my ability to adapt to new environments, and I'm excited about the learning curve that comes with joining a financial markets company."

### Gap 6: The Career Gap

See [Section 2](#2-the-career-gap--your-biggest-challenge) for the full strategy. The short version:

> "I made a strategic decision to invest in my education and certifications. The MSc deepened my technical knowledge; the ISTQB Advanced certification sharpened my testing expertise. I'm returning with stronger foundations than I had when I stepped away."

---

## 12. Questions You Should Ask Them

Asking good questions demonstrates preparation, curiosity, and strategic thinking. Tailor questions to each interviewer.

### Questions for Amy Lee (Director)

1. **"Your LinkedIn mentions AI-driven test automation — could you tell me more about LSEG's vision for AI in quality engineering? Where are you on that journey?"**
   *Why this works:* Shows you've researched her. Opens a conversation about her passion topic. Demonstrates forward-thinking mindset.

2. **"How does the quality engineering team at LSEG measure success? What metrics matter most?"**
   *Why this works:* Strategic question that shows you think beyond test execution.

3. **"What does the career progression path look like for an SDET at LSEG? Where do you see this role leading in 2-3 years?"**
   *Why this works:* Shows long-term commitment. Also helps you understand the actual scope of the role.

4. **"How does the QE team collaborate with development teams? Is it embedded, centralised, or a hybrid model?"**
   *Why this works:* Shows you understand different QA org models and care about how quality is integrated into the SDLC.

5. **"What's the biggest quality challenge your team is currently facing?"**
   *Why this works:* Shows problem-solving orientation. Also gives you valuable intel about the actual work.

### Questions for Andy Purtell (QE Manager)

1. **"What does a typical day or sprint look like for an SDET on your team?"**
   *Why this works:* Practical question that helps you understand the actual work. Shows you care about the day-to-day reality, not just the title.

2. **"What tech stack does the team currently use for test automation? What are you considering adopting?"**
   *Why this works:* The JD doesn't mention the current stack. This fills a critical information gap and shows practical readiness.

3. **"You've been at LSEG (and its predecessor organisations) for a significant time — what keeps you here? What's kept the work interesting?"**
   *Why this works:* Personal question that builds rapport. Also gives you genuine insight into the culture.

4. **"How large is the QA team I'd be joining? What's the team structure?"**
   *Why this works:* Practical information you need. Shows you're thinking about how you fit in.

5. **"What would success look like in the first 90 days for someone in this role?"**
   *Why this works:* Shows you're already thinking about how to deliver value quickly.

6. **"The role mentions supporting production releases and internal customers — how does that work in practice?"**
   *Why this works:* Shows you read the JD carefully and are preparing for the full scope of the role.

### Questions to Avoid

- Don't ask about salary, benefits, or time off in the first interview.
- Don't ask questions that are easily answered by the JD or LSEG's website.
- Don't ask "What does LSEG do?" — you should already know this.
- Don't ask more than 3-4 questions per interviewer — be respectful of time.

---

## 13. Practical Tips and Do/Don't Lists

### Before the Interview

| Do | Don't |
|---|---|
| Research LSEG's recent news (quarterly earnings, product launches, acquisitions) | Don't just skim the "About Us" page |
| Study both interviewers' LinkedIn profiles | Don't mention that you researched them unless it comes up naturally |
| Prepare 5-6 STAR stories covering: mentoring, conflict, critical bug, process improvement, technical challenge, cross-team collaboration | Don't memorise scripts — prepare frameworks and key points |
| Set up a clean, quiet interview space | Don't have distracting backgrounds or poor lighting |
| Test your camera, microphone, and internet connection | Don't scramble with tech issues at interview time |
| Prepare a 60-second "tell me about yourself" opener | Don't ramble for 5 minutes — be concise |
| Have a copy of your CV visible for reference | Don't read from your CV — use it as a prompt |
| Prepare a small coding environment in case of live coding | Don't be caught without an IDE if they ask you to code |

### During the Interview

| Do | Don't |
|---|---|
| Use specific numbers and examples from your experience | Don't make vague claims ("I improved quality") |
| Be honest about gaps — then bridge to what you bring | Don't pretend you have experience you lack |
| Show enthusiasm for learning and the LSEG domain | Don't act like financial markets is just another domain |
| Listen carefully and answer the actual question asked | Don't give pre-rehearsed answers that don't fit the question |
| Take a moment to think before answering complex questions | Don't rush into answers — pausing is professional |
| Mirror the interviewer's communication style (strategic with Amy, practical with Andy) | Don't use the same approach for both interviewers |
| Reference your ISTQB Advanced certification when relevant | Don't oversell certifications as a substitute for experience |
| Ask clarifying questions if something is unclear | Don't guess at what they're asking |
| Show curiosity about AI in QA (especially with Amy) | Don't dismiss or be ignorant about AI's impact on testing |
| Demonstrate that you understand quality at the business level (MBA angle) | Don't position yourself as "just a tester" |

### Common Mistakes to Avoid

1. **Over-indexing on tools.** Saying "I know Selenium, Playwright, Appium, REST Assured, TestNG, JUnit, Cucumber, Pytest" is a list, not a skill. Instead, describe *how* you used a specific tool to solve a specific problem.

2. **Being defensive about the gap.** If you're defensive, it signals you think it's a problem too. Be matter-of-fact and forward-looking.

3. **Claiming "over four years" of experience.** If challenged, your credibility suffers. Be precise: "approximately three and a half years of hands-on QA experience, supplemented by my MSc and ISTQB Advanced certification."

4. **Not asking questions.** Having no questions signals disinterest. Prepare at least 3 per interviewer.

5. **Generic answers about quality.** "Quality is important" and "I'm passionate about testing" are empty statements. Ground everything in specifics.

6. **Ignoring the financial domain.** Even though the JD lists it as "nice to have," both interviewers live and breathe financial data. Showing zero interest or preparation for the domain will hurt you.

7. **Treating this as just another QA role.** LSEG is financial markets infrastructure. Show that you understand the gravity and responsibility of ensuring quality in systems that global markets depend on.

---

## 14. Pre-Interview Checklist

### One Week Before

- [ ] Research LSEG: recent quarterly results, press releases, product updates.
- [ ] Study both interviewer LinkedIn profiles — note commonalities and talking points.
- [ ] Review Elektron/LSEG Real-Time basics: what it does, why it matters.
- [ ] Prepare and rehearse 6 STAR stories.
- [ ] Brush up on Java coding basics: write a few small programs.
- [ ] Review SQL fundamentals: JOINs, GROUP BY, HAVING, subqueries.
- [ ] Study basic Linux commands and be able to explain what each does.
- [ ] Prepare your "career gap" narrative and practice it until it sounds natural, not rehearsed.
- [ ] Read about AI in testing: know at least 3 specific applications and 2 tool names.
- [ ] Review ISTQB Advanced Level syllabus topics: test techniques, coverage criteria, white-box testing.
- [ ] Study financial markets basics: what market data is, why latency matters, what FIX protocol is.

### One Day Before

- [ ] Confirm interview time, platform (Zoom/Teams/etc.), and any access credentials.
- [ ] Test camera, microphone, and internet connection.
- [ ] Prepare your workspace: clean background, good lighting, glass of water.
- [ ] Print (or have digitally ready) your CV, the JD, and your STAR stories.
- [ ] Review your prepared questions for each interviewer.
- [ ] Get a good night's sleep.

### Day of Interview

- [ ] Log in 5 minutes early.
- [ ] Have your notes nearby but out of camera view.
- [ ] Take a deep breath. You have strong credentials. You belong in this interview.
- [ ] Remember: Amy wants to see a future quality leader. Andy wants to see a capable, honest engineer who can grow. Show them both.

---

## Final Thought

You have genuine strengths that many candidates don't: ISTQB Advanced certification, an MSc in a highly relevant field, an MBA that gives you business acumen, quantifiable results from your QA work, and a published research paper. The career gap and single-employer history are real challenges, but they're manageable with honest, forward-looking framing.

The key to this interview is **bridging**: connecting what you have done to what LSEG needs. Every answer should follow the pattern: *"Here's what I've done → Here's how it connects to what you need → Here's how I'll grow into the rest."*

Go in prepared, be honest about gaps, be enthusiastic about the opportunity, and let your genuine strengths speak for themselves.
