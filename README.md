<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:161b22,100:1f6feb&height=180&section=header&text=&fontSize=0" width="100%"/>

<br>

```
                   ____     __       __
   ________  _____/ __/__  / /______/ /_
  / ___/ _ \/ ___/ /_/ _ \/ __/ ___/ __ \
 (__  )  __/ /__/ __/  __/ /_/ /__/ / / /
/____/\___/\___/_/  \___/\__/\___/_/ /_/
```

<br>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&repeat=true&width=550&height=50&lines=Linux+Security+Inspection+CLI;Like+neofetch%2C+but+for+your+security;One+command.+Full+overview.+Zero+bloat.)](https://github.com/ake13-art/secfetch)

<br>

![Version](https://img.shields.io/badge/version-1.4-1f6feb?style=for-the-badge&labelColor=0d1117)
![License](https://img.shields.io/badge/license-GPL--3.0-58a6ff?style=for-the-badge&labelColor=0d1117)
![Python](https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117)
![Platform](https://img.shields.io/badge/platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white&labelColor=0d1117)

<br>

> **This project uses AI as a development tool.**
> **All code is human‑reviewed, tested and maintained by the author.**

</div>

<br>

---

<br>

<div align="center">

## ⚡ Quick Start

</div>

<br>

```bash
git clone https://github.com/ake13-art/secfetch.git && cd secfetch && pip install .
```

```bash
secfetch
```

<br>

---

<br>

<div align="center">

## 🖥️ Commands

</div>

<br>

<div align="center">

| Command | What it does |
|:---|:---|
| `secfetch` | Full security overview |
| `secfetch fastscan` | Only enabled checks — faster |
| `secfetch --short` | Compact one‑box summary |
| `secfetch live` | Live monitoring — auto refresh every 5s |
| `secfetch live --interval <n>` | Custom refresh interval |
| `secfetch help <check>` | Detailed info, risk level & fix |
| `secfetch -h` | Show all available options |

</div>

<br>

---

<br>

<div align="center">

## 🔍 Security Checks

</div>

<br>

<table>
<tr>
<td width="50%" valign="top">

### 🖥️ System
| Check | Risk |
|:---|:---|
| `kernel` | ℹ️ Info |
| `secure boot` | ⚠️ Medium |

### 🛡️ Kernel Security
| Check | Risk |
|:---|:---|
| `aslr` | 🔴 High |
| `lockdown` | ⚠️ Medium |
| `lsm` | ⚠️ Medium |

### 🔒 Kernel Hardening
| Check | Risk |
|:---|:---|
| `kptr_restrict` | ⚠️ Medium |
| `dmesg_restrict` | ⚠️ Medium |
| `ptrace_scope` | ⚠️ Medium |
| `modules_disabled` | 🟢 Low |
| `unprivileged_bpf` | ⚠️ Medium |

</td>
<td width="50%" valign="top">

### 🌐 Network
| Check | Risk |
|:---|:---|
| `firewall` | ⚠️ Medium |
| `firewall rules` | 🟢 Low |
| `ipv6` | 🟢 Low |
| `open ports` | ⚠️ Medium |
| `services` | ⚠️ Medium |
| `tcp syn cookies` | ⚠️ Medium |
| `reverse path filter` | ⚠️ Medium |

### 📁 Filesystem
| Check | Risk |
|:---|:---|
| `world writable files` | 🔴 High |
| `suid binaries` | ⚠️ Medium |
| `/tmp noexec` | ⚠️ Medium |
| `/tmp sticky bit` | 🟢 Low |

<br>

> Use `secfetch help <check>` for details on any check.

</td>
</tr>
</table>

<br>

---

<br>

<div align="center">

## 📸 Example Output

</div>

<br>

<details>
<summary><b>🔎 Full Mode</b> — <code>secfetch</code></summary>
<br>

```
                   ____     __       __
   ________  _____/ __/__  / /______/ /_
  / ___/ _ \/ ___/ /_/ _ \/ __/ ___/ __ \
 (__  )  __/ /__/ __/  __/ /_/ /__/ / / /
/____/\___/\___/_/  \___/\__/\___/_/ /_/

  System
  ────────────────────────────────────────
    •  Kernel                  6.19.6-arch1-1
    ✖  Secure Boot             Disabled

  Kernel Security
  ────────────────────────────────────────
    ✔  ASLR                    Full
    ⚠  Lockdown                none
    ✔  LSM                     capability,landlock

  Kernel Hardening
  ────────────────────────────────────────
    ✖  kptr_restrict           Unrestricted
    ✔  dmesg_restrict          Enabled
    ✔  ptrace_scope            Restricted
    ⚠  modules_disabled        Disabled
    ✔  unprivileged_bpf        Permanently Disabled

  Network
  ────────────────────────────────────────
    ⚠  Firewall Rules          No rules found
    •  IPv6                    Enabled
    ⚠  Open Ports              53 (domain/UDP), 68 (bootpc/UDP)
    ✔  Reverse Path Filter     Strict
    ⚠  Services                28 running, 26 unexpected
    ✔  TCP SYN Cookies         Enabled

  Security Score
  ────────────────────────────────────────
    System                [░░░░░░░░░░░░]  0/100
    Kernel Security       [██████████░░]  85/100
    Kernel Hardening      [████████░░░░]  72/100
    Network               [███████░░░░░]  65/100
  ────────────────────────────────────────
    Total                 [████████░░░░]  67/100
```

</details>

<details>
<summary><b>📡 Live Mode</b> — <code>secfetch live</code></summary>
<br>

```
                   ____     __       __
   ________  _____/ __/__  / /______/ /_
  / ___/ _ \/ ___/ /_/ _ \/ __/ ___/ __ \
 (__  )  __/ /__/ __/  __/ /_/ /__/ / / /
/____/\___/\___/_/  \___/\__/\___/_/ /_/

  System
  ────────────────────────────────────────
    •  Kernel                  6.19.6-arch1-1
    ✖  Secure Boot             Disabled

  Kernel Security
  ────────────────────────────────────────
    ✔  ASLR                    Full
    ⚠  Lockdown                none
    ✔  LSM                     capability,landlock

  Kernel Hardening
  ────────────────────────────────────────
    ✖  kptr_restrict           Unrestricted
    ✔  dmesg_restrict          Enabled
    ✔  ptrace_scope            Restricted
    ⚠  modules_disabled        Disabled
    ✔  unprivileged_bpf        Permanently Disabled

  Network
  ────────────────────────────────────────
    ⚠  Firewall Rules          No rules found
    •  IPv6                    Enabled
    ⚠  Open Ports              53 (domain/UDP), 68 (bootpc/UDP)
    ✔  Reverse Path Filter     Strict
    ⚠  Services                28 running, 26 unexpected
    ✔  TCP SYN Cookies         Enabled

  Security Score
  ────────────────────────────────────────
    System                [░░░░░░░░░░░░]  0/100
    Kernel Security       [██████████░░]  85/100
    Kernel Hardening      [████████░░░░]  72/100
    Network               [███████░░░░░]  65/100
  ────────────────────────────────────────
    Total                 [████████░░░░]  67/100

  Refreshing every 5s — Press Q + Enter to stop
```

</details>

<details>
<summary><b>⚡ Short Mode</b> — <code>secfetch --short</code></summary>
<br>

```
  ┌──────────────────────────────────────────────────────────┐
  │  System    Kernel: 6.19.6-arch1-1   Secure Boot: ✖      │
  │  Security  ASLR: ✔ Full             Lockdown: ⚠ none    │
  │  Network   Firewall: N/A            Ports: ⚠ 53, 68     │
  │  Score     [████████░░░░]  67/100                        │
  └──────────────────────────────────────────────────────────┘
```

*Designed for `.bashrc` / `.zshrc` as a terminal startup overview.*

</details>

<br>

---

<br>

<div align="center">

## ⚙️ Configuration

</div>

<br>

Fastscan checks can be toggled in `config.conf` (created on first run).

Short mode layout can be changed in `output.py`:

```python
SHORT_LAYOUT = "box"    # bordered box (default)
# SHORT_LAYOUT = "side" # logo left, info right
```

<br>

---

<br>

<div align="center">

## 🗺️ Roadmap

</div>

<br>

<table>
<tr>
<td align="center" width="50%">

### 🔧 v1.5

`secfetch improve`
Scan → find vulnerabilities → suggest fixes

`secfetch improve --auto`
Apply simple fixes automatically
*(with consent prompt)*

</td>
<td align="center" width="50%">

### 🚀 v2.0

`secfetch deepscan`
CVE lookups & system fingerprinting and much more

</td>
</tr>
</table>

<br>

---

<br>

<div align="center">

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL‑3.0)**.
See the [LICENSE](LICENSE) file for details.

<br>

---

<br>

<img src="https://img.shields.io/github/stars/ake13-art/secfetch?style=for-the-badge&logo=github&color=f0c000&logoColor=white&labelColor=0d1117" />
<img src="https://img.shields.io/github/forks/ake13-art/secfetch?style=for-the-badge&logo=git&color=58a6ff&logoColor=white&labelColor=0d1117" />
<img src="https://img.shields.io/github/issues/ake13-art/secfetch?style=for-the-badge&logo=github&color=8b949e&logoColor=white&labelColor=0d1117" />

<br><br>

*⭐ Star this repo if secfetch is useful to you*

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:161b22,100:1f6feb&height=120&section=footer" width="100%"/>

</div>
