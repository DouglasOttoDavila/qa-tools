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

function renderModal(title, content) {
    let processedContent = content;
    const urlRegex = /(https?:\/\/[^\s]+)/g;
    processedContent = processedContent.replace(urlRegex, '<a href="$1" target="_blank">$1</a>');

    const modalHtml = `
        <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="myModalLabel">${title}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        ${processedContent}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHtml);

    const myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();

    document.getElementById('myModal').addEventListener('hidden.bs.modal', function (event) {
        document.getElementById('myModal').remove();
    });
}
