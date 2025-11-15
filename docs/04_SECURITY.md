# 🔐 Security & Deployment Guide

## Overview

This guide covers the security implementation for GitHub token management and deployment procedures.

---

## Security Implementation Summary

### Problem
The GitHub Personal Access Token was hardcoded in `utils.py`:
```python
# ❌ BEFORE: Token exposed
def get_github_stats(token: str = 'your_token_here'):
```

### Solution
Implemented industry-standard environment variable pattern:
```python
# ✅ AFTER: Secure environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_github_stats(username: str = None, token: str = None):
    token = token or GITHUB_TOKEN
```

---

## What Changed

### Code Changes
- **utils.py** - Removed hardcoded token, uses `os.getenv("GITHUB_TOKEN")`
- **.gitignore** - Added protection for `.env`, `.streamlit/secrets.toml`, `*.key`, `*.pem`
- **requirements.txt** - Includes `python-dotenv`

### New Files Created
- `.env` - Local token storage (git ignored)
- `.env.example` - Template for developers
- `.streamlit/secrets.toml.example` - Streamlit Cloud template

---

## Quick Start - 5 Minutes

### Step 1: Revoke Old Token ⚠️
1. Go to: https://github.com/settings/tokens
2. If you had any tokens exposed, revoke them immediately
3. Click: Delete on old tokens
4. **Time: 1 minute**

### Step 2: Create New Token
1. Visit: https://github.com/settings/tokens
2. Click: "Generate new token (classic)"
3. Name: "Portfolio App Token"
4. Expiration: 90 days
5. Scopes: ✅ `public_repo`, ✅ `read:user`, ✅ `user:email`
6. Copy token immediately
7. **Time: 1 minute**

### Step 3: Configure Local Development
1. Edit `.env` file:
   ```env
   GITHUB_USERNAME=SNEHILUPADHYAY007
   GITHUB_TOKEN=your_token_here
   ```
2. **Time: 1 minute**

### Step 4: Verify Setup
```bash
streamlit run app.py
# App should load with GitHub stats
```
**Time: 1 minute**

### Step 5: Push to GitHub
```bash
git add .
git commit -m "chore: implement secure environment variable configuration"
git push origin main
```
**Time: 1 minute**

**Total Time: 5 minutes ✅**

---

## Security Verification Checklist

Before pushing, verify:

```bash
# ✓ Check 1: No hardcoded tokens in code
grep -r "ghp_" --include="*.py" .
# Should return: nothing

# ✓ Check 2: .env not tracked by git
git status | grep -i ".env"
# Should return: nothing

# ✓ Check 3: No secrets in staged changes
git diff --cached | grep -i "token\|password"
# Should return: nothing

# ✓ Check 4: Imports work
python -c "from utils import get_github_stats; print('✓')"

# ✓ Check 5: Token loads
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(f'Token set: {bool(os.getenv(\"GITHUB_TOKEN\"))}')"
```

---

## Local Development Setup

### Initial Setup
```bash
# 1. Copy template
cp .env.example .env

# 2. Edit .env with your token
# Edit .env and add: GITHUB_TOKEN=your_token_here

# 3. Test
streamlit run app.py
```

### Environment Variables
- `GITHUB_USERNAME` - GitHub username (defaults to "SNEHILUPADHYAY007")
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
