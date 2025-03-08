function processContent() {
    const content = document.getElementById("inputField").innerHTML;
    fetch("/api/v1/process_requirements", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({content: content})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const resultsDiv = document.getElementById("results");
        renderEvaluationTable(data, resultsDiv);
        resultsDiv.style.display = "block";
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function renderEvaluationTable(data, resultsDiv) {
    resultsDiv.innerHTML = "";
    const table = document.createElement("table");
    table.className = "table table-dark table-striped table-bordered";
    table.innerHTML = `
        <thead>
            <tr>
                <th colspan="2" class="bg-primary text-white">User Story Evaluation</th>
            </tr>
        </thead>
        <tbody>
            ${Object.entries(data.evaluation).map(([key, value]) => `
                <tr>
                    <td class="text-capitalize">${key.replace("_", " ")}</td>
                    <td>
                        <strong>Score:</strong> ${value.score}<br>
                        <strong>Feedback:</strong> ${value.feedback}
                    </td>
                </tr>
            `).join('')}
            <tr>
                <td><strong>Overall Score</strong></td>
                <td>${data.overall_score}</td>
            </tr>
            <tr>
                <td><strong>Total Score</strong></td>
                <td>${data.total_score}</td>
            </tr>
            <tr>
                <td colspan="2"><strong>Summary:</strong><br> ${formatMarkdown(data.summary)}</td>
            </tr>
            <tr>
                <td colspan="2"><h2>Suggested Story Content</h2> ${formatMarkdown(jsonToMarkdown(data.suggested_user_story))}</td>
            </tr>
        </tbody>
    `;
    resultsDiv.appendChild(table);

    // Call the function after rendering the evaluation table
    appendSendToJiraButton(resultsDiv, data.suggested_user_story);
}

function appendSendToJiraButton(resultsDiv, jsonObject) {
    const button = document.createElement("button");
    button.className = "btn btn-secondary mt-3";
    button.textContent = "Send to Jira";
    button.onclick = function() { sendToJira(jsonObject) };
    resultsDiv.appendChild(button);
}

async function sendToJira(jsonObject) {
    const response = await fetch('/api/v1/send_to_jira', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonObject)
    });
    const data = await response.json();
    console.log(data);
    renderModal(`Jira Issue`, `The issue ${data.key} was successfully created!`);
}

function formatMarkdown(text) {
    text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    text = text.replace(/\n/g, "<br>");
    return text;
}

function jsonToMarkdown(jsonObject) {
    const presentationSchema = {
        title: "**Title**: {title}",
        description: "**Description**:\n{description}",
    };

    const markdown = Object.entries(presentationSchema).map(([key, value]) => {
        return value.replace(/{([^}]+)}/g, (match, p1) => {
            return jsonObject[p1];
        });
    }).join("\n\n");
    return markdown;
}

