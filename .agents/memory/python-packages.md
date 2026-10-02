---
name: Python package installation
description: Nix-managed base Python package installation constraint for this imported project.
---

The base Python runtime may reject standard package installation as an externally managed environment. Use development environment variables `PIP_USER=1` and `PIP_BREAK_SYSTEM_PACKAGES=1` with the package installation callback, rather than changing the stack or creating a virtual environment.

**Why:** The initial install attempted to modify the immutable Nix Python environment. User-scoped installation succeeded without replacing the imported runtime.

**How to apply:** If dependency installation reports an externally managed environment, preserve the current runtime and use user-scoped installation. Never attempt to write into the Nix store.