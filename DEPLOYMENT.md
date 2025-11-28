# 🚀 Deployment Guide: Hosting on GitHub + Streamlit Cloud

This guide shows you how to host your Carbon Footprint Analyzer on GitHub and deploy it for free on **Streamlit Community Cloud**.

---

## 📋 Prerequisites

- GitHub account ([sign up here](https://github.com/join))
- Streamlit Community Cloud account ([sign up here](https://streamlit.io/cloud) - free with GitHub)
- Your API keys ready:
  - **OpenAI API Key** (required) - [Get one here](https://platform.openai.com/api-keys)
  - **Groq API Key** (optional) - [Get one here](https://console.groq.com/keys)

---

## 🔧 Step 1: Prepare Your Repository

Your repository is already connected to GitHub:
```
https://github.com/Suryam1976/carbon_footprint_langgraph
```

### Files Added for Deployment

✅ `.streamlit/config.toml` - Streamlit theme configuration  
✅ `packages.txt` - System dependencies (poppler-utils for PDF processing)  
✅ `.streamlit/secrets.toml.example` - Template for API keys  
✅ `requirements.txt` - Python dependencies  

---

## 📤 Step 2: Commit and Push to GitHub

Run these commands in your terminal:

```bash
# Navigate to project directory
cd /Users/sanjayfuloria/projects/carbon_footprint/carbon_footprint_langgraph

# Stage all changes
git add .

# Commit with a message
git commit -m "Add Streamlit deployment config and UI improvements"

# Push to GitHub
git push origin main
```

**Important:** Your `.env` file is already in `.gitignore`, so your API keys won't be pushed to GitHub (which is good for security!).

---

## ☁️ Step 3: Deploy on Streamlit Community Cloud

### 3.1 Sign in to Streamlit Cloud

1. Go to [https://share.streamlit.io/](https://share.streamlit.io/)
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub repositories

### 3.2 Create New App

1. Click **"New app"** button
2. Fill in the deployment form:
   - **Repository:** `Suryam1976/carbon_footprint_langgraph`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
   - **App URL:** Choose a custom subdomain (e.g., `carbon-footprint-analyzer`)

3. Click **"Advanced settings"** (optional):
   - **Python version:** 3.11 or 3.12 (recommended)
   - **Secrets:** We'll add these next

### 3.3 Add API Keys as Secrets

**Critical:** Don't put API keys directly in your code or GitHub. Use Streamlit's secrets management.

1. In the deployment settings, click **"Advanced settings"**
2. Scroll to **"Secrets"** section
3. Paste your API keys in TOML format:

```toml
# Required: OpenAI API Key
OPENAI_API_KEY = "sk-proj-your-actual-openai-key-here"

# Optional: Groq API Key (if using Groq models)
GROQ_API_KEY = "gsk_your-actual-groq-key-here"

# Optional: LangSmith Tracing (for debugging)
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = "your-langsmith-key-here"
LANGCHAIN_PROJECT = "carbon-footprint-analyzer"
LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
```

**Note:** Only `OPENAI_API_KEY` is required. Add others if you want to use Groq or LangSmith.

4. Click **"Deploy!"**

---

## ⏱️ Step 4: Wait for Deployment

Streamlit Cloud will:
1. ✅ Clone your repository
2. ✅ Install system packages from `packages.txt` (poppler-utils)
3. ✅ Install Python packages from `requirements.txt`
4. ✅ Start your Streamlit app

**Deployment time:** Usually 2-3 minutes

You'll see real-time logs. If it fails, check the logs for missing dependencies or errors.

---

## 🎉 Step 5: Your App is Live!

Once deployed, you'll get a public URL:
```
https://your-app-name.streamlit.app
```

Share this link with anyone! They can:
- Upload bank statements
- Analyze carbon footprints
- Get insights and recommendations

---

## 🔄 Updating Your App

Whenever you push changes to GitHub, Streamlit Cloud auto-deploys:

```bash
# Make changes to your code
# ...

# Commit and push
git add .
git commit -m "Update feature XYZ"
git push origin main
```

Streamlit will detect the push and redeploy automatically (usually within 1-2 minutes).

---

## 🔐 Security Best Practices

### ✅ DO:
- Store API keys in Streamlit Cloud secrets (done above)
- Keep `.env` in `.gitignore` (already configured)
- Use environment variables for sensitive data
- Regenerate API keys if accidentally exposed

### ❌ DON'T:
- Commit `.env` file to GitHub
- Hardcode API keys in Python files
- Share your secrets.toml with others
- Use production API keys for testing

---

## 🐛 Troubleshooting

### Problem: "App is not loading"
**Solution:** Check logs in Streamlit Cloud dashboard. Common issues:
- Missing `OPENAI_API_KEY` in secrets
- Wrong Python version (use 3.11+)
- Package installation failures

### Problem: "PDF parsing not working"
**Solution:** Ensure `packages.txt` contains `poppler-utils`. Redeploy if needed.

### Problem: "Connection error" when extracting transactions
**Solution:** 
- Verify `OPENAI_API_KEY` is valid in secrets
- Try switching to Groq in the UI (add `GROQ_API_KEY` to secrets)
- Check API quota/billing at [OpenAI Dashboard](https://platform.openai.com/usage)

### Problem: "Module not found" error
**Solution:** Add missing package to `requirements.txt`, commit, and push:
```bash
echo "missing-package-name" >> requirements.txt
git add requirements.txt
git commit -m "Add missing dependency"
git push origin main
```

---

## 📊 Managing Secrets After Deployment

To update API keys later:

1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Click on your app
3. Click **"Settings"** (⚙️ icon)
4. Select **"Secrets"**
5. Update keys and click **"Save"**
6. App will automatically restart with new secrets

---

## 💰 Cost & Limits

### Streamlit Community Cloud (Free Tier):
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Auto-scaling
- ✅ HTTPS included
- ❌ No private apps (upgrade to Streamlit Cloud Pro for $20/month)

### API Costs:
- **OpenAI GPT-4o-mini:** ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens
- **Groq (Llama 3.3 70B):** Free tier: 14,400 requests/day, then ~$0.59 per 1M tokens

**Typical usage:** Analyzing a 50-page bank statement ≈ $0.05-0.15 per analysis

---

## 🌍 Sharing Your App

### Public URL:
Share your Streamlit Cloud URL with anyone:
```
https://carbon-footprint-analyzer.streamlit.app
```

### Embed in Website:
Add iframe to your website:
```html
<iframe src="https://your-app.streamlit.app" width="100%" height="800"></iframe>
```

### Social Media:
Use Streamlit's built-in sharing button (top-right in deployed app).

---

## 🚀 Advanced: Custom Domain

Streamlit Cloud Pro ($20/month) allows custom domains:
1. Upgrade to Pro
2. Add CNAME record in your DNS:
   ```
   app.yourdomain.com  →  your-app.streamlit.app
   ```
3. Configure in Streamlit Cloud settings

---

## 📞 Support

- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io/)
- **Streamlit Forum:** [discuss.streamlit.io](https://discuss.streamlit.io/)
- **GitHub Issues:** [Your repo issues](https://github.com/Suryam1976/carbon_footprint_langgraph/issues)

---

## 🎯 Quick Reference Commands

```bash
# Check repository status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View remote URL
git remote -v
```

---

**🎉 That's it! Your Carbon Footprint Analyzer is now live on the internet!**

Questions? Open an issue on GitHub or contact the maintainer.
