# 4. Infrastructure, Cloud & Networking

---

### Q27: Compare how you'd set up a test environment on AWS vs. Azure. What services would you use?

**What's being evaluated:** Cloud familiarity (AWS/Azure mentioned in JD), practical infrastructure knowledge.

**Answer guidance:**

| Concern | AWS | Azure |
|---|---|---|
| **Compute** | EC2 instances or ECS/EKS for containers | Virtual Machines or AKS for containers |
| **Database** | RDS, DynamoDB | Azure SQL, Cosmos DB |
| **Networking** | VPC, Security Groups, ALB | VNet, NSG, Application Gateway |
| **CI/CD Integration** | CodePipeline, or Jenkins on EC2 | Azure DevOps Pipelines |
| **Infrastructure as Code** | CloudFormation, Terraform | ARM Templates, Terraform |
| **Test Environment Provisioning** | Use Terraform/CDK to spin up ephemeral environments per feature branch | Same with Terraform or Bicep |
| **Cost Management** | Use spot instances for test environments, auto-shutdown schedules | Use B-series VMs, auto-shutdown |

**Tips:**
- Emphasize ephemeral environments: "I spin up test environments on demand and tear them down after tests complete to save costs."
- Mention security: "Test environments should mirror production security controls (VPCs, encryption, IAM roles) to catch security-related issues early."

---

### Q28: Explain the basics of TCP/IP. How would you troubleshoot a connectivity issue between two services in a test environment?

**What's being evaluated:** Networking fundamentals (mentioned as nice-to-have), systematic troubleshooting.

**Answer guidance:**

**TCP/IP basics:**
- **IP (Internet Protocol)** — Handles addressing and routing packets between hosts.
- **TCP (Transmission Control Protocol)** — Provides reliable, ordered, error-checked delivery of data. Uses a 3-way handshake (SYN, SYN-ACK, ACK) to establish connections.
- **Ports** — Identify specific services on a host (e.g., 80 for HTTP, 443 for HTTPS, 5432 for PostgreSQL).

**Troubleshooting steps:**

1. **Verify DNS resolution:** `nslookup` or `dig` — can the client resolve the server's hostname?
2. **Check network reachability:** `ping` — is the host reachable at the IP level?
3. **Check port connectivity:** `telnet host port` or `nc -zv host port` — is the service port open and accepting connections?
4. **Check firewall/security groups:** Are the right ports allowed in the security group or firewall rules?
5. **Check the service:** Is the target service actually running? (`systemctl status`, `docker ps`, check logs)
6. **Check routing:** `traceroute` — are packets taking the expected path? Any hops timing out?
7. **Check TLS/certificates:** If HTTPS, are certificates valid and trusted?
8. **Capture traffic:** Use `tcpdump` or Wireshark to inspect actual packets if all else looks correct.

**Tips:**
- Walk through a real example: "Service A couldn't reach Service B. Ping worked but telnet to port 8080 timed out. Turned out the security group only allowed traffic from the old subnet."

---

### Q29: You need to test a distributed system across Windows Server and Linux. How do you manage environment consistency?

**What's being evaluated:** Cross-platform proficiency (both mentioned in JD), practical environment management.

**Answer guidance:**

- **Containerization** — Use Docker to standardize the application runtime regardless of host OS. This eliminates "works on my machine" issues.
- **Infrastructure as Code** — Define environments using Terraform or Ansible. Ansible is particularly good for cross-platform provisioning (Windows and Linux modules).
- **Configuration management** — Centralize configuration (e.g., environment variables, config files) and use tools like Ansible, Puppet, or Chef to ensure consistency.
- **CI/CD matrix builds** — Run the same test suite on both platforms in the pipeline (e.g., GitHub Actions matrix strategy with `windows-latest` and `ubuntu-latest`).
- **Shared test scripts** — Write tests in cross-platform languages (Python, Java) rather than platform-specific scripts (PowerShell vs. Bash).
- **Platform-specific tests** — Some tests may need to be platform-specific (e.g., Windows service management vs. systemd). Clearly tag and separate these.

**Tips:**
- Mention any experience managing Windows Server environments — it's less common among SDETs and stands out.

---

### Q30: How do you use containers (Docker/Kubernetes) in your testing workflow?

**What's being evaluated:** Modern DevOps practices, environment management skills.

**Answer guidance:**

- **Test environment provisioning** — `docker-compose up` to spin up the entire application stack (app + database + message queue) locally or in CI.
- **Test isolation** — Each test run gets a fresh set of containers — no leftover state from previous runs.
- **Service virtualization** — Run mock/stub services in containers (e.g., WireMock for API mocks).
- **Parallel test execution** — Spin up multiple containers to run tests in parallel against isolated instances.
- **Kubernetes for scale testing** — Deploy the application to a K8s cluster to test auto-scaling, pod failures, and rolling updates.
- **Testcontainers library** — Programmatically spin up containers within test code (e.g., spin up a PostgreSQL container before integration tests, tear it down after).

**Tips:**
- If you've used Testcontainers, mention it — it shows modern testing practices.
- Relate to the JD: "In a DevOps team, being able to spin up and tear down test environments quickly is essential for fast feedback loops."

---

### Q31: How do you manage test data in cloud environments?

**What's being evaluated:** Cloud-native testing practices, data management in distributed systems, security awareness.

**Answer guidance:**

**Challenges of test data in the cloud:**
- Data residency and compliance requirements (GDPR, data sovereignty).
- Cost of maintaining large test datasets in cloud storage/databases.
- Data consistency across multiple services and regions.
- Security of sensitive test data (especially in financial systems).

**Strategies:**

1. **Ephemeral test databases:**
   - Spin up a fresh database instance for each test run using IaC (Terraform) or Testcontainers.
   - Populate with seed data, run tests, tear down. No persistent test data to manage.

2. **Data subsetting:**
   - Extract a representative subset of production data (anonymized/masked) for testing.
   - Tools like Delphix, Tonic, or custom scripts can create realistic subsets.

3. **Synthetic data generation:**
   - Generate test data programmatically that matches production patterns.
   - Use libraries like Faker (Python) or custom generators for domain-specific data (e.g., realistic trade records, price feeds).

4. **Shared reference data services:**
   - Centralize reference data (instrument lists, currency codes, exchange calendars) in a read-only service accessible by all test environments.

5. **Data versioning:**
   - Version test data alongside application code so the right test data is always paired with the right code version.
   - Use database migration tools (Flyway, Liquibase) for schema evolution.

6. **Security controls:**
   - Encrypt test data at rest and in transit.
   - Use IAM roles to restrict access to test data stores.
   - Never use real customer data in test environments — always mask or synthesize.

**Tips:**
- In financial systems, test data often needs to include realistic market data scenarios (volatile markets, market halts, corporate actions). Random data won't exercise the right code paths.
- Mention cost optimization: "We tag all test resources and use automated cleanup to avoid runaway cloud costs from forgotten test environments."

---

### Q32: Explain the difference between horizontal and vertical scaling. How does this affect your test strategy?

**What's being evaluated:** Infrastructure knowledge, ability to design tests that validate scaling behavior.

**Answer guidance:**

**Definitions:**

| | Vertical Scaling (Scale Up) | Horizontal Scaling (Scale Out) |
|---|---|---|
| **What** | Add more resources (CPU, RAM) to a single server. | Add more servers/instances to distribute the load. |
| **Limit** | Bounded by maximum hardware capacity. | Theoretically unlimited (add more nodes). |
| **Complexity** | Simple — no application changes needed. | Requires stateless design, load balancing, distributed data management. |
| **Downtime** | May require restart to resize. | Can scale without downtime (auto-scaling). |
| **Cost** | Exponentially more expensive at higher tiers. | Linear cost scaling. |

**Impact on test strategy:**

1. **Vertical scaling testing:**
   - Test on different instance sizes to find the optimal cost/performance ratio.
   - Verify the application takes advantage of additional resources (e.g., multi-threaded).
   - Test the upper bound — what happens when you can't scale up further?

2. **Horizontal scaling testing:**
   - **Auto-scaling validation:** Verify that new instances spin up under load and scale down when load decreases.
   - **State management:** Test that sessions/data are not lost when requests are routed to different instances.
   - **Load balancer behavior:** Verify even distribution, health check accuracy, and sticky session behavior.
   - **Data consistency:** Test that distributed caches, databases, and message queues remain consistent across nodes.
   - **Failover testing:** Kill individual nodes during load testing to verify the system recovers without user impact.

3. **Combined approach (most common):**
   - Test both strategies: scale up the individual nodes, then scale out the number of nodes.
   - Find the "right-sizing" sweet spot: optimal instance size × number of instances.

**Tips:**
- Financial systems often use horizontal scaling for stateless services (API gateways, data distribution) and vertical scaling for stateful components (databases, matching engines).
- Mention auto-scaling metrics: "I configure scale-out triggers based on CPU utilization, request queue depth, or custom metrics like message processing lag."

---

### Q33: How do you test applications deployed in a microservices architecture?

**What's being evaluated:** Modern architecture understanding, testing strategy for distributed systems, ability to handle complexity.

**Answer guidance:**

**Challenges of testing microservices:**
- Many independently deployable services with complex interactions.
- Service version compatibility — Service A v2 may not work with Service B v1.
- Distributed data management — no single database to verify.
- Network-related failures (latency, timeouts, partial failures).

**Testing strategy layers:**

1. **Unit tests (per service):**
   - Each service has its own unit tests covering business logic.
   - Developers own these; fast feedback on every commit.

2. **Contract tests (between services):**
   - Use Pact or Spring Cloud Contract to verify that API contracts between consumer and provider are maintained.
   - Run independently for each service — no need to deploy all services together.
   - Catches breaking changes early without full integration environments.

3. **Integration tests (per service):**
   - Test each service with its real dependencies (database, message queue) using Testcontainers.
   - Verify database interactions, message production/consumption.

4. **End-to-end tests (full system):**
   - Deploy all services together in a staging environment.
   - Test critical business flows that span multiple services.
   - Keep these minimal — they're slow and brittle.

5. **Chaos/resilience testing:**
   - Use tools like Chaos Monkey, Gremlin, or Litmus to inject failures.
   - Test: What happens when a service is down? When the network is slow? When a database is unavailable?
   - Verify circuit breakers, retries, and fallback behaviors.

6. **Observability testing:**
   - Verify that distributed tracing (Jaeger, Zipkin) correctly tracks requests across services.
   - Test that logging is consistent and correlated across services.
   - Verify monitoring alerts fire correctly.

**Tips:**
- Emphasize contract testing: "In a microservices architecture, contract tests are the most valuable investment because they catch integration issues without the cost of full system deployment."
- In financial systems, data consistency across microservices is critical — mention eventual consistency patterns and how you test for them (e.g., verifying that a trade recorded in the order service eventually appears in the settlement service).
