# Questions to solve

- 14 and 26 from section 2.6
- 11 and 17 from section 2.7
- 9 and 21 from section 3.1
- 16 from section 3.2
- 18 from section 3.3
- 7 and 12 from section 3.4
- 10 from section 3.5

## 🔧 Coding Tasks 
### ✅ **Task 1: Matrix Multiplication for Elimination**

**Concept:** Row operations as matrix multiplications

```python
def elimination_matrix(n, i, j, multiplier):
    """
    Creates an n x n elimination matrix E that subtracts `multiplier` times row i from row j.

    Parameters:
    - n: Size of the square matrix
    - i: Source row index (0-based)
    - j: Target row index (0-based)
    - multiplier: Value to subtract (E[j][i] = -multiplier)

    Returns:
    - Matrix E (list of lists)
    """
    pass

```

**Input:**

```python
E = elimination_matrix(3, 0, 1, 1.5)
```

---

### ✅ **Task 2: Forward Substitution (for Lower Triangular Systems)**

**Concept:** Solve 𝐿𝑥 = 𝑏 when 𝐿 is lower triangular

```python
def forward_substitution(L, b):
    """
    Solves Lx = b for x using forward substitution.

    Parameters:
    - L: Lower triangular matrix (list of lists)
    - b: Right-hand side vector

    Returns:
    - Solution vector x
    """
    pass

```
**Input:**

```python
L = [[2, 0, 0], [3, 1, 0], [1, -1, 1]]
b = [4, 5, 6]
```


---

### ✅ **Task 3: Back Substitution (for Upper Triangular Systems)**

**Concept:** Solve Ux=b when U is upper triangular (result of Gaussian elimination)

```python
def back_substitution(U, b):
    """
    Solves Ux = b for x using back substitution.

    Parameters:
    - U: Upper triangular matrix (list of lists)
    - b: Right-hand side vector

    Returns:
    - Solution vector x
    """
    pass

```

**Input:**

```python
U = [[2, -1, 3], [0, 1, 4], [0, 0, 2]]
b = [5, 6, 4]
```

---

### ✅ **Loop Recurrence and Stability**

**Concept:** Solve a recurrence relation iteratively
**Goal:** Write a function to compute and plot the values of 𝑢𝑛 for given initial values,constants a and b, and number of steps N

```python
def recurrence_loop(u0, a, b, N):
    """
    Computes the recurrence: u_{n+1} = a * u_n + b

    Parameters:
    - u0: Initial value
    - a: Multiplier
    - b: Constant addition
    - N: Number of iterations

    Returns:
    - List of values [u0, u1, ..., uN]
    """
    pass

```

**Input:**

```python
u0 = 1
a = 0.5
b = 2
N = 10
```

**Bonus:** Use matplotlib to plot the output sequence.

---
