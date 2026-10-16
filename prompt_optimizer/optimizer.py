
def check_component(prompt, keywords):
    prompt_lower = prompt.lower()
    return any(keyword in prompt_lower for keyword in keywords)


def optimize_prompt(prompt):

    role_keywords = [
        "act as", "you are", "role", "expert",
        "specialist", "teacher", "developer", "consultant"
    ]

    context_keywords = [
        "for a beginner", "for students", "for college students",
        "for professionals", "audience", "background",
        "context", "assuming", "beginner", "student"
    ]

    task_keywords = [
        "explain", "write", "create", "generate",
        "summarize", "compare", "analyze", "design",
        "develop", "list", "describe", "calculate",
        "suggest", "provide", "tell", "give"
    ]

    format_keywords = [
        "bullet points", "bullets", "table", "steps",
        "headings", "format", "json", "paragraph",
        "numbered list", "numbered"
    ]

    constraint_keywords = [
        "within", "under", "maximum", "max", "limit",
        "concise", "short", "simple", "avoid",
        "include", "do not", "don't", "only",
        "less than", "at least"
    ]

    components = {
        "Role / Persona": check_component(prompt, role_keywords),
        "Context / Audience": check_component(prompt, context_keywords),
        "Clear Task": check_component(prompt, task_keywords),
        "Output Format": check_component(prompt, format_keywords),
        "Constraints": check_component(prompt, constraint_keywords)
    }

    weights = {
        "Role / Persona": 15,
        "Context / Audience": 20,
        "Clear Task": 30,
        "Output Format": 15,
        "Constraints": 20
    }

    score = 0

    for component, present in components.items():
        if present:
            score += weights[component]

    words = prompt.split()

    if len(words) >= 3:
        score += 15

    if len(words) >= 6:
        score += 5

    score = min(score, 100)

    if score >= 85:
        level = "Excellent"
    elif score >= 75:
        level = "Very Good"
    elif score >= 60:
        level = "Good"
    elif score >= 40:
        level = "Needs Improvement"
    else:
        level = "Needs Major Improvement"

    missing = [
        name for name, present in components.items()
        if not present
    ]

    optimized = prompt.strip()

    if not components["Role / Persona"]:
        optimized = "Act as an expert assistant. " + optimized

    if not components["Context / Audience"]:
        optimized += (
            "\n\nProvide the explanation in a clear and "
            "beginner-friendly way."
        )

    if not components["Output Format"]:
        optimized += (
            "\n\nUse clear headings and bullet points "
            "where appropriate."
        )

    if not components["Constraints"]:
        optimized += (
            "\n\nKeep the response concise, accurate, "
            "practical, and focused."
        )

    return {
        "original": prompt,
        "optimized": optimized,
        "score": score,
        "level": level,
        "components": components,
        "missing": missing,
        "before_words": len(prompt.split()),
        "after_words": len(optimized.split())
    }
