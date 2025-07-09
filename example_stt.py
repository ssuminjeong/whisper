import whisper
import torch

model = whisper.load_model("medium")  # small, medium, large 도 가능
result = model.transcribe("iusong.mp4", language="ko")

print("-------------------------------")
print(result["text"])
