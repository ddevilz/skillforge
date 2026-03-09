# ToolMark 🔨

> **ESLint + Jest + npm publish — for AI Agent Tools.**

Build, test, scan, and ship tools across **OpenClaw/ClawHub**, **Claude Code**, **Cursor**, and **Windsurf** — from a single CLI.

[![PyPI](https://img.shields.io/pypi/v/toolmark)](https://pypi.org/project/toolmark/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://github.com/ddevilz/toolmark/actions/workflows/toolmark.yml/badge.svg)](https://github.com/ddevilz/toolmark/actions)

---

## Why ToolMark?

13,000+ tools are published on ClawHub. **13% contain critical security flaws** *(Snyk ToxicTools Report, Feb 2026)*. Tools break silently on platforms other than the one they were tested on. There is no `pytest` for agent tools — until now.

```
toolmark init my-tool --template github-api
toolmark test          # LLM-as-judge evaluation
toolmark scan          # prompt injection, dynamic fetch, credential leaks
toolmark compat        # check all 4 platforms at once
toolmark publish       # sign with Ed25519, push to ClawHub + Claude Code
```

---

## Install

```bash
pip install toolmark
```

Requires Python 3.12+.

---

## Quick Start

```bash
# 1. Scaffold
toolmark init my-github-tool --template github-api

# 2. Edit tool.md and tests/
cd my-github-tool

# 3. Test
ANTHROPIC_API_KEY=sk-ant-... toolmark test

# 4. Scan
toolmark scan

# 5. Check platform compatibility
toolmark compat

# 6. Publish
toolmark publish --platforms clawhub,claude-code
```

---

## Commands

| Command               | What it does                                              |
|-----------------------|-----------------------------------------------------------|
| `toolmark init`     | Scaffold a new tool from a template                      |
| `toolmark test`     | LLM-as-judge evaluation against YAML test cases           |
| `toolmark scan`     | Security scanner (prompt injection, dynamic fetch, creds) |
| `toolmark compat`   | Cross-platform compatibility check (4 platforms)          |
| `toolmark bench`    | Benchmark latency, tokens, compute quality score (0–100)  |
| `toolmark publish`  | Sign with Ed25519, publish to configured registries       |

---

## Templates

```bash
toolmark init my-tool --template github-api      # GitHub REST API wrapper
toolmark init my-tool --template file-ops         # Local filesystem tool
toolmark init my-tool --template mcp-integration  # Wraps an MCP server tool
toolmark init my-tool --template web-search       # Search API tool
toolmark init my-tool --template loom-query       # Loom knowledge graph tool
toolmark init my-tool --template blank            # Minimal scaffold
```

---

## Test Cases (YAML)

```yaml
# tests/test_search.yaml
- id: search_open_prs
  input: "find my open pull requests"
  expect_invoked: true
  expect_tool: search_pull_requests
  expect_params:
    state: open
    assignee: "@me"
  tolerance: fuzzy     # strict | fuzzy | invoked
  tags: [smoke]
```

Run: `toolmark test --tags smoke`

---

## Security

toolmark catches:
- **SF001** — Dynamic fetch (`curl | bash`, `eval(fetch(...))`)
- **SF002** — Hardcoded credentials (API keys, passwords)
- **SF003** — Prompt injection phrases in tool descriptions
- **SF004** — Undeclared network endpoints
- **SNYK-*** — 138 rules via Snyk agent-scan (if installed)

---

## Provenance Signing

Every published tool is signed with Ed25519:

```bash
toolmark keygen              # creates ~/.toolmark/signing.key
toolmark publish --sign      # signs + publishes
toolmark verify my-tool     # verify any published tool
```

---

## GitHub Actions

Every `toolmark init` project includes a ready-to-use workflow:

```yaml
# .github/workflows/toolmark.yml — already in your project
- toolmark compat    # platform check
- toolmark scan      # security gate
- toolmark test      # LLM evaluation (needs ANTHROPIC_API_KEY secret)
```

---

## Quality Leaderboard

See how your tool ranks: **[toolmark.dev/leaderboard](https://toolmark.dev/leaderboard)**

Quality Score = test pass rate (50%) + security score (30%) + compat score (20%).

---

## Roadmap

- [x] `init` — scaffold with 6 templates
- [x] `test` — LLM-as-judge evaluation
- [x] `scan` — built-in security rules + Snyk integration
- [x] `compat` — 4-platform compatibility matrix
- [x] `bench` — composite quality score
- [x] `publish` — Ed25519 signing + ClawHub
- [ ] `watch` — re-run tests on save
- [ ] VS Code extension
- [ ] Rust benchmark runner
- [ ] Claude Code + Cursor + Windsurf publish

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We always have [good first issues](https://github.com/ddevilz/toolmark/issues?q=label%3A%22good+first+issue%22).

## License

MIT — see [LICENSE](LICENSE).

---

*Built by [@ddevilz](https://github.com/ddevilz) as part of the [Loom](https://github.com/ddevilz/loom) AI tooling ecosystem.*
