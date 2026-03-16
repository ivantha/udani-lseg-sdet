# 2. Test Automation & Programming

---

### Q11: Describe your test automation framework architecture. What design patterns do you use?

**What's being evaluated:** Technical depth, architectural thinking, hands-on automation experience (2+ years required).

**Answer guidance:**

Describe a framework you've built or contributed to. A strong answer covers:

- **Architecture layers:**
  - **Test Layer** — Test cases and test suites.
  - **Business Logic Layer** — Page Objects (for UI) or API client wrappers (for API testing).
  - **Utility/Common Layer** — Logging, reporting, config management, test data helpers.
  - **Driver/Infrastructure Layer** — WebDriver, REST clients, database connectors.

- **Design patterns:**
  - **Page Object Model (POM)** — Encapsulates UI element locators and interactions. Reduces maintenance when UI changes.
  - **Data-Driven Testing** — Externalize test data (CSV, JSON, database) to run the same test with different inputs.
  - **Keyword-Driven** — Abstract test steps into keywords (common with Robot Framework).
  - **Factory Pattern** — For creating test data objects.
  - **Singleton** — For managing browser/driver instances.

- **Reporting:** Allure, ExtentReports, or built-in Robot Framework reports.
- **CI Integration:** Tests triggered by Jenkins/GitHub Actions on every commit or nightly.

**Tips:**
- Be specific about tools: "I used Python + pytest + Selenium with POM for UI tests, and requests + pytest for API tests."
- Mention how you handle test data, environment configuration, and parallel execution.
- If you've used Robot Framework, highlight it — it's mentioned in the JD.

---

### Q12: Write a small script (pseudocode is fine) that reads a CSV of test cases, executes them against an API, and reports pass/fail.

**What's being evaluated:** Practical coding ability, automation thinking.

**Answer guidance (Python example):**

```python
import csv
import json
import requests

def run_tests(csv_file, base_url):
    results = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            endpoint = row['endpoint']
            method = row['method']
            expected_status = int(row['expected_status'])
            payload = json.loads(row['payload']) if row.get('payload') else None

            response = requests.request(
                method,
                f"{base_url}{endpoint}",
                json=payload
            )

            status = "PASS" if response.status_code == expected_status else "FAIL"
            results.append({
                'test': row['test_name'],
                'status': status,
                'expected': expected_status,
                'actual': response.status_code
            })
            print(f"[{status}] {row['test_name']}: "
                  f"Expected {expected_status}, Got {response.status_code}")

    passed = sum(1 for r in results if r['status'] == 'PASS')
    print(f"\nResults: {passed}/{len(results)} passed")
    return results
```

**Java equivalent (preferred — Udani's primary language, uses REST Assured):**

```java
import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;

import java.io.BufferedReader;
import java.io.FileReader;

public class CsvApiTestRunner {

    @DataProvider(name = "csvTestData")
    public Object[][] readCsvData() throws Exception {
        List<Object[]> data = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("test_cases.csv"))) {
            String line = br.readLine(); // skip header
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                data.add(new Object[]{
                    values[0], // testName
                    values[1], // endpoint
                    values[2], // method
                    Integer.parseInt(values[3]), // expectedStatus
                    values.length > 4 ? values[4] : "" // payload
                });
            }
        }
        return data.toArray(new Object[0][]);
    }

    @Test(dataProvider = "csvTestData")
    public void executeApiTest(String testName, String endpoint,
                                String method, int expectedStatus, String payload) {
        Response response = RestAssured.given()
            .baseUri("https://api.example.com")
            .header("Content-Type", "application/json")
            .body(payload.isEmpty() ? "" : payload)
            .request(method, endpoint);

        assertEquals(response.getStatusCode(), expectedStatus,
            String.format("[%s] Expected %d, got %d", testName,
                          expectedStatus, response.getStatusCode()));
    }
}
```

> **Note:** Java + REST Assured is Udani's primary stack. The Python example above is equally valid — choose based on the interviewer's preference. REST Assured's fluent API makes test code highly readable and is widely used in enterprise test automation.

**Tips:**
- Show error handling awareness (timeouts, connection errors).
- Mention how you'd extend it: parameterized headers, authentication, response body validation.
- Keep it clean and readable — they're assessing code quality too.

---

### Q13: How do you handle flaky tests in your automation suite?

**What's being evaluated:** Practical experience with real-world automation challenges, systematic debugging approach.

**Answer guidance:**

1. **Identify** — Track flaky tests with metrics (tests that pass/fail inconsistently without code changes). Tag them in your test management tool.
2. **Quarantine** — Move flaky tests to a separate suite so they don't block the CI pipeline, but don't delete them.
3. **Root Cause Analysis:**
   - **Timing issues** — Add explicit waits (not sleep), use polling/retry mechanisms for async operations.
   - **Test data dependencies** — Ensure tests create and clean up their own data (test isolation).
   - **Environment instability** — Shared environments with other teams causing interference.
   - **Order dependency** — Tests that rely on other tests running first.
4. **Fix** — Address the root cause. If it's an application bug causing inconsistency, log a defect.
5. **Prevent** — Code reviews for test code, guidelines for writing stable tests, mandatory wait strategies.

**Tips:**
- Never say "just add retries" as the solution — that masks the problem.
- Mention the business impact: "Flaky tests erode team trust in automation and slow down delivery."

---

### Q14: What's your approach to maintaining test scripts as the application evolves rapidly?

**What's being evaluated:** Long-term thinking, sustainable automation practices.

**Answer guidance:**

- **Modular design** — Use Page Object Model or service layers so changes to the UI/API are isolated to one place.
- **Configuration over hardcoding** — Externalize URLs, credentials, test data, and environment settings.
- **Version control** — Test code lives in the same repo (or a linked repo) as application code. PRs for test changes reviewed alongside feature changes.
- **Tagging and categorization** — Tag tests by feature, priority, and type (smoke, regression) so you can selectively run subsets.
- **Regular maintenance sprints** — Dedicate time to update deprecated tests, remove dead code, and refactor.
- **Shift-left** — Developers write unit and integration tests; SDETs focus on higher-level automation. This distributes the maintenance burden.

**Tips:**
- Mention that in a DevOps environment, test maintenance is a continuous activity, not a phase.

---

### Q15: How do you integrate automated tests into a CI/CD pipeline? What tools have you used?

**What's being evaluated:** DevOps integration skills, CI/CD understanding — role explicitly sits within a DevOps team.

**Answer guidance:**

**Pipeline stages:**
1. **Commit stage** — Unit tests and static analysis run on every push. Fast feedback (< 5 min).
2. **Build stage** — Application is compiled/built, Docker images created.
3. **Integration test stage** — API and integration tests run against a deployed test environment.
4. **System test stage** — Full end-to-end and system tests (can be nightly if slow).
5. **Performance test stage** — Load/stress tests on a staging environment (scheduled, not on every commit).
6. **Gate** — Pipeline fails if tests don't meet defined thresholds (e.g., >95% pass rate, no critical defects).

**Tools:**
- **CI/CD:** Jenkins, GitLab CI, GitHub Actions, Azure DevOps.
- **Test execution:** pytest, JUnit, Robot Framework, TestNG.
- **Containerization:** Docker for consistent test environments.
- **Reporting:** Allure, JUnit XML reports integrated into CI dashboards.
- **Notifications:** Slack/email alerts on failure.

**Tips:**
- Show that you understand the trade-off between pipeline speed and test thoroughness.
- Mention parallelizing tests to reduce pipeline time.

---

### Q16: Explain the Robot Framework. When would you choose it over pytest or a JUnit-based approach?

**What's being evaluated:** Familiarity with Robot Framework (mentioned in JD), ability to choose the right tool for the context.

**Answer guidance:**

**Robot Framework** is a keyword-driven, open-source test automation framework written in Python. It uses a tabular syntax that makes tests readable by non-technical stakeholders.

**Key features:**
- **Keyword-driven** — Tests are written as sequences of keywords (e.g., `Open Browser`, `Input Text`, `Click Button`).
- **Extensible** — Libraries for web (SeleniumLibrary), API (RequestsLibrary), database, SSH, and more.
- **Built-in reporting** — Generates HTML reports and logs out of the box.
- **Tag-based execution** — Run subsets of tests by tags.

**When to choose Robot Framework:**
- Tests need to be readable by non-technical team members (BAs, manual testers).
- You want a unified framework for UI, API, and database testing.
- Keyword reuse across teams is valuable.

**When to choose pytest/JUnit instead:**
- You need maximum flexibility and complex test logic.
- The team is highly technical and prefers code over keywords.
- Performance or low-level unit testing where keyword abstraction adds overhead.

**Tips:**
- If you have Robot Framework experience, describe a specific project.
- If you don't, be honest but show willingness: "I've primarily used pytest, but I understand Robot Framework's value for cross-functional teams and I'm comfortable picking it up."

---

### Q17: How do you handle test data management in automation?

**What's being evaluated:** Practical automation experience, understanding of test isolation and data lifecycle challenges.

**Answer guidance:**

**Test data strategies:**

1. **Create and tear down** — Each test creates its own data before execution and cleans it up after. Ensures test isolation.
   - Use API calls or database scripts to seed data.
   - Use `setup` and `teardown` fixtures (pytest) or `@BeforeEach`/`@AfterEach` (JUnit).

2. **Data factories** — Use the Factory pattern (e.g., FactoryBot, custom builders) to generate realistic test data programmatically.
   - Avoids hardcoded data that rots over time.
   - Can generate edge cases and random variations.

3. **Shared reference data** — Some data is static and shared across tests (e.g., country codes, instrument lists). Maintain this in version-controlled seed scripts.

4. **Database snapshots** — Restore a known database state before test suites run. Useful for complex legacy systems where creating data programmatically is difficult.

5. **Data masking/anonymization** — When using production-like data for testing, ensure sensitive information (PII, financial data) is masked to comply with regulations.

**Challenges in financial systems:**
- Test data must be realistic — random strings won't expose bugs in price calculation or trade matching logic.
- Regulatory constraints may limit what data can be used in test environments.
- Cross-system test data dependencies (e.g., an instrument must exist in the reference data system before it can be traded).

**Tips:**
- Emphasize test isolation: "Each test should be able to run independently, in any order, without depending on or interfering with other tests."
- Mention that poor test data management is one of the top causes of flaky tests.

---

### Q18: How do you implement API test automation? Walk through your approach.

**What's being evaluated:** Hands-on API testing skills, systematic approach to API quality assurance.

**Answer guidance:**

**Step-by-step approach:**

1. **Understand the API:**
   - Review API documentation (Swagger/OpenAPI specs).
   - Identify endpoints, methods, request/response schemas, authentication, and rate limits.

2. **Design test categories:**
   - **Positive tests** — Valid inputs, expected responses, correct status codes.
   - **Negative tests** — Invalid inputs, missing required fields, unauthorized access, malformed payloads.
   - **Boundary tests** — Min/max values, empty strings, large payloads.
   - **Security tests** — Authentication/authorization checks, injection attempts, sensitive data exposure.
   - **Performance tests** — Response time under load, concurrent requests.

3. **Implement the framework:**
   - Use `requests` + `pytest` (Python) or `RestAssured` (Java).
   - Create a base API client class that handles authentication, headers, and base URL configuration.
   - Write assertion helpers for common checks (status code, response schema, specific field values).

4. **Schema validation:**
   - Use JSON Schema validation to verify response structure automatically.
   - This catches breaking changes even when specific field values are correct.

5. **Contract testing:**
   - Use tools like Pact to ensure consumer-provider API contracts are maintained.
   - Especially important in microservices architectures.

6. **CI integration:**
   - Run API tests on every PR merge — they're fast and stable.
   - Include response time assertions to catch performance regressions early.

**Tips:**
- API tests give the best ROI in the testing pyramid — fast, reliable, and cover critical business logic.
- In financial systems, validate decimal precision, currency handling, and timestamp formats rigorously.

---

### Q19: What is BDD? How have you used Cucumber/Gherkin in test automation?

**What's being evaluated:** Understanding of Behavior-Driven Development, ability to bridge communication between technical and non-technical stakeholders.

**Answer guidance:**

**BDD (Behavior-Driven Development)** is a collaborative approach where developers, testers, and business stakeholders define application behavior using structured natural language before development begins.

**Gherkin syntax:**
```gherkin
Feature: Order Placement
  Scenario: Successful market order
    Given a client account with sufficient balance
    And the market is open for trading
    When the client places a market order for 100 shares of "LSEG.L"
    Then the order should be accepted
    And the order status should be "Filled"
    And the account balance should be reduced by the trade amount
```

**How Cucumber works:**
- **Feature files** — Written in Gherkin by BAs/testers to describe business scenarios.
- **Step definitions** — Code (Python/Java) that maps each Gherkin step to automation logic.
- **Runners** — Execute scenarios and generate reports.

**Benefits:**
- Living documentation — feature files serve as both specs and tests.
- Shared understanding — reduces miscommunication between business and development.
- Traceability — each scenario maps to a business requirement.

**Challenges:**
- Overhead — writing and maintaining step definitions adds effort.
- Anti-pattern risk — overly technical Gherkin defeats the purpose (e.g., "When I click the submit button on the /api/v2/orders endpoint").
- Step definition explosion — too many unique steps become unmaintainable.

**Tips:**
- Be pragmatic: "BDD is most valuable when there's active collaboration between testers and business analysts. If the feature files are only read by developers, the overhead may not be justified."
- Mention tools: Cucumber (Java), Behave (Python), or Robot Framework as a keyword-driven alternative.

---

### Q20: How do you ensure your automation tests are reliable across different environments?

**What's being evaluated:** Environment management skills, understanding of configuration challenges, practical DevOps experience.

**Answer guidance:**

**Key strategies:**

1. **Externalize configuration:**
   - Use environment variables or config files for URLs, credentials, database connections, and feature flags.
   - Never hardcode environment-specific values in test code.
   - Use a config hierarchy: defaults → environment-specific overrides → command-line parameters.

2. **Containerized test environments:**
   - Use Docker Compose or Testcontainers to create consistent, reproducible environments.
   - Same database version, same service versions, same network configuration.

3. **Test data isolation:**
   - Each environment has its own test data. Don't rely on data that exists in one environment but not another.
   - Use data factories that create required data before each test run.

4. **Environment health checks:**
   - Before running tests, verify that the target environment is available and services are healthy.
   - Fail fast with a clear message rather than running tests against a broken environment.

5. **Abstraction layers:**
   - Abstract environment-specific behaviors behind interfaces (e.g., authentication may work differently in dev vs. staging).
   - Use environment-specific implementations behind a common API.

6. **Consistent test execution:**
   - Use the same test runner, same Python/Java version, same dependency versions across environments.
   - Lock dependency versions in requirements.txt or pom.xml.

**Tips:**
- Mention a real scenario: "We had tests passing in dev but failing in staging because the database schema was different. I introduced Flyway migrations for test databases to ensure schema consistency."
- In financial systems, environment parity is critical — a test that passes in a non-production environment must behave the same way with production-like data volumes and configurations.

---

### Q88: How do you automate testing for Salesforce Lightning applications with Selenium?

**What's being evaluated:** Hands-on experience with a notoriously difficult automation target. This is a key differentiator — most SDET candidates haven't automated Salesforce Lightning.

**Answer guidance:**

Salesforce Lightning presents unique automation challenges that standard Selenium approaches can't handle out of the box:

**Challenge 1: Shadow DOM**

Lightning Web Components use shadow DOM, which standard Selenium locators cannot penetrate.

**Solution:** Use JavaScriptExecutor to pierce shadow DOM boundaries:

```java
// Piercing shadow DOM to access elements inside Lightning components
WebElement shadowHost = driver.findElement(By.cssSelector("lightning-input"));
SearchContext shadowRoot = (SearchContext) ((JavascriptExecutor) driver)
    .executeScript("return arguments[0].shadowRoot", shadowHost);
WebElement inputField = shadowRoot.findElement(By.cssSelector("input"));
inputField.sendKeys("test value");
```

**Challenge 2: Dynamic Element IDs**

Salesforce generates dynamic IDs that change across sessions and deployments (e.g., `input-47;a`).

**Solution:** Use stable locator strategies:
- **Relative CSS selectors** based on component hierarchy: `lightning-input[field-label='Account Name']`
- **Custom `data-*` attributes** (if the development team cooperates): `[data-testid='account-name-input']`
- **XPath with text matching** as a last resort: `//lightning-button[.//span[text()='Save']]`
- **Component-level selectors** based on Salesforce component names rather than rendered HTML

**Challenge 3: Iframes**

Salesforce uses iframes extensively — Visualforce pages, embedded components, and classic pages within Lightning Experience.

```java
// Switch to Visualforce iframe embedded in Lightning
driver.switchTo().frame(driver.findElement(
    By.cssSelector("iframe[title='accessibility title']")));
// Interact with elements inside iframe
driver.findElement(By.id("page:form:field")).sendKeys("value");
// Switch back to main content
driver.switchTo().defaultContent();
```

**Challenge 4: Asynchronous rendering**

Lightning components render asynchronously. Standard waits may not work.

**Solution:** Custom wait conditions for Lightning's loading states:

```java
// Wait for Lightning components to finish loading
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
wait.until(driver -> {
    return (Boolean) ((JavascriptExecutor) driver).executeScript(
        "return document.querySelector('.slds-spinner') === null " +
        "&& document.readyState === 'complete'"
    );
});
```

**Challenge 5: Sandbox management and test data**

- Salesforce sandboxes refresh periodically, resetting test data.
- **Solution:** API-first data setup using Salesforce REST API or Bulk API to create test data before UI test execution, rather than relying on pre-existing data.

```java
// Create test data via Salesforce REST API before UI test
RestAssured.given()
    .baseUri(sfBaseUrl)
    .header("Authorization", "Bearer " + accessToken)
    .body("{\"Name\": \"Test Account\", \"Industry\": \"Technology\"}")
    .post("/services/data/v58.0/sobjects/Account")
    .then().statusCode(201);
```

**Tips:**
- This is your strongest differentiator. Most candidates automate standard web apps — Salesforce Lightning automation requires specialised knowledge.
- Structure your answer as: "Here are the specific challenges I faced, and here's how I solved each one."
- Mention BrowserStack for cross-browser Salesforce testing (it's on your CV).
- For Andy: this demonstrates exactly the kind of hands-on problem-solving he values.

---

### Q89: How do you approach database testing and SQL validation in your automation?

**What's being evaluated:** Ability to validate data integrity across systems, SQL proficiency, understanding of data-driven testing in enterprise environments.

**Answer guidance:**

**Context from Udani's experience:** At Sysco LABS, testing SAP → Salesforce integrations required validating that data transformations were correct at the database level — an invoice created in SAP should appear with correct values in Salesforce, and vice versa.

**Database testing approach:**

**1. Cross-system data validation:**

The most critical database testing pattern in enterprise integration: verify that data flowing between systems arrives correctly.

```sql
-- Validate invoice data between SAP and Salesforce
SELECT
    sap.invoice_id,
    sap.amount AS sap_amount,
    sf.amount AS sf_amount,
    sap.currency,
    sap.vendor_id
FROM sap_invoices sap
JOIN sf_invoices sf ON sap.invoice_id = sf.external_reference_id
WHERE sap.amount != sf.amount
   OR sap.currency != sf.currency;
-- Any rows returned = data transformation bug
```

**2. Common SQL patterns for testing:**

| Pattern | SQL | Use Case |
|---|---|---|
| **Duplicate detection** | `SELECT column, COUNT(*) FROM table GROUP BY column HAVING COUNT(*) > 1` | Find duplicate records that shouldn't exist |
| **NULL/missing data** | `SELECT * FROM orders WHERE customer_id IS NULL OR order_date IS NULL` | Validate mandatory fields are populated |
| **Referential integrity** | `SELECT o.id FROM orders o LEFT JOIN customers c ON o.customer_id = c.id WHERE c.id IS NULL` | Find orphaned records |
| **Data range validation** | `SELECT * FROM prices WHERE unit_price <= 0 OR unit_price > 999999.99` | Validate business rules on data values |
| **Aggregation verification** | `SELECT order_id, SUM(line_amount) AS calc_total, order_total FROM orders JOIN order_lines... HAVING calc_total != order_total` | Verify calculated totals match stored totals |
| **Temporal consistency** | `SELECT * FROM audit_log WHERE created_date > modified_date` | Catch timestamp anomalies |

**3. JDBC in automation framework:**

Integrate database validation into your test automation:

```java
// Database validation in TestNG test using JDBC
@Test
public void verifyInvoiceDataIntegrity() throws SQLException {
    Connection conn = DriverManager.getConnection(dbUrl, dbUser, dbPass);

    String query = "SELECT sap.invoice_id, sap.amount, sf.amount " +
                   "FROM sap_invoices sap " +
                   "JOIN sf_invoices sf ON sap.invoice_id = sf.external_ref " +
                   "WHERE ABS(sap.amount - sf.amount) > 0.01";

    ResultSet rs = conn.createStatement().executeQuery(query);

    List<String> mismatches = new ArrayList<>();
    while (rs.next()) {
        mismatches.add(String.format("Invoice %s: SAP=%.2f, SF=%.2f",
            rs.getString("invoice_id"),
            rs.getDouble(2), rs.getDouble(3)));
    }

    assertTrue(mismatches.isEmpty(),
        "Data mismatches found: " + String.join("; ", mismatches));

    conn.close();
}
```

**4. Financial context — why this matters:**

- In financial systems, data integrity is non-negotiable. A price discrepancy between systems can cause incorrect trading decisions.
- Reconciliation testing (comparing data across systems) is a daily operation in financial infrastructure.
- Decimal precision matters — use `ABS(a - b) > 0.01` rather than `a != b` for floating-point comparison, but understand the required precision for the business context.

**Tips:**
- Connect to your real experience: "In the Vendor Invoice Management project, I automated SQL-based validation of invoice data flowing from SAP to Salesforce — verifying amounts, currencies, vendor mappings, and line item totals."
- Mention test data cleanup: "After each test, I ran cleanup queries to remove test data — maintaining database hygiene is critical for test independence."
- For financial systems: "At LSEG, I'd expect database testing to include market data validation — ensuring prices, volumes, and timestamps in the database match what was received from exchange feeds."
