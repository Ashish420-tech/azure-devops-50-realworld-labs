# Troubleshooting: GitHub SSH Authentication Failure

## Problem Statement
While pushing code to GitHub, Git repeatedly asked for username/password
or failed with the error:

Permission denied (publickey).

## Symptoms Observed
- git push prompted for username and password
- HTTPS authentication failed
- SSH test returned:
  Permission denied (publickey)

## Investigation Steps
1. Checked Git remote URL using:
   git remote -v

2. Found repository was using HTTPS instead of SSH.

3. Verified SSH keys present on system:
   ls ~/.ssh

4. Identified multiple SSH keys:
   - id_rsa
   - jenkins_rsa
   - jenkins_wsl_key

5. Tested SSH connectivity:
   ssh -T git@github.com

## Root Cause
GitHub did not have the correct SSH public key registered,
and the SSH agent was not using the correct key.

## Resolution Steps
1. Added the correct public key to GitHub:
   ~/.ssh/id_rsa.pub

2. Started SSH agent:
   eval "$(ssh-agent -s)"

3. Added SSH key to agent:
   ssh-add ~/.ssh/id_rsa

4. Updated Git remote to use SSH:
   git remote add origin git@github.com:Ashish420-tech/azure-devops-50-realworld-labs.git

## Verification
- SSH authentication test succeeded:
  Hi Ashish420-tech! You've successfully authenticated.

- git push worked without asking for username/password.

## Final Outcome
GitHub authentication was successfully configured using SSH.
Future git push and pull operations work without credentials.

## Interview Explanation
If asked in interview:

"I faced a GitHub authentication issue due to HTTPS usage and missing SSH key
registration. I switched to SSH, added the correct public key to GitHub,
configured the SSH agent, and verified authentication using ssh -T."
o

