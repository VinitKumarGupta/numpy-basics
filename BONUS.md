# This is just a short yet helpful read if you reached till the end :)

---
## 🕒 What is **Wall Time**?

* **Wall Time** = The **real-world time** that passes from the start to the end of your program or operation.
* Measured by looking at the **wall clock** on the wall 🕰️.
* Includes:

  * CPU time
  * Waiting for I/O
  * Context switching
  * Any other delays.

✅ **In Python:** `time.time()` measures **wall time**.

---

### VS **CPU Time**:

* **CPU Time** = Only counts the time your program spends **on the CPU**.
* Excludes waiting for disk, network, or other processes.
  
✅ **In Python:** `time.process_time()` measures **CPU time**.

---

### Why does this matter?

When using NumPy:

* Operations might **offload work to C routines** or even **parallel threads**.
* Your Python process may spend **very little CPU time** but total wall time still includes any thread scheduling or memory transfer.

---

## ⚡ Why is NumPy SO MUCH Faster?

The secret is **Vectorization + Native Code + SIMD**.

---

### 1. **Vectorization (No Python loops)**

When you do:

```python
arr1 + arr2
```

NumPy doesn't loop in Python. Instead, it calls a **compiled C function** to add two arrays in memory.

✅ Result: No Python-level `for i in range(...)` → no interpreter overhead.

---

### 2. **Implemented in C**

* NumPy’s core is written in **C** (and some Fortran).
* C code runs **orders of magnitude faster** than interpreted Python.

✅ Python: interpreted line by line 🐢<br>
✅ C: compiled and optimized 🏎️

---

### 3. **SIMD (Single Instruction Multiple Data)**

Modern CPUs have **vector registers (SSE, AVX)**.
NumPy exploits this:

* Adds multiple elements in one CPU instruction.
* Example:

  ```
  arr1: [a1, a2, a3, a4]
  arr2: [b1, b2, b3, b4]
  ```

  One SIMD instruction computes all `a[i] + b[i]` in parallel.

✅ Python can’t do this in native loops.

---

### 4. **Parallelism**

Some NumPy operations (like matrix multiplication) use **multi-threading** (via BLAS/LAPACK libraries).

* Your CPU cores work together instead of 1-by-1.

✅ This is why NumPy gets **near hardware-level performance**.

---

### 5. **Memory Efficiency**

NumPy arrays are stored in **contiguous blocks of memory** (like C arrays), not scattered Python objects like lists.

✅ Less memory overhead.<br>
✅ Faster access (CPU cache friendly).

---

## So why is Python loop slow?

Python:

* Interpreter overhead (each iteration → interpreted bytecode).
* Dynamic typing (each `arr1[i] + arr2[i]` involves type checking, method dispatch).
* Poor CPU cache locality with lists.

NumPy:

* Zero interpreter overhead (it calls native code).
* Static typing (knows data type ahead of time).
* Vectorized memory access.

---

## 🧠 Bonus: Under the Hood Example

When you write:

```python
arr1 + arr2
```

NumPy roughly does:

```c
for (i = 0; i < size; i++) {
    result[i] = arr1[i] + arr2[i];
}
```

But in **compiled C** and **SIMD optimized**, so 4–8 additions per clock cycle.

In Python:

```python
for i in range(len(arr1)):
    result[i] = arr1[i] + arr2[i]
```

is interpreted **one step at a time**. 🥲
