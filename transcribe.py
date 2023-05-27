from torch import ExcludeDispatchKeyGuard
from datetime import timedelta
import os
import whisper

model = whisper.load_model("large") # Change this to your desired model (large)
print("Whisper model loaded.")

def transcribe_audio(file_path):
    transcribe = model.transcribe(audio=file_path,
                                  verbose=True,
                                  patience=2,
                                  beam_size=5,
                                  language="Hindi",
                                  task='translate')
    segments = transcribe['segments']

    output_file_name = file_path.split(".")[:-1]
    output_file_name = '.'.join(output_file_name)
    srtFilename = f"{output_file_name}.srt"
    print(srtFilename)
    
    with open(srtFilename, 'w', encoding='utf-8') as srtFile:
      pass

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        print(text)
        segmentId = segment['id']+1
        try:
          segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
        except IndexError:
          segment = f"{segmentId}\n{startTime} --> {endTime}\n{text}\n\n"

        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename

file = input("input file name")
print("Currently transcribing:", file)
print(transcribe_audio(file))
print("__________________________________________")
