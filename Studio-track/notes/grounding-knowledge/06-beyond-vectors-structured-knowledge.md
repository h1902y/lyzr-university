# Beyond vectors — structured knowledge

*Lesson 01 · Ground in Knowledge — Studio: Knowledge Graph & Semantic Model*

## What you'll learn

- Classify enterprise data into three structural shapes: text (unstructured), connections (relational graphs), and tables (structured SQL databases).
- Select the correct Lyzr retrieval architecture (Knowledge Base, Knowledge Graph, or Semantic Data Model) to match the shape of the data.
- Understand the limits of vector search (RAG) when querying interconnected policy rules or structured tabular metrics.
- Stack multiple knowledge architectures within a single agent to handle multi-modal enterprise queries.

## Key concepts

**Knowledge comes in three distinct shapes, each requiring a different retrieval architecture.** The three shapes are: paragraphs of text (solved by basic Knowledge Bases), connected entities and relationships (solved by Knowledge Graphs), and tabular data (solved by Semantic Data Models).

**Basic vector RAG is the wrong tool for questions that require exact relational hops.** Standard vector retrieval chunks documents and searches by similarity. It fails when a question relies on understanding how different policy conditions, exemptions, or entity nodes relate to each other.

**Knowledge Graphs store entities and relationships, mapping how facts connect.** By representing information as nodes (entities) and edges (relationships), a Knowledge Graph allows agents to hop across connections (e.g., warranty conditions linked to product tiers) to synthesize complex logic.

**Semantic Data Models teach agents database schemas to run exact computations.** When querying numerical values like total sales or order counts, agents must write and execute SQL queries against relational tables instead of searching for "similar paragraphs" about revenue.

**One agent can carry all three knowledge types, stacking their capabilities.** A production agent does not need to choose a single architecture; it can retrieve unstructured context from a knowledge base, navigate connections in a graph, and query database tables in parallel.

## In Studio

Studio feature: **Build → Knowledge**. Here's a tour of the three tabs that represent the shapes of data:

1. Navigate to the **Knowledge** screen under **Build** in the left-hand navigation panel.
2. Note the three tabs at the top: **Knowledge Base**, **Knowledge Graph**, and **Semantic Data Model**.
3. Choose **Knowledge Base** when uploading manuals, policies, or markdown docs where passage similarity search is sufficient.
4. Choose **Knowledge Graph** to connect entity relationships extracted from text and synchronize them with a graph database like Neo4j.
5. Choose **Semantic Data Model** to teach the agent your relational database schema (SQL) for exact calculations and aggregations.
6. Under agent settings, attach one, two, or all three knowledge assets to a single agent to combine their retrieval paths.

## Try this

1. Match these three customer service queries to their correct knowledge architecture:
   - *"What is our company's refund policy?"*
   - *"Which customer account manager handles the distributor that bought our model X?"*
   - *"How many refunds did we process yesterday?"*
2. Open the **Knowledge** section in Studio. Navigate between the three tabs and inspect their different connection requirements.

## Transcript

In the knowledge track, we grounded agents in documents. Upload files, the agents finds the right passage, answers from it. That covers a lot. But some questions don't live in a passage. How many orders did our biggest customer place last quarter? Which return policy applies to an open non-defective item? Those answers live in the structure of your data, not in any paragraph. This track is about giving your agent that structure. Welcome to advanced knowledge. Everything in Lyzr's knowledge system lives on one page, and the tabs give the game away. A knowledge base, a knowledge graph, and a semantic data model. Three architectures because knowledge comes in three shapes. The first shape is text: policies, manuals, docs. A basic knowledge base chunks the text, embeds it as vectors, and retrieval finds the passage closest in meaning to your question. That's the RAG we've been using, and when the answer is written down somewhere, it's the right tool. The second shape is connections. Think about a return policy. Unopened items, thirty days, full refund. Open items, fifteen days, restocking fee. The facts matter less than how they link up. A knowledge graph stores entities, the things in your world, and the relationships between them. When a question needs to hop across those links, which conditions get which refund under which warranty? A graph answers what a pile of chunks can't. The third shape is tables: orders, customers, transactions, rows and columns with exact numbers. Vector search is the wrong tool here. You don't want the closest sounding passage about revenue. You want the actual sum. A semantic data model teaches the agent your database schema, what each table and column means, so we can write a real query and compute the real answer. So the rule of thumb: if the answer lives in a paragraph, use a knowledge base. If the answer is about how things connect, use a knowledge graph. Now, if the answer is a number in a table, use a semantic model. And they stack. One agent can carry all three. In the next few videos, we build all of this. A knowledge graph on a real graph database, a semantic model of real sales data, and an agent that answers questions by writing its own SQL. I'm Felipe. I'll see you there.
