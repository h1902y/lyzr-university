# The Semantic Model

*Lesson 03 · Ground in Knowledge — Studio: Knowledge Graph & Semantic Model*

## What you'll learn

- Understand why vector RAG fails at structured data queries and how text-to-SQL bridges the gap.
- Connect a data source (e.g. CSV or SQL database) to a Semantic Data Model in Studio.
- Configure a Documentation Agent to auto-generate English schema descriptions of tables and columns.
- Inject custom business logic into column descriptions to guide text-to-SQL generation.
- Build an agent that uses Data Query to query database tables and return accurate answers.

## Key concepts

**Text-to-SQL enables exact data retrieval where vector search fails.** If a question requires counting, summing, or filtering columns, similarity search returns wrong or hallucinated values. A semantic model lets the agent generate and run SQL queries against the database instead.

**A Documentation Agent auto-generates schema documentation to guide the query builder.** To write accurate SQL, the LLM needs plain English context of what each table and column represents. A Documentation Agent reads the schema and drafts these descriptions automatically.

**Business logic is injected directly into column descriptions to steer the agent's SQL logic.** By tuning descriptions—such as defining `total` as `line total in USD, quantity times unit price`—you give the agent the precise context it needs to choose and compute columns correctly.

**The Data Query feature allows the agent to run and return SQL computations in seconds.** Once attached to a semantic model, the agent translates human questions into SQL, runs it against the connected source, and presents the structured calculation results.

## In Studio

Studio feature: **Build → Knowledge → Semantic Data Model**. Here is the configuration and testing flow:

1. Connect a data source under **Data Connectors** (e.g., upload a CSV file or connect Postgres, MySQL, or BigQuery).
2. Go to **Build → Knowledge**, click **New**, and select **Semantic Data Model**.
3. Enter a name, select the connected data source, and choose a **Documentation Agent** to scan the schema.
4. Open the created model to review the auto-generated table and column descriptions.
5. Edit and refine column descriptions to embed specific formulas or business rules (e.g., specifying currency or calculation rules).
6. Attach the semantic model to your agent under the **Data Query** feature in the agent settings.
7. Test in the Playground by asking complex aggregation queries (e.g., *"Which customer has spent the most in total?"*) and trace the query execution in the activity panel.

## Try this

1. Match these two queries to the correct retrieval type (Vector RAG vs. Data Query):
   - *"Give me a summary of our company's refund rules for late shipments."*
   - *"Calculate the total number of refunds processed for late shipments last month."*
2. Create a test database schema with a `price` and `discount` column. Write a description for the total field that instructs the agent how to calculate net sales.

## Transcript

Ask a language model what your revenue was last month, and it will make up a confident number. The data is sitting right there in your database, but the model can't see tables. Today, we fix that with a semantic model, a layer that teaches your agent what your data means, so it can query it for real. First, the data. For this demo, I'm using a CSV of Northwind orders, thirty rows of customers, products, and totals. In Lyzr, a file upload works as a data source, and mine is already connected. Under Data Connectors, in the File Upload card, and there it is, Northwind Sales. If your data lives in Postgres, MySQL, BigQuery, or a warehouse, you'd connect that on this page, and everything downstreams works identically. Now, the semantic model itself. On the Knowledge page, I go to New, and this time, I pick Semantic Data Model. Creating one takes three choices: a name, the database it points at, and one piece you haven't seen before, a documentation agent. That's a small model whose only job is to read your schema and write plain English descriptions of your tables and columns. I've already built mine, so let me cancel out of here and open it Here's why that documentation agent matters. Text to SQL fails when the model doesn't know what your columns mean. So the agent went through my orders table and describes the whole schema. Listen to a couple of these. Order ID, unique integer identifier for the order. Customer segment label, example SMB enterprise. Every column described and typed. Nobody wrote these by hand And these aren't locked. This is exactly where you inject your business logic. I'll sharpen the description of the total column to line total in US dollars, quantity times unit price, because tomorrow when the agent decides which column to sum, this sentence is what it reads. A quick preview shows the real rows behind it and save. The table is part of the model. And so you see where this goes. Here's an agent that already uses this model through a feature called Data Query. I'll ask it something no keyword search could answer. Which customer has spent the most in total? Nine seconds later, Ironwood MFG has spent the most in total, with thirteen thousand two hundred sixty-three dollars spent. It wrote the SQL, ran it, and summed the right column, the one whose description we just tuned. The full build of this agent is its own video. So that's the semantic model. Your schema described in plain English, ready for an agent to query. Next video, we handle the other kind of standing knowledge, global context, and after that, we build that analytics agent properly end to end. I am Felipe Wolizer. I'll see you there.
