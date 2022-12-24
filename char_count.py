import os

# OpenAI's Embeddings API has a max input of 8,192 tokens
# 37,000 characters is ~ 8,000 tokens
# Identify the files that have more than 37,000 characters

# Set the dir where the files are located
directory = "/path/to/directory"

# Create a new file of the character count
output_file = open("char_count.txt", "w")

# Go through each file and count the characters
for filename in os.listdir(directory):
    # Only count characters in .txt files
    if filename.endswith(".txt"):
        # Open file and read its contents
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            # Count the characters in the file
            num_chars = len(contents)
            # Only write if more than 37,000 characters
            if num_chars > 37000:
                output_file.write(f"{filename}: {num_chars}\n")

output_file.close()