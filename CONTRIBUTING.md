# Contributing

## Development Setup

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
pip install -e ".[dev]"
pytest
```

## Code Style

- Format: `ruff format .`
- Lint: `ruff check .`
- Type check: `mypy .`

## Pull Request Process

1. Create feature branch from `main`
2. Write tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit PR with clear description
