from __future__ import annotations

from secfetch.core.check import security_check
from secfetch.core.error_handling import handle_check_errors


@security_check(name="LSM", category="kernel_security", risk="high")
@handle_check_errors
def check() -> dict[str, str]:
    with open("/sys/kernel/security/lsm") as f:
        value = f.read().strip()

    if value:
        return {"status": "ok", "value": value}
    return {"status": "warn", "value": "none"}
