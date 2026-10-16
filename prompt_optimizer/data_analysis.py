import pandas as pd
from optimizer import optimize_prompt


df = pd.read_csv("prompt_dataset.csv")

results = []

for _, row in df.iterrows():

    result = optimize_prompt(row["prompt"])

    results.append({
        "prompt": row["prompt"],
        "category": row["category"],
        "original_score": result["score"],
        "before_words": result["before_words"],
        "after_words": result["after_words"],
        "missing_components": len(result["missing"])
    })


results_df = pd.DataFrame(results)

results_df.to_csv("analysis_results.csv", index=False)

print("\n===== PROMPT DATASET ANALYSIS =====")

print("Number of prompts:", len(results_df))

print(
    "Average original score:",
    round(results_df["original_score"].mean(), 2)
)

print(
    "Average original word count:",
    round(results_df["before_words"].mean(), 2)
)

print(
    "Average optimized word count:",
    round(results_df["after_words"].mean(), 2)
)

print(
    "Average missing components:",
    round(results_df["missing_components"].mean(), 2)
)

print("\nAverage score by category:")

print(
    results_df.groupby("category")["original_score"].mean()
)

print("\nAnalysis completed successfully!")

print("Created file: analysis_results.csv")