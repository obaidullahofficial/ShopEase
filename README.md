## Branching Strategy

- **main**: Stable, production-ready code.
- **develop**: Active development.
- **feature/\***: Specific feature development (e.g., `feature/user-auth`).
- **hotfix/\***: Urgent bug fixes (e.g., `hotfix/urgent-bug-fix`).

### Workflow:
1. Create a feature branch from `develop`.
2. Develop the feature and commit changes.
3. Push the feature branch to GitHub.
4. Create a Pull Request (PR) to merge the feature into `develop`.
5. After review and testing, merge `develop` into `main`.
6. For urgent fixes, create a `hotfix` branch from `main`, fix the issue, and merge back into both `main` and `develop`.
