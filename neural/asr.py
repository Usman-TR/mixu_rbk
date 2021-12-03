#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json



def transcribe(path_to_filename):
    SetLogLevel(-1)
    wf = wave.open(path_to_filename, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        return -1

    model = Model('./model')
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    output = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            data_json = json.loads(str(rec.Result()))
            #print(data_json['text'])
            output.append(data_json['text'])
        else:
            pass
            #print(rec.PartialResult())
    return output
    #print(rec.FinalResult())
