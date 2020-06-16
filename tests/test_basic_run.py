from runnow import run


# pydocstyle: disable=D103


def test_raised_fail():
    # Try with raised error
    try:
        exit_code, result = run("return 1")
    except Exception as ex:
        expected, actual = "Command failed (exit code 1)", str(ex)
        assert actual.startswith(expected), (
            f"Wrong error message. Expected={expected}.\nActual={actual}",
        )
    else:
        assert False, "Should have raised error."


def test_silent_fail():
    # Try with silent error
    exit_code, result = run("return 1", raise_error=False)
    assert exit_code == 1, f"Wrong error code. Expected=1; Actual={exit_code}"


def test_success():
    try:
        exit_code, output = run("echo Hey")
    except Exception as ex:
        raise ex
    else:
        assert (
            exit_code == 0
        ), f"Should have returns exit code 0. Actual return={exit_code}"
        assert output == "Hey", "Should have printed 'Hey'"


if __name__ == "__main__":
    test_raised_fail()
    test_silent_fail()
    test_success()
