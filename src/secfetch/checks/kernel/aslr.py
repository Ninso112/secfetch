from __future__ import annotations

from secfetch.core.check import security_check
from secfetch.core.error_handling import safe_read_file


@security_check(name="ASLR", category="kernel_security", risk="high")
def check() -> dict[str, str]:
    val = safe_read_file("/proc/sys/kernel/randomize_va_space", default=None)
    if val is None:
        return {"status": "info", "value": "not available"}
    return {
        "status": {"2": "ok", "1": "warn"}.get(val, "bad"),
        "value": {"2": "Full", "1": "Partial"}.get(val, "Disabled"),
    }
