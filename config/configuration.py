JSON_MIMETYPE = "application/json" # Mimetype for JSON | Do not change
API_PREFIX = "/api/v1/" # Prefix for all API endpoints (If replaced, needs to be changed in static/scripts/user_story_analyzer/scripts.js)
MODE = "local" # "local" or "vault" | If "vault" will get secrets from Infisical (Needs Infisical credentials in .env file)
JIRA_LINK = False # Bool | If "True", will send to Jira (Needs Jira credentials in .env file)
DUMMY_ANALYSIS = False # Bool | If "True", will return dummy analysis (No Gemini process required)