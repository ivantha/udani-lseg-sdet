# 9. Scenario-Based / Problem-Solving

---

### Q62: You're given a legacy system with no existing tests. How do you build a test strategy from scratch?

**What's being evaluated:** Strategic thinking, prioritization, ability to work independently within defined parameters.

**Answer guidance:**

1. **Understand the system:**
   - Review documentation (if any), architecture diagrams, and codebase.
   - Interview developers, ops, and business users to understand critical workflows and known pain points.
   - Review production incident history to identify fragile areas.

2. **Prioritize by risk:**
   - Identify the most critical business flows (e.g., order processing, data feeds, reporting).
   - Focus first on areas with highest risk of failure and highest business impact.

3. **Start with characterization tests:**
   - Write tests that document the current behavior (not expected behavior). These act as a safety net before making changes.

4. **Build incrementally:**
   - Add smoke tests for critical paths (can be run in < 15 minutes).
   - Add regression tests for areas being actively modified.
   - Introduce API tests before UI tests (faster to write, more stable, better ROI).

5. **Establish infrastructure:**
   - Set up a CI pipeline, even a basic one, to run tests automatically.
   - Set up test environments and test data management.

6. **Set targets:**
   - Define coverage goals per quarter. Track and report progress.

**Tips:**
- Emphasize pragmatism: "I wouldn't try to achieve 90% coverage in a month. I'd focus on the top 10 critical workflows first."
- Mention that you'd make recommendations to your immediate manager (per the JD scope).

---

### Q63: A system integration test is failing intermittently in the CI pipeline but passes locally. Walk us through your debugging approach.

**What's being evaluated:** Systematic debugging, analytical capability, understanding of CI/CD environments.

**Answer guidance:**

1. **Gather data:**
   - How often does it fail? (20% of the time? Only on certain days?)
   - Is it always the same assertion that fails?
   - Check CI logs for the exact error message and stack trace.

2. **Identify differences between local and CI:**
   - **Environment:** OS, installed dependencies, database version, service versions.
   - **Timing:** CI machines may be slower or faster, causing race conditions.
   - **State:** Is there leftover data from previous test runs in CI? Locally you might have a clean slate.
   - **Resources:** CI runners may have limited CPU/memory, causing timeouts.
   - **Parallelism:** Are other tests running concurrently in CI that share resources?

3. **Reproduce:**
   - Try running the test multiple times locally in a loop: `for i in {1..50}; do pytest test_x.py; done`
   - Run in a Docker container matching the CI environment.
   - Run with the same parallelism settings as CI.

4. **Common culprits:**
   - **Race conditions** — Async operations completing in different orders.
   - **Shared test data** — Tests not properly isolating their data.
   - **External dependencies** — Third-party service being flaky.
   - **Clock/timezone** — CI server in a different timezone than local.

5. **Fix and verify:**
   - Address the root cause (not just add a retry).
   - Run the test 100+ times in CI to confirm stability.

**Tips:**
- Show systematic thinking — don't jump to conclusions.
- Mention that you'd add better logging/screenshots for future debugging.

---

### Q64: You discover that a third-party API your system depends on has changed its response format with no notice. What do you do?

**What's being evaluated:** Incident response, communication, proactive testing practices.

**Answer guidance:**

**Immediate response:**
1. **Assess impact** — What functionality is broken? How many users/systems are affected?
2. **Communicate** — Alert the team, product owner, and service management immediately. If production is affected, trigger the incident process.
3. **Investigate** — Confirm the change by comparing current responses to documented API specs. Capture evidence.
4. **Workaround** — If possible, implement a temporary fix (e.g., adapter layer to transform the new format to the expected format).

**Resolution:**
5. **Contact the vendor** — Report the undocumented change. Ask for release notes, a migration guide, or a rollback.
6. **Fix the code** — Update the application to handle the new format. Update tests accordingly.
7. **Test thoroughly** — Run regression tests with both old and new response formats if backward compatibility is needed.

**Prevention:**
8. **Contract tests** — Implement API contract tests (e.g., Pact) that run regularly against the third-party API to detect changes early.
9. **Version pinning** — If the API supports versioning, pin to a specific version.
10. **Monitoring** — Add health checks that validate expected response structure from third-party APIs.

**Tips:**
- Show that you think beyond the immediate fix to prevention.
- In financial systems, a broken third-party API (e.g., market data provider) can have severe consequences — convey that urgency.

---

### Q65: How would you test a real-time market data streaming service for correctness and performance simultaneously?

**What's being evaluated:** Ability to design complex test scenarios for LSEG's core domain.

**Answer guidance:**

**Correctness testing:**
- **Data validation** — Compare received data against a trusted reference source (e.g., exchange direct feed vs. consolidated feed). Verify symbol, price, volume, timestamp accuracy.
- **Sequencing** — Verify messages arrive in the correct order. Detect and flag gaps or duplicates.
- **Completeness** — Ensure all subscribed instruments are being received. No missing symbols.
- **Edge cases** — Market halt/resume messages, corporate actions (splits, dividends), zero-volume instruments, negative price adjustments.

**Performance testing:**
- **Throughput** — Measure messages processed per second under various load levels.
- **Latency** — Measure end-to-end latency from source to consumer at p50, p95, p99, and max.
- **Sustained load** — Run for extended periods (8+ hours simulating a full trading day) to detect degradation.
- **Burst handling** — Simulate sudden spikes (e.g., market open, major news events).

**Simultaneous approach:**
- Run correctness checks as consumers of the streaming data alongside performance monitoring.
- Use a "canary consumer" that validates every Nth message for correctness while the performance harness measures throughput and latency.
- Compare timestamps across the pipeline to identify where latency is introduced.

**Tools:** Custom consumers in Java/C++ for low-latency measurement, Kafka consumer lag monitoring, Prometheus/Grafana for dashboards.

**Tips:**
- Show understanding that correctness and performance can be at odds — e.g., adding validation logic introduces latency.
- Mention market replay testing using historical data.

---

### Q66: You have one week before release and the automation suite covers only 40% of the new features. What's your plan?

**What's being evaluated:** Prioritization under pressure, risk-based thinking, practical decision-making.

**Answer guidance:**

1. **Risk-based prioritization:**
   - List all untested features. Classify by business criticality and risk.
   - Focus automation on the highest-risk, most critical paths.

2. **Smart testing strategy:**
   - **Automate the top 20%** — The critical happy-path scenarios that must work.
   - **Manual testing for the rest** — Experienced testers do exploratory and edge-case testing on medium-risk features.
   - **Skip low-risk, low-impact features** — Document them as known coverage gaps with a plan to cover post-release.

3. **Parallel work:**
   - Split the team: some writing automation, others doing targeted manual testing.
   - If possible, pair SDETs with manual testers — SDETs automate while testers execute manually.

4. **Communicate:**
   - Report the coverage gap to the project manager and product owner with a clear risk assessment.
   - Get agreement on what's acceptable and document the decision.

5. **Post-release plan:**
   - Commit to increasing automation coverage to 80%+ in the next sprint.
   - Add the remaining tests to the backlog with estimated effort.

**Tips:**
- Don't promise 100% coverage in a week — show realistic judgment.
- Emphasize risk-based decisions: "I'd rather have 100% coverage of the 5 most critical features than 40% coverage of everything."
- Mention that in financial systems, you might recommend delaying the release if critical regulatory or data-integrity features are uncovered — show you know when to escalate.

---

### Q67: The team wants to migrate from monolith to microservices. How do you adapt the test strategy?

**What's being evaluated:** Architectural awareness, ability to evolve testing practices, strategic thinking about long-term quality.

**Answer guidance:**

**Phase 1: Before migration (testing the monolith):**
- Establish a comprehensive regression test suite for the monolith — this becomes your safety net.
- Write characterization tests that document current behavior.
- Identify integration points that will become service boundaries.

**Phase 2: During migration (strangler fig pattern):**
- **Contract tests** — As each service is extracted, implement contract tests (Pact) between the new service and remaining monolith.
- **Parallel running** — Run both old and new implementations simultaneously. Compare outputs for consistency.
- **Feature flags** — Toggle between monolith and microservice implementations. Test both paths.
- **Integration tests** — Focus on service boundaries. Does the extracted service behave identically to the monolith component it replaced?

**Phase 3: After migration (microservices architecture):**
- **Per-service testing** — Each service has its own unit and integration tests.
- **Contract testing** — Mandatory for all service-to-service interactions.
- **End-to-end tests** — Minimal, covering only critical business flows.
- **Chaos testing** — Test resilience: service failures, network partitions, latency injection.
- **Observability** — Verify distributed tracing, correlated logging, and monitoring.

**Key changes in testing approach:**

| Aspect | Monolith | Microservices |
|---|---|---|
| **Unit tests** | Test within a single codebase. | Test within each service independently. |
| **Integration tests** | Database and internal modules. | Service-to-service communication, message queues. |
| **Deployment testing** | One deployment to test. | Multiple independent deployments — test compatibility. |
| **Data testing** | Single database. | Distributed data — eventual consistency, data duplication. |
| **Failure modes** | Process crash, memory leak. | Network failures, partial outages, cascading failures. |

**Tips:**
- Emphasize that testing strategy must evolve with the architecture: "You can't test microservices the same way you test a monolith."
- Contract tests become the most important investment — highlight this.
- Mention the risk of a "distributed monolith" — tightly coupled microservices that are worse than the original monolith.

---

### Q68: You're asked to test a system with no documentation. What do you do?

**What's being evaluated:** Resourcefulness, exploratory testing skills, ability to work with ambiguity.

**Answer guidance:**

**Step-by-step approach:**

1. **Gather context from people:**
   - Interview developers — ask about architecture, critical flows, known issues, and recent changes.
   - Talk to operations — what breaks most? What does monitoring show?
   - Talk to business users — what are the critical workflows? What matters most?
   - Review support tickets and incident history for patterns.

2. **Explore the system:**
   - **Exploratory testing** — Use the system as a user would. Map out features, workflows, and data flows.
   - **Code review** — Read the source code to understand business logic, edge cases, and error handling.
   - **API exploration** — Use tools like Swagger UI, Postman, or curl to discover and test APIs.
   - **Database inspection** — Review schema, relationships, and stored procedures to understand data models.

3. **Create documentation as you go:**
   - Map out system architecture and data flows.
   - Document discovered features and their expected behavior.
   - This becomes both test documentation and system documentation.

4. **Build tests incrementally:**
   - Start with characterization tests — capture current behavior as the baseline.
   - Add smoke tests for discovered critical paths.
   - Use exploratory testing sessions with session-based test management (SBTM) to systematically cover the system.

5. **Validate your understanding:**
   - Share your documentation with developers and business users: "Is this how it works?"
   - Correct misunderstandings early before they become incorrect tests.

**Tips:**
- Frame this as an opportunity, not a problem: "An undocumented system is a chance to add significant value — the documentation I create as part of testing becomes a lasting asset for the team."
- Mention that you'd use tools to accelerate understanding: log analysis, network traffic capture, database query logs.
- Show that you don't wait for perfect information to start testing: "I begin exploratory testing on day one. Formal test cases follow as my understanding deepens."

---

### Q69: How would you test a disaster recovery failover for a trading system?

**What's being evaluated:** Understanding of high-availability requirements in financial systems, ability to test critical infrastructure scenarios.

**Answer guidance:**

**Why DR testing matters in trading systems:**
- Trading systems must meet strict uptime SLAs (often 99.99%+).
- An outage during market hours means lost trades, regulatory scrutiny, and reputational damage.
- Regulators (e.g., SEC, FCA) may require evidence of DR testing.

**DR test plan:**

1. **Define recovery objectives:**
   - **RTO (Recovery Time Objective)** — How quickly must the system recover? (e.g., < 30 seconds for trading systems)
   - **RPO (Recovery Point Objective)** — How much data loss is acceptable? (e.g., zero for trade data)

2. **Test scenarios:**
   - **Primary data center failure** — Simulate complete DC outage. Verify automatic failover to DR site.
   - **Database failover** — Primary DB goes down. Verify replica promotion and data integrity.
   - **Network partition** — Connectivity between primary and DR site is lost. Verify split-brain prevention.
   - **Partial failure** — Single service/component failure. Verify circuit breakers and fallback behavior.
   - **Failback** — After recovery, switch back to the primary site. Verify no data loss or duplication.

3. **Validation criteria:**
   - **Recovery time** — Measure actual RTO against the target.
   - **Data integrity** — Verify no trades were lost, duplicated, or corrupted during failover.
   - **Functionality** — Run smoke tests against the DR system to confirm all critical functions work.
   - **Performance** — Verify the DR system can handle production load (not just a "warm" backup).
   - **Monitoring** — Verify that alerts fire correctly during the failover and that the operations team is notified.

4. **Execution approach:**
   - Schedule DR tests during non-market hours initially (weekends/holidays).
   - Progress to "game day" exercises during market hours (with proper risk controls).
   - Involve operations, development, and business teams.
   - Document everything — results, issues found, timing measurements.

5. **Post-test activities:**
   - Review results against RTO/RPO targets.
   - Document any issues and track remediation.
   - Update runbooks based on lessons learned.

**Tips:**
- Show awareness of the business impact: "A failed DR failover during a real outage is catastrophic for a trading system. That's why we test it regularly, not just once."
- Mention regulatory requirements: "Regulators expect financial institutions to demonstrate DR capability. Test results may be reviewed during audits."
- Relate to LSEG: "For a market infrastructure provider like LSEG, DR is existential — the exchange going down affects entire markets."

---

### Q70: A critical automated test has been disabled for months because "nobody has time to fix it." How do you handle it?

**What's being evaluated:** Ownership mentality, ability to address systemic issues, practical prioritization.

**Answer guidance:**

**Step 1: Assess the situation**
- What does the disabled test cover? What's the risk of not having it?
- Why was it disabled? What's the root cause — flaky test, environment issue, or actual application bug?
- Is there any manual testing covering the same scenario? If not, it's an unguarded risk.

**Step 2: Quantify the risk**
- "This test validates trade settlement calculations. Without it, a regression in settlement could reach production undetected."
- Frame in business terms: cost of a potential production incident vs. cost of fixing the test.

**Step 3: Make a case for fixing it**
- Don't ask for permission — if it's within your scope, just fix it.
- If it requires broader effort, present the risk to your manager with a clear recommendation.
- Propose a time-boxed investigation: "Give me 4 hours to diagnose and fix this. If it's bigger than that, I'll come back with an estimate."

**Step 4: Fix or retire**
- **Fix** — Investigate the root cause, fix it, verify the test is stable (run 50+ times), re-enable it.
- **Refactor** — If the test is poorly written or testing the wrong thing, rewrite it properly.
- **Retire** — If the test is genuinely obsolete (feature was removed, test is redundant), delete it. A disabled test that nobody needs is worse than no test — it creates the illusion of coverage.

**Step 5: Prevent recurrence**
- Establish a team policy: disabled tests must have an associated ticket with an owner and a deadline.
- Track disabled tests as a metric — report on the count in sprint reviews.
- Add a CI check: if a test has been disabled for > 2 weeks, flag it automatically.

**Tips:**
- Show ownership: "I wouldn't wait to be asked. If I notice a disabled test covering a critical area, I'd investigate it proactively."
- Address the cultural issue: "A culture where tests stay disabled for months indicates that test maintenance isn't prioritized. Part of the fix is changing the team's attitude toward test health."
- Relate to the LSEG value of **Excellence**: "Accepting disabled tests as normal is accepting mediocrity. Excellence means maintaining the tools we depend on."
