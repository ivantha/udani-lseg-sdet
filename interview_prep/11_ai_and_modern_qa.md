# 11. AI & Modern QA Practices

> **Why this section matters:** Amy Lee's current focus is AI-driven test automation — this is her passion topic and likely evaluation lens. Demonstrating knowledge here will resonate strongly with her. Your CV lists "Gen AI driven QA and test automation" as an interest — be prepared to back that up with substance.

---

### Q78: How is AI changing the SDET role? What's your view on AI in test automation?

**What's being evaluated:** Awareness of industry trends, ability to think critically about emerging technology (not just hype), strategic thinking about the future of quality engineering.

**Answer guidance:**

Structure your answer around **three layers of AI impact**:

**1. AI as an accelerator (today — already practical):**
- **Code generation assistance** — GitHub Copilot, Amazon CodeWhisperer generate boilerplate test code, assertion patterns, and data factories. Saves time on repetitive scaffolding.
- **Test case generation from requirements** — Tools like CodiumAI (now Qodo) analyse source code and generate unit/integration tests with edge cases humans might miss.
- **Log analysis and failure triage** — AI models identify patterns in test failure logs, cluster similar failures, and suggest root causes. Reduces time spent manually triaging CI failures.

**2. AI as a quality multiplier (emerging — early adoption):**
- **Intelligent test selection** — ML models predict which tests are most likely to fail based on code changes, reducing suite execution time by 60–80% while maintaining defect detection.
- **Self-healing test frameworks** — AI automatically adapts element locators and test steps when the application UI changes, dramatically reducing maintenance overhead.
- **Visual AI testing** — Computer vision detects visual regressions that pixel-comparison misses — layout shifts, font changes, colour inconsistencies across browsers.

**3. AI as a paradigm shift (future — strategic):**
- **Autonomous test design** — AI that understands application behaviour and designs test strategies, not just individual test cases.
- **Predictive quality** — ML models that predict defect-prone areas before testing begins, based on code complexity, change velocity, and historical defect patterns.
- **Shift from "test more" to "test smarter"** — The SDET role evolves from writing test scripts to curating AI-generated test strategies, building quality feedback loops, and designing the systems that AI uses to learn.

**Financial domain connection:**

> "In financial systems, AI in testing is particularly valuable because the combinatorial explosion of test scenarios — instruments × markets × currencies × regulatory rules — makes exhaustive manual test design impossible. AI-driven test generation and intelligent selection can cover scenarios that humans would never enumerate."

**Tips:**
- Don't be purely theoretical — mention specific tools by name (see table below).
- Acknowledge limitations: AI-generated tests still need human review for business logic correctness. AI hallucinates test scenarios that don't match real requirements.
- For Amy: position yourself as an eager adopter, not a skeptic. Show you've been following this space and are ready to contribute to LSEG's AI-driven QA initiatives.
- For Andy: ground it in practical value — less maintenance, faster feedback, better coverage.

---

### Q79: What is intelligent test selection? How does ML-based test prioritisation work?

**What's being evaluated:** Depth of understanding of a specific AI/ML application in testing, ability to explain technical concepts clearly.

**Answer guidance:**

**The problem:** Running the full regression suite on every code change is slow and wasteful. In a large system (like LSEG's 500+ products), full regression might take hours or days. Most of those tests aren't relevant to the specific change.

**The solution — intelligent test selection:**

ML models learn the relationship between code changes and test outcomes. When new code is committed, the model predicts which tests are most likely to fail and runs only those first.

**How it works:**

1. **Training data:** Historical records of code changes (which files changed, which functions were modified) paired with test results (which tests passed/failed).
2. **Feature engineering:** Code change features (files changed, lines modified, author, time of day, component) + test features (test history, flakiness score, last failure date).
3. **Model:** Typically gradient-boosted trees or neural networks that predict failure probability for each test given the current change.
4. **Selection:** Tests ranked by predicted failure probability. Run the top N% first (e.g., top 20% likely covers 95% of actual failures).
5. **Feedback loop:** Actual results feed back into the model, continuously improving predictions.

**Key tools:**

| Tool | Approach | Notable Feature |
|---|---|---|
| **Launchable** | ML-based test selection as a service | Integrates with JUnit, pytest, TestNG; claims 80% suite reduction |
| **Predictive Test Selection (Azure DevOps)** | Built into Azure Pipelines | Analyses code changes to select relevant tests |
| **Codecov Test Analytics** | Coverage-based impact analysis | Maps code changes to tests via coverage data |
| **Custom/in-house** | Build your own using test history + code change data | Full control, requires ML expertise |

**Limitations:**
- Cold start problem — needs historical data to be effective.
- Can miss tests affected by indirect dependencies (e.g., config changes, shared libraries).
- Must still run the full suite periodically (nightly/weekly) to catch missed regressions.

**Tips:**
- Connect to LSEG's scale: "With 500+ products across multiple platforms, intelligent test selection could dramatically reduce CI pipeline time while maintaining confidence in releases."
- Mention that this complements, not replaces, a solid test architecture — you still need well-designed, independent, well-maintained tests.

---

### Q80: What are self-healing test frameworks? How do they work?

**What's being evaluated:** Understanding of a practical AI application that solves a real SDET pain point — test maintenance.

**Answer guidance:**

**The problem:** UI test automation is fragile. When developers change element IDs, class names, or page structure, Selenium locators break. In large suites, locator maintenance consumes 30–40% of SDET effort.

**The solution — self-healing:**

Self-healing frameworks use AI to automatically find and update element locators when the original locator fails, without human intervention.

**How it works:**

1. **Multi-locator strategy:** Each element is identified by multiple attributes (ID, CSS, XPath, text, position, visual appearance) during test creation.
2. **Failure detection:** When the primary locator fails, the framework doesn't immediately fail the test.
3. **Alternative search:** AI algorithms try alternative locators based on:
   - Attribute similarity (e.g., ID changed from `btn-submit` to `submit-btn`).
   - DOM structure (element is still the 3rd button in the form).
   - Visual position (element is still in the same screen location).
   - Text content (button still says "Submit").
4. **Healing:** If an alternative locator finds the element, the test continues. The framework logs the healed locator for review.
5. **Learning:** Over time, the framework learns which locator strategies are most stable for each element type.

**Key tools:**

| Tool | Type | How It Works |
|---|---|---|
| **Healenium** | Open-source | Selenium extension; uses ML to find elements when locators break. Stores locator history in a database. |
| **Testim** | Commercial | AI-powered locators that adapt to UI changes. Learns from test execution history. |
| **mabl** | Commercial SaaS | Auto-healing with visual + DOM analysis. Includes AI-driven test creation. |
| **Selenium IDE (newer versions)** | Open-source | Basic fallback locator strategies built in. |

**Practical considerations:**
- Self-healing is valuable for **reducing false negatives** (tests failing due to locator changes, not real bugs).
- It should NOT silently heal — changes must be reviewed. A healed locator might indicate a legitimate UI change that needs new test assertions.
- Works best for stable applications with incremental UI changes. Major redesigns still require manual test updates.

**Connection to Udani's experience:**

> "In my Salesforce Lightning testing experience, dynamic element IDs were one of the biggest challenges. Self-healing frameworks would have reduced the locator maintenance burden significantly — Salesforce generates dynamic IDs that change across deployments, so traditional locator strategies break frequently. I used JavaScript executor and custom wait strategies as a manual equivalent, but AI-driven self-healing would be a step-change improvement."

**Tips:**
- For Andy: frame this as a practical solution to the maintenance challenge he faces with 500+ products.
- For Amy: frame this as a strategic investment that frees SDET capacity from maintenance toward higher-value test design work.

---

### Q81: How can generative AI (Copilot, CodiumAI) be used in day-to-day SDET work?

**What's being evaluated:** Practical awareness of GenAI tools, ability to distinguish hype from genuine productivity gains, judgment about when AI helps vs. when it gets in the way.

**Answer guidance:**

**Practical use cases for GenAI in SDET work:**

| Use Case | Tool(s) | What It Does | Limitation |
|---|---|---|---|
| **Boilerplate generation** | GitHub Copilot, Amazon CodeWhisperer | Generates test method scaffolding, assertion patterns, page object structures | May not follow project conventions; needs review |
| **Test case generation from code** | Qodo (formerly CodiumAI), Diffblue Cover | Analyses source code and generates unit/integration tests with edge cases | Generated tests may not reflect real business requirements |
| **Test data generation** | ChatGPT, Copilot | Creates realistic test data sets, boundary values, edge case inputs | Financial data requires domain-specific validity (e.g., valid ISINs, correct currency codes) |
| **Regex and XPath generation** | Copilot, ChatGPT | Generates complex locators, validation patterns, SQL queries from natural language | Must verify correctness — AI-generated regex can have subtle errors |
| **Debugging assistance** | Copilot Chat, Claude | Analyses error logs, suggests root causes, explains stack traces | Lacks project-specific context; suggestions are starting points |
| **Documentation** | Copilot, ChatGPT | Generates test plan templates, test case descriptions, framework documentation | May produce generic content that doesn't match project specifics |
| **Code review assistance** | Qodo, SonarQube AI | Reviews test code for quality, suggests improvements, identifies anti-patterns | Cannot assess business logic correctness |

**A realistic perspective:**

> "I see GenAI as a productivity multiplier, not a replacement for SDET judgment. It excels at generating boilerplate, suggesting edge cases I might miss, and accelerating routine tasks. But it doesn't understand business context — it can generate a test for a function, but it can't tell you whether that function's behaviour is correct for the business requirement. The SDET's role shifts from writing every line of test code to curating, reviewing, and directing AI-generated output."

**What NOT to say:**
- Don't claim AI will replace testers — this sounds naive.
- Don't dismiss AI as "just hype" — this sounds resistant to change, especially to Amy.
- Don't claim extensive hands-on experience if you haven't used these tools — say you've explored them and are ready to integrate them into your workflow.

**Tips:**
- If asked whether you've used these tools, be honest: "I've used Copilot for test code generation and explored CodiumAI for automated test generation. I'm actively building my fluency with these tools because I believe they'll be fundamental to SDET productivity in the next 2–3 years."
- For Amy: connect to the strategic shift — "AI doesn't reduce the need for quality engineers; it elevates the role from test execution to test strategy and AI oversight."

---

### Q82: What is visual AI testing? How does it differ from traditional visual regression testing?

**What's being evaluated:** Understanding of a specific AI-driven testing technique, ability to compare approaches and articulate trade-offs.

**Answer guidance:**

**Traditional visual regression testing:**
- Takes screenshot of baseline (expected) and compares pixel-by-pixel to current screenshot.
- Any pixel difference = failure. This creates massive false positive rates:
  - Font rendering differences across OS/browser.
  - Anti-aliasing variations.
  - Dynamic content (timestamps, ads, user-specific data).
  - Sub-pixel rendering differences.
- Requires constant baseline updates and manual triage.

**Visual AI testing:**
- Uses computer vision and ML models trained on how humans perceive visual differences.
- Understands page structure, layout, and visual hierarchy — not just pixels.
- Can distinguish meaningful visual changes (broken layout, wrong colour, missing element) from noise (font rendering, sub-pixel differences).

**Comparison:**

| Aspect | Traditional (Pixel Comparison) | Visual AI |
|---|---|---|
| **False positive rate** | High (20–40% of flagged changes are noise) | Low (AI filters noise like anti-aliasing) |
| **Cross-browser accuracy** | Poor (rendering differences flagged as bugs) | Good (understands acceptable rendering variance) |
| **Dynamic content handling** | Manual ignore regions required | AI can identify and handle dynamic areas automatically |
| **Layout validation** | Limited to pixel match | Understands layout structure, spacing, alignment |
| **Maintenance** | High (baseline updates, ignore regions) | Lower (AI learns acceptable variance) |
| **Cost** | Free/open-source tools available | Typically commercial (Applitools: ~$500/user/month) |

**Key tools:**

| Tool | Approach | Best For |
|---|---|---|
| **Applitools Eyes** | Visual AI with Ultrafast Grid for cross-browser | Enterprise visual testing at scale |
| **Percy (BrowserStack)** | Snapshot comparison with smart diff | CI-integrated visual regression |
| **Chromatic** | Visual testing for Storybook components | Component-level visual testing |
| **BackstopJS** | Open-source screenshot comparison | Budget-conscious teams |

**Financial domain connection:**

> "In financial applications, visual accuracy matters — a misaligned decimal point in a trading dashboard or an incorrectly rendered chart could lead to wrong trading decisions. Visual AI testing could validate that financial data is displayed correctly across different screen sizes, browsers, and user contexts without the false positive noise that makes pixel comparison impractical at scale."

**Tips:**
- If you haven't used visual AI testing, be honest but informed: "I haven't implemented visual AI testing in a production environment, but I understand the technology and its advantages over pixel comparison. In my Salesforce testing, we relied on manual visual verification supplemented by basic screenshot comparison — visual AI would have significantly improved that workflow."
- For Amy: connect to the broader AI-in-QA strategy. Visual AI is one piece of the puzzle alongside intelligent test selection and self-healing frameworks.
- For Andy: frame in terms of practical value — reduced maintenance, fewer false positives, faster triage.
