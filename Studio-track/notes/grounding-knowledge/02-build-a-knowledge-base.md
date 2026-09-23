# Build a Knowledge Base

*Lesson 02 · Knowledge & RAG*

## What you'll learn

- Create a knowledge base from an empty slate in Lyzr Agent Studio in about five minutes
- Choose a vector store and embedding model — and know why the defaults are the safe call
- Fill a knowledge base from three source types: a text file, a PDF, and a live website crawl
- Test retrieval with the built-in analyzer before you trust the knowledge base with a customer
- Attach the finished knowledge base to an agent and prove it's grounded in your documents

## Key concepts

**A knowledge base starts empty, and the choices you make while building it decide how good your answers turn out.** Building one from scratch takes about five minutes: name it, accept two technical defaults, add your sources, and test. The whole point is to go from a blank slate to an agent that can answer from your documents.

**The two technical choices — vector store and embedding model — both have defaults that just work.** The vector store is where the searchable version of your documents lives; Lyzr's hosted Qdrant is already selected. The embedding model turns your text into something the agent can actually search; its default is fine too. You can change them, but for almost every build you accept both and move on to the part that matters: the knowledge.

**One simple flow ingests every source type — files and the web alike.** Add a text file or a PDF and Lyzr reads it, breaks it into chunks, and indexes it; two different file types go through the same flow. Because so much knowledge already lives on a website, you can also point Lyzr at a doc site by pasting its URL and crawling it, pulling that content in the same way.

**Test retrieval before you wire the knowledge base to anything — it's the fastest way to know it works.** Type a query right in the knowledge base and the analyzer shows you exactly what it pulls back and how well each piece scores. A top match around seventy-nine percent from your support docs, with the next results coming from the PDF, tells you the index is healthy before a single customer ever asks.

**Attaching the knowledge base to an agent is the whole point — that's what grounds it in your documents.** Tuning lives under Configure (retrieval strategy, how many chunks come back, a score threshold to filter weak matches), but the defaults are good. The real final step is opening your agent, adding the knowledge base, and proving in Playground that it now answers from documents that didn't exist when you started.

## In Studio

Primary surface: **Knowledge → Knowledge Base**.

1. Go to **Knowledge → Knowledge Base → New**, and give the knowledge base a name.
2. Confirm the two technical choices: the **vector store** (Lyzr-hosted **Qdrant** is already selected) and the **embedding model** (leave the default). Click **Create**.
3. Click **Add source → Add file** and bring in your documents — for example a support-policies text file and a product-warranty PDF. Lyzr reads each one, chunks it, and indexes it.
4. Click **Add source → Website**, paste your doc-site URL, optionally open the advanced options to control how it crawls, then **Crawl website** to pull that content in too.
5. Test retrieval right there: type a query like `return policy`. The analyzer shows what it pulls back and each piece's score — e.g. a top match around 79% from the support docs, followed by results from the product PDF.
6. To tune retrieval, open **Configure** — the retrieval strategy, the number of chunks returned, and a score threshold to filter out weak matches. The defaults are good; leave them and **Save**.
7. Attach it: open your agent (e.g. the **Northwind** agent), go to **Knowledge**, and add the knowledge base you just built.
8. Prove it landed in **Playground** — ask `what is the warranty policy?` and confirm the answer (down to detail like dead pixels and backlit defects on a specific monitor) comes straight from the uploaded PDF.

## Try this

1. Create a brand-new knowledge base from **Knowledge → Knowledge Base → New**, accept the default Qdrant vector store and embedding model, and add two sources of different types — one file (text or PDF) and one website URL.
2. Before attaching it to anything, type a real question into the knowledge base and read the analyzer scores. Note which source the top match came from and its percentage, then try a query you *expect* to fail and confirm it returns weak or no matches.
3. Attach the knowledge base to one of your agents under its **Knowledge** tab, then ask the same question in **Playground**. Verify the answer cites a detail that could only have come from a document you just uploaded.

## Transcript

Last video, RAG leaned on a knowledge base we had already built. Now let's build one from scratch, from an empty slate to an agent that can answer from it. It takes about five minutes, and the choices you make here decide how good your answers turn out. I'll head to knowledge, knowledge base, and new. I'll give it a name. Then two technical choices the vector store, which is where the searchable version of your documents live The Lyzr hosted Qdrant is already selected and it just works. And the embedding model, which turns your text into something the agent can actually search. The default's fine. Let's go ahead and create it. Now the real knowledge. Add source, add file. I'll bring in two documents, our support policies as a text file, and a product warranty guide as a PDF. Lyzr reads them, breaks them into chunks, and indexes them. Two different file types, same simple flow A lot of your knowledge already lives on a website, so I'll also point Lyzr at our doc site. Add source, website, paste the URL. There are advanced options if you want to control how it crawls and then crawl website. Now that content comes in too. Before I trust this with a customer, I test it. Right here, I type a query, return policy, analyzer shows me exactly what it pulls back and how well each piece scores. The top match, around seventy-nine percent, comes from our support docs, and the next results comes from the PDF, and the next results come from the product PDF. This is the fastest way to know your knowledge base actually works before you wire it to anything. If you want to tune retrieval, that's under configure. The retrieval strategy, how many chunks come back, and a score threshold to filter out weak matches. The defaults are good, so I'll leave them and save. Last step, and it's the whole point, attach it. I'll open our Northwind agent, go to knowledge, and add the knowledge base we just built. Let's prove it landed. In Playground, I ask, what is the warranty policy? And look at this, laptops and monitors, a one-year limited warranty, et cetera. And for the Northview twenty-seven monitor specifically, it even calls out dead pixels and backlit defects. That detail came straight from the product PDF we uploaded two minutes ago. The agent is now grounded in documents that didn't exist when we started this video. So that's Knowledge Base end-to-end. Create it, fill it from files and the web, test the retrieval, and attach it. In the next video, we go one level deeper into how documents get parsed and ingested and why that quietly decides how good your answers are. I'm Felipe Widlizer. I'll see you there
