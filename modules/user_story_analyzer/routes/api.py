from flask import Blueprint, jsonify, request
from configuration.config import API_PREFIX, JIRA_LINK, DUMMY_ANALYSIS
from services.gemini_sdk import get_gemini_response
from helpers.general_helpers import replace_placeholders, get_dynamic_values
from services.atlassian_sdk import get_jira_issue, create_jira_issue

rr_api = Blueprint("rr_api", __name__)

@rr_api.route(API_PREFIX + "send_to_jira", methods=["POST"])
def send_to_jira():
    data = request.json
    if JIRA_LINK:
        issue = create_jira_issue(data["title"], data["description"])
        print(issue)
        return jsonify(issue)
    else:
        return jsonify({"response": "Not sending to Jira in local mode", "key" : "n/a"})


@rr_api.route(API_PREFIX + "process_requirements", methods=["POST"])
def process_requirements():
    if DUMMY_ANALYSIS :
        story_analysis = {'evaluation': {'clarity': {'score': 4, 'feedback': "The story is generally clear and easy to understand. The persona (user) and the desired functionality (seeing the temperature) are well-defined. The 'so that' clause clarifies the user's motivation. However, the story could benefit from explicitly stating where the temperature is being displayed beyond just 'main screen'. For example, which application or device main screen?"}, 'completeness': {'score': 4, 'feedback': 'The story covers the core requirements, including who (user), what (see temperature), and why (decide what to wear). It also touches upon important considerations like units and accuracy. However, it misses defining the data source. Where is the temperature data coming from? This is a critical element for a complete understanding.'}, 'testability': {'score': 5, 'feedback': 'The acceptance criteria are well-defined and make the story highly testable. Each criterion provides clear instructions on how to verify the functionality. Accuracy, update frequency, error handling, and visual clarity are all addressed in a way that can be directly translated into test cases.'}, 'feasibility': {'score': 4, 'feedback': "Displaying the temperature based on a user's location is generally feasible using readily available APIs and location services. The accuracy requirement of +/- 2 degrees is also achievable. However, 'network issues' causing temperature retrieval failure needs more specification; what type of network issue, and is there any tolerance for failure? Define appropriate retry logic or cache strategy."}, 'relevance': {'score': 5, 'feedback': 'The story is highly relevant. Providing users with the current temperature to help them decide what to wear directly addresses a common and practical need. It aligns well with user-centric design principles.'}, 'acceptance_criteria': {'score': 5, 'feedback': 'The acceptance criteria are comprehensive and well-written. They cover essential aspects of the functionality, including units, accuracy, update frequency, error handling, visual presentation, and location awareness. They provide a solid foundation for development and testing.'}}, 'overall_score': 4.5, 'total_score': 27, 'summary': "The user story is well-written and addresses a relevant user need. Its strengths lie in its clarity, testability, and relevance, as well as the comprehensive acceptance criteria. The main weaknesses are the lack of specific details regarding the data source for the temperature and the absence of information regarding the exact 'main screen'. Addressing these omissions will further improve the story's completeness and clarity. Specifying retry logic or a cache strategy if the temperature cannot be retrieved would be beneficial. Defining which 'main screen' the temperature is to be displayed on will improve clarity. Overall, it's a solid user story that requires minor refinements.", 'suggested_user_story': {'title': 'Display Current Temperature on Mobile App Dashboard', 'description': 'As a user, I want to see the current temperature displayed on the dashboard of the mobile application, using my current location, so that I can quickly decide what to wear before leaving the house.\n\nAcceptance Criteria:\n* AC1: The current temperature should be displayed in degrees Fahrenheit or Celsius, based on the user\'s preference setting in the app.\n* AC2: The displayed temperature should be accurate to within +/- 2 degrees Fahrenheit of the temperature reported by the configured weather data source (e.g., AccuWeather API).\n* AC3: The temperature should be updated at least every 15 minutes while the app is in the foreground.\n* AC4: The display should clearly indicate the units of temperature (e.g., "°F" or "°C").\n* AC5: If the temperature cannot be retrieved from the weather data source due to network connectivity issues or API errors, an error message "Unable to retrieve temperature. Please check your internet connection or try again later." should be displayed.\n* AC6: The temperature display should be visually clear and easily readable, with a font size of at least 24 points and sufficient contrast against the background.\n* AC7: The temperature should be based on the user\'s current location, as determined by the device\'s location services (with appropriate user permissions granted).\n* AC8: If the location services are unavailable or permissions are denied, the application should prompt the user to enable location services or enter a default location manually.\n* AC9: The application should attempt to retrieve the temperature a maximum of 3 times with a 5-second interval between retries if the initial retrieval fails. If all retries fail, display AC5 error message.'}}
        print("\n\nResponse:\n", story_analysis)
    else:
        data = request.json
        content = data.get("content")
        json_schema = get_dynamic_values("/ai_context", "JSON_SCHEMA", "dev")
        prompt = get_dynamic_values("/ai_context", "ANALYSIS_PROMPT", "dev")
        enhanced_story_json_schema = get_dynamic_values("/ai_context", "ENHANCED_STORY_JSON_SCHEMA", "dev")
        
        updated_prompt = replace_placeholders(
            original_content = prompt, 
            placeholders = [
                "[[USER_STORY]]",
                "[[JSON_SCHEMA]]"
            ], 
            replacements = [content,json_schema]
        )
        print("\n\nPrompt:\n", updated_prompt)

        story_analysis = get_gemini_response(updated_prompt)

        enhanced_story_prompt = get_dynamic_values("/ai_context", "ENHANCE_USER_STORY_PROMPT", "dev") 
        
        updated_enhanced_story_prompt = replace_placeholders(
            original_content = enhanced_story_prompt, 
            placeholders = [
                "[[USER_STORY]]", 
                "[[ANALYSIS]]", 
                "[[ENHANCED_STORY_JSON_SCHEMA]]"
            ], 
            replacements = [content, story_analysis, enhanced_story_json_schema]
        )
        print("\n\nEnhanced Story Prompt:\n", updated_enhanced_story_prompt)

        suggested_story = get_gemini_response(updated_enhanced_story_prompt)

        story_analysis["suggested_user_story"] = suggested_story
        print("\n\nResponse:\n", story_analysis)
    
    return jsonify(story_analysis)