# 3. Performance & Non-Functional Testing

> **Honest framing:** This is a gap area. Udani's direct experience with dedicated performance testing tools (JMeter, Gatling, Locust) is limited. Her performance validation experience has been at the API level — using REST Assured to assert response times and monitoring API throughput during integration testing. **Strategy:** Acknowledge the gap honestly, demonstrate strong conceptual understanding, describe API-level performance validation you have done with REST Assured, and show readiness to learn dedicated tools quickly.

---

### Q21: How would you design a performance test for a high-throughput financial data feed?

**What's being evaluated:** Performance testing knowledge applied to LSEG's core domain — market data.

**Answer guidance:**

1. **Define objectives:**
   - Throughput: How many messages/second must the system handle? (e.g., 100,000 ticks/second)
   - Latency: What's the acceptable end-to-end latency? (e.g., < 5ms for market data)
   - Sustained load: Can it maintain performance over hours?

2. **Test types:**
   - **Load test** — Simulate expected peak load (e.g., market open, high-volatility events).
   - **Stress test** — Push beyond expected capacity to find the breaking point.
   - **Endurance/soak test** — Run at normal load for extended periods to detect memory leaks or resource exhaustion.
   - **Spike test** — Sudden bursts of activity (e.g., flash crash scenario).

3. **Test design:**
   - Use realistic data patterns (not just random payloads).
   - Simulate multiple data consumers.
   - Measure at multiple points: producer, network, consumer.

4. **Tools:** JMeter, Gatling, Locust, or custom tools for low-latency protocols.

5. **Metrics to capture:** Throughput (msg/sec), latency (p50, p95, p99), CPU/memory utilization, GC pauses, network I/O, error rate.

6. **Analysis:** Compare against SLAs, identify bottlenecks, profile hotspots.

**Tips:**
- Mention that financial data feeds often use specialized protocols (e.g., FIX, ITCH, proprietary binary) — generic HTTP load testing tools may not suffice.
- Show awareness that latency outliers (p99) matter more than averages in financial systems.

---

### Q22: What tools have you used for performance/load testing? Walk us through a test you've designed.

**What's being evaluated:** Hands-on experience, ability to articulate a complete performance test scenario.

**Answer guidance:**

Pick a real example and walk through it:

- **Context:** "We had an API serving real-time pricing data. Before a major release, we needed to validate it could handle 10x current traffic."
- **Tool choice:** "I used Locust (Python-based) because the team was already proficient in Python and we needed custom load shapes."
- **Script design:** "Created user classes simulating different client behaviors — some polling every second, some subscribing to WebSocket feeds."
- **Environment:** "Deployed the test target on AWS using production-equivalent infrastructure (same instance types, same database size)."
- **Execution:** "Ramped up from 100 to 5,000 concurrent users over 30 minutes, then held steady for 2 hours."
- **Findings:** "Discovered that database connection pooling was exhausted at 3,000 users. Response times degraded from 50ms to 2s. The fix was increasing the pool size and adding read replicas."
- **Outcome:** "After the fix, the system handled 7,000 concurrent users with p99 latency under 200ms."

**Tips:**
- Be specific about numbers and outcomes.
- Show that you don't just run the test — you analyze, report, and drive the fix.

**Udani's honest framing:**

> "I want to be upfront: my direct experience with dedicated performance testing tools like JMeter or Gatling is limited. My performance validation has been at the API level — using REST Assured to assert response times and throughput during integration testing. For example, in the Vendor Invoice Management project, I added response time assertions to our API tests to catch performance regressions when invoice processing time exceeded acceptable thresholds.
>
> However, I understand the fundamentals well: load testing to validate capacity, stress testing to find breaking points, endurance testing for memory leaks and degradation over time, and spike testing for sudden load changes. I know the key metrics — p50, p95, p99 latency, throughput, error rates, and resource utilisation.
>
> To reduce this gap, I'm preparing to deepen my hands-on skills with JMeter before starting the role — familiarising myself with thread groups, samplers, listeners, and assertions. I understand that performance is mission-critical in financial markets infrastructure, and I'm committed to developing this capability quickly."

**Pre-interview preparation checklist:**
- [ ] Install Apache JMeter and run a basic load test against a public API.
- [ ] Learn key JMeter concepts: thread groups (virtual users), samplers (HTTP requests), listeners (results visualisation), assertions, and timers.
- [ ] Create a simple test plan: ramp 50 users over 2 minutes, hold steady for 5 minutes, measure response times and error rates.
- [ ] Understand how to read a JMeter results summary: mean/median/p95/p99 response times, throughput (requests/sec), error percentage.
- [ ] Be able to explain the difference between JMeter, Gatling, and Locust at a high level.

---

### Q23: How do you identify performance bottlenecks — at the application layer vs. network layer vs. database layer?

**What's being evaluated:** In-depth analysis capability (explicitly required in JD), systematic debugging approach.

**Answer guidance:**

**Systematic approach:**

1. **Establish baseline metrics** across all layers before testing.

2. **Application layer:**
   - Profile the application (e.g., Java Flight Recorder, Python cProfile, .NET Profiler).
   - Check for CPU-bound operations, memory leaks, inefficient algorithms, excessive garbage collection.
   - Monitor thread/connection pool utilization.

3. **Network layer:**
   - Check latency between services (ping, traceroute).
   - Monitor bandwidth utilization, packet loss, TCP retransmissions.
   - Look for DNS resolution delays, firewall/proxy overhead.
   - Tools: Wireshark, tcpdump, netstat.

4. **Database layer:**
   - Identify slow queries (slow query log, EXPLAIN plans).
   - Monitor connection pool usage, lock contention, deadlocks.
   - Check I/O wait times, index utilization, table scan frequency.
   - Tools: Database-native monitoring, APM tools.

5. **Infrastructure:**
   - CPU, memory, disk I/O, network I/O on each host.
   - Cloud-specific: check if you're hitting service limits (e.g., AWS throttling).

**Tips:**
- Describe a real scenario where you narrowed down a bottleneck: "Initially it looked like the API was slow, but profiling showed the application was waiting on database queries. The root cause was a missing index on a frequently-joined column."

---

### Q24: What's the difference between load, stress, soak, and spike testing?

**What's being evaluated:** Clarity of performance testing concepts, ability to choose the right test type for the situation.

**Answer guidance:**

| Test Type | Purpose | Load Profile | Duration | What It Reveals |
|---|---|---|---|---|
| **Load Testing** | Validate system behavior under expected peak load. | Ramp up to expected max concurrent users/transactions. | Minutes to hours | Whether SLAs are met under normal peak conditions. |
| **Stress Testing** | Find the system's breaking point by exceeding expected capacity. | Increase load progressively beyond expected maximum until failure. | Until failure occurs | Maximum capacity, failure mode, and recovery behavior. |
| **Soak (Endurance) Testing** | Detect issues that emerge over extended periods — memory leaks, resource exhaustion, connection pool depletion. | Steady, moderate load (e.g., 70% of peak). | Hours to days (8+ hours typical) | Memory leaks, GC degradation, disk space exhaustion, log file growth. |
| **Spike Testing** | Validate behavior under sudden, dramatic load changes. | Sudden jump from low to very high load, then back. | Short bursts | Auto-scaling behavior, queue overflow handling, error rates during surges. |

**How to choose:**
- **Before release:** Load test (meets SLAs?), stress test (what's the ceiling?).
- **Before production deployment:** Soak test (stable over a trading day?).
- **For event readiness:** Spike test (IPO day, index rebalancing, earnings announcements).

**Tips:**
- In financial systems, soak testing is critical — the system must remain stable throughout a full trading day (6.5+ hours for equities markets).
- Mention that stress testing should also verify graceful degradation: "When the system reaches capacity, does it reject new connections cleanly, or does it crash?"

---

### Q25: How do you set performance baselines and SLAs?

**What's being evaluated:** Strategic thinking about performance, ability to define measurable quality targets, stakeholder communication.

**Answer guidance:**

**Setting baselines:**

1. **Measure current performance:**
   - Run performance tests against the existing system to establish current metrics.
   - Capture: response time (p50, p95, p99), throughput, error rate, resource utilization.
   - Run during realistic conditions (production-like data volume, concurrent users).

2. **Document baselines:**
   - Record metrics with environment details, data volume, and test date.
   - These become the reference point for detecting regressions.

3. **Trend tracking:**
   - Run the same performance tests regularly (weekly or per release).
   - Plot metrics over time to detect gradual degradation.

**Defining SLAs:**

1. **Collaborate with stakeholders:**
   - Business owners define acceptable user experience (e.g., "market data must update within 10ms").
   - Operations defines infrastructure constraints (e.g., "system must handle 50,000 concurrent connections").

2. **Use percentiles, not averages:**
   - "p99 response time < 200ms" is more meaningful than "average response time < 100ms" because averages hide outliers.

3. **Include error budgets:**
   - "99.9% of requests return successfully" — this allows 0.1% error rate, which is realistic for distributed systems.

4. **Make SLAs testable:**
   - Every SLA should be automatically verifiable in the performance test suite.
   - Pipeline gates should enforce SLAs: fail the build if p99 latency exceeds the threshold.

**Tips:**
- In financial markets, SLAs are often driven by regulatory requirements and competitive pressure — a data feed that's 1ms slower than a competitor's loses customers.
- Show that you understand the difference between SLIs (what you measure), SLOs (what you target), and SLAs (what you promise).

---

### Q26: Describe how you'd performance-test a database-heavy application.

**What's being evaluated:** Practical performance testing skills, database performance knowledge, ability to design targeted tests.

**Answer guidance:**

**Approach:**

1. **Identify database-intensive operations:**
   - Review the application to find operations with heavy database interaction: reports, searches, batch processing, transaction histories.
   - Check for N+1 query patterns, large result sets, complex joins.

2. **Prepare realistic test data:**
   - Load the database with production-scale data volumes (not just 100 rows).
   - Include realistic data distribution (e.g., some accounts with 10 trades, others with 10 million).
   - Ensure indexes are built and statistics are up to date.

3. **Design targeted test scenarios:**
   - **Query performance:** Benchmark individual critical queries with EXPLAIN/ANALYZE.
   - **Concurrent access:** Simulate multiple users performing reads and writes simultaneously.
   - **Lock contention:** Test scenarios where multiple transactions update the same rows.
   - **Connection pooling:** Gradually increase concurrent connections to find the pool saturation point.
   - **Batch operations:** Test ETL jobs, end-of-day processing, bulk inserts under load.

4. **Monitor at all levels:**
   - **Application:** Response times, queue depths, thread pool usage.
   - **Database:** Slow query log, lock waits, buffer pool hit ratio, disk I/O, active connections.
   - **Infrastructure:** CPU, memory, disk IOPS, network throughput.

5. **Optimize and retest:**
   - Add missing indexes, optimize queries, tune connection pool sizes.
   - Consider read replicas, caching layers, or query result pagination.
   - Retest to verify improvements and ensure no regressions.

**Tips:**
- In financial systems, end-of-day batch processing (settlement, reconciliation, reporting) often puts extreme load on databases. Test these scenarios specifically.
- Mention that you'd test with production-scale data: "Testing with 1,000 rows won't reveal issues that appear with 100 million rows — query plans change, indexes behave differently, and memory requirements shift."
- Show awareness of database-specific tuning: PostgreSQL's `work_mem`, Oracle's SGA, SQL Server's max degree of parallelism.
