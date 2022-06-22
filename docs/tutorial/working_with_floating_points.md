# Working with floating points

## An example

```python
import concrete.numpy as cnp
import numpy as np

# Function using floating points values converted back to integers at the end
@cnp.compiler({"x": "encrypted"})
def f(x):
    return np.fabs(50 * (2 * np.sin(x) * np.cos(x))).astype(np.int64)
    # astype is to go back to the integer world

circuit = f.compile(range(64))

print(circuit.encrypt_run_decrypt(3) == f(3))
print(circuit.encrypt_run_decrypt(0) == f(0))
print(circuit.encrypt_run_decrypt(1) == f(1))
print(circuit.encrypt_run_decrypt(10) == f(10))
print(circuit.encrypt_run_decrypt(60) == f(60))

print("All good!")
```

You can look to [numpy supported functions](../howto/numpy\_support.md) for information about possible float operations.

## Limitations

Floating point support in **Concrete Numpy** is very limited for the time being. They can't appear on inputs, or they can't be outputs. However, they can be used in intermediate results. Unfortunately, there are limitations on that front as well.

This biggest one is that, because floating point operations are fused into table lookups with a single unsigned integer input and single unsigned integer output, only univariate portion of code can be replaced with table lookups, which means multivariate portions cannot be compiled.

To give a precise example, `100 - np.fabs(50 * (np.sin(x) + np.sin(y)))` cannot be compiled because the floating point part depends on both `x` and `y` (i.e., it cannot be rewritten in the form `100 - table[z]` for a `z` that could be computed easily from `x` and `y`).

To dive into implementation details, you may refer to [Fusing Floating Point Operations](../../developer/float-fusing.md) document.