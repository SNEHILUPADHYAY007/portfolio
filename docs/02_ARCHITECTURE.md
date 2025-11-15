# 📐 Architecture & Implementation

## System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────┐
│              Browser (User)                  │
└────────────────┬────────────────────────────┘
                 │
         ┌───────┴────────┐
         │                │
    ┌────▼────┐      ┌───▼─────┐
    │ Streamlit│      │ GitHub  │
    │   App    │      │  API    │
    └────┬────┘      └────┬────┘
         │                │
    ┌────▼────────────────▼────┐
    │   Main App (app.py)       │
    │  - Navigation             │
    │  - Sidebar (Quick Stats)  │
    │  - Page Routing           │
    └────┬──────────────────────┘
         │
    ┌────▼───────────────────────┐
    │      Views Layer           │
    │ ├─ about_me.py            │
    │ ├─ skills.py              │
    │ ├─ projects.py            │
    │ ├─ contact.py             │
    │ └─ work_experience.py      │
    └────┬──────────────────────┘
         │
    ┌────▼───────────────────────┐
    │    Utilities (utils.py)    │
    │ ├─ get_github_stats()      │
    │ ├─ get_github_contributions│
    │ ├─ get_total_skills()      │
    │ └─ Cache management        │
    └────┬──────────────────────┘
         │
    ┌────▼───────────────────────┐
    │  Configuration Layer       │
    │  (JSON files)              │
    │ ├─ app_config.json         │
    │ ├─ about_me_config.json    │
    │ ├─ skills_config.json      │
    │ ├─ projects_config.json    │
    │ ├─ contact_config.json     │
    │ └─ work_experience_config  │
    └───────────────────────────┘
```

---

## Data Flow

### Static Content Flow
```
Config JSON
    │
    ├─ Load from file
    │
    ├─ Parse JSON
    │
    └─ Display in Streamlit
```

### Dynamic Content Flow
```
GitHub API
    │
    ├─ API call (first time)
    │
    ├─ @st.cache_data caches result
    │
    ├─ Return from cache (subsequent calls)
    │
    └─ Display in Streamlit
```

### Page Load Timeline

```
Time 0ms
  │
  ├─ Load app_config.json
  │
  ├─ Render sidebar with Quick Stats
  │   ├─ GitHub stats (cached/API)
  │   └─ Skills count (from config)
  │
  ├─ Render navigation
  │
└─ Page ready for routing

User clicks "About Me"
  │
  ├─ Load about_me_config.json
  │
  ├─ Render static sections (instant)
  │   ├─ Profile
  │   ├─ Beliefs
  │   └─ Achievements
  │
  ├─ Fragment starts (background)
  │   ├─ get_github_stats() (cached/API)
  │   └─ get_github_contributions() (API)
  │
  ├─ Metrics appear (when ready)
  │
  └─ Page complete
```

---

## Component Details

### 1. app.py (Main App)
**Purpose:** Entry point and navigation hub

**Responsibilities:**
- Load app configuration
- Create page navigation
- Display logo in sidebar
- Show Quick Stats in sidebar
- Manage page routing

**Key Code:**
```python
# Load config
config = json.load(open("config/app_config.json"))

# Create pages
pages = [st.Page(...) for page in config["pages"]]

# Show sidebar stats
github_stats = get_github_stats()
total_skills = get_total_skills()

# Navigate
pg = st.navigation(...)
pg.run()
```

### 2. views/ (Page Components)

#### about_me.py
- Profile section (static)
- Beliefs section (static)
- Achievements section (static)
- Fun Facts section (dynamic - fragment)

#### skills.py
- Skills organized by category
- Lottie animations
- Skill levels

#### projects.py
- Project showcase
- Tech stacks
- Project links

#### contact.py
- Contact form
- Contact methods
- Form validation

#### work_experience.py
- Experience timeline
- Career history
- Resume links

### 3. utils.py (Utilities)

**Key Functions:**

```python
@st.cache_data
def get_github_stats():
    """GitHub repos count"""
    # Returns: {"total_repos": X, "repos_this_year": Y}

@st.cache_data
def get_github_contributions():
    """GitHub contributions"""
    # Returns: {"total_contributions": X, "contributions_this_year": Y}

@st.cache_data
def get_total_skills():
    """Count skills from config"""
    # Returns: Total skill count
```

### 4. Configuration Layer

Each view has a corresponding JSON config:
- Centralized content management
- No code changes needed for updates
- Easy to maintain and scale

---

## Performance Optimizations

### 1. Caching Strategy
```python
@st.cache_data  # Cache based on function args
def expensive_function():
    # First call: Execute
    # Next calls: Return cached result
    pass
```

**Benefits:**
- Eliminates repeated API calls
- First load: 2-3 seconds (API call)
- Cached loads: < 0.1 seconds
- Session-based caching

### 2. Fragment Pattern (Async Loading)
```python
@st.fragment
def background_section():
    # Loads independently
    # Doesn't block main page
    pass

# Main page renders
display_static_content()

# Fragment runs in background
background_section()
```

**Benefits:**
- Static content visible instantly (< 0.5s)
- Dynamic content loads in background
- Page interactive while loading
- Progressive enhancement

### 3. Configuration-Driven Design
```python
# Load once, use everywhere
config = json.load(open("config.json"))

# No hardcoded data
# Easy to update
# Scales well
```

**Benefits:**
- Reduced code duplication
- Single source of truth
- Easy maintenance
- Quick updates

---

## Error Handling

### Try-Catch Pattern
```python
try:
    data = get_github_stats()
    display_metrics(data)
except Exception as e:
    show_fallback_ui()
    log_error(e)
```

**Benefits:**
- Graceful degradation
- User sees something meaningful
- Page doesn't crash
- Errors logged for debugging

### Fallback UI
- Shows "N/A" or "Loading..." if API fails
- Static content always visible
- Page remains functional
- Error message shown

---

## Deployment Considerations

### Environment Setup
```bash
# Python environment
python -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### Configuration
- GitHub API token (in utils.py)
- Webhook URL (in config/contact_config.json)
- Asset paths (in view configs)

### Performance
- Initial load: ~3 seconds
- Cached loads: < 1 second
- Mobile 3G: ~2-5 seconds

---

## Scalability

### Adding New Pages
1. Create `views/new_page.py`
2. Add to `config/app_config.json`
3. Create corresponding config JSON
4. Page automatically added to navigation

### Adding New Sections
1. Use `@st.fragment` for async loading
2. Add to appropriate config
3. Load data dynamically
4. Implement error handling

### Extending Features
- Add more GitHub API calls (cached)
- Add more skill categories
- Expand project showcase
- More contact methods

---

## Technology Stack

- **Frontend:** Streamlit
- **Animations:** Streamlit Lottie
- **API Calls:** Requests library
- **Configuration:** JSON
- **Caching:** Streamlit cache system
- **Styling:** HTML/CSS in Streamlit

---

## Best Practices Implemented

✅ Configuration-driven design  
✅ Cache optimization  
✅ Fragment pattern (async)  
✅ Error handling  
✅ Code organization  
✅ DRY principle  
✅ Separation of concerns  
✅ Progressive enhancement  

---

**Last Updated:** November 15, 2025
