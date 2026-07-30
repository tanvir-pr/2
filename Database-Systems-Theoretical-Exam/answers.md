# Database Systems — Theoretical Exam Answers

## Question 1: Elevator Algorithm (5 points)

The **elevator algorithm** (SCAN/C-SCAN) is a disk scheduling strategy that speeds up disk access by reducing unnecessary head movement.

**How it works:**
- The disk arm moves in one direction (e.g., towards higher cylinder numbers), servicing all pending I/O requests along the way.
- When it reaches the last request (or the end of the disk), it reverses direction and services requests going back.
- Similar to how an elevator moves up and down a building, stopping at requested floors.

**How it is stored:**
- Pending requests are stored in a queue (sorted by cylinder/track number). The algorithm picks requests in order of the arm's current direction of travel.

**Advantages:**
- Reduces total seek time compared to FCFS
- Prevents starvation — every request will eventually be served
- Fair — treats requests on both sides equally

**Disadvantages:**
- Requests at the edges may wait longer
- Not optimal — SSTF may have lower average seek time
- Uneven wait times — requests just behind the head must wait for a full sweep

---

## Question 2: Complete the Table (6 points)

**Given:**
- `sc = Distance * 4`
- `A = Location_code LIKE '%C' AND sc < 1500`
- `B = Location_code LIKE '%C' OR sc < 1500`

| Location_code | Distance | sc | LIKE '%C' | sc < 1500 | A (AND) | B (OR) |
|---|---|---|---|---|---|---|
| DP_SHP | 500 | 2000 | No | No | **No** | **No** |
| DP_SLS | NULL | NULL | No | Unknown | **No** | **No** |
| DP_PRC | 200 | 800 | Yes | Yes | **Yes** | **Yes** |
| DP_FNC | NULL | NULL | Yes | Unknown | **No** | **Yes** |

---

## Question 3: Linear Convolution / Linear Hashing (5 points)

**Linear Hashing** is a dynamic hashing technique that allows a hash table to grow gradually (one bucket at a time).

**How it works:**
1. Start with N buckets and hash function `h0(k) = k mod N`
2. Maintain a split pointer (p) starting at bucket 0
3. When overflow occurs:
   - Split bucket at position p using `h1(k) = k mod 2N`
   - Advance p to p+1
4. When p reaches N, reset p to 0, N doubles, use next-level hash function

**Key characteristics:**
- No directory needed (unlike extendible hashing)
- Graceful, incremental growth
- Lookup: use `h0(k)`; if result < p, use `h1(k)` instead

---

## Question 4: Logical Query Plan Structure (5 points)

A **logical query plan** is a tree-structured representation of relational algebra.

**Structure:**
- **Leaf nodes** = base relations (tables)
- **Internal nodes** = relational algebra operators
- **Edges** = data flow (upward)
- **Root** = final result

**Elements:**
| Operator | Symbol | Purpose |
|---|---|---|
| Selection | σ | Filters rows (WHERE) |
| Projection | π | Selects columns (SELECT) |
| Join | ⋈ | Combines rows from two tables |
| Cartesian Product | × | All combinations of rows |
| Union | ∪ | Combines results |
| Difference | − | Rows in one but not another |
| Rename | ρ | Renames relations/attributes |
| Grouping | γ | GROUP BY + aggregates |

---

## Question 5: Logical Query Design + Optimization (5 points)

**SQL Query:**
```sql
SELECT c1, d1, d2
FROM c, d
WHERE c2 = d3
  AND c2 = 'HU'
  AND d4 = 50;
```

### Initial (Naive) Plan:
```
    π (c1, d1, d2)
        |
    σ (c2 = d3 AND c2 = 'HU' AND d4 = 50)
        |
       × (Cartesian product)
      / \
     c    d
```

### Optimized Plan:
```
      π (c1, d1, d2)
          |
        ⋈ (c2 = d3)
       /         \
σ(c2='HU')    σ(d4=50)
    |              |
 π(c1,c2)     π(d1,d2,d3,d4)
    |              |
    c              d
```

Optimizations: Push selections down, replace Cartesian product with join, push projections down.

---

## Question 6: Syntactic Category with Recursive Definition (4 points)

Example: **\<expr\>** (arithmetic expression)

**Recursive BNF:**
```
<expr> ::= <number>
          | <expr> + <expr>
          | <expr> - <expr>
          | <expr> * <expr>
          | ( <expr> )
```

**Parse tree for `3 + 5 * 2`:**
```
        <expr>
       /  |  \
  <expr>  +  <expr>
    |        /  |  \
    3   <expr> * <expr>
          |        |
          5        2
```

The definition is recursive because `<expr>` refers to itself in its own production rules.
