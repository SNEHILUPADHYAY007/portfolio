# 🔐 Security & Deployment Guide# 🔐 Security & Deployment Guide



## Overview## Overview



This guide covers the security implementation for GitHub token management and deployment procedures.This guide covers the security implementation for GitHub token management and deployment procedures.



------



## Security Implementation## Security Implementation Summary



### Token Management### Problem

GitHub tokens are now managed securely using environment variables instead of hardcoded values:The GitHub Personal Access Token was hardcoded in `utils.py` as a default parameter value, exposing credentials in source code.



```python### Solution

# Load tokens from environment, never from codeImplemented industry-standard environment variable pattern:

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")```python

```# ✅ AFTER: Secure environment variable

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

This ensures credentials are:

- ✅ Never exposed in source codedef get_github_stats(username: str = None, token: str = None):

- ✅ Never committed to Git    token = token or GITHUB_TOKEN

- ✅ Safely stored locally```

- ✅ Easily configurable per environment

Now tokens are loaded from environment variables, never from code.

---

---

## Local Development Setup

## What Changed

### Step 1: Create GitHub Personal Access Token

1. Visit: https://github.com/settings/tokens### Code Changes

2. Click: "Generate new token (classic)"- **utils.py** - Removed hardcoded token, uses `os.getenv("GITHUB_TOKEN")`

3. Token name: "Portfolio App Token"- **.gitignore** - Added protection for `.env`, `.streamlit/secrets.toml`, `*.key`, `*.pem`

4. Expiration: 90 days recommended- **requirements.txt** - Includes `python-dotenv`

5. Scopes: Select `public_repo`, `read:user`, `user:email`

6. Click: "Generate token"### New Files Created

7. **Copy the token immediately** (it won't be shown again)- `.env` - Local token storage (git ignored)

- `.env.example` - Template for developers

### Step 2: Configure Local Environment- `.streamlit/secrets.toml.example` - Streamlit Cloud template

1. Create `.env` file in project root:

   ```---

   GITHUB_USERNAME=SNEHILUPADHYAY007

   GITHUB_TOKEN=<paste_your_token_here>## Quick Start - 5 Minutes

   ```

2. Save the file### Step 1: Revoke Old Token ⚠️

3. Verify `.env` is in `.gitignore` (it is!)1. Go to: https://github.com/settings/tokens

2. If you had any old tokens exposed, revoke them immediately

### Step 3: Verify Setup3. Click: Delete on old tokens

Run the app:4. **Time: 1 minute**

```bash

streamlit run app.py### Step 2: Create New Token

```1. Visit: https://github.com/settings/tokens

2. Click: "Generate new token (classic)"

The app will automatically load your credentials from `.env`.3. Name: "Portfolio App Token"

4. Expiration: 90 days

---5. Scopes: ✅ `public_repo`, ✅ `read:user`, ✅ `user:email`

6. Copy token immediately

## Production Deployment (Streamlit Cloud)7. **Time: 1 minute**



### Step 1: Create Deployment Token### Step 3: Configure Local Development

Same as local setup - create a new personal access token with same scopes.1. Edit `.env` file:

   ```env

### Step 2: Add to Streamlit Cloud Secrets   GITHUB_USERNAME=SNEHILUPADHYAY007

1. Open your app settings in Streamlit Cloud   GITHUB_TOKEN=paste_your_token_here

2. Navigate to: "Secrets"   ```

3. Add your configuration:2. **Time: 1 minute**

   ```toml

   GITHUB_USERNAME = "SNEHILUPADHYAY007"### Step 4: Verify Setup

   GITHUB_TOKEN = "your_token_here"```bash

   ```streamlit run app.py

4. Save secrets# App should load with GitHub stats

```

### Step 3: Deploy**Time: 1 minute**

Your app will use the secrets from Streamlit Cloud dashboard automatically.

### Step 5: Push to GitHub

---```bash

git add .

## File Protectiongit commit -m "chore: implement secure environment variable configuration"

git push origin main

The following files are protected in `.gitignore`:```

- `.env` - Local credentials (never commit)**Time: 1 minute**

- `.streamlit/secrets.toml` - Cloud credentials (never commit)

- `*.key`, `*.pem` - Private keys (never commit)**Total Time: 5 minutes ✅**



------



## Best Practices## Security Verification Checklist



1. **Token Rotation**: Create new tokens every 90 daysBefore pushing, verify:

2. **Limited Scope**: Only request necessary permissions (`public_repo`, `read:user`, `user:email`)

3. **Multiple Tokens**: Use different tokens for development vs production```bash

4. **Revoke Immediately**: If a token is exposed, revoke it on GitHub immediately# ✓ Check 1: No hardcoded tokens in code

5. **Environment Variables**: Never put tokens in code or config filesgrep -r "token" --include="*.py" .

# Should return: only os.getenv patterns

---

# ✓ Check 2: .env not tracked by git

## Troubleshootinggit status | grep -i ".env"

# Should return: nothing

### "GitHub API request failed"

- Check token is valid: https://github.com/settings/tokens# ✓ Check 3: No secrets in staged changes

- Verify token hasn't expiredgit diff --cached | grep -i "token\|password"

- Ensure token has required scopes# Should return: nothing



### "API rate limit exceeded"# ✓ Check 4: Imports work

- Unauthenticated requests: 60 per hourpython -c "from utils import get_github_stats; print('✓')"

- Authenticated requests: 5,000 per hour

- Check rate limit: https://api.github.com/rate_limit# ✓ Check 5: Token loads

python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(f'Token set: {bool(os.getenv(\"GITHUB_TOKEN\"))}')"

### App won't load GitHub data```

1. Check `.env` file exists with valid token

2. Run: `pip install python-dotenv`---

3. Verify token has `public_repo` scope

4. Restart Streamlit: `streamlit run app.py`## Local Development Setup



---### Initial Setup

```bash

## Files Modified# 1. Copy template

cp .env.example .env

- `utils.py` - Uses environment variables via `os.getenv()`

- `.gitignore` - Enhanced protection for sensitive files# 2. Edit .env with your token

- `requirements.txt` - Includes `python-dotenv`# Edit .env and add your personal access token



---# 3. Test

streamlit run app.py

## New Configuration Files```



- `.env.example` - Template for developers### Environment Variables

- `.streamlit/secrets.toml.example` - Template for Streamlit Cloud- `GITHUB_USERNAME` - GitHub username (defaults to "SNEHILUPADHYAY007")

- `GITHUB_TOKEN` - Personal Access Token (required for full rate limit)

### Working Without Token
The app works without a token but with limited rate limits:
- **With token:** 5,000 requests/hour
- **Without token:** 60 requests/hour

---

## Production Deployment

### Streamlit Cloud

1. Deploy your app to Streamlit Cloud
2. Go to: https://share.streamlit.io/
3. Find your app → Settings → Secrets
4. Add your credentials:
   ```toml
   GITHUB_USERNAME = "SNEHILUPADHYAY007"
   GITHUB_TOKEN = "your_github_personal_access_token"
   ```
5. The app will automatically read from these secrets

### Other Platforms (Heroku, AWS, Azure, etc.)

Set environment variables in your platform's dashboard:
- `GITHUB_USERNAME=SNEHILUPADHYAY007`
- `GITHUB_TOKEN=your_github_personal_access_token`

### Docker

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Token passed at runtime
CMD streamlit run app.py
```

Run with:
```bash
docker run -e GITHUB_TOKEN=your_token your_image
```

---

## Token Management Best Practices

### Token Creation
- ✅ Minimal required scopes: `public_repo`, `read:user`, `user:email`
- ✅ Set expiration: 90 days recommended
- ✅ Use different tokens per environment if possible
- ✅ Copy immediately (won't be shown again)

### Token Rotation
- Rotate every 90 days
- Create new token before expiration
- Update in all environments
- Revoke old token after verification

### If Token is Exposed
1. **Immediately revoke** on GitHub
2. **Create new token** right away
3. **Update all environments** with new token
4. **Monitor** GitHub audit logs

### Token Security
- ✅ Never commit to git
- ✅ Protected by `.gitignore`
- ✅ Use environment variables
- ✅ Minimal access scopes
- ✅ Regular rotation

---

## How It Works

### Local Development Flow
```
.env file
    ↓
python-dotenv loads
    ↓
os.getenv("GITHUB_TOKEN")
    ↓
GitHub API calls
```

### Production Flow (Streamlit Cloud)
```
Streamlit Secrets Dashboard
    ↓
Streamlit Cloud passes to app
    ↓
os.getenv("GITHUB_TOKEN")
    ↓
GitHub API calls
```

### Production Flow (Other Platforms)
```
Platform Environment Variables
    ↓
Runtime passes to process
    ↓
os.getenv("GITHUB_TOKEN")
    ↓
GitHub API calls
```

---

## Files Protected by .gitignore

The `.gitignore` now protects:
- `.env` - Local environment variables
- `.env.local` - Local overrides
- `.env.*.local` - Variant-specific locals
- `.streamlit/secrets.toml` - Streamlit secrets
- `*.key` - SSH keys
- `*.pem` - Certificates
- `credentials.json` - Service accounts

---

## Troubleshooting

### App can't find GitHub token
**Problem:** GitHub stats not loading
**Solution:**
1. Check `.env` file exists in project root
2. Check `GITHUB_TOKEN=xxx` is set
3. Verify token hasn't expired
4. Restart app: `streamlit run app.py`

### Rate limit errors
**Problem:** "API rate limit exceeded"
**Solution:**
1. Verify token is set in `.env`
2. Check token has correct scopes
3. Restart app to reload token

### Token won't load
**Problem:** `os.getenv("GITHUB_TOKEN")` returns None
**Solution:**
1. Verify `.env` file syntax
2. Check no spaces around `=`
3. Verify `.env` is in project root
4. Restart Python/app

### Can't push to GitHub
**Problem:** "token not found in diff"
**Solution:**
1. Run: `git status` (should not show `.env`)
2. Run: `git diff --cached | grep -i token` (should be empty)
3. Then push: `git push origin main`

---

## Monitoring & Maintenance

### Daily
- Monitor app for errors
- Check GitHub stats load correctly

### Weekly
- Check GitHub audit log: https://github.com/settings/audit-log
- Verify no unusual API activity

### Monthly
- Review token usage
- Check app performance
- Monitor error logs

### Quarterly
- Token rotation (if 90+ days old)
- Review access scopes needed
- Update documentation if needed

---

## References

- [GitHub Personal Access Token Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

## Summary

✅ Token removed from source code
✅ Environment variable system implemented
✅ Git protection in place
✅ Documentation complete
✅ Ready for production deployment

**Status: Production Ready 🟢**
