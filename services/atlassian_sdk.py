import os, requests, html2text
from atlassian import Jira
from atlassian import Confluence
from dotenv import load_dotenv
from helpers.general_helpers import html_to_markdown
from modules.user_story_analyzer.config.configuration import JIRA_ISSUE_TYPE, JIRA_PROJECT_KEY

load_dotenv()

jira = Jira(
    url=os.getenv('JIRA_URL'), 
    username=os.getenv('JIRA_USER'),
    password = os.getenv('JIRA_TOKEN')
)

confluence = Confluence(
    url=os.getenv('JIRA_URL'), 
    username=os.getenv('JIRA_USER'),
    password = os.getenv('JIRA_TOKEN')
)


def create_jira_issue(issue_title: str, issue_description: str):
    try:
        fields = dict(summary=issue_title, project = dict(key=JIRA_PROJECT_KEY), issuetype = dict(name=JIRA_ISSUE_TYPE), description=issue_description) 
        return jira.issue_create(fields=fields)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Text: {e.response.text}")
        return None

def get_jira_issue(issue_key: str) -> dict:
    try:
        issue = jira.issue(issue_key)
        return issue
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Text: {e.response.text}")
        return None


def get_confluence_page(page_title: str):
    try:
        page_id = confluence.get_page_id("~71202094efd024e26d4d63b8f43d0eb2da7706", page_title)
        page_full = confluence.get_page_by_id(page_id, expand="body.view", status=None, version=None)
        page_text = html_to_markdown(page_full["body"]["view"]["value"])
        return page_text
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Text: {e.response.text}")
        return None