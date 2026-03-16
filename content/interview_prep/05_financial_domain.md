# 5. Financial Domain & LSEG Context

> **Known gap area.** Both interviewers have spent their entire careers in financial data — Amy at Thomson Reuters/Refinitiv/LSEG, Andy deeply embedded in Elektron/real-time data systems. You don't have direct financial markets experience. **Use the bridging pattern throughout this section:** *"Here's what I know → Here's what connects from my experience → Here's how I'll close the gap."* Your Chartered Accountancy background is an untapped differentiator — most SDET candidates have zero financial knowledge.

---

### Q34: What do you know about LSEG and its products?

**What's being evaluated:** Research effort, genuine interest in the company and domain.

**Answer guidance:**

**LSEG (London Stock Exchange Group)** is a leading global financial markets infrastructure and data provider. Key divisions:

- **Capital Markets** — Operates the London Stock Exchange, Borsa Italiana, and Turquoise (equities trading venues).
- **Data & Analytics (Refinitiv)** — Provides financial data, analytics, and trading platforms (Eikon/Workspace, Elektron data feeds). Acquired Refinitiv in 2021.
- **FTSE Russell** — Global index provider (FTSE 100, Russell 2000, etc.). Used for benchmarking, ETFs, and derivatives.
- **Post Trade** — Clearing (LCH) and settlement services.

**Purpose:** Driving financial stability, empowering economies, enabling sustainable growth.

**Values:** Integrity, Partnership, Excellence, Change.

**Scale:** 25,000 people across 65 countries.

**Tips:**
- Don't just recite facts — connect them to the role: "As an SDET testing financial data systems, I understand that data accuracy and system reliability directly impact market participants and, by extension, financial stability."
- Mention recent news or initiatives (e.g., LSEG's partnership with Microsoft, cloud migration efforts).

**Udani's bridging answer:**

> "While I haven't worked directly in financial markets, I've done my research on LSEG. I know LSEG is more than the London Stock Exchange — it includes Refinitiv for data and analytics, FTSE Russell for indexing, and LCH for clearing. I'm particularly interested in the Data & Analytics division and LSEG Real-Time (formerly Elektron), which delivers real-time market data to financial institutions globally.
>
> What connects to my background: my Chartered Accountancy studies at CA Sri Lanka gave me a working understanding of financial data, reporting, and the importance of data integrity in financial contexts. And my experience testing complex enterprise integrations — SAP to Salesforce data flows, cross-system invoice reconciliation — is directly analogous to the data pipeline testing that LSEG's infrastructure requires. The stakes are different — market data errors can cause incorrect trading decisions worth millions — but the testing principles of data fidelity, transformation validation, and end-to-end integrity are the same. I'm eager to deepen this into financial markets specifically."

---

### Q35: How does testing financial markets software differ from testing a typical web application?

**What's being evaluated:** Domain awareness, understanding of the unique challenges in fintech/capital markets.

**Answer guidance:**

| Aspect | Financial Software | Typical Web App |
|---|---|---|
| **Data accuracy** | Must be exact to decimal precision. A rounding error can mean millions in losses. | Minor display inconsistencies may be tolerable. |
| **Latency** | Microsecond-to-millisecond latency requirements for market data and trading. | Sub-second response times are usually acceptable. |
| **Reliability** | Near-zero downtime. Market hours are critical — an outage during trading means regulatory scrutiny and financial loss. | Some downtime may be acceptable with proper communication. |
| **Regulatory compliance** | Must comply with regulations (MiFID II, SEC rules, etc.). Audit trails are mandatory. | Compliance varies by industry but is typically less strict. |
| **Concurrency** | Massive concurrent transactions during market events (e.g., market open, index rebalancing). | Concurrent users, but typically less extreme. |
| **Data volume** | Millions of price updates per second across thousands of instruments. | Typically lower data throughput. |
| **Security** | Financial data is highly sensitive. Encryption, access controls, and penetration testing are critical. | Important but consequences of breach may be less severe. |
| **Rollback complexity** | Financial transactions may be irreversible. Testing must ensure correctness before production. | Easier to roll back or fix in production. |

**Tips:**
- Show respect for the domain: "I understand that in financial systems, a bug isn't just a user inconvenience — it can have regulatory, financial, and reputational consequences."

**Udani's bridging answer:**

> "I can see the parallels between my experience and financial systems testing, even though the domains differ. In my E-Commerce testing, I dealt with:
>
> - **Data accuracy at scale** — pricing calculations across thousands of products, discount rules, VAT calculations. A rounding error in an invoice affects customer trust and revenue. In financial markets, that same principle applies at a much higher magnitude — a data error in a market data feed can cause incorrect trading decisions.
> - **Latency sensitivity** — our E-Commerce platform needed real-time inventory updates. If stock levels lagged behind orders, customers could purchase out-of-stock items. Financial systems take this to another level — microsecond latency matters for market data.
> - **Regulatory and audit requirements** — our Salesforce and SAP integrations had to maintain audit trails for invoicing and customer data changes. Financial systems extend this with regulations like MiFID II and SOX.
>
> My Chartered Accountancy studies also give me a foundation that most SDET candidates lack — I understand financial statements, data integrity in accounting contexts, and the business processes behind financial reporting. I'm committed to deepening this into capital markets specifics — I've already been studying market data flows, FIX protocol basics, and LSEG's product suite."

---

### Q36: What considerations are important when testing systems that handle market data or trade execution?

**What's being evaluated:** Domain-specific testing knowledge, understanding of financial system criticality.

**Answer guidance:**

- **Data integrity** — Verify that prices, volumes, and timestamps are accurate end-to-end. Compare against source data feeds.
- **Latency testing** — Measure and validate that processing latency meets SLAs (often single-digit milliseconds).
- **Sequencing** — Market data must arrive in the correct order. Test for out-of-order message handling.
- **Completeness** — Ensure all subscribed instruments are being received. No missing symbols.
- **Edge cases** — Market halt/resume messages, corporate actions (splits, dividends), zero-volume instruments, negative price adjustments.
- **Failover and resilience** — Test what happens when a feed goes down. Does the system switch to backup feeds? Are stale prices flagged?
- **Market replay** — Use recorded market data to replay historical scenarios (e.g., flash crash, high-volatility events) and validate system behavior.
- **Regulatory compliance** — Ensure timestamps meet regulatory precision requirements (e.g., MiFID II requires microsecond-level timestamps). Verify audit trails are complete.
- **Security** — Ensure unauthorized users cannot access sensitive trading data or execute unauthorized trades.

**Tips:**
- If you have financial markets experience, this is your moment to shine.
- If you don't, show that you've researched the domain and understand the stakes.

---

### Q37: Have you worked with FIX protocol or any financial messaging standards?

**What's being evaluated:** Domain-specific technical knowledge (nice-to-have per JD).

**Answer guidance:**

**FIX (Financial Information eXchange)** is the standard messaging protocol for electronic trading. It defines message formats for orders, executions, market data, and more.

**Key concepts:**
- **Sessions** — A FIX connection between two parties (initiator and acceptor) with sequence number management.
- **Message types** — NewOrderSingle (D), ExecutionReport (8), MarketDataRequest (V), Heartbeat (0), etc.
- **Tags** — Each field has a numeric tag (e.g., Tag 35 = MsgType, Tag 55 = Symbol, Tag 44 = Price).
- **Testing FIX:** Use tools like QuickFIX (open-source FIX engine), FIX analyzers, or custom simulators to send/receive FIX messages and validate behavior.

**If you haven't worked with FIX:**
"I haven't worked directly with FIX protocol, but I understand it's the industry standard for trading communication. I've worked with similar message-based protocols and I'm confident I can learn FIX quickly. I've already reviewed the FIX specification to understand the message structure."

**Tips:**
- Even surface-level knowledge of FIX protocol terminology will impress.
- Mention related experience: message queues (Kafka, RabbitMQ), binary protocols, or any financial messaging.

---

### Q38: What is market data and how does it flow through a trading system?

**What's being evaluated:** Understanding of LSEG's core domain, ability to articulate data flows in financial systems.

**Answer guidance:**

**What is market data?**
Market data is real-time and historical information about financial instruments — prices, volumes, order book depth, trade executions, and corporate actions. It originates from exchanges and is distributed to market participants (traders, portfolio managers, risk systems).

**Data flow in a typical trading system:**

1. **Source/Exchange** → Generates raw market data (trades, quotes, order book updates).
2. **Feed handler** → Receives raw data via exchange-specific protocols (e.g., ITCH, FIX, proprietary binary), normalizes it into a common format.
3. **Ticker plant / Data platform** → Aggregates, enriches, and distributes data. Applies entitlements (who can see what).
4. **Distribution layer** → Publishes data via APIs, message buses (Kafka, Solace), or proprietary platforms (Refinitiv Elektron).
5. **Consumer applications** → Trading desks (Eikon/Workspace), algorithmic trading engines, risk management systems, compliance systems.
6. **Persistence** → Time-series databases store historical data for analytics, backtesting, and regulatory reporting.

**Key testing considerations:**
- **Latency at each hop** — Where is latency introduced? Is each component meeting its SLA?
- **Data fidelity** — Is the data identical at the consumer as it was at the source?
- **Throughput** — Can each component handle peak data rates (e.g., market open, high-volatility events)?
- **Failover** — If one feed handler fails, does the system seamlessly switch to a backup?
- **Entitlements** — Are data access controls enforced correctly? (e.g., a client entitled to delayed data shouldn't receive real-time data)

**Tips:**
- Connect to the role: "As an SDET at LSEG, I'd expect to test the data platform and distribution layers — ensuring data accuracy, latency, and entitlements work correctly across the pipeline."
- Show you understand the business impact: "Inaccurate market data can lead to wrong trading decisions, regulatory fines, and loss of client trust."

---

### Q39: How do you test for regulatory compliance (e.g., MiFID II, SOX)?

**What's being evaluated:** Awareness of regulatory requirements in financial systems, ability to translate compliance rules into testable criteria.

**Answer guidance:**

**Key regulations and their testing implications:**

| Regulation | Key Requirement | What to Test |
|---|---|---|
| **MiFID II** (EU) | Transaction reporting, best execution, timestamp precision (microsecond). | Verify timestamps are microsecond-precise. Test transaction reporting completeness and accuracy. Validate best execution logic. |
| **SOX** (US) | Financial reporting accuracy, internal controls, audit trails. | Verify audit logs capture all data modifications. Test access controls (separation of duties). Validate data integrity in financial reports. |
| **GDPR** (EU) | Data privacy, right to erasure, consent management. | Test data masking/anonymization. Verify deletion workflows actually remove data. Test consent tracking. |
| **MAR** (EU) | Market abuse detection, suspicious transaction reporting. | Test surveillance system alerts. Verify detection rules for insider trading patterns, market manipulation. |

**Testing approach:**

1. **Translate regulations into test requirements:**
   - Work with compliance teams to understand the specific rules.
   - Create a traceability matrix: regulation clause → system requirement → test case.

2. **Audit trail testing:**
   - Verify every user action, data modification, and system event is logged.
   - Test that logs are tamper-proof and include who, what, when, and from where.
   - Validate log retention periods meet regulatory requirements.

3. **Access control testing:**
   - Test role-based access controls (RBAC) — users should only access functions appropriate to their role.
   - Verify separation of duties (e.g., the person who creates a trade cannot also approve it).

4. **Data accuracy testing:**
   - Financial calculations must be precise — test with known inputs and expected outputs.
   - Verify rounding behavior matches regulatory standards.

5. **Reporting testing:**
   - Validate regulatory reports (content, format, timeliness).
   - Test report generation under high-volume conditions.

**Tips:**
- You don't need to be a compliance expert — show that you know how to collaborate with compliance teams and translate their requirements into testable criteria.
- Mention that compliance tests should be part of the automated regression suite — they run on every release, not just during audits.

---

### Q40: What is reconciliation testing in the context of financial systems?

**What's being evaluated:** Understanding of a critical financial testing practice, attention to data integrity.

**Answer guidance:**

**What is reconciliation?**
Reconciliation is the process of comparing two or more sets of data to verify they agree. In financial systems, it ensures that records across different systems are consistent — for example, that the trades recorded in the order management system match the trades recorded in the settlement system.

**Types of reconciliation in financial systems:**

1. **Trade reconciliation** — Verify that trades captured in the front-office system match those in the back-office/settlement system.
2. **Position reconciliation** — Confirm that the positions (holdings) calculated by the trading system match those in the custody/accounting system.
3. **Cash reconciliation** — Ensure that cash balances across accounts, banks, and internal systems agree.
4. **Market data reconciliation** — Compare market data received by your system against the official exchange data to detect discrepancies.
5. **Regulatory reconciliation** — Verify that data reported to regulators matches internal records.

**How to test reconciliation:**

1. **Set up test scenarios with known discrepancies:**
   - Missing records, duplicate records, mismatched amounts, timing differences.
   - Verify the reconciliation process detects and flags each type of discrepancy.

2. **Test break resolution workflow:**
   - When a reconciliation "break" (mismatch) is found, test the workflow for investigating and resolving it.
   - Verify that breaks are properly escalated based on severity and age.

3. **Volume testing:**
   - Reconciliation processes often handle millions of records. Test with production-scale volumes.
   - Verify performance doesn't degrade as data volume grows.

4. **Timing tests:**
   - Reconciliation is often time-sensitive (e.g., must complete before market open).
   - Test that the process finishes within the required window.

**Tips:**
- Reconciliation failures in financial systems can indicate fraud, system errors, or data corruption — testing these processes is critical.
- Show understanding of the T+1/T+2 settlement cycle: "Trade reconciliation must account for settlement timing — a trade executed today may not settle for 1-2 business days."
- Mention that reconciliation testing is particularly important during system migrations: "When migrating to a new platform, we'd run parallel reconciliation between old and new systems to validate data integrity."
