PROMPTS = {
    "ANALYSIS_PROMPT" : """
        Analyze the following user story for quality and adherence to best practices. Evaluate it based on clarity, completeness, testability, feasibility, relevance, and acceptance criteria. Provide a structured assessment, scoring each criterion from 1 (Poor) to 5 (Excellent) based on the defined evaluation system. Include a summary of strengths and weaknesses and suggest improvements.

        **User Story:**
        [[USER_STORY]]

        **Evaluation Criteria:**
        - **Clarity**: Is the story written in a way that is easy to understand?
        - **Completeness**: Does it contain all necessary details, including who, what, and why?
        - **Testability**: Can the story be easily tested based on the given description?
        - **Feasibility**: Is the implementation realistic given known constraints?
        - **Relevance**: Does the story align with business goals and user needs?
        - **Acceptance Criteria**: Are acceptance criteria well-defined and actionable?

        Provide constructive feedback for each criterion and suggest improvements where applicable.

        Return the analysis following the JSON schema below:
        [[JSON_SCHEMA]]
    """,

    "ENHANCE_USER_STORY_PROMPT" : """
        Objective: To generate an enhanced and refined user story based on an original user story and a provided AI-generated analysis.

        Instructions:
        "You are an expert product development assistant tasked with refining user stories for clarity, completeness, and testability. You will receive two inputs:

        Original User Story: A user story provided by a user.
        AI-Generated Analysis: An analysis of the original user story, including potential issues, missing information, and suggested improvements.

        Your task is to generate an enhanced user story that addresses the identified issues and incorporates the suggested improvements. 

        The enhanced user story should:
        1. Be written in a clear, concise, and user-centered manner.
        2. Follow the standard user story format: "As a [user role], I want [goal/desire] so that [benefit/value]."
        3. Include specific and measurable acceptance criteria.
        4. Address any ambiguities or missing information identified in the analysis.
        5. Improve the overall clarity and testability of the user story.
        6. Maintain the original intent of the user story while enriching it with the analysis data.

        Here are the inputs:

        Original User Story:
        [[USER_STORY]]

        AI-Generated Analysis:
        [[ANALYSIS]]

        The enhanced user story must be provided using the following JSON schema:
        [[ENHANCED_STORY_JSON_SCHEMA]]
    """,

    "ENHANCED_STORY_JSON_SCHEMA" : """
        {
            "title" : "{Enhanced title}",
            "description": "{Enhanced user story description}"
        }
    """,

    "JSON_SCHEMA" : """
        {
            "evaluation": {
                "clarity": {
                "score": 0,
                "feedback": "{Feedback on clarity}"
                },
                "completeness": {
                "score": 0,
                "feedback": "{Feedback on completeness}"
                },
                "testability": {
                "score": 0,
                "feedback": "{Feedback on testability}"
                },
                "feasibility": {
                "score": 0,
                "feedback": "{Feedback on feasibility}"
                },
                "relevance": {
                "score": 0,
                "feedback": "{Feedback on relevance}"
                },
                "acceptance_criteria": {
                "score": 0,
                "feedback": "{Feedback on acceptance criteria}"
                }
            },
            "overall_score": 0,
            "total_score": 0,
            "summary": "{General summary of strengths, weaknesses, and suggested improvements}"
        }
    """
}
