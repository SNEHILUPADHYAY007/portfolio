# 🚀 Quick Start Guide

## Getting Started

### Installation & Setup
```bash
# Install dependencies
pip install streamlit streamlit-lottie requests

# Run the app
streamlit run app.py
```

### Access the App
- **Local:** http://localhost:8503
- **Network:** http://192.168.1.4:8503

---

## 📁 Project Structure

```
portfolio/
├── app.py                 # Main application
├── utils.py              # Utility functions (GitHub API, caching, skills)
├── README.md             # Main guide (start here!)
├── config/               # Configuration files (JSON)
│   ├── app_config.json
│   ├── about_me_config.json
│   ├── skills_config.json
│   ├── projects_config.json
│   ├── contact_config.json
│   └── work_experience_config.json
├── views/                # Page components
│   ├── about_me.py
│   ├── skills.py
│   ├── projects.py
│   ├── contact.py
│   └── work_experience.py
├── assets/               # Media files (images, lottie, gifs)
└── docs/                 # Documentation
```

---

## 🔧 How to Update Content

### Update Profile Info
Edit: `config/about_me_config.json`
```json
{
  "profile": {
    "name": "Your Name",
    "title": "Your Title",
    "bio": "Your bio here",
    "location": "Your Location"
  }
}
```

### Update Skills
Edit: `config/skills_config.json`
```json
{
  "skills": {
    "Programming Languages": {
      "skills": [
        {"name": "Python", "level": "Expert", "asset_key": "python"}
      ]
    }
  }
}
```

### Update Projects
Edit: `config/projects_config.json`
```json
{
  "projects": [
    {
      "title": "Project Name",
      "description": "Description",
      "tech_stack": ["Tech1", "Tech2"]
    }
  ]
}
```

### Update Contact
Edit: `config/contact_config.json`
```json
{
  "webhook_url": "Your webhook URL",
  "contact_methods": [
    {"method": "Email", "link": "mailto:..."}
  ]
}
```

---

## 🎯 Key Features

### ⚡ Performance
- **Static content:** Loads instantly (<0.5s)
- **Dynamic content:** Loads in background
- **Caching:** Data cached for fast repeats
- **Async loading:** Non-blocking operations

### 🛡️ Error Handling
- GitHub API failures handled gracefully
- Fallback UI displays if data unavailable
- Page remains functional even if APIs fail

### 📊 Dynamic Data
- **Projects:** Fetched from GitHub API (cached)
- **Contributions:** GitHub contribution data
- **Skills:** Counted from configuration
- **Stats:** All calculated automatically

---

## 🧪 Testing

### Test Static Load
1. Go to About Me page
2. Profile/beliefs/achievements appear instantly
3. GitHub metrics appear a moment later

### Test Caching
1. Visit About Me
2. Wait for GitHub data
3. Refresh page
4. See instant metrics (from cache)

### Test Error Handling
1. Go offline
2. Refresh page
3. Static content still visible
4. Error shown gracefully

---

## 📋 Configuration Reference

### app_config.json
- Navigation pages
- Logo and sidebar
- App metadata

### about_me_config.json
- Profile information
- Beliefs and achievements
- Personal details

### skills_config.json
- All skills organized by category
- Asset paths (images/lottie)
- Skill levels

### projects_config.json
- Project details
- Technologies used
- Project links

### contact_config.json
- Contact methods
- Webhook URL
- Form validation

### work_experience_config.json
- Experience entries
- Timeline information
- Resume links

---

## 🔗 Quick Links

| Page | Location | Purpose |
|------|----------|---------|
| About Me | views/about_me.py | Profile & stats |
| Skills | views/skills.py | Skills showcase |
| Projects | views/projects.py | Project portfolio |
| Work Experience | views/work_experience.py | Career timeline |
| Contact | views/contact.py | Contact form |

---

## 💡 Tips

- **Edit config files** to update content
- **No coding needed** for content changes
- **Restart app** after changing config files
- **Check browser console** for errors
- **Monitor network tab** to see GitHub API calls

---

## 🆘 Troubleshooting

### App not starting?
```bash
# Check Python version
python --version

# Check dependencies
pip list | grep streamlit

# Reinstall if needed
pip install --upgrade streamlit
```

### GitHub data not showing?
- Check internet connection
- Verify GitHub token in utils.py
- Check GitHub API rate limits
- Review browser console for errors

### Caching not working?
- Clear browser cache
- Restart Streamlit app
- Check for error messages

---

## 📖 More Information

For detailed documentation, see:
- `02_ARCHITECTURE.md` - System architecture
- `03_IMPLEMENTATION.md` - Implementation details
- `README.md` - Comprehensive guide

---

**Status:** ✅ Active  
**Last Updated:** November 15, 2025
