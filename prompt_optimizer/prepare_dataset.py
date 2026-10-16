
import pandas as pd

# Change this to the actual downloaded CSV filename
df = pd.read_csv("prompt-refinement-dataset.csv")

print("Available columns:", df.columns.tolist())

# Convert the dataset into the format used by our project
if "input" in df.columns and "output" in df.columns:
    project_df = pd.DataFrame({
        "prompt": df["input"],
        "category": "Prompt Refinement",
        "optimized_prompt": df["output"]
    })

elif "prompt" in df.columns and "optimized_prompt" in df.columns:
    project_df = pd.DataFrame({
        "prompt": df["prompt"],
        "category": "Prompt Refinement",
        "optimized_prompt": df["optimized_prompt"]
    })

else:
    print("Dataset columns do not match the expected format.")
    print("Please check the columns printed above.")
    raise SystemExit

# Remove empty rows and duplicate original prompts
project_df = project_df.dropna(subset=["prompt"])
project_df = project_df.drop_duplicates(subset=["prompt"])

project_df.to_csv("prompt_dataset.csv", index=False)

print("Dataset prepared successfully!")
print("Total prompts:", len(project_df))
print("Saved as prompt_dataset.csv")
