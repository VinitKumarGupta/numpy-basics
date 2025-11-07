# 🚀 NumPy Basics: A Hands-On Tutorial

**Author:** Vinit Kumar Gupta

---

[![Python](https://img.shields.io/badge/Language-Python-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Library](https://img.shields.io/badge/Library-NumPy-013243.svg?style=for-the-badge&logo=numpy)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## ✨ Overview

This repository is a collection of simple, yet complete, Python scripts designed to introduce and demonstrate the core functionalities of the NumPy library. Each file focuses on a specific topic, making it easy to learn the fundamental building blocks for numerical computing and data science in Python.

From array creation and manipulation to advanced linear algebra and performance optimization, this guide covers everything you need to start using NumPy effectively.

## 📚 Table of Contents

| File | Topic | Description |
| :--- | :--- | :--- |
| `01_basics.py` | Array Creation | Creating 1D/2D arrays, zeros, ones, and using `np.arange`. |
| `02_array_operations.py` | Slicing & Element-wise Ops | Simple arithmetic and indexing using slices and steps. |
| `03_reshaping_array.py` | Reshaping & Flattening | Converting array dimensions (`.reshape()`, `.flatten()`). |
| `04_stacking_splitting_array.py` | Stacking & Splitting | Combining and dividing arrays using `np.hstack`, `np.vstack`, `np.hsplit`, and `np.vsplit`. |
| `05_copying_viewing_array.py` | Copy vs. View | Understanding the difference between `arr.copy()` (deep copy) and `arr.view()` (shallow view). |
| `06_mathematical_operations.py` | Mathematical Functions | Using universal functions (ufuncs) like `np.add`, `np.subtract`, `np.sin`, and `np.cos`. |
| `07_statistical_operations.py` | Statistical Analysis | Calculating `np.mean`, `np.median`, and `np.std` (standard deviation). |
| `08_linear_algebra.py` | Linear Algebra | Matrix multiplication using `np.dot()` or the `@` operator, and solving linear equations with `np.linalg.solve`. |
| `09_Broadcasting_Vectorization.py`| Vectorization & Broadcasting | A conceptual deep dive into why NumPy is fast and how broadcasting works. |
| `10_loading_data.py` | Loading Data | Best practices for loading data from CSV files using `np.loadtxt` and `np.genfromtxt`, and loading binary `.npy` files. |
| `11_save_data.py` | Saving Data | Saving arrays to text files (`np.savetxt`) and efficient binary `.npy` files (`np.save`). |
| `12_handling_missing_data.py` | Missing Data (NaN) | Identifying, replacing (`np.nan_to_num`), and removing `np.nan` values. |
| `13_structured_arrays.py` | Structured Arrays | Creating arrays with mixed data types (e.g., ID, Name, Age). |
| `14_random_numbers.py` | Random Numbers | Generating random floats and arrays for simulations. |
| `15_advanced_indexing.py` | Advanced Indexing | Demonstrating Boolean Indexing and Fancy Indexing. |
| `16_optimization.py` & `17_optimExamples.py` | Performance Comparison | Benchmarking the speed difference between Python loops and vectorized NumPy operations. |
| `18_numpy_with_pandas.py` | NumPy & Pandas | How to seamlessly convert NumPy arrays to Pandas DataFrames and vice versa. |
| `19_numpy_with_matplotlib` | NumPy & Matplotlib | Creating visualizations (e.g., a Sine Wave plot) using NumPy data. |

## ⚡ Why NumPy is SO FAST (The Animation)

This is the secret sauce of NumPy, why it crushes standard Python loops:

### 🐍 Python Loop (Slow) vs. 🚀 NumPy Vectorization (Fast)

| Python Loop (Interpreted) | NumPy (Compiled C Code) |
| :--- | :--- |
| **I** **N** **T** **E** **R** **P** **R** **E** **T** **E** **D** | ⚡ **V** **E** **C** **T** **O** **R** **I** **Z** **E** **D** ⚡ |
| `for i in range(N):` | `arr1 + arr2` (Single Instruction Multiple Data - SIMD) |
| Interpreted line-by-line | Executes highly optimized C/Fortran routines |

```python
# The NumPy 'Animation' in Code:

# Python Loop (Sequential Execution)
result[0] = arr1[0] + arr2[0]  # 🐢
result[1] = arr1[1] + arr2[1]  # 🐢
result[2] = arr1[2] + arr2[2]  # 🐢
# ...

# NumPy (Parallel/SIMD Execution)
# All additions happen almost simultaneously in native code.
# 🚀 [a0+b0, a1+b1, a2+b2, ...] 🚀 
result = arr1 + arr2
````

For a detailed breakdown of **Wall Time**, **CPU Time**, and the technical reasons behind NumPy's speed, read the **[BONUS.md]** file.

## 🛠️ Requirements

To run the scripts in this repository, you only need Python and the packages listed in `requirements.txt`:

1.  **Clone the repository:**

    ```bash
    git clone [YOUR_REPO_URL_HERE]
    cd numpy-basics
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run any example:**

    ```bash
    python 07_statistical_operations.py
    ```

Happy Coding\! 📊
