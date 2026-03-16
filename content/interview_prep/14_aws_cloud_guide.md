# AWS for SDETs — Interview Preparation Guide

**For:** Udani Weerasinghe | **Role:** Associate Lead SDET, LSEG
**Why this matters:** The JD requires "Familiarity with Cloud technologies such as AWS/Azure." Both interviewers (Amy Lee, Andy Purtell) have infrastructure backgrounds. LSEG runs large-scale financial infrastructure — expect questions about testing in cloud environments.

---

## Table of Contents

1. [AWS Core Concepts Every SDET Must Know](#1-aws-core-concepts-every-sdet-must-know)
2. [Compute & Containers — Where Tests Run](#2-compute--containers--where-tests-run)
3. [CI/CD on AWS — Your Strongest Connection](#3-cicd-on-aws--your-strongest-connection)
4. [Networking & Security — What Interviewers from Infra Backgrounds Ask](#4-networking--security--what-interviewers-from-infra-backgrounds-ask)
5. [Storage & Databases — Test Data Management](#5-storage--databases--test-data-management)
6. [Monitoring, Logging & Observability](#6-monitoring-logging--observability)
7. [Serverless & Event-Driven Architectures](#7-serverless--event-driven-architectures)
8. [Infrastructure as Code — Test Environment Provisioning](#8-infrastructure-as-code--test-environment-provisioning)
9. [Performance & Load Testing on AWS](#9-performance--load-testing-on-aws)
10. [Security Testing on AWS](#10-security-testing-on-aws)
11. [Financial Services Context (LSEG-Specific)](#11-financial-services-context-lseg-specific)
12. [Quick Reference — Services Cheat Sheet](#12-quick-reference--services-cheat-sheet)
13. [Interview Answer Templates](#13-interview-answer-templates)

---

## 1. AWS Core Concepts Every SDET Must Know

### Regions and Availability Zones

- **Region:** A geographical area (e.g., `eu-west-1` for Ireland, `ap-southeast-1` for Singapore). Each region has multiple Availability Zones.
- **Availability Zone (AZ):** An isolated data centre within a region. Applications are deployed across multiple AZs for high availability.
- **Why it matters for testing:** LSEG serves global markets. Tests may need to verify latency from specific regions, data residency compliance, and failover behaviour across AZs.

### The Shared Responsibility Model

| AWS Manages | You (LSEG) Manage |
|-------------|-------------------|
| Physical security, hardware, networking | Data, identity & access, application security |
| Hypervisor, host OS | Guest OS, patches, firewall rules |
| Service availability | Configuration, encryption, compliance |

**SDET angle:** You test what LSEG manages — application security, access controls, data encryption, and configuration correctness. AWS handles the infrastructure underneath.

### IAM (Identity and Access Management)

This is **the most important AWS service for an SDET to understand**.

- **Users:** Individual identities (human or service accounts).
- **Roles:** Assumed by services, applications, or users temporarily. **Test automation services should use roles, not hardcoded credentials.**
- **Policies:** JSON documents defining what actions are allowed/denied on which resources.
- **Principle of least privilege:** Every user/role should have only the minimum permissions required.

**What you should be able to discuss:**
- How your test automation authenticates to AWS (roles, not access keys).
- How you test that IAM policies are correctly configured (e.g., a "reader" role cannot write).
- How to test for privilege escalation — can a lower-privileged user access admin resources?

### AWS CLI & SDKs

- **AWS CLI:** Command-line tool for interacting with AWS services. SDETs use this in CI/CD scripts.
- **AWS SDKs:** Libraries for Java, Python, JavaScript, etc. Used to interact with AWS programmatically in test code.
  - **Boto3** (Python) — the most common for test scripting.
  - **AWS SDK for Java** — relevant since Udani's automation stack is Java-based.

---

## 2. Compute & Containers — Where Tests Run

### EC2 (Elastic Compute Cloud)

Virtual servers in the cloud. As an SDET you should know:

| Concept | What It Means | Testing Relevance |
|---------|--------------|-------------------|
| Instance types | Different CPU/memory configurations (e.g., `t3.medium`, `c5.xlarge`) | Choose the right size for test execution agents — too small = slow tests, too large = wasted cost |
| AMIs (Amazon Machine Images) | Pre-configured OS templates | Create standardised test environment images |
| Security Groups | Virtual firewalls controlling inbound/outbound traffic | Test that only expected ports are open |
| Key Pairs | SSH authentication | Used to access test servers for debugging |
| Auto Scaling | Automatically add/remove instances based on demand | Test that the application handles scaling events correctly |

### ECS (Elastic Container Service) & EKS (Elastic Kubernetes Service)

| Service | What It Is | When to Use |
|---------|-----------|-------------|
| **ECS** | AWS-managed container orchestration | Simpler container workloads, tightly integrated with AWS |
| **EKS** | Managed Kubernetes | Complex microservices, multi-cloud, or when the team already knows Kubernetes |
| **Fargate** | Serverless compute for containers (works with both ECS and EKS) | No server management — just define CPU/memory and run containers |

**SDET relevance:**
- **Running test suites in containers:** Package your Selenium/Playwright tests as Docker images, run them on ECS/Fargate. Each CI pipeline run spins up fresh containers.
- **Testing containerised applications:** Verify health checks, container startup/shutdown, inter-container networking.
- **Selenium Grid on ECS/EKS:** Run a scalable Selenium Grid using containers instead of managing VMs.

### Docker & ECR (Elastic Container Registry)

- **ECR** stores Docker images. Your test automation Docker images are pushed here and pulled during CI/CD.
- **Key workflow:** Build test image → Push to ECR → CI/CD pipeline pulls image → Runs tests on ECS/Fargate.

**Udani's connection:** Your MSc in Cloud Native Computing likely covered containerisation extensively. Link this to your Sysco LABS experience where you integrated tests into CI/CD (Jenkins + Git + AWS).

---

## 3. CI/CD on AWS — Your Strongest Connection

This is where your experience directly maps. At Sysco LABS, you used Jenkins + Git + AWS for CI/CD.

### AWS CI/CD Services

| Service | Purpose | Equivalent You Know |
|---------|---------|-------------------|
| **CodeCommit** | Git repository hosting | Git/GitLab/Bitbucket |
| **CodeBuild** | Build and test execution (serverless) | Jenkins build agents |
| **CodePipeline** | Orchestrates the CI/CD pipeline | Jenkins Pipeline |
| **CodeDeploy** | Automates deployment to EC2, ECS, Lambda | Jenkins deployment steps |

### Jenkins on AWS (What You Actually Used)

The most common pattern — and likely what LSEG uses:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  CodeCommit  │────▶│   Jenkins    │────▶│  Test Env    │
│  or GitHub   │     │  (on EC2)    │     │  (EC2/ECS)   │
└──────────────┘     └──────────────┘     └──────────────┘
                            │
                     ┌──────┴──────┐
                     │  Jenkins    │
                     │  Agents     │
                     │  (EC2/ECS)  │
                     └─────────────┘
```

**How to explain your experience:**
> "At Sysco LABS, I integrated our Selenium + TestNG + REST Assured automation suites into Jenkins pipelines that deployed and tested on AWS. The pipeline would trigger on Git pushes, build the test artifacts, deploy to test environments, run the full regression suite, and report results. I was responsible for maintaining both the test code and the pipeline configuration."

### Key Things to Know for the Interview

1. **Build specifications:** How to define what CodeBuild/Jenkins does — install dependencies, run tests, publish results.
2. **Artifact management:** Where test results, screenshots, and logs are stored (S3).
3. **Environment variables and secrets:** Using AWS Systems Manager Parameter Store or Secrets Manager — never hardcode credentials.
4. **Parallel test execution:** Running test suites across multiple build agents to reduce execution time.
5. **Pipeline gating:** Tests that must pass before deployment proceeds (quality gates).

---

## 4. Networking & Security — What Interviewers from Infra Backgrounds Ask

Amy was a Unix admin and Andy tested across infrastructure. Expect at least one question here.

### VPC (Virtual Private Cloud)

A logically isolated network within AWS. Think of it as your own private data centre in the cloud.

```
┌─────────────────── VPC (10.0.0.0/16) ───────────────────┐
│                                                           │
│  ┌─── Public Subnet ───┐   ┌─── Private Subnet ───┐     │
│  │  • Load balancers    │   │  • Application servers│     │
│  │  • Bastion hosts     │   │  • Databases          │     │
│  │  • NAT Gateways      │   │  • Internal services  │     │
│  └──────────────────────┘   └────────────────────────┘    │
│                                                           │
│  Internet Gateway ←→ Public Subnet                        │
│  NAT Gateway: Private Subnet → Internet (outbound only)   │
└───────────────────────────────────────────────────────────┘
```

**SDET relevance:**
- **Test environments** typically live in private subnets (not directly accessible from the internet).
- **VPN or bastion hosts** are used to access test environments for debugging.
- **Security groups and NACLs** control which traffic flows between subnets — test that internal services are not accidentally exposed.

### Key Networking Concepts

| Concept | What It Is | Testing Relevance |
|---------|-----------|-------------------|
| **Security Groups** | Stateful firewall rules at the instance level | Verify only required ports are open |
| **NACLs** | Stateless firewall rules at the subnet level | Additional layer of network testing |
| **Route Tables** | Define how traffic flows between subnets | Verify test environment routing is correct |
| **Elastic Load Balancer (ELB/ALB/NLB)** | Distributes traffic across instances | Test load balancing behaviour, health checks, sticky sessions |
| **Route 53** | DNS service | Test DNS resolution, failover routing |
| **CloudFront** | CDN for content delivery | Test caching behaviour, cache invalidation |

### What You Should Be Able to Answer

- *"How do you access a test environment that's in a private subnet?"*
  → Through a VPN connection or a bastion/jump host in the public subnet. In CI/CD, the build agents run inside the same VPC so they have direct access.

- *"How do you test an application behind a load balancer?"*
  → Test through the load balancer URL (as users would), but also test individual instances directly to isolate issues. Verify health check endpoints return correct status. Test behaviour when one instance goes down.

---

## 5. Storage & Databases — Test Data Management

### S3 (Simple Storage Service)

Object storage for anything — test artifacts, screenshots, logs, test data files.

| Feature | Testing Use |
|---------|-------------|
| **Buckets** | Store test reports, failure screenshots, log files |
| **Versioning** | Track changes to test data files over time |
| **Lifecycle policies** | Auto-delete old test artifacts after 30 days (cost control) |
| **Pre-signed URLs** | Generate temporary access links to test reports for stakeholders |
| **Event notifications** | Trigger a Lambda function when a new test report is uploaded |

**Common SDET tasks:**
- Upload test results to S3 after each CI/CD run.
- Download test data files from S3 before test execution.
- Verify that the application correctly handles S3 file uploads/downloads.

### RDS (Relational Database Service)

Managed databases: PostgreSQL, MySQL, Oracle, SQL Server.

**SDET relevance:**
- **Test database provisioning:** Spin up a dedicated RDS instance for test runs, tear it down afterward.
- **Snapshots:** Create a snapshot of a known good database state. Restore it before each test run for consistent test data.
- **Read replicas:** Test that the application correctly reads from replicas and writes to the primary.
- **Connection testing:** Verify connection pooling, timeouts, and failover behaviour.

**Udani's connection:** Your CV lists PostgreSQL and Oracle experience. RDS is simply managed PostgreSQL/Oracle in the cloud — same SQL, same concepts, AWS handles the patching and backups.

### DynamoDB

Fully managed NoSQL database. Key-value and document data model.

| Aspect | What to Know |
|--------|-------------|
| **Tables, items, attributes** | Core data model (no fixed schema) |
| **Partition key / sort key** | How data is distributed and queried |
| **Provisioned vs on-demand capacity** | Cost and performance model |
| **DynamoDB Streams** | Capture changes to items (for event-driven testing) |

**Testing relevance:** If the application uses DynamoDB, test data modelling, query patterns, error handling for throttled requests, and consistency modes (eventually consistent vs strongly consistent reads).

---

## 6. Monitoring, Logging & Observability

### CloudWatch

The central monitoring service. SDETs use it heavily.

| Feature | SDET Use |
|---------|----------|
| **Metrics** | Monitor application performance during test runs (CPU, memory, request count, error rate) |
| **Logs** | View application logs to debug test failures — no need to SSH into servers |
| **Alarms** | Set up alerts if error rate exceeds a threshold during testing |
| **Dashboards** | Create test monitoring dashboards showing test execution metrics |
| **Log Insights** | Query and analyse logs with SQL-like syntax — useful for investigating intermittent failures |

### X-Ray

Distributed tracing for microservices. Traces a request as it flows through multiple services.

**Testing relevance:**
- Debug slow API responses by identifying which downstream service is the bottleneck.
- Verify that requests flow through the expected services.
- Identify N+1 query patterns and unnecessary service calls.

### CloudTrail

Logs every API call made in the AWS account. An audit trail.

**Testing relevance:**
- Verify that security-sensitive actions are logged (who created/deleted a resource).
- Test compliance requirements — financial regulators often require complete audit trails.
- Investigate test environment issues — "who changed this configuration?"

---

## 7. Serverless & Event-Driven Architectures

### Lambda

Run code without managing servers. You upload a function, AWS runs it in response to events.

| Trigger | Testing Scenario |
|---------|-----------------|
| API Gateway request | Test the API endpoint that invokes the Lambda |
| S3 file upload | Test that processing triggers correctly when files are uploaded |
| SQS message | Test that messages are consumed and processed correctly |
| CloudWatch scheduled event | Test that scheduled tasks (cron jobs) execute as expected |
| DynamoDB Stream | Test that data changes trigger downstream processing |

**SDET testing considerations:**
- **Cold starts:** First invocation after idle period is slower. Test that cold start latency is acceptable.
- **Timeouts:** Lambda has a maximum execution time (15 min). Test behaviour when functions approach the limit.
- **Concurrency limits:** Test what happens when too many invocations occur simultaneously.
- **Error handling:** Test retry behaviour for failed invocations (Lambda retries automatically for async invocations).
- **Local testing:** Use AWS SAM (Serverless Application Model) or LocalStack to test Lambda functions locally before deploying.

### SQS (Simple Queue Service) & SNS (Simple Notification Service)

| Service | What It Does | Testing Focus |
|---------|-------------|---------------|
| **SQS** | Message queue (decouple services) | Test message ordering, visibility timeout, dead letter queues, duplicate handling |
| **SNS** | Pub/sub notifications (fan-out) | Test that all subscribers receive messages, test filtering, test failure scenarios |

**SDET relevance for LSEG:** Financial systems often use message queues for order processing, trade execution, and market data distribution. Testing message flow integrity is critical.

### API Gateway

Managed service for creating, publishing, and managing APIs.

**Testing focus:**
- Request validation and throttling.
- Authentication (API keys, IAM, Cognito, Lambda authorizers).
- Response caching behaviour.
- Rate limiting — especially important for financial APIs.
- CORS configuration.

---

## 8. Infrastructure as Code — Test Environment Provisioning

### CloudFormation

AWS-native IaC tool. Defines infrastructure in YAML/JSON templates.

```yaml
# Example: A test environment definition
Resources:
  TestDatabase:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceClass: db.t3.micro
      Engine: postgres
      MasterUsername: testuser
      MasterUserPassword: !Ref DBPassword

  TestServer:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.small
      ImageId: ami-0abcdef1234567890
```

**SDET relevance:**
- **Ephemeral test environments:** Spin up a complete environment from a template before tests, tear it down after. Every test run gets a clean, identical environment.
- **Environment parity:** Same template for dev, test, staging — only parameters differ (instance size, database name).
- **Testing the infrastructure itself:** Verify that CloudFormation templates deploy correctly and produce the expected resources.

### Terraform (not AWS-native but widely used)

Multi-cloud IaC tool. Many organisations (including those on AWS) prefer Terraform for its cloud-agnostic approach.

**Same principles as CloudFormation but:**
- Uses HCL (HashiCorp Configuration Language) instead of YAML/JSON.
- Can manage resources across AWS, Azure, GCP, and other providers.
- Has a stronger community ecosystem and module registry.

**Udani's connection:** Your MSc in Cloud Native Computing almost certainly covered IaC. Mention it as a tool for ensuring consistent, reproducible test environments.

---

## 9. Performance & Load Testing on AWS

### Running Load Tests on AWS

| Approach | How It Works |
|----------|-------------|
| **Distributed JMeter on EC2** | Run JMeter master + multiple slave instances across regions |
| **k6 on EC2/ECS** | Containerised k6 workers for scalable load generation |
| **Gatling on CodeBuild** | Serverless execution — no infrastructure to manage |
| **AWS Distributed Load Testing** | AWS solution using Fargate + Taurus for managed load tests |

### Key Considerations

1. **Test from the right region:** If LSEG serves European clients, run load tests from `eu-west-1`, not `us-east-1`. Latency matters.
2. **Avoid testing AWS limits, not your app:** AWS services have default quotas (e.g., API Gateway: 10,000 requests/sec). Know the difference between your application bottleneck and an AWS throttle.
3. **Cost awareness:** Large-scale load tests on EC2 can be expensive. Use spot instances for load generators (they're disposable anyway).
4. **Auto-scaling verification:** Load test to verify that Auto Scaling policies trigger correctly and the application handles scale-out/scale-in without dropping requests.
5. **Monitor during tests:** Use CloudWatch dashboards to watch metrics in real-time during load tests.

---

## 10. Security Testing on AWS

### AWS Security Services an SDET Should Know

| Service | Purpose | SDET Use |
|---------|---------|----------|
| **IAM Access Analyzer** | Identifies resources shared externally | Verify no test resources are accidentally public |
| **GuardDuty** | Threat detection (monitors for malicious activity) | Verify alerts fire during security testing |
| **Inspector** | Vulnerability scanning for EC2 and containers | Include in CI/CD pipeline for automated vulnerability checks |
| **Secrets Manager** | Stores and rotates secrets (API keys, passwords) | Test code should retrieve credentials from here, never hardcode |
| **KMS (Key Management Service)** | Encryption key management | Verify data is encrypted at rest and in transit |
| **WAF (Web Application Firewall)** | Protects against common web exploits | Test that WAF rules block SQL injection, XSS, etc. |
| **Config** | Tracks resource configuration changes | Verify compliance rules are enforced |

### Security Testing Checklist for AWS Applications

- [ ] All data encrypted at rest (S3 bucket encryption, RDS encryption, EBS encryption).
- [ ] All data encrypted in transit (TLS/HTTPS, no HTTP endpoints).
- [ ] IAM roles follow least privilege — test with restricted roles and verify access is denied where expected.
- [ ] S3 buckets are not publicly accessible (unless explicitly intended).
- [ ] Security groups don't have overly permissive rules (no `0.0.0.0/0` on sensitive ports).
- [ ] Secrets are not hardcoded — pulled from Secrets Manager or Parameter Store.
- [ ] CloudTrail is enabled for audit logging.
- [ ] VPC flow logs are enabled for network monitoring.

---

## 11. Financial Services Context (LSEG-Specific)

LSEG operates critical financial infrastructure. AWS usage in financial services has specific requirements:

### Compliance & Regulatory

| Requirement | AWS Mechanism | Testing Focus |
|-------------|--------------|---------------|
| **Data residency** | Deploy in specific regions (e.g., EU data stays in EU regions) | Verify data doesn't leave required regions |
| **Audit trails** | CloudTrail + CloudWatch Logs | Verify all actions are logged and tamper-proof |
| **Encryption** | KMS + S3/RDS/EBS encryption | Verify encryption is enabled everywhere |
| **Disaster recovery** | Multi-AZ deployments, cross-region replication | Test failover scenarios |
| **Access controls** | IAM, VPC, Security Groups | Test that only authorised users access sensitive data |

### High Availability & Disaster Recovery

Financial systems cannot have downtime. Testing DR scenarios is critical:

1. **Multi-AZ failover:** Kill a database in one AZ → verify automatic failover to standby AZ.
2. **Cross-region failover:** Simulate an entire region outage → verify traffic routes to DR region.
3. **RTO/RPO testing:**
   - **RTO (Recovery Time Objective):** How quickly must the system recover? Test that failover completes within the target.
   - **RPO (Recovery Point Objective):** How much data loss is acceptable? Test that replicated data is current.
4. **Chaos engineering:** Use AWS Fault Injection Simulator (FIS) to inject failures and verify resilience.

### Real-Time Data Processing (LSEG Context)

LSEG's real-time market data systems likely use:

| AWS Service | Purpose | Testing Focus |
|-------------|---------|---------------|
| **Kinesis Data Streams** | Real-time data ingestion | Test message ordering, throughput, shard splitting |
| **MSK (Managed Kafka)** | Event streaming | Test consumer lag, partition rebalancing, exactly-once semantics |
| **ElastiCache (Redis)** | Low-latency caching | Test cache hit/miss ratios, TTL behaviour, failover |
| **DynamoDB** | Low-latency key-value lookups | Test read/write capacity, throttling behaviour |

---

## 12. Quick Reference — Services Cheat Sheet

### Services You MUST Know (High Priority)

| Service | One-Line Description |
|---------|---------------------|
| **IAM** | Who can do what |
| **EC2** | Virtual servers |
| **S3** | Object/file storage |
| **RDS** | Managed relational databases |
| **VPC** | Your private network |
| **CloudWatch** | Monitoring and logging |
| **Lambda** | Serverless functions |
| **ECS/Fargate** | Container orchestration |
| **CodeBuild/CodePipeline** | CI/CD services |
| **Secrets Manager** | Secure credential storage |

### Services You Should Know (Medium Priority)

| Service | One-Line Description |
|---------|---------------------|
| **DynamoDB** | NoSQL database |
| **SQS/SNS** | Message queuing and notifications |
| **API Gateway** | Managed API endpoints |
| **CloudFormation** | Infrastructure as code |
| **ECR** | Docker image registry |
| **X-Ray** | Distributed tracing |
| **Route 53** | DNS management |
| **ELB/ALB** | Load balancing |

### Services to Be Aware Of (Lower Priority)

| Service | One-Line Description |
|---------|---------------------|
| **Kinesis** | Real-time data streaming |
| **Step Functions** | Workflow orchestration |
| **CloudFront** | CDN |
| **ElastiCache** | In-memory caching (Redis/Memcached) |
| **CloudTrail** | API audit logging |
| **WAF** | Web application firewall |
| **Inspector** | Vulnerability scanning |
| **Config** | Compliance monitoring |

---

## 13. Interview Answer Templates

### "How do you manage test environments in the cloud?"

> "At Sysco LABS, our test environments were provisioned on AWS. I integrated our automation suites — Selenium with TestNG and REST Assured — into Jenkins pipelines that deployed and tested against AWS-hosted environments. The pipeline would trigger on code push, deploy to a test environment, execute the regression suite, and publish results.
>
> In my MSc in Cloud Native Computing, I went deeper into containerisation and infrastructure-as-code, which are the foundation for modern test environment management. The ideal approach is to define test environments as code — using CloudFormation or Terraform — so every CI/CD run gets an identical, fresh environment. Containers (Docker on ECS or Fargate) make this fast and cost-effective because you only pay for the compute time you use.
>
> For a financial institution like LSEG, I'd also emphasise environment isolation and security — test environments in private subnets, credentials stored in Secrets Manager, and strict IAM roles so test automation only has the access it needs."

### "How do you ensure test automation is secure on AWS?"

> "There are several layers I'd focus on. First, **credentials management** — test automation should never use hardcoded AWS access keys. Instead, use IAM roles for EC2/ECS instances, or retrieve secrets from AWS Secrets Manager at runtime. Second, **least privilege** — the IAM role for test automation should only have permissions for what it needs (read from S3, write to RDS, etc.), nothing more. Third, **test data security** — especially in financial services, test environments should never contain real customer data. We use synthetic data generators and ensure test databases are encrypted. Finally, **network isolation** — test environments should be in their own VPC or subnets, with security groups restricting access."

### "What's your experience with AWS?"

> "I have both practical and academic experience with AWS. At Sysco LABS, I integrated test automation suites into CI/CD pipelines using Jenkins deployed on AWS, with test environments hosted on AWS infrastructure. I worked with EC2 instances, S3 for artifact storage, and AWS-integrated Jenkins for pipeline orchestration.
>
> My MSc in Cloud Native Computing gave me deeper knowledge of cloud architecture — containerisation with Docker and Kubernetes, infrastructure as code, microservices testing, and cloud-native CI/CD patterns. I understand how services like VPC, IAM, CloudWatch, and RDS work together to support a testing infrastructure.
>
> While my primary hands-on experience is with the CI/CD and compute layer, I'm confident in my understanding of the broader AWS ecosystem and how it supports quality engineering at scale."

### "How would you test a microservices application deployed on AWS?"

> "I'd approach this in layers. First, **individual service testing** — each microservice gets its own unit and integration tests, running in containers on ECS or CodeBuild. Dependencies are mocked or stubbed using tools like WireMock or LocalStack.
>
> Second, **contract testing** — since microservices communicate via APIs, I'd implement Pact or similar contract tests to ensure services agree on their interfaces without needing to deploy everything together.
>
> Third, **end-to-end testing** in a staging environment — deploy all services to a test environment and run key user journeys. Use AWS X-Ray for distributed tracing to debug any issues across service boundaries.
>
> Fourth, **resilience testing** — use AWS Fault Injection Simulator to test how the system handles failures: what happens if a downstream service goes down? Does the circuit breaker activate? Does the system degrade gracefully?
>
> Finally, **monitoring-based testing** — even after deployment, CloudWatch alarms and dashboards verify the system is healthy. This is especially important for financial systems where real-time data integrity is critical."

---

*Focus your study on Sections 1–6 and 11 — these are the most likely interview topics given the LSEG role and the interviewers' infrastructure backgrounds. Sections 7–10 are valuable for demonstrating depth if the conversation goes there.*
