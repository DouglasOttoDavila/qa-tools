import os, requests
from atlassian import Jira
from atlassian import Confluence
from dotenv import load_dotenv

load_dotenv()

jira = Jira(
    url=os.getenv('JIRA_URL'), 
    username=os.getenv('JIRA_USER'),
    password = os.getenv('JIRA_TOKEN')
)

# To be implemented SOON
#confluence = Confluence(server = os.environ['JIRA_URL'], basic_auth=(os.environ['JIRA_USER'], os.environ['JIRA_TOKEN']))

def create_jira_issue(issue_title: str, issue_description: str):
    try:
        fields = dict(summary=issue_title, project = dict(key='KAN'), issuetype = dict(name='Task'), description=issue_description) 
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

#issue = get_jira_issue("KAN-1")
#print(issue["fields"]["description"])