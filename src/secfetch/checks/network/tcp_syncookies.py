from __future__ import annotations

from secfetch.core.check import security_check
from secfetch.core.error_handling import handle_check_errors, sysctl_check


@security_check(name="TCP SYN Cookies", category="network", risk="medium")
@handle_check_errors
def check() -> dict[str, str]:
    return sysctl_check("/proc/sys/net/ipv4/tcp_syncookies", _TCP_SYN)
