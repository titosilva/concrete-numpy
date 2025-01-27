"""
Tests of execution of transpose operation.
"""

import numpy as np
import pytest

import concrete.numpy as cnp


@pytest.mark.parametrize(
    "function,parameters",
    [
        pytest.param(
            lambda x: np.transpose(x),
            {
                "x": {"shape": (3, 2), "range": [0, 10], "status": "encrypted"},
            },
        ),
        pytest.param(
            lambda x: x.transpose(),
            {
                "x": {"shape": (3, 2), "range": [0, 10], "status": "encrypted"},
            },
        ),
        pytest.param(
            lambda x: x.T,
            {
                "x": {"shape": (3, 2), "range": [0, 10], "status": "encrypted"},
            },
        ),
    ],
)
def test_transpose(function, parameters, helpers):
    """
    Test transpose.
    """

    parameter_encryption_statuses = helpers.generate_encryption_statuses(parameters)
    configuration = helpers.configuration()

    compiler = cnp.Compiler(function, parameter_encryption_statuses)

    inputset = helpers.generate_inputset(parameters)
    circuit = compiler.compile(inputset, configuration)

    sample = helpers.generate_sample(parameters)
    helpers.check_execution(circuit, function, sample)
