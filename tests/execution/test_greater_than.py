"""
Tests of execution of and operation.
"""

import numpy as np
import pytest

import concrete.numpy as cnp


@pytest.mark.parametrize(
    "function,parameters",
    [
        pytest.param(
            lambda x, y: x > y,
            {
                "x": {"range": [0, 10], "status": "encrypted"},
                "y": {"range": [0, 10], "status": "encrypted"},
            },
            id="x > y",
        ),
    ],
)
def test_gt(function, parameters, helpers):
    """
    Test gt where one of the operators is a constant.
    """

    parameter_encryption_statuses = helpers.generate_encryption_statuses(parameters)
    configuration = helpers.configuration()

    compiler = cnp.Compiler(function, parameter_encryption_statuses)

    inputset = helpers.generate_inputset(parameters)
    circuit = compiler.compile(inputset, configuration)

    sample = helpers.generate_sample(parameters)
    helpers.check_execution(circuit, function, sample)
