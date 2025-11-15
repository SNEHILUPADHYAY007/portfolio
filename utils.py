import requests
from datetime import datetime
import streamlit as st
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub API URLs
REST_API_URL = "https://api.github.com"
GRAPHQL_API_URL = "https://api.github.com/graphql"

# Get GitHub credentials from environment variables
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "SNEHILUPADHYAY007")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Function to get total skills count
@st.cache_data
def get_total_skills():
    """Count total number of skills from skills config"""
    try:
        config_path = os.path.join(os.path.dirname(__file__), "config", "skills_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        total_skills = 0
        for section in config.get("skills", {}).values():
            total_skills += len(section.get("skills", []))
        
        return total_skills
    except Exception as e:
        return 0

# Function to fetch GitHub user repos and stats
@st.cache_data
def get_github_stats(username: str = None, token: str = None):
    """
    Fetch public GitHub repositories and stats for a given username.

    Args:
        username (str): GitHub username (defaults to GITHUB_USERNAME env var)
        token (str): GitHub Personal Access Token (defaults to GITHUB_TOKEN env var)

    Returns:
        dict: Dictionary with repo stats
    """
    # Use environment variables if not provided
    username = username or GITHUB_USERNAME
    token = token or GITHUB_TOKEN
    
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"} if token else {}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        st.error(f"Error fetching repos: {response.status_code}")
        return {}

    repos = response.json()
    total_repos = len(repos)

    # Current year
    this_year = datetime.now().year
    repos_this_year = sum(
        1 for repo in repos if datetime.fromisoformat(repo["created_at"][:-1]).year == this_year
    )

    return {
        "total_repos": total_repos,
        "repos_this_year": repos_this_year
    }

@st.cache_data
def get_github_contributions(username: str = None, token: str = None):
    """
    Fetch total contributions (all years) and contributions for the current year.

    Args:
        username (str): GitHub username (defaults to GITHUB_USERNAME env var)
        token (str): GitHub Personal Access Token (defaults to GITHUB_TOKEN env var)

    Returns:
        dict: Dictionary with total_contributions and contributions_this_year
    """
    # Use environment variables if not provided
    username = username or GITHUB_USERNAME
    token = token or GITHUB_TOKEN

    if not username or not token:
        st.warning("GitHub token not configured. Public data will be displayed without higher rate limits.")
        return {
            "total_contributions": 0,
            "contributions_this_year": 0
        }

    headers = {"Authorization": f"Bearer {token}"}
    query = """
    query($username:String!, $from:DateTime!, $to:DateTime!) {
      user(login: $username) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """

    def run_query(from_date, to_date):
        variables = {"username": username, "from": from_date, "to": to_date}
        res = requests.post(GRAPHQL_API_URL, json={"query": query, "variables": variables}, headers=headers)
        data = res.json()

        if "errors" in data:
            raise Exception(f"GitHub API Error: {data['errors']}")

        return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

    # Contributions this year
    this_year = datetime.now().year
    from_this_year = f"{this_year}-01-01T00:00:00Z"
    to_this_year = f"{this_year}-12-31T23:59:59Z"
    contributions_this_year = run_query(from_this_year, to_this_year)

    # All-time contributions (loop year by year)
    total_contributions = 0
    current_year = datetime.now().year
    for year in range(2008, current_year + 1):
        from_date = f"{year}-01-01T00:00:00Z"
        to_date = f"{year}-12-31T23:59:59Z"
        total_contributions += run_query(from_date, to_date)

    return {
        "total_contributions": total_contributions,
        "contributions_this_year": contributions_this_year
    }
