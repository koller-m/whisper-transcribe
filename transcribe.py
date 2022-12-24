import os
import whisper

# Load the model
model = whisper.load_model("tiny")

# Set the input and output directories
input_dir = "/path/to/input/dir"
output_dir = "/path/to/output/dir"

for file in os.listdir(input_dir):
    # Check if the file is a mp3
    if file.endswith(".mp3"):
        # Transcribe the audio file
        # fp16=False & language="English" optional
        result = model.transcribe(os.path.join(input_dir, file), fp16=False, language="English")

        # Extract the transcription
        transcription = result["text"]

        # Write the transcription to a .txt file in the output dir
        with open(os.path.join(output_dir, file.replace(".mp3", ".txt")), "w") as f:
            f.write(transcription)