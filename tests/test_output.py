"""Tests for pure utility functions in ui/output.py."""
from secfetch.ui.colors import GREEN, RED, RESET, YELLOW
from secfetch.ui.output import _SCORE_GOOD, _SCORE_WARN, score_bar


class TestScoreBar:
    def test_good_score_uses_green(self):
        result = score_bar(80)
        assert GREEN in result
        assert YELLOW not in result
        assert RED not in result

    def test_warn_score_uses_yellow(self):
        result = score_bar(60)
        assert YELLOW in result
        assert GREEN not in result
        assert RED not in result

    def test_bad_score_uses_red(self):
        result = score_bar(30)
        assert RED in result
        assert GREEN not in result
        assert YELLOW not in result

    def test_threshold_exact_good(self):
        result = score_bar(_SCORE_GOOD)
        assert GREEN in result

    def test_threshold_exact_warn(self):
        result = score_bar(_SCORE_WARN)
        assert YELLOW in result

    def test_just_below_good_threshold_uses_yellow(self):
        result = score_bar(_SCORE_GOOD - 1)
        assert YELLOW in result

    def test_just_below_warn_threshold_uses_red(self):
        result = score_bar(_SCORE_WARN - 1)
        assert RED in result

    def test_width_controls_bar_length(self):
        result = score_bar(50, width=10)
        # strip ANSI codes to count bar characters
        inner = result.replace(GREEN, "").replace(YELLOW, "").replace(RED, "").replace(RESET, "")
        # inner is "[<bar>]"
        bar_content = inner[1:-1]
        assert len(bar_content) == 10

    def test_score_100_produces_full_bar(self):
        result = score_bar(100, width=8)
        inner = result.replace(GREEN, "").replace(YELLOW, "").replace(RED, "").replace(RESET, "")
        bar_content = inner[1:-1]
        assert bar_content == "█" * 8

    def test_score_0_produces_empty_bar(self):
        result = score_bar(0, width=8)
        inner = result.replace(GREEN, "").replace(YELLOW, "").replace(RED, "").replace(RESET, "")
        bar_content = inner[1:-1]
        assert bar_content == "░" * 8

    def test_output_is_wrapped_in_brackets(self):
        result = score_bar(50, width=5)
        inner = result.replace(GREEN, "").replace(YELLOW, "").replace(RED, "").replace(RESET, "")
        assert inner.startswith("[")
        assert inner.endswith("]")
