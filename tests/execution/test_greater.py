"""
Tests of execution of greater operation.
"""

import numpy as np
import pytest

import concrete.numpy as cnp


@pytest.mark.parametrize(
    "function,parameters",
    [
        pytest.param(
            lambda x: x > 0,
            {
                "x": { "range": [0, 10], "status": "encrypted" },
            },
        ),
        pytest.param(
            lambda x, y: x > y,
            {
                "x": { "range": [0, 10], "status": "encrypted" },
                "y": { "range": [0, 10], "status": "encrypted" },
            },
        ),
        pytest.param(
            lambda x, y: x > y,
            {
                "x": { "range": [300, 500], "status": "encrypted" },
                "y": { "range": [300, 500], "status": "encrypted" },
            },
        ),
    ],
)
def test_greater(function, parameters, helpers):
    """
    Test greater.
    """

    parameter_encryption_statuses = helpers.generate_encryption_statuses(parameters)
    configuration = helpers.configuration()

    compiler = cnp.Compiler(function, parameter_encryption_statuses)

    inputset = helpers.generate_inputset(parameters)
    circuit = compiler.compile(inputset, configuration)

    sample = helpers.generate_sample(parameters)
    helpers.check_execution(circuit, function, sample)
