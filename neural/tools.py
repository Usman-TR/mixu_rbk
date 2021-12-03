from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json
import moviepy.editor as mp
import librosa
import soundfile as sf


path_to_model = "./neural/model"
model = Model(path_to_model)

def transcribe(path_to_filename):
    SetLogLevel(-1)
    wf = wave.open(path_to_filename, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        return -1

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    output = []
    output_with_time = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            data_json = json.loads(str(rec.Result()))
            output.append(data_json.get('text'))
            if data_json.get('result'):
                output_with_time.extend(data_json.get('result'))
        else:
            pass
    output = { 'transcript': ''.join(map(str, output)), 'text_with_timestamps': output_with_time }
    return output


def video_to_audio(videoFile):
    video_clip = mp.VideoFileClip(videoFile)
    video_clip.audio.write_audiofile(str(videoFile) + ".wav")


def convert_khz(audioFile):
    y, sr = librosa.load(audioFile, sr=16000)
    sf.write(audioFile, y, sr)

def create_audio(mp4_file):
    video_to_audio(mp4_file)
    convert_khz(str(mp4_file) + ".wav")
    return str(mp4_file) + ".wav"
