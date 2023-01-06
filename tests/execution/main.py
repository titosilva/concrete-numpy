import concrete.numpy as cnp
import numpy as np
from timeit import default_timer as timer

configuration = cnp.Configuration(
    enable_unsafe_features=True,
    use_insecure_key_cache=True,
    # show_optimizer=True,
    # verbose=True,
    show_graph=True,
    insecure_key_cache_location=".keys",
)

# @cnp.compiler({"x": "encrypted"})
# def f(x):
#     return x > 50

# inputset = [np.random.randint(0, 2 ** 15) for _ in range(100)]
# circuit = f.compile(inputset, configuration, verbose=False)

# for i in range(0, 14):
#     start = timer()
#     print(f"Test: 2**{i} > 50; Result: {circuit.encrypt_run_decrypt(2 ** i)}; Time: {timer() - start} s")

# BOTH ENCRYPTED
@cnp.compiler({"x": "encrypted", "y": "encrypted"})
def f(x, y):
    return x <= y

inputset = [(np.random.randint(0, 2 ** 15), np.random.randint(0, 2 ** 15)) for _ in range(100)]
circuit = f.compile(inputset, configuration, verbose=False)

for i in range(0, 14):
    start = timer()
    x = np.random.randint(0, 2 ** 15)
    y = np.random.randint(0, 2 ** 15)

    if np.random.randint(0, 2) == 1:
        x = y

    print(f"Test: {x} <= {y}; Result: {circuit.encrypt_run_decrypt(x, y)}; Time: {timer() - start} s")