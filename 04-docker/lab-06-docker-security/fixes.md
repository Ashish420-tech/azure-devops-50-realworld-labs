## Fix 1: Docker security scan failure

- Switched to node:18-slim
- Reduced unnecessary packages
- Rebuilt image
- Scan passed successfully
- Clarified CI behavior where Docker images are built temporarily for security scanning and not persisted unless pushed.
