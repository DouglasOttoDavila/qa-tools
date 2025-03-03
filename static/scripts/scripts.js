function expandSidebar(sidebar, sidebarContent, arrow, sidebarLogo) {
    if (sidebarContent.style.width === "0px") {
        sidebarContent.style.width = "250px";
        sidebar.style.width = "280px";
        arrow.innerHTML = "&#9664;";
        sidebarContent.style.display = "block"; // Show content when expanded
        sidebarLogo.style.display = "flex";
    } else {
        sidebarContent.style.width = "0px";
        sidebar.style.width = "30px";
        arrow.innerHTML = "&#9654;";
        sidebarContent.style.display = "none"; // Hide content when collapsed
        sidebarLogo.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const sidebarLogo = document.getElementById("logo_sidebar");
    const sidebar = document.getElementById("sidebar");
    const sidebarContent = document.getElementById("sidebar-content");
    const toggleSidebar = document.getElementById("toggle-sidebar");
    const arrow = toggleSidebar.querySelector("span");

    sidebarContent.style.width = "250px";
    sidebar.style.width = "280px";
    sidebarContent.style.overflow = "visible"; // Ensure content is visible initially

    toggleSidebar.addEventListener("click", function() {
        expandSidebar(sidebar, sidebarContent, arrow, sidebarLogo);
    });
});

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
        //document.getElementById("results").innerHTML = marked.parse(`<strong>Analyzed Content:</strong><br>${data.response}`);
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
                <td colspan="2"><strong>Summary:</strong> ${formatMarkdown(data.summary)}</td>
            </tr>
            <tr>
                <td colspan="2"><h2>Suggested Story Content</h2> ${formatMarkdown(data.suggested_user_story)}</td>
            </tr>
        </tbody>
    `;
    resultsDiv.appendChild(table);
}

function formatMarkdown(text) {
    text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    text = text.replace(/\n/g, "<br>");
    return text;
}