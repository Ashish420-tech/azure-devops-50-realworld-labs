## Issue: Windows npm executed instead of Linux npm in WSL

**Lab Path:**
/home/ashish/azure-devops-50-realworld-labs/01-foundation/lab-04-nodejs-ci

**Symptoms:**
- `npm test` triggered `cmd.exe`
- Jest failed with UNC path error
- Working directory resolved to `C:\Windows`

**Evidence:**
- `which npm` returned:
  /mnt/c/Program Files/nodejs/npm
- `$PATH` contained multiple `/mnt/c/...` entries

**Root Cause:**
- WSL auto-injected Windows PATH
- Windows `npm.cmd` took precedence over Linux npm

**Fix Applied:**
- Installed Node.js inside WSL
- Disabled Windows PATH injection using `/etc/wsl.conf`
- Performed full WSL restart using `wsl --shutdown`
- Verified:
  `which npm` → `/usr/bin/npm`

**Prevention:**
- Always validate toolchain with `which npm`
- Keep Linux-only PATH for CI parity
## Issue: npm failed due to missing package.json in mono-repo
**Root Cause:** npm commands executed from repo root while package.json existed in subfolder  
**Impact:** npm install failed with ENOENT  
**Fix:** Set workingDirectory to application folder in Azure Pipelines YAML
