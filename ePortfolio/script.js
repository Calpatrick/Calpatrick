// About Modal Logic
document.addEventListener("DOMContentLoaded", () => {
    const aboutModal = document.querySelector("#about-modal");
    const aboutBtn = document.querySelector("#about-btn");
    const closeBtn = document.querySelector(".close-btn");

    // Show Modal
    if (aboutBtn) {
        aboutBtn.addEventListener("click", () => {
            aboutModal.style.display = "block";
        });
    }

    // Hide Modal
    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            aboutModal.style.display = "none";
        });
    }

    // Close Modal on Outside Click
    window.addEventListener("click", (e) => {
        if (e.target === aboutModal) {
            aboutModal.style.display = "none";
        }
    });

    // Form Validation
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", (e) => {
            const name = document.querySelector("#name").value.trim();
            const email = document.querySelector("#email").value.trim();
            const message = document.querySelector("#message").value.trim();

            if (!name || !email || !message) {
                e.preventDefault();
                alert("Please fill in all fields before submitting.");
            }
        });
    }
});
