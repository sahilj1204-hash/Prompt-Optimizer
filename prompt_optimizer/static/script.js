const promptInput = document.getElementById("promptInput");
const optimizeBtn = document.getElementById("optimizeBtn");
const charCount = document.getElementById("charCount");

const loading = document.getElementById("loading");
const results = document.getElementById("results");

const score = document.getElementById("score");
const level = document.getElementById("level");
const missing = document.getElementById("missing");

const originalPrompt = document.getElementById("originalPrompt");
const optimizedPrompt = document.getElementById("optimizedPrompt");

const beforeWords = document.getElementById("beforeWords");
const afterWords = document.getElementById("afterWords");

const copyBtn = document.getElementById("copyBtn");


promptInput.addEventListener("input", function () {

    charCount.textContent =
        `${promptInput.value.length} characters`;

});


document.querySelectorAll(".sample").forEach(button => {

    button.addEventListener("click", function () {

        promptInput.value = this.dataset.prompt;

        charCount.textContent =
            `${promptInput.value.length} characters`;

        promptInput.focus();

    });

});


optimizeBtn.addEventListener("click", async function () {

    const prompt = promptInput.value.trim();

    if (!prompt) {

        alert("Please enter a prompt first.");

        return;

    }


    loading.style.display = "block";
    results.style.display = "none";

    optimizeBtn.disabled = true;
    optimizeBtn.textContent = "Optimizing...";


    try {

        const response = await fetch("/optimize", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                prompt: prompt
            })

        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Something went wrong."
            );

        }


        score.textContent = data.score;

        level.textContent = data.level;


        if (data.missing.length === 0) {

            missing.textContent =
                "All important components are present.";

        } else {

            missing.textContent =
                data.missing.join(" • ");

        }


        originalPrompt.textContent =
            data.original;

        optimizedPrompt.textContent =
            data.optimized;


        beforeWords.textContent =
            `${data.before_words} words`;

        afterWords.textContent =
            `${data.after_words} words`;


        results.style.display = "block";


        results.scrollIntoView({
            behavior: "smooth"
        });


    } catch (error) {

        alert(error.message);

    }


    loading.style.display = "none";

    optimizeBtn.disabled = false;

    optimizeBtn.textContent =
        "Optimize Prompt ✨";

});


copyBtn.addEventListener("click", async function () {

    const text = optimizedPrompt.textContent;

    await navigator.clipboard.writeText(text);

    copyBtn.textContent = "Copied ✓";

    setTimeout(() => {

        copyBtn.textContent = "Copy";

    }, 1500);

});