# 1. Testing Fundamentals & Methodology

---

### Q1: Walk us through how you approach test planning for a new feature — from requirements analysis to test execution.

**What's being evaluated:** Structured thinking, end-to-end understanding of the QA lifecycle, ability to work independently within defined parameters.

> **Delivery note:** Pick 4–5 key steps and give depth rather than listing all 8. Aim for 2–3 minutes. The interviewer wants to see your thinking process, not a recitation of a textbook list.

**Answer guidance:**

1. **Requirements Analysis** — Review functional and non-functional requirements. Clarify ambiguities with product owners and developers. Identify testable acceptance criteria.
2. **Risk Assessment** — Identify high-risk areas (e.g., data integrity in financial transactions, performance under load). Prioritize testing effort accordingly.
3. **Test Strategy & Plan** — Define scope, test types needed (functional, integration, performance, regression), environments, tools, entry/exit criteria, and timelines.
4. **Test Case Design** — Write test cases using techniques like equivalence partitioning, boundary value analysis, decision tables, and state transition diagrams. Trace each case back to a requirement.
5. **Automation Assessment** — Decide which cases are candidates for automation based on repeatability, stability, and ROI.
6. **Environment Setup** — Coordinate test environment provisioning (cloud or on-prem), test data preparation, and stub/mock services if needed.
7. **Execution & Reporting** — Execute tests (manual + automated), log defects with clear reproduction steps, track metrics (pass/fail rate, defect density), and report status to stakeholders.
8. **Closure** — Verify exit criteria are met, prepare test summary report, document lessons learned.

**Tips:**
- Reference a real project where you followed this process.
- Mention how you fit into a DevOps team and how testing integrates with CI/CD.
- LSEG values process maturity (CMM/CMMI), so emphasize structured documentation.

---

### Q2: What's the difference between system testing, integration testing, system/network integration testing, and acceptance testing? When would you use each?

**What's being evaluated:** Depth of testing knowledge, understanding of the test levels mentioned explicitly in the job description.

**Answer guidance:**

| Test Level | Purpose | When |
|---|---|---|
| **Integration Testing** | Verify interactions between modules/components (e.g., service A calling service B). | After unit testing, when individual components are combined. |
| **System Testing** | Validate the complete, integrated system against functional and non-functional requirements. | After integration testing, in an environment that mirrors production. |
| **System/Network Integration Testing** | Verify the system works correctly across network boundaries, firewalls, load balancers, and with external systems. | Critical in financial infrastructure — e.g., ensuring market data feeds traverse network segments correctly. |
| **Acceptance Testing** | Confirm the system meets business requirements and is ready for production. Often involves UAT with stakeholders. | Final stage before release. |

**Tips:**
- Give a concrete example: "In a trading platform, integration testing checks that the order management module correctly sends orders to the matching engine. System/network integration testing verifies this works across data centers with expected latency."
- Mention that at LSEG, system/network integration testing is especially important given the distributed, multi-region financial infrastructure.

---

### Q3: How do you decide what to automate versus what to test manually?

**What's being evaluated:** Pragmatic judgment, ROI thinking, automation maturity.

**Answer guidance:**

**Automate when:**
- Tests are repetitive and run frequently (regression, smoke).
- Tests are stable — the feature under test is unlikely to change drastically.
- Tests involve large data sets or many combinations (data-driven testing).
- Tests require precision (e.g., verifying exact financial calculations to decimal places).
- Tests are part of CI/CD and need fast feedback.

**Keep manual when:**
- Exploratory testing or usability evaluation.
- One-off tests or features still in active flux.
- Tests that require human judgment (e.g., visual validation, UX assessment).
- The cost of building and maintaining automation exceeds the benefit.

**Framework for decision:** Use a simple scoring matrix — frequency of execution, stability of feature, complexity of automation, and business criticality. High scores across all four = automate.

**Tips:**
- Avoid the "automate everything" trap — interviewers want to see you think about ROI.
- Mention that in financial systems, automating calculations and data validation is high-priority because errors have monetary consequences.

---

### Q4: Explain your understanding of CMM/CMMI. How has it influenced your testing process in previous roles?

**What's being evaluated:** Process maturity awareness, ability to work within formal SDLC frameworks — explicitly required in the job description.

**Answer guidance:**

**CMMI (Capability Maturity Model Integration)** is a process improvement framework with 5 maturity levels:

1. **Initial** — Processes are ad-hoc and chaotic.
2. **Managed** — Projects are planned, measured, and controlled.
3. **Defined** — Processes are standardized across the organization.
4. **Quantitatively Managed** — Processes are measured and controlled using statistical methods.
5. **Optimizing** — Continuous process improvement driven by data.

**How it influences testing:**
- At Level 2+, testing has defined plans, reviews, and tracking.
- At Level 3+, test processes are consistent across teams — e.g., standardized test case templates, defect lifecycle, and review gates.
- At Level 4+, you track metrics like defect escape rate, test effectiveness, and use them to drive decisions.

**Tips:**
- Be honest about your organization's maturity level and your role in improving it.
- Tie it back to the JD: "I've recommended process improvements to my manager based on defect trend analysis" — this directly maps to the scope described.

**Udani's bridging answer (Agile-only experience):**

> "I haven't worked in a formally CMMI-assessed organisation — my experience has been in Agile/Scrum environments. However, I've applied many of the same principles that CMMI formalises:
>
> - At Level 2 (Managed): I created standardised test plan templates and entry/exit criteria for every sprint, ensuring testing was planned, tracked, and controlled rather than ad-hoc.
> - At Level 3 (Defined): I worked to standardise our test automation approach across multiple teams at Sysco LABS — common page object patterns, shared utility libraries, consistent reporting formats — so that any team member could understand and contribute to any team's automation suite.
> - At Level 4 (Quantitatively Managed): I tracked defect metrics — escape rates, defect density by module, regression pass rates over time — and used these to drive decisions about where to invest automation effort.
>
> So while I haven't operated within a formal CMMI framework, I understand and have applied the underlying principles. I'd be interested to learn how LSEG applies process maturity frameworks in practice."

---

### Q5: How do you measure test coverage, and when is "enough" testing enough?

**What's being evaluated:** Analytical thinking, risk-based testing mindset.

**Answer guidance:**

**Types of coverage:**
- **Requirements coverage** — % of requirements with at least one test case mapped.
- **Code coverage** — Line, branch, and path coverage from automated tests (useful but not sufficient alone).
- **Risk coverage** — Are high-risk areas tested more thoroughly? Use risk matrices.

**"Enough" testing:**
- All critical/high-priority test cases pass.
- Exit criteria defined in the test plan are met (e.g., 95% pass rate, zero critical defects open).
- Risk-based assessment: remaining untested areas are low-risk and acceptable to stakeholders.
- Defect discovery rate is trending toward zero (diminishing returns).

**Tips:**
- Emphasize that 100% coverage is a myth — what matters is covering the right things.
- In financial systems, regulatory and compliance-related tests are non-negotiable.

---

### Q6: Describe a situation where you found a critical defect late in the cycle. How did you handle it?

**What's being evaluated:** Problem-solving under pressure, communication skills, ownership mentality.

**Answer guidance (STAR format):**

- **Situation:** Describe the project, timeline pressure, and the defect.
- **Task:** Your responsibility — assessing impact, communicating urgency.
- **Action:** Steps you took — reproduced the defect reliably, documented it with clear evidence, escalated to the dev lead and project manager, participated in root cause analysis, and re-tested the fix.
- **Result:** The outcome — was the release delayed? Was a hotfix deployed? What process change prevented this from happening again?

**Tips:**
- Show ownership: "I took it upon myself to investigate further rather than just logging it."
- Mention how you communicated the risk to stakeholders — this shows the customer service awareness LSEG values.
- End with a process improvement you suggested to catch similar issues earlier.

---

### Q7: What are the key test design techniques you use? When would you apply each one?

**What's being evaluated:** Depth of knowledge in systematic test design, ability to choose the right technique for the situation.

**Answer guidance:**

| Technique | What It Does | When to Use |
|---|---|---|
| **Equivalence Partitioning** | Divides input data into partitions where all values in a partition are expected to behave the same. Test one value per partition. | When inputs have clear ranges or categories (e.g., age groups, transaction amounts). |
| **Boundary Value Analysis (BVA)** | Tests at the exact boundaries of equivalence partitions (min, min+1, max-1, max). | When boundary-related bugs are likely (e.g., off-by-one errors in financial calculations). |
| **Decision Tables** | Maps combinations of conditions to expected actions/outcomes in a tabular format. | When multiple conditions interact to determine behavior (e.g., eligibility rules, pricing tiers). |
| **State Transition Testing** | Models the system as a finite state machine and tests transitions between states. | When the system has distinct states with defined transitions (e.g., order lifecycle: New → Filled → Settled → Cancelled). |
| **Pairwise/Combinatorial Testing** | Tests all possible pairs of parameter values rather than all combinations, dramatically reducing test count. | When there are many configurable parameters and full combinatorial testing is infeasible. |

**Tips:**
- Show you don't just use one technique — you pick the right one based on the feature. For example: "For a trade matching engine, I'd use state transition testing for the order lifecycle and BVA for price matching thresholds."
- Mention tools like PICT or AllPairs for pairwise testing.

---

### Q8: How do you write effective test cases? What makes a good test case?

**What's being evaluated:** Practical test design skills, attention to detail, communication through documentation.

**Answer guidance:**

**Characteristics of a good test case:**
- **Clear title** — Describes what is being tested and the expected outcome (e.g., "Verify order rejection when account balance is insufficient").
- **Preconditions** — State what must be true before the test runs (environment, data, user state).
- **Steps** — Numbered, specific, reproducible steps. Anyone should be able to execute them.
- **Expected result** — Concrete, verifiable outcome for each step or the overall test.
- **Test data** — Explicit values, not vague descriptions ("enter 10,000.50" not "enter a large amount").
- **Traceability** — Linked to a requirement, user story, or acceptance criterion.
- **Independence** — Does not depend on other test cases having run first.

**Common mistakes to avoid:**
- Vague steps ("test the login feature").
- Missing negative test cases — only testing the happy path.
- Hardcoded environment-specific data that breaks in other environments.

**Tips:**
- Mention that you use a standard template across the team for consistency (aligns with CMMI Level 3+ practices).
- In financial systems, test cases for regulatory features need extra rigor — they may be audited.

> **Elevation note for Associate Lead level:** Keep your answer concise and practical, then elevate to automated test design considerations: "Beyond manual test case quality, I also think about how test cases translate to automation — are they data-driven? Are assertions specific and deterministic? Can they run independently in any order? Good test case design at the planning stage directly reduces automation maintenance downstream."

---

### Q9: Explain the testing pyramid. How do you apply it in practice?

**What's being evaluated:** Understanding of test architecture, practical application of testing levels, strategic thinking about test ROI.

**Answer guidance:**

**The testing pyramid (bottom to top):**

1. **Unit Tests (base — largest number)**
   - Test individual functions/methods in isolation.
   - Fast, cheap, and reliable. Run in milliseconds.
   - Developers typically own these.

2. **Integration/Service Tests (middle)**
   - Test interactions between components, APIs, and databases.
   - Slower than unit tests but validate critical interfaces.
   - SDETs often focus here — API contract tests, database integration tests.

3. **End-to-End / UI Tests (top — fewest)**
   - Test complete user workflows through the UI.
   - Slowest, most brittle, most expensive to maintain.
   - Reserve for critical business flows only.

**Applying it in practice:**
- Advocate for a high ratio of unit tests to catch bugs early and cheaply.
- Push integration bugs down to unit tests when possible ("if this API test found the bug, could a unit test have caught it faster?").
- Limit E2E tests to 10–20 critical scenarios to avoid a top-heavy pyramid (the "ice cream cone anti-pattern").
- In CI/CD, run unit tests on every commit, integration tests on every merge, and E2E tests nightly or on release branches.

**Tips:**
- Relate to the SDET role: "As an SDET, I focus most of my automation effort on the integration/API layer — it gives the best balance of coverage, speed, and stability."
- In financial systems, the middle layer is critical — API and service tests validate data accuracy, message formats, and business logic without the fragility of UI tests.

---

### Q10: What is risk-based testing and how do you implement it?

**What's being evaluated:** Strategic thinking, ability to prioritize testing effort based on business impact, practical risk assessment skills.

**Answer guidance:**

**Risk-based testing** prioritizes testing effort based on the likelihood and impact of failure for each feature or component.

**Implementation steps:**

1. **Identify risks:**
   - Review requirements, architecture, and past defect data.
   - Consult with developers, product owners, and operations.
   - Consider: What can go wrong? What's the impact if it does?

2. **Assess each risk on two dimensions:**
   - **Likelihood** — How probable is a defect? (New code = high, stable code = low; complex logic = high, simple CRUD = low)
   - **Impact** — What's the business consequence if it fails? (Financial loss, regulatory breach, data corruption, reputational damage)

3. **Create a risk matrix:**

   | | Low Impact | High Impact |
   |---|---|---|
   | **High Likelihood** | Medium priority | **Highest priority** |
   | **Low Likelihood** | Lowest priority | Medium priority |

4. **Allocate testing effort:**
   - High-risk areas get the most test cases, deepest coverage, and earliest testing.
   - Low-risk areas get basic smoke tests or are deferred.

5. **Review and adjust:**
   - Risks change as the project evolves. Reassess regularly (e.g., after each sprint).

**Tips:**
- Give a concrete example: "In a payment processing module, I classified the transaction calculation logic as high-likelihood/high-impact and wrote 50+ test cases. The admin settings page was low-likelihood/low-impact and got 5 basic tests."
- Mention that risk-based testing aligns with LSEG's need to protect financial data integrity — you test what matters most, not just what's easiest to test.
- Show that you communicate risk assessments to stakeholders so they can make informed decisions about test coverage and release readiness.
