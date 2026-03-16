# 12. Security Testing

> **Why this section matters:** The job description mentions security testing awareness, and financial systems demand it. Udani lists Veracode on her CV, and financial data handling raises the security stakes significantly. Both interviewers will appreciate security consciousness — it signals maturity as a quality engineer.

---

### Q83: What is the OWASP Top 10 and how does it influence your testing?

**What's being evaluated:** Awareness of common security vulnerabilities, ability to translate security knowledge into practical testing activities.

**Answer guidance:**

**OWASP (Open Worldwide Application Security Project) Top 10** is the most widely recognised list of critical web application security risks, updated periodically based on real-world data.

**Current OWASP Top 10 (2021 edition) with testing implications:**

| # | Vulnerability | What It Is | How to Test |
|---|---|---|---|
| A01 | **Broken Access Control** | Users can act outside their intended permissions. | Test role-based access: can a viewer modify data? Can user A access user B's records? Test direct URL manipulation, API endpoint access without auth. |
| A02 | **Cryptographic Failures** | Sensitive data exposed due to weak or missing encryption. | Verify HTTPS everywhere, check for sensitive data in URLs/logs, validate encryption of data at rest, check password hashing algorithms. |
| A03 | **Injection** | Untrusted data sent to an interpreter (SQL, OS command, LDAP). | Send SQL injection payloads (`' OR 1=1 --`), test input fields with special characters, verify parameterised queries are used. |
| A04 | **Insecure Design** | Flaws in the design/architecture, not just implementation. | Review business logic for abuse cases (e.g., can a user bypass payment by manipulating order flow?). Threat modelling during design phase. |
| A05 | **Security Misconfiguration** | Default configurations, open cloud storage, verbose error messages. | Check default credentials, verify error pages don't leak stack traces, scan for unnecessary open ports, review HTTP security headers. |
| A06 | **Vulnerable Components** | Using libraries/frameworks with known vulnerabilities. | Scan dependencies with SCA tools (Snyk, OWASP Dependency-Check), monitor CVE databases, keep dependencies updated. |
| A07 | **Authentication Failures** | Broken authentication, weak passwords, session management issues. | Test brute force protection, session timeout, token invalidation on logout, password complexity rules, MFA enforcement. |
| A08 | **Data Integrity Failures** | Code and infrastructure without integrity verification (insecure CI/CD, unsigned updates). | Verify CI/CD pipeline security, check for unsigned packages, validate data integrity checksums. |
| A09 | **Logging & Monitoring Failures** | Insufficient logging to detect breaches. | Verify security events are logged (failed logins, access denials), test that logs don't contain sensitive data, validate alerting thresholds. |
| A10 | **Server-Side Request Forgery (SSRF)** | Application fetches remote resources without validating user-supplied URLs. | Test URL input fields with internal addresses (`localhost`, `169.254.169.254` for cloud metadata), verify allowlists are enforced. |

**How to use OWASP Top 10 in practice:**

1. **Test planning:** Include OWASP Top 10 checks in the test plan for any web-facing application.
2. **Test case design:** Create specific negative test cases for each relevant vulnerability category.
3. **Automation:** Integrate basic security checks into automated regression suites (e.g., verify auth headers, test access control boundaries).
4. **Shift-left:** Include security test scenarios in code reviews and design reviews.

**Tips:**
- You don't need to be a penetration tester — show that you understand common vulnerabilities and include security considerations in your testing approach.
- In financial systems, A01 (Broken Access Control) and A02 (Cryptographic Failures) are especially critical — unauthorized access to trading data or leaked financial information has regulatory consequences.
- Mention that OWASP also provides testing guides (OWASP Testing Guide) and tools (ZAP) — showing awareness of the broader ecosystem.

---

### Q84: Explain SAST, DAST, and IAST — when would you use each?

**What's being evaluated:** Understanding of security testing approaches, ability to choose the right tool/approach for the context.

**Answer guidance:**

| Aspect | SAST (Static) | DAST (Dynamic) | IAST (Interactive) |
|---|---|---|---|
| **Full name** | Static Application Security Testing | Dynamic Application Security Testing | Interactive Application Security Testing |
| **When it runs** | During development (analyses source code) | Against running application | During test execution (agent inside app) |
| **What it analyses** | Source code, bytecode, or binary | Application behaviour via HTTP requests | Real-time code execution paths |
| **Finds** | Code-level vulnerabilities (SQL injection patterns, hardcoded secrets, insecure functions) | Runtime vulnerabilities (XSS, auth bypass, misconfigurations) | Both code-level and runtime vulnerabilities with exact code location |
| **False positive rate** | Higher (analyses code paths that may not be reachable) | Lower (tests actual application behaviour) | Lowest (combines static and dynamic analysis) |
| **Speed** | Fast (no running application needed) | Slower (requires deployed application) | Medium (runs during test execution) |
| **CI/CD integration** | Early in pipeline (commit/build stage) | Later in pipeline (test/staging stage) | During functional test execution |
| **Language dependent?** | Yes (needs parser for each language) | No (language-agnostic, tests via HTTP) | Yes (agent runs inside application runtime) |
| **Example tools** | SonarQube, Veracode Static, Checkmarx, Semgrep | OWASP ZAP, Burp Suite, Veracode Dynamic | Contrast Security, Synopsys Seeker |

**When to use each:**

1. **SAST — Use early, use often:**
   - Integrate into IDE and CI pipeline so developers get feedback on every commit.
   - Catches insecure coding patterns before code is even built.
   - Best for: finding hardcoded credentials, injection vulnerabilities, insecure crypto usage.

2. **DAST — Use in testing/staging:**
   - Run against deployed applications in test environments.
   - Simulates real attacks without needing source code access.
   - Best for: finding authentication issues, XSS, CSRF, server misconfigurations.

3. **IAST — Use during functional testing:**
   - Runs alongside your existing functional tests — no separate security test suite needed.
   - Provides the most accurate results (lowest false positives) because it sees both code and runtime behaviour.
   - Best for: comprehensive security validation during QA cycles.

**Recommended pipeline integration:**

```
Commit → [SAST] → Build → [SCA] → Deploy to Test → [DAST + IAST during functional tests] → Staging → [Pen Test]
```

**Tips:**
- Connect to your experience: "At Sysco LABS, we used SonarQube for static analysis as part of our quality gates, and Veracode for security scanning. SonarQube caught code quality and basic security issues on every commit, while Veracode provided deeper security analysis."
- Emphasise the "shift-left" principle: catching security issues in SAST is 10x cheaper than finding them in DAST, and 100x cheaper than finding them in production.
- For financial systems: "In a financial environment, I'd advocate for all three layers — SAST in the IDE and CI pipeline, DAST against staging environments, and periodic penetration testing by specialists."

---

### Q85: How do you integrate security testing into CI/CD pipelines (DevSecOps)?

**What's being evaluated:** Understanding of DevSecOps principles, ability to embed security into automated workflows without slowing delivery.

**Answer guidance:**

**DevSecOps** embeds security testing into every stage of the CI/CD pipeline, making security a continuous activity rather than a gate at the end.

**Pipeline integration model:**

| Pipeline Stage | Security Activity | Tools | Blocking? |
|---|---|---|---|
| **Pre-commit** | Secret scanning (prevent credential leaks) | git-secrets, TruffleHog, pre-commit hooks | Yes — block commit if secrets detected |
| **Commit/Build** | SAST — static code analysis | SonarQube, Veracode, Semgrep | Yes — fail build on critical/high severity |
| **Dependency resolution** | SCA — software composition analysis | Snyk, OWASP Dependency-Check, Dependabot | Yes — block if known CVEs in dependencies |
| **Test environment** | DAST — dynamic scanning of deployed app | OWASP ZAP, Burp Suite Enterprise | Advisory — alert on findings, don't block |
| **Functional testing** | IAST — security analysis during test execution | Contrast Security | Advisory for medium, block for critical |
| **Pre-production** | Container scanning, infrastructure-as-code scanning | Trivy, Checkov, tfsec | Yes — block deployment with vulnerable images |
| **Production** | Runtime protection, WAF monitoring | RASP tools, cloud WAFs | Monitor and alert |

**Key principles:**

1. **Automate everything possible:** Manual security reviews don't scale. Integrate scanning tools that run automatically on every pipeline execution.
2. **Gate on severity:** Not every finding should block the pipeline. Define severity thresholds — block on critical/high, alert on medium, track low.
3. **Fast feedback:** SAST and SCA run in minutes. DAST may take longer — run it in parallel with functional tests.
4. **Developer ownership:** Security findings should surface in the developer's PR, not in a separate security report weeks later. Shift-left means shift responsibility left too.
5. **Metrics:** Track mean time to remediate (MTTR) for security findings. Target: critical findings fixed before merge; high findings fixed within one sprint.

**Tips:**
- Connect to your CI/CD experience: "At Sysco LABS, I integrated SonarQube quality gates into our Jenkins pipeline — this included basic security checks alongside code quality. I'd extend this approach with dedicated SAST/DAST tools for a financial systems context."
- For financial systems: "In a regulated environment like LSEG, security testing in the pipeline isn't optional — it's a compliance requirement. Regulatory bodies expect evidence that security is tested continuously, not just at release boundaries."
- Don't position security as "someone else's job" — an SDET who understands DevSecOps is significantly more valuable.

---

### Q86: What security considerations are specific to financial systems?

**What's being evaluated:** Domain awareness, understanding of the heightened security requirements in financial infrastructure.

**Answer guidance:**

Financial systems have security requirements that go significantly beyond typical web applications:

**1. Data classification and protection:**

| Data Type | Sensitivity | Protection Required |
|---|---|---|
| Market data (prices, trades) | High | Encryption in transit, access controls, entitlement enforcement |
| Customer PII | Critical | Encryption at rest + in transit, data masking in non-prod, GDPR compliance |
| Trading credentials / API keys | Critical | Hardware security modules (HSMs), secrets management, rotation policies |
| Transaction records | High | Tamper-proof audit trails, immutable logging |
| Regulatory reports | High | Access controls, integrity verification, retention policies |

**2. Access control and entitlements:**
- **Granular entitlements:** Users see only the data they're entitled to. A client with delayed data entitlement must not receive real-time data.
- **Separation of duties:** The person who creates a trade cannot approve it. Testing must verify these controls.
- **Multi-tenancy isolation:** One client's data must never leak to another client's view.

**3. Regulatory requirements:**
- **MiFID II** (EU): Transaction reporting, best execution, audit trails, timestamp precision.
- **SOX** (US): Internal controls, financial reporting accuracy, change management controls.
- **PCI DSS** (if handling payment data): Network segmentation, encryption, access logging.
- **Cyber resilience regulations:** Financial regulators increasingly require proof of cyber resilience testing (e.g., EU DORA regulation).

**4. Specific attack vectors in finance:**
- **Market manipulation via data injection:** What if someone injects false price data into the feed?
- **Insider trading enablement:** Can system access be abused to gain trading advantage?
- **DDoS against trading infrastructure:** Testing resilience against availability attacks during market hours.
- **API abuse:** Rate limiting, authentication bypass, data scraping via APIs.

**5. Testing implications:**
- Security testing in financial systems must be **continuous, automated, and auditable**.
- Test environments must handle data masking — you cannot use real customer data or real trading data in test environments.
- Penetration testing must be carefully scheduled to avoid impacting live systems.
- All security testing activities must be documented for regulatory audits.

**Tips:**
- Connect to your experience: "While I haven't worked in financial markets specifically, the data integrity and access control challenges are analogous to what I tested in SAP-Salesforce integrations — ensuring the right data reaches the right system with the right permissions."
- Show awareness of the business impact: "A security breach at a financial infrastructure company like LSEG doesn't just affect one organisation — it can undermine trust in the entire market."
- For Amy: position security testing as part of the overall quality strategy, not a separate activity.

---

### Q87: Tell us about your experience with Veracode.

**What's being evaluated:** Hands-on experience with a specific security testing tool (listed on your CV), ability to describe practical application in STAR format.

**Answer guidance (STAR format):**

> **Situation:** "At Sysco LABS, during the Hybris E-Commerce project, we were responsible for ensuring our application met the client's (Brakes UK) security compliance requirements before each production release."
>
> **Task:** "As the QA engineer on the team, I was involved in conducting security testing using Veracode to identify vulnerabilities in our codebase and ensure compliance with the client's security standards."
>
> **Action:** "I worked with Veracode's static analysis (SAST) scanning capabilities. We integrated Veracode scans into our release process — before each major release, we submitted the application build for scanning. My specific responsibilities included:
> - Reviewing the scan results and triaging findings by severity (critical, high, medium, low).
> - Collaborating with developers to understand and remediate findings — explaining the vulnerability, its potential impact, and suggesting fixes.
> - Verifying that remediated issues were resolved in subsequent scans.
> - Documenting the security testing outcomes in the release report for stakeholder sign-off.
>
> One specific example: Veracode flagged a potential SQL injection vulnerability in a search function that used string concatenation instead of parameterised queries. I worked with the developer to refactor the code to use prepared statements, verified the fix resolved the Veracode finding, and added a targeted test case to our automation suite to prevent regression."
>
> **Result:** "Our application consistently passed Veracode security scans with zero critical or high findings at release time. The process also improved the team's security awareness — developers started proactively checking for common vulnerability patterns during code reviews, which reduced the number of findings in each subsequent scan."

**Broader Veracode knowledge to demonstrate:**

| Veracode Feature | What It Does |
|---|---|
| **Static Analysis (SAST)** | Scans source code or compiled binaries for security vulnerabilities |
| **Dynamic Analysis (DAST)** | Tests running applications for runtime vulnerabilities |
| **Software Composition Analysis (SCA)** | Identifies vulnerabilities in third-party libraries and dependencies |
| **Manual Penetration Testing** | Veracode also offers human-led pen testing services |
| **Veracode Fix** | AI-assisted remediation suggestions for identified vulnerabilities |
| **Policy compliance** | Define security policies and track compliance across applications |

**Tips:**
- Be honest about your depth of experience — don't claim to be a Veracode expert if you primarily reviewed results rather than configured scans.
- Connect to the SDET role: "Security scanning is another dimension of quality. As an SDET, I advocate for integrating security checks into the CI/CD pipeline alongside functional quality gates — Veracode's CI integration capabilities support exactly this approach."
- For financial systems: "In a financial infrastructure company like LSEG, security scanning isn't a nice-to-have — it's a regulatory requirement. Veracode or similar tools should be part of every pipeline."
