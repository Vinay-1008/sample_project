def pytest_addoption(parser):
    parser.addoption(
        "--input_name",  # Custom argument name
        action="store",  # Store the value passed to this argument
        default="default_name",  # Optional default value
        help="Provide a name",  # Description of the argument for `--help`
    )

import pytest

@pytest.fixture
def input_name(request):
    # Retrieve the value of the --names option
    return request.config.getoption("--input_name")