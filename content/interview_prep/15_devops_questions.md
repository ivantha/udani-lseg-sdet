# DevOps Interview Questions & Answers for SDETs

**Context:** LSEG Associate Lead SDET role — the JD places this role "as a member of a DevOps team" and requires CI/CD, cloud, and infrastructure familiarity.

---

## Table of Contents

1. [DevOps Culture & Principles](#1-devops-culture--principles)
2. [Version Control & Branching](#2-version-control--branching)
3. [CI/CD Pipelines](#3-cicd-pipelines)
4. [Containerisation & Orchestration](#4-containerisation--orchestration)
5. [Infrastructure as Code](#5-infrastructure-as-code)
6. [Configuration Management](#6-configuration-management)
7. [Monitoring, Logging & Alerting](#7-monitoring-logging--alerting)
8. [Networking & Linux](#8-networking--linux)
9. [Cloud & Scalability](#9-cloud--scalability)
10. [DevOps for Quality Engineering](#10-devops-for-quality-engineering)

---

## 1. DevOps Culture & Principles

### Q1.1: What is DevOps and why does it matter?

DevOps is a set of practices, cultural philosophies, and tools that unify software **development** (Dev) and IT **operations** (Ops) to shorten the development lifecycle and deliver high-quality software continuously.

**Core pillars (CALMS):**

| Pillar | Meaning |
|--------|---------|
| **C** — Culture | Shared responsibility between dev, ops, and QA; no "throw it over the wall" |
| **A** — Automation | Automate builds, tests, deployments, and infrastructure |
| **L** — Lean | Eliminate waste, reduce batch sizes, deliver incrementally |
| **M** — Measurement | Measure everything — lead time, deployment frequency, MTTR, change failure rate |
| **S** — Sharing | Shared tools, knowledge, and visibility across teams |

**Why it matters for SDETs:** In a DevOps team, the SDET is not a gatekeeper at the end of the pipeline. You're embedded in the team, contributing to CI/CD pipelines, writing automated quality gates, and ensuring that the speed of delivery doesn't compromise quality.

---

### Q1.2: What are the four key DORA metrics?

The **DORA (DevOps Research and Assessment)** metrics measure software delivery performance:

| Metric | What It Measures | Elite Performance |
|--------|-----------------|-------------------|
| **Deployment Frequency** | How often code is deployed to production | Multiple times per day |
| **Lead Time for Changes** | Time from commit to production deployment | Less than 1 hour |
| **Change Failure Rate** | Percentage of deployments causing failures | 0–15% |
| **Mean Time to Recovery (MTTR)** | Time to restore service after a failure | Less than 1 hour |

**SDET connection:** Your test automation directly impacts all four metrics:
- Fast, reliable tests → shorter lead time.
- Comprehensive tests → lower change failure rate.
- Good test observability → faster MTTR (tests help pinpoint what broke).
- Stable CI/CD → enables higher deployment frequency.

---

### Q1.3: What is the difference between DevOps, SRE, and Platform Engineering?

| Discipline | Focus | Key Responsibility |
|-----------|-------|-------------------|
| **DevOps** | Culture and practices for fast, reliable delivery | CI/CD, automation, breaking silos between dev and ops |
| **SRE (Site Reliability Engineering)** | Reliability of production systems | SLOs, error budgets, incident response, toil reduction |
| **Platform Engineering** | Building self-service internal platforms | Developer experience, internal tooling, golden paths |

**Overlap:** All three value automation and measurement. An SDET in a DevOps team may interact with SRE practices (e.g., testing against SLOs) and platform engineering (e.g., using an internal test infrastructure platform).

---

### Q1.4: Explain the concept of "shift-left" and "shift-right" in DevOps.

| Direction | Meaning | Practices |
|-----------|---------|-----------|
| **Shift-left** | Move testing and quality earlier in the lifecycle | TDD, BDD, static analysis, code reviews, unit tests, contract tests |
| **Shift-right** | Extend testing and monitoring into production | Canary deployments, feature flags, A/B testing, production monitoring, chaos engineering |

**Both together:** Shift-left catches bugs early (cheaper to fix). Shift-right catches issues that only appear in production (real traffic patterns, edge cases, infrastructure differences). A mature DevOps team does both.

---

### Q1.5: What is "Infrastructure as Code" and why is it a DevOps principle?

**Infrastructure as Code (IaC)** means managing and provisioning infrastructure through machine-readable configuration files rather than manual processes.

**Why it's a DevOps principle:**
- **Reproducibility:** Spin up identical environments every time — eliminates "works on my machine."
- **Version control:** Infrastructure definitions live in Git alongside application code. Changes are reviewed, tracked, and auditable.
- **Automation:** Environments can be created/destroyed automatically in CI/CD pipelines.
- **Self-service:** Developers and testers can provision their own environments without waiting for an ops team.
- **Drift detection:** Compare the actual state of infrastructure against the desired state defined in code.

**Tools:** Terraform, AWS CloudFormation, Pulumi, Ansible, Chef, Puppet.

---

## 2. Version Control & Branching

### Q2.1: Explain Git branching strategies. Which would you recommend and why?

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **Git Flow** | Long-lived `develop` and `main` branches; feature, release, and hotfix branches | Scheduled releases, larger teams, strict release process |
| **GitHub Flow** | Single `main` branch; short-lived feature branches merged via PRs | Continuous deployment, small teams, SaaS products |
| **Trunk-Based Development** | Everyone commits to `main` (trunk) directly or via very short-lived branches (< 1 day) | High-performing DevOps teams, continuous deployment |
| **GitLab Flow** | Environment branches (`staging`, `production`) alongside feature branches | Teams that need environment-specific deployments |

**Recommendation for an SDET:**
- For a financial institution like LSEG with strict release processes → **Git Flow** or **GitLab Flow** (structured, auditable).
- For test automation repository specifically → **GitHub Flow** (simpler, feature branches merged after review).

---

### Q2.2: What is a merge conflict and how do you resolve it?

A **merge conflict** occurs when two branches modify the same lines of a file, and Git cannot automatically determine which change to keep.

**Resolution process:**
1. Git marks conflicts in the file with `<<<<<<<`, `=======`, `>>>>>>>` markers.
2. Open the file and understand both changes.
3. Decide which change to keep, or combine both.
4. Remove the conflict markers.
5. Stage the resolved file and commit.

**Prevention strategies:**
- Pull frequently from the main branch to stay current.
- Keep branches short-lived — merge within 1–2 days.
- Communicate with teammates about who's working on what.
- Use code ownership / CODEOWNERS files to route reviews appropriately.

---

### Q2.3: What are Git hooks and how are they useful in DevOps?

**Git hooks** are scripts that run automatically at specific points in the Git workflow.

| Hook | When It Runs | DevOps Use |
|------|-------------|------------|
| `pre-commit` | Before a commit is created | Run linters, formatters, static analysis; block commits with secrets |
| `commit-msg` | After commit message is written | Enforce commit message format (e.g., Jira ticket prefix) |
| `pre-push` | Before pushing to remote | Run unit tests; block pushes to protected branches |
| `post-merge` | After a merge completes | Notify CI/CD system, rebuild dependencies |
| `pre-receive` (server-side) | Before accepting a push on the server | Enforce branch protection, run security checks |

**Tools that leverage hooks:** Husky (Node.js), pre-commit (Python), Lefthook (polyglot).

---

### Q2.4: What is the difference between `git rebase` and `git merge`?

| Aspect | `git merge` | `git rebase` |
|--------|------------|--------------|
| **History** | Preserves all branch history with a merge commit | Rewrites history to create a linear sequence |
| **Merge commits** | Creates a merge commit | No merge commit — commits are replayed on top of the target branch |
| **Safety** | Safe for shared branches | Dangerous on shared branches (rewrites public history) |
| **Use case** | Merging feature branches into main | Keeping a feature branch up to date with main before merging |

**Golden rule:** Never rebase commits that have been pushed to a shared branch. Rebase is for cleaning up your local history before merging.

---

## 3. CI/CD Pipelines

### Q3.1: Design a CI/CD pipeline for a microservices application. What stages would you include?

```
┌──────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ Code │──▶│  Static  │──▶│  Build   │──▶│   Unit    │──▶│Integration│──▶│ Security │──▶│  Deploy  │
│ Push │   │ Analysis │   │ & Package│   │  Tests    │   │  Tests    │   │  Scans   │   │ Staging  │
└──────┘   └──────────┘   └──────────┘   └───────────┘   └──────────┘   └──────────┘   └──────────┘
                                                                                              │
           ┌──────────┐   ┌──────────┐   ┌───────────┐                                       │
           │  Deploy  │◀──│ Manual   │◀──│   E2E &   │◀──────────────────────────────────────┘
           │Production│   │ Approval │   │  Smoke    │
           └──────────┘   └──────────┘   └───────────┘
```

**Stage details:**

| Stage | What Happens | Gate |
|-------|-------------|------|
| **Static Analysis** | Linting, code style, SonarQube, type checking | Fail on critical issues |
| **Build & Package** | Compile code, build Docker image, push to registry | Build must succeed |
| **Unit Tests** | Run unit test suite | All must pass; coverage ≥ threshold |
| **Integration Tests** | Test service interactions, database queries, API contracts | All must pass |
| **Security Scans** | SAST, dependency scanning (Snyk/Trivy), secret detection | Fail on critical/high CVEs |
| **Deploy to Staging** | Deploy to a pre-production environment | Deployment must succeed |
| **E2E & Smoke Tests** | Run end-to-end tests against staging | All must pass |
| **Manual Approval** | Human gate for production deployment | Required for financial systems |
| **Deploy to Production** | Blue/green or canary deployment | Health checks must pass |

---

### Q3.2: What is the difference between blue/green deployment and canary deployment?

**Blue/Green Deployment:**
```
                    ┌─────────────┐
                    │ Load        │
                    │ Balancer    │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼                         ▼
     ┌────────────────┐      ┌────────────────┐
     │  Blue (v1)     │      │  Green (v2)    │
     │  (current)     │      │  (new)         │
     └────────────────┘      └────────────────┘
```

- Two identical environments. The load balancer switches all traffic from blue (old) to green (new) at once.
- **Rollback:** Switch the load balancer back to blue. Instant.
- **Drawback:** Requires double the infrastructure. All-or-nothing switch — if v2 has a subtle bug, all users are affected.

**Canary Deployment:**
```
     100% traffic          90% → v1,  10% → v2         100% → v2
     ┌──────┐              ┌──────┐  ┌──────┐          ┌──────┐
     │  v1  │    ──▶       │  v1  │  │  v2  │   ──▶    │  v2  │
     └──────┘              └──────┘  └──────┘          └──────┘
```

- Route a small percentage of traffic to the new version. Gradually increase if metrics look good.
- **Rollback:** Route all traffic back to v1. Only a small percentage of users were affected.
- **Advantage:** Real-world validation with limited blast radius.

**For LSEG (financial systems):** Canary deployments are preferred because they limit risk. A bug in a trading system affecting 100% of users could have catastrophic financial impact.

**SDET role:** Write automated health checks and smoke tests that run against the canary. If error rates or latency increase, the canary is automatically rolled back.

---

### Q3.3: How do you handle secrets in a CI/CD pipeline?

**Never do:**
- Hardcode secrets in source code.
- Store secrets in plain text config files committed to Git.
- Pass secrets as plain text environment variables visible in CI logs.

**Best practices:**

| Approach | Tool | How It Works |
|----------|------|-------------|
| **Secret management service** | AWS Secrets Manager, HashiCorp Vault, Azure Key Vault | Secrets stored encrypted, retrieved at runtime via API |
| **CI/CD built-in secrets** | Jenkins Credentials, GitHub Secrets, GitLab CI Variables | Secrets configured in the CI platform, injected as masked env vars |
| **Environment-specific configs** | AWS Parameter Store, Consul | Different secrets per environment (dev/staging/prod) |
| **Secret scanning** | gitleaks, truffleHog, git-secrets | Pre-commit hooks that block commits containing secrets |

**SDET concern:** Test automation often needs credentials (database passwords, API keys, service accounts). Store these in the CI platform's secret store and inject them at runtime. Never log them.

---

### Q3.4: What is a pipeline-as-code? Give an example.

**Pipeline-as-code** defines CI/CD pipelines in version-controlled configuration files rather than through a UI.

**Benefits:**
- Versioned alongside application code — changes to the pipeline are reviewed and tracked.
- Reproducible — the pipeline definition is the same across environments.
- Portable — moving to a new CI server means copying the config file.

**Examples by tool:**

**Jenkinsfile (Declarative):**
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                sh 'deploy.sh staging'
            }
        }
    }
}
```

**GitHub Actions:**
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test
```

**GitLab CI (.gitlab-ci.yml):**
```yaml
stages:
  - test
  - deploy

unit-tests:
  stage: test
  script:
    - pytest tests/

deploy-staging:
  stage: deploy
  script:
    - ./deploy.sh staging
  only:
    - main
```

---

### Q3.5: What is artifact management and why is it important?

An **artifact** is any output of the build process — compiled binaries, Docker images, test reports, JAR/WAR files, npm packages.

**Artifact management** is the practice of storing, versioning, and distributing these artifacts reliably.

| Tool | What It Stores |
|------|---------------|
| **JFrog Artifactory** | Maven/Gradle JARs, Docker images, npm packages, generic files |
| **Nexus Repository** | Same as Artifactory — Maven, npm, Docker, PyPI |
| **AWS ECR** | Docker images |
| **AWS S3** | Generic artifacts (test reports, binaries) |
| **GitHub Packages** | npm, Maven, Docker, NuGet |

**Why it matters:**
- **Reproducibility:** Deploy the exact same artifact that was tested, not a rebuild.
- **Traceability:** Every artifact is tagged with its Git commit, build number, and test results.
- **Speed:** Download pre-built artifacts instead of rebuilding from source.
- **Rollback:** Previous versions are stored and can be redeployed instantly.

**SDET relevance:** Store test reports, failure screenshots, and performance baselines as artifacts. When a test fails in CI, the artifact (screenshot, log) is the first thing you examine.

---

### Q3.6: How do you implement quality gates in a CI/CD pipeline?

A **quality gate** is a checkpoint in the pipeline that must pass before proceeding to the next stage.

| Gate | Criteria | Tool |
|------|----------|------|
| **Code quality** | No critical SonarQube issues, code coverage ≥ 80% | SonarQube, CodeClimate |
| **Unit tests** | 100% pass rate | JUnit, TestNG, pytest |
| **Integration tests** | 100% pass rate | REST Assured, Testcontainers |
| **Security** | No critical/high vulnerabilities | Snyk, Trivy, OWASP Dependency-Check |
| **Performance** | Response time < threshold, no regression > 10% | k6, Gatling, JMeter |
| **E2E tests** | All critical paths pass | Selenium, Playwright, Cypress |
| **Manual approval** | Human sign-off for production | Jenkins input step, GitHub environment protection |

**Implementation pattern:**
```
Stage → Run checks → Evaluate against criteria → Pass? → Next stage
                                                → Fail? → Block pipeline + notify team
```

**SDET ownership:** The SDET typically owns the test-related quality gates — defining the criteria, maintaining the tests, and ensuring gates are reliable (not flaky).

---

## 4. Containerisation & Orchestration

### Q4.1: What is Docker and why is it important for DevOps?

**Docker** packages an application and its dependencies into a **container** — a lightweight, portable unit that runs consistently anywhere.

**Key concepts:**

| Concept | Description |
|---------|-------------|
| **Image** | A read-only template with the application + dependencies. Built from a `Dockerfile`. |
| **Container** | A running instance of an image. Isolated process with its own filesystem and network. |
| **Dockerfile** | Instructions to build an image (`FROM`, `COPY`, `RUN`, `CMD`). |
| **Registry** | Where images are stored (Docker Hub, AWS ECR, private registries). |
| **Volume** | Persistent storage that survives container restarts. |
| **Network** | Virtual networks connecting containers together. |

**Why it matters for DevOps:**
- **Consistency:** "It works on my machine" is eliminated — the container is the same everywhere.
- **Isolation:** Each service runs in its own container, preventing dependency conflicts.
- **Speed:** Containers start in seconds (vs. minutes for VMs).
- **Scalability:** Spin up multiple container instances behind a load balancer.

**SDET use cases:**
- Run test suites inside containers for consistent execution.
- Use Docker Compose to spin up the application + database + message queue for integration testing.
- Run Selenium Grid as containers (selenium/hub + selenium/node-chrome).

---

### Q4.2: Write a Dockerfile for a test automation project.

```dockerfile
# Base image with Java (for TestNG/Selenium projects)
FROM maven:3.9-eclipse-temurin-17

# Install Chrome for Selenium tests
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /tests

# Copy project files
COPY pom.xml .
COPY src/ ./src/

# Download dependencies (cached layer if pom.xml hasn't changed)
RUN mvn dependency:resolve

# Default command: run tests
CMD ["mvn", "test", "-Dbrowser=chrome-headless"]
```

**Key practices:**
- **Layer caching:** Copy `pom.xml` first, then `src/`. Dependencies are only re-downloaded if `pom.xml` changes.
- **Headless browser:** Run Chrome in headless mode inside the container (no display).
- **Clean up:** Remove apt caches to keep image size small.

---

### Q4.3: What is Docker Compose and how do you use it for testing?

**Docker Compose** defines and runs multi-container applications using a YAML file.

```yaml
version: '3.8'
services:
  app:
    build: ./app
    ports:
      - "8080:8080"
    environment:
      - DB_HOST=db
      - DB_PORT=5432
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: testuser
      POSTGRES_PASSWORD: testpass
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U testuser"]
      interval: 5s
      timeout: 5s
      retries: 5

  tests:
    build: ./tests
    depends_on:
      app:
        condition: service_started
    environment:
      - BASE_URL=http://app:8080
```

**Testing workflow:**
```bash
# Start everything, run tests, tear down
docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
```

**Benefits:** The entire application stack (app + database + tests) is defined in one file. Anyone can run the full test suite with a single command — no environment setup needed.

---

### Q4.4: What is Kubernetes and why does an SDET need to know it?

**Kubernetes (K8s)** is a container orchestration platform that automates deployment, scaling, and management of containerised applications.

**Core concepts:**

| Concept | Description |
|---------|-------------|
| **Pod** | The smallest deployable unit — one or more containers sharing network/storage |
| **Deployment** | Manages a set of identical pods, handles rolling updates |
| **Service** | Stable network endpoint to access a set of pods |
| **Namespace** | Logical isolation within a cluster (e.g., `dev`, `staging`, `prod`) |
| **ConfigMap / Secret** | Externalised configuration and sensitive data |
| **Ingress** | HTTP/HTTPS routing from external traffic to services |
| **Horizontal Pod Autoscaler** | Automatically scales pods based on CPU/memory or custom metrics |

**Why SDETs need it:**

1. **Testing K8s-deployed applications:** Verify rolling updates don't cause downtime, health checks work, pods restart on failure.
2. **Test infrastructure on K8s:** Run Selenium Grid, test databases, and test agents as K8s workloads.
3. **Ephemeral test environments:** Create a namespace per feature branch, deploy the application, run tests, delete the namespace.
4. **Chaos testing:** Kill pods, drain nodes, inject network latency — verify the application is resilient.

---

### Q4.5: What is the difference between a Docker container and a virtual machine?

| Aspect | Container | Virtual Machine |
|--------|-----------|----------------|
| **Isolation** | Process-level (shares host OS kernel) | Hardware-level (runs its own OS kernel) |
| **Size** | Megabytes (app + dependencies only) | Gigabytes (full OS + app + dependencies) |
| **Startup time** | Seconds | Minutes |
| **Resource usage** | Lightweight, many containers per host | Heavy, fewer VMs per host |
| **Portability** | Highly portable (runs anywhere Docker runs) | Less portable (hypervisor-dependent) |
| **Use case** | Microservices, CI/CD, test execution | Legacy applications, OS-level isolation, multi-OS environments |

**When to use VMs for testing:** When you need to test on a specific OS (e.g., Windows Server testing on a Linux host), or when the application requires kernel-level features not available in containers.

---

### Q4.6: What is a container registry and how do you manage image security?

A **container registry** stores and distributes Docker images.

| Registry | Type |
|----------|------|
| Docker Hub | Public/private |
| AWS ECR | Private (AWS-native) |
| Google Artifact Registry | Private (GCP-native) |
| Azure Container Registry | Private (Azure-native) |
| Harbor | Self-hosted, open-source |
| JFrog Artifactory | Universal artifact management |

**Image security practices:**

1. **Use minimal base images:** `alpine` or `distroless` instead of `ubuntu` — smaller attack surface.
2. **Scan for vulnerabilities:** Use Trivy, Snyk, or AWS ECR scanning to detect known CVEs in image layers.
3. **Don't run as root:** Use `USER nonroot` in Dockerfile.
4. **Pin image versions:** Use `node:18.17.0-alpine` instead of `node:latest` — reproducible builds.
5. **Sign images:** Use Docker Content Trust or Sigstore to verify image integrity.
6. **Secrets never in images:** Never `COPY` secret files or set credentials as `ENV` in the Dockerfile.

---

## 5. Infrastructure as Code

### Q5.1: Compare Terraform and CloudFormation.

| Aspect | Terraform | CloudFormation |
|--------|-----------|---------------|
| **Provider** | HashiCorp (open-source) | AWS (native) |
| **Cloud support** | Multi-cloud (AWS, Azure, GCP, etc.) | AWS only |
| **Language** | HCL (HashiCorp Configuration Language) | YAML or JSON |
| **State management** | External state file (S3, Terraform Cloud) | Managed by AWS automatically |
| **Drift detection** | `terraform plan` shows drift | Built-in drift detection |
| **Modularity** | Modules from Terraform Registry | Nested stacks, modules |
| **Preview changes** | `terraform plan` | Change sets |
| **Rollback** | Manual (apply previous state) | Automatic rollback on failure |

**When to choose:**
- **Terraform:** Multi-cloud environments, team prefers HCL, need to manage non-AWS resources.
- **CloudFormation:** Pure AWS environment, want native integration, prefer AWS-managed state.

---

### Q5.2: What is Terraform state and why is it important?

**Terraform state** is a file (`terraform.tfstate`) that maps your Terraform configuration to real-world resources. It tracks what Terraform has created so it knows what to update or delete.

**Why it matters:**
- Without state, Terraform doesn't know which resources it manages — it would try to create duplicates.
- State enables `terraform plan` to show what will change before applying.
- State contains sensitive data (resource IDs, outputs, sometimes passwords).

**Best practices:**
- **Remote state:** Store state in S3 (with DynamoDB locking) or Terraform Cloud — never in local files for team projects.
- **State locking:** Prevent two people from applying changes simultaneously (DynamoDB lock table).
- **State encryption:** Enable S3 server-side encryption for the state bucket.
- **Never edit state manually:** Use `terraform state mv`, `terraform import`, or `terraform state rm`.

---

### Q5.3: How do you test Infrastructure as Code?

| Level | What to Test | Tool |
|-------|-------------|------|
| **Static analysis** | Syntax errors, security misconfigurations, best practice violations | `tflint`, `checkov`, `tfsec`, `cfn-lint` |
| **Unit testing** | Individual module logic (does this module create the right resources?) | Terratest (Go), `terraform validate`, `cfn-guard` |
| **Integration testing** | Deploy infrastructure to a test account, verify it works, tear it down | Terratest, Kitchen-Terraform, `taskcat` (CloudFormation) |
| **Compliance testing** | Verify infrastructure meets security/compliance policies | Open Policy Agent (OPA), Sentinel (Terraform Enterprise), AWS Config Rules |
| **Drift detection** | Verify actual infrastructure matches the defined state | `terraform plan` (should show no changes if in sync) |

**SDET angle:** Testing IaC is a natural extension of the SDET role — you're applying the same principles (automated validation, shift-left, quality gates) to infrastructure.

---

## 6. Configuration Management

### Q6.1: What is configuration management and which tools are used?

**Configuration management** ensures that systems are configured consistently and maintained in a desired state.

| Tool | Approach | Language | Agentless? |
|------|----------|----------|-----------|
| **Ansible** | Procedural (do this, then that) | YAML (playbooks) | Yes (SSH-based) |
| **Chef** | Declarative (desired state) | Ruby (recipes) | No (agent on each node) |
| **Puppet** | Declarative | Puppet DSL (manifests) | No (agent on each node) |
| **Salt** | Both | YAML/Python | Both (agent or SSH) |

**Ansible** is the most common choice today because it's agentless, uses simple YAML, and can handle both configuration and orchestration.

**SDET relevance:**
- Provision test environments with the correct software versions and configurations.
- Verify server configurations (e.g., ensure the test database has the correct settings).
- Automate test environment setup/teardown.

---

### Q6.2: What is the difference between mutable and immutable infrastructure?

| Aspect | Mutable | Immutable |
|--------|---------|-----------|
| **Updates** | Modify existing servers in-place (install patches, change configs) | Never modify existing servers — build new ones and replace |
| **Drift risk** | High — servers diverge over time ("snowflake servers") | None — every deployment is a fresh, identical image |
| **Rollback** | Complex — undo changes on live servers | Simple — deploy the previous image |
| **Tools** | Ansible, Chef, Puppet (configuration management) | Packer + Terraform, Docker, AMI-based deployments |
| **Analogy** | Repairing a car part by part | Replacing the entire car with a new one |

**Modern DevOps favours immutable infrastructure.** Build a new server image (AMI, Docker image) with every change. Deploy the new image. If something breaks, deploy the previous image.

**Testing benefit:** Immutable infrastructure guarantees that the test environment is identical every time — no configuration drift between test runs.

---

## 7. Monitoring, Logging & Alerting

### Q7.1: What are the three pillars of observability?

| Pillar | What It Provides | Tools |
|--------|-----------------|-------|
| **Metrics** | Quantitative measurements over time (CPU, request count, error rate) | Prometheus, Grafana, CloudWatch, Datadog |
| **Logs** | Detailed event records (structured text with timestamps) | ELK Stack (Elasticsearch, Logstash, Kibana), Fluentd, CloudWatch Logs, Splunk |
| **Traces** | End-to-end request flow across services | Jaeger, Zipkin, AWS X-Ray, Datadog APM |

**Why SDETs care:**
- **Metrics** tell you if something is wrong (error rate spiked).
- **Logs** tell you what went wrong (error message, stack trace).
- **Traces** tell you where it went wrong (which service in the chain failed).

When a test fails in CI/CD, the first debugging step is checking logs and metrics — not re-running the test.

---

### Q7.2: What is the ELK Stack?

**ELK** = **Elasticsearch** + **Logstash** + **Kibana** (now often called the Elastic Stack, with Beats added).

| Component | Role |
|-----------|------|
| **Elasticsearch** | Search and analytics engine — stores and indexes logs |
| **Logstash** | Data processing pipeline — collects, transforms, and sends logs to Elasticsearch |
| **Kibana** | Visualisation dashboard — search logs, create charts, set up alerts |
| **Beats** | Lightweight agents that ship data (Filebeat for logs, Metricbeat for metrics) |

**Flow:**
```
Application → Filebeat → Logstash → Elasticsearch → Kibana
```

**SDET use:** Query application logs during test execution to correlate test actions with server-side behaviour. Set up Kibana dashboards showing test execution metrics.

---

### Q7.3: What is Prometheus and Grafana?

**Prometheus** is an open-source monitoring system that collects metrics via a pull model (scrapes HTTP endpoints).

**Grafana** is a visualisation platform that creates dashboards from Prometheus (and other) data sources.

**How they work together:**
```
Application ──▶ /metrics endpoint ──▶ Prometheus (scrapes & stores) ──▶ Grafana (visualises)
```

**Key Prometheus concepts:**
- **Metrics types:** Counter (monotonically increasing), Gauge (can go up or down), Histogram (distribution), Summary.
- **PromQL:** Query language for metrics (`rate(http_requests_total[5m])`).
- **Alertmanager:** Routes alerts to Slack, email, PagerDuty based on Prometheus rules.

**SDET relevance:**
- Monitor application metrics during performance tests.
- Create Grafana dashboards for test execution metrics (pass rate over time, test duration trends).
- Set up alerts for metric thresholds (response time > 500ms triggers an alert during load testing).

---

### Q7.4: What is structured logging and why does it matter?

**Unstructured log:**
```
2024-03-15 10:30:45 ERROR - Failed to process order 12345 for user john@example.com
```

**Structured log (JSON):**
```json
{
  "timestamp": "2024-03-15T10:30:45Z",
  "level": "ERROR",
  "message": "Failed to process order",
  "orderId": "12345",
  "userId": "john@example.com",
  "service": "order-service",
  "traceId": "abc-123-def",
  "error": "PaymentDeclined",
  "duration_ms": 230
}
```

**Why structured logging matters:**
- **Searchable:** Query by any field (`orderId=12345 AND level=ERROR`).
- **Parseable:** Machines can process structured logs automatically.
- **Correlatable:** Use `traceId` to follow a request across services.
- **Aggregatable:** Calculate error rates, average durations, counts per service.

**SDET impact:** When debugging a test failure, structured logs let you filter by test run ID or trace ID and see exactly what happened server-side during your test execution.

---

## 8. Networking & Linux

### Q8.1: Explain the essential Linux commands an SDET should know.

| Command | Purpose | Example |
|---------|---------|---------|
| `ssh` | Connect to remote servers | `ssh user@test-server.internal` |
| `scp` / `rsync` | Copy files to/from remote servers | `scp report.html user@server:/tmp/` |
| `curl` | Make HTTP requests from the command line | `curl -X GET https://api.example.com/health` |
| `grep` | Search text in files/output | `grep -r "ERROR" /var/log/app/` |
| `tail -f` | Follow log files in real time | `tail -f /var/log/app/application.log` |
| `ps aux` | List running processes | `ps aux \| grep java` |
| `top` / `htop` | Monitor CPU and memory usage | `htop` |
| `netstat` / `ss` | View network connections | `ss -tlnp` (listening ports) |
| `df -h` | Check disk space | `df -h /` |
| `chmod` / `chown` | Change file permissions/ownership | `chmod +x run-tests.sh` |
| `systemctl` | Manage services | `systemctl restart nginx` |
| `journalctl` | View systemd logs | `journalctl -u app-service -f` |
| `awk` / `sed` | Text processing | `awk '{print $1}' access.log` |
| `crontab` | Schedule recurring tasks | `crontab -e` |

---

### Q8.2: What is the difference between TCP and UDP?

| Aspect | TCP | UDP |
|--------|-----|-----|
| **Connection** | Connection-oriented (three-way handshake) | Connectionless |
| **Reliability** | Guaranteed delivery, ordering, retransmission | No guarantee — packets may be lost or arrive out of order |
| **Speed** | Slower (overhead for reliability) | Faster (minimal overhead) |
| **Use case** | HTTP/HTTPS, SSH, database connections | DNS lookups, video streaming, real-time market data feeds |
| **Header size** | 20 bytes minimum | 8 bytes |

**LSEG relevance:** Real-time market data feeds often use UDP (or multicast UDP) for speed. Trade execution uses TCP for reliability. An SDET testing LSEG systems may need to understand both protocols.

---

### Q8.3: What is DNS and how does it work?

**DNS (Domain Name System)** translates human-readable domain names (e.g., `api.lseg.com`) to IP addresses (e.g., `52.84.123.45`).

**Resolution flow:**
```
Browser → Local cache → OS cache → Router cache → ISP DNS → Root DNS →
TLD DNS (.com) → Authoritative DNS (lseg.com) → Returns IP
```

**Key record types:**

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Maps domain to IPv4 address | `api.lseg.com → 52.84.123.45` |
| **AAAA** | Maps domain to IPv6 address | `api.lseg.com → 2001:db8::1` |
| **CNAME** | Alias for another domain | `www.lseg.com → lseg.com` |
| **MX** | Mail server | `lseg.com → mail.lseg.com` |
| **TXT** | Text records (SPF, DKIM, verification) | Domain verification strings |
| **NS** | Name server for the domain | `lseg.com → ns1.awsdns.com` |

**Testing relevance:**
- Verify DNS resolution works correctly for test environments.
- Test failover — when primary DNS record changes, does traffic route correctly?
- Test TTL (Time to Live) — how quickly do DNS changes propagate?
- DNS-based load balancing (Route 53 weighted routing).

---

### Q8.4: What happens when you type a URL in a browser? (Common interview question)

1. **DNS resolution:** Browser resolves the domain name to an IP address.
2. **TCP connection:** Browser establishes a TCP connection with the server (three-way handshake: SYN → SYN-ACK → ACK).
3. **TLS handshake:** If HTTPS, negotiate encryption (exchange certificates, agree on cipher suite, generate session keys).
4. **HTTP request:** Browser sends an HTTP GET request with headers (User-Agent, Accept, cookies).
5. **Server processing:** Server receives the request, processes it (query database, run business logic), generates a response.
6. **HTTP response:** Server sends back the response (status code, headers, HTML body).
7. **Rendering:** Browser parses HTML, requests CSS/JS/images (parallel requests), builds the DOM, paints the page.
8. **JavaScript execution:** Browser executes JavaScript, which may make additional API calls (AJAX/fetch).

**SDET angle:** Each step is a potential failure point you can test — DNS misconfiguration, certificate expiry, slow server processing, broken rendering, JavaScript errors.

---

## 9. Cloud & Scalability

### Q9.1: What is horizontal vs vertical scaling?

| Aspect | Vertical Scaling (Scale Up) | Horizontal Scaling (Scale Out) |
|--------|---------------------------|-------------------------------|
| **Method** | Add more resources to a single machine (more CPU, RAM) | Add more machines behind a load balancer |
| **Limit** | Hardware ceiling (can't infinitely upgrade one server) | Virtually unlimited (add as many instances as needed) |
| **Downtime** | Usually requires restart | No downtime (add instances while running) |
| **Complexity** | Simple (same application, bigger machine) | Complex (need stateless design, load balancing, data synchronisation) |
| **Cost** | Exponentially expensive at the top end | Linear cost scaling |
| **Example** | Upgrade EC2 from `t3.medium` to `t3.xlarge` | Add more `t3.medium` instances behind an ALB |

**SDET testing considerations:**
- **Vertical:** Test application behaviour before and after scaling. Verify it utilises added resources.
- **Horizontal:** Test load balancer health checks. Test session management (sticky sessions vs. stateless). Test data consistency across instances. Test auto-scaling triggers.

---

### Q9.2: What is a load balancer and what types exist?

A **load balancer** distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.

**AWS Load Balancer types:**

| Type | Layer | Best For |
|------|-------|----------|
| **Application Load Balancer (ALB)** | Layer 7 (HTTP/HTTPS) | Web applications, API routing, path-based routing |
| **Network Load Balancer (NLB)** | Layer 4 (TCP/UDP) | High-performance, low-latency, real-time data |
| **Gateway Load Balancer (GLB)** | Layer 3 | Third-party virtual appliances (firewalls, inspection) |
| **Classic Load Balancer (CLB)** | Layer 4/7 | Legacy (avoid for new applications) |

**Testing focus:**
- **Health checks:** Verify the load balancer correctly detects unhealthy instances and stops routing traffic to them.
- **Routing rules:** Test path-based routing (`/api/*` → API servers, `/static/*` → CDN).
- **SSL termination:** Verify HTTPS is handled correctly at the load balancer.
- **Sticky sessions:** If enabled, verify the same user hits the same server.
- **Failover:** Kill a backend instance and verify traffic seamlessly shifts.

---

### Q9.3: What is a CDN and how do you test caching behaviour?

A **Content Delivery Network (CDN)** caches content at edge locations worldwide, serving users from the nearest location to reduce latency.

**AWS CloudFront** is AWS's CDN service.

**Testing caching behaviour:**
1. **Cache hit/miss:** Check response headers (`X-Cache: Hit from cloudfront` vs `Miss from cloudfront`).
2. **TTL (Time to Live):** Verify content expires and refreshes after the configured TTL.
3. **Cache invalidation:** After deploying new content, verify invalidation clears stale cache.
4. **Cache-Control headers:** Verify the application sets appropriate headers (`Cache-Control: max-age=3600`, `no-cache`, `no-store`).
5. **Dynamic vs static content:** Verify dynamic content (API responses) is not cached when it shouldn't be.
6. **Geographic testing:** Verify users in different regions receive content from their nearest edge location.

---

### Q9.4: What are microservices and how do they differ from monoliths?

| Aspect | Monolith | Microservices |
|--------|----------|--------------|
| **Structure** | Single deployable unit | Multiple independently deployable services |
| **Scaling** | Scale the entire application | Scale individual services independently |
| **Deployment** | All-or-nothing deployment | Deploy services independently |
| **Technology** | Single tech stack | Each service can use different languages/databases |
| **Failure** | One bug can crash the entire application | Failure isolated to one service (if designed correctly) |
| **Communication** | In-process function calls | Network calls (HTTP/REST, gRPC, message queues) |
| **Testing** | Simpler integration testing (everything in one process) | Complex — need contract testing, service virtualisation |

**SDET challenges with microservices:**
- **Test environment complexity:** Need to run multiple services for end-to-end testing.
- **Contract testing:** Ensure services agree on API contracts (Pact, Spring Cloud Contract).
- **Service virtualisation:** Mock unavailable or unstable services (WireMock, Mountebank).
- **Distributed tracing:** Debug failures that span multiple services.
- **Data consistency:** Eventual consistency between services needs specific test strategies.

---

## 10. DevOps for Quality Engineering

### Q10.1: How does an SDET contribute to a DevOps team?

| Area | SDET Contribution |
|------|-------------------|
| **CI/CD pipeline** | Build and maintain automated test stages, define quality gates |
| **Test automation** | Write and maintain unit, integration, API, and E2E tests |
| **Infrastructure testing** | Test environment provisioning, IaC validation, disaster recovery testing |
| **Monitoring** | Define test-related metrics, create dashboards, set up alerts for quality regressions |
| **Security** | Integrate security testing into the pipeline (SAST, DAST, dependency scanning) |
| **Performance** | Build and run performance tests, establish baselines, detect regressions |
| **Incident response** | Provide test data and analysis during incidents; write regression tests for post-mortems |
| **Process improvement** | Analyse test metrics, reduce flakiness, optimise test execution time |

---

### Q10.2: What is ChatOps and how does it relate to DevOps?

**ChatOps** integrates DevOps tools with team chat platforms (Slack, Teams) so that operations are visible and executable from chat.

**Examples:**
- `/deploy staging` in Slack triggers a deployment pipeline.
- Bot posts test results in a channel after each CI/CD run.
- Alerts from monitoring tools appear in a dedicated channel.
- `/rollback production v2.3.1` triggers a rollback.

**Benefits:**
- **Visibility:** Everyone sees what's happening — deployments, test results, incidents.
- **Auditability:** Chat history provides a log of who did what and when.
- **Speed:** Execute operations without switching to a separate tool.
- **Collaboration:** Incident response happens in a shared channel, not in silos.

---

### Q10.3: What is GitOps?

**GitOps** uses Git as the single source of truth for both application code and infrastructure. All changes (code, configuration, infrastructure) go through Git pull requests.

**Principles:**
1. **Declarative:** The entire system is described declaratively (YAML/HCL files in Git).
2. **Versioned:** All changes are tracked in Git history.
3. **Automated:** Approved changes are automatically applied by an operator (ArgoCD, Flux).
4. **Self-healing:** If the actual state drifts from the desired state in Git, the operator corrects it automatically.

**Workflow:**
```
Developer pushes change → PR reviewed & approved → Merged to main →
GitOps operator detects change → Applies to cluster → Verifies convergence
```

**Tools:** ArgoCD (Kubernetes), Flux (Kubernetes), Jenkins X.

**SDET relevance:** In a GitOps workflow, test environment configurations are also in Git. Changes to test infrastructure go through the same PR process, ensuring review and traceability.

---

### Q10.4: What is chaos engineering and how do you implement it?

**Chaos engineering** is the practice of intentionally injecting failures into a system to test its resilience.

**Principles (from Netflix):**
1. Define the system's "steady state" (normal behaviour in terms of metrics).
2. Hypothesise that steady state will continue during the experiment.
3. Introduce real-world failures (server crash, network latency, disk full).
4. Observe whether the hypothesis holds — does the system remain stable?

**Types of failures to inject:**

| Failure | What to Test |
|---------|-------------|
| **Instance termination** | Does auto-scaling replace it? Do requests failover? |
| **Network latency** | Does the application handle slow responses gracefully (timeouts, circuit breakers)? |
| **DNS failure** | Does the application retry? Does it fail with a useful error? |
| **Disk full** | Does the application handle write failures without corruption? |
| **Dependency unavailable** | Does the circuit breaker open? Does the application degrade gracefully? |
| **CPU/memory stress** | Does the application remain responsive under resource pressure? |

**Tools:**

| Tool | Platform |
|------|----------|
| **AWS Fault Injection Simulator (FIS)** | AWS-native chaos engineering |
| **Chaos Monkey** | Netflix OSS — randomly kills instances |
| **Gremlin** | Commercial chaos engineering platform |
| **Litmus** | Kubernetes-native chaos engineering |
| **Toxiproxy** | Simulates network conditions (latency, timeouts) |

---

### Q10.5: What is a service mesh and why should an SDET know about it?

A **service mesh** is a dedicated infrastructure layer that handles service-to-service communication in microservices architectures.

**Popular implementations:** Istio, Linkerd, Consul Connect.

**What it provides:**

| Feature | Description | Testing Relevance |
|---------|-------------|-------------------|
| **Traffic management** | Routing, load balancing, traffic splitting | Test canary deployments, A/B routing |
| **Security** | Mutual TLS between services, access policies | Verify encryption in transit, test access controls |
| **Observability** | Metrics, logs, traces for every service call | Debug test failures across services |
| **Resilience** | Circuit breakers, retries, timeouts | Test fault tolerance behaviour |
| **Rate limiting** | Control request rates between services | Test throttling behaviour |

**SDET relevance:** If LSEG uses a service mesh, the SDET can leverage its built-in observability for debugging, test traffic routing configurations, and verify security policies between services.

---

*This guide covers DevOps topics from an SDET perspective — focusing on what you need to understand, discuss, and test rather than deep operational expertise. For the LSEG interview, prioritise Sections 1, 3, 4, and 7 — these are the most likely discussion areas given the DevOps team structure mentioned in the JD.*
