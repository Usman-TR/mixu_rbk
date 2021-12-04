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

    model = Model('./model_ru')
    model_en = Model('./model_en')

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    rec_en = KaldiRecognizer(model_en, wf.getframerate())
    rec_en.SetWords(True)

    output = []
    timestamps_ru = []
    output_en = []
    timestamps_en = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            data_json = json.loads(str(rec.Result()))
            output.append(data_json['text'])
            if 'result' in data_json:
                timestamps_ru.extend(data_json['result'])

        if rec_en.AcceptWaveform(data):
            data_json = json.loads(str(rec_en.Result()))
            output_en.append(data_json['text'])
            if 'result' in data_json:
                timestamps_en.extend(data_json['result'])

    output = []
    for word in timestamps_ru:
        if word['conf'] < 0.9:
            en_word = find_better(timestamps_en, word['start'], word['conf'])
            if en_word:
                output.append(en_word)
            else:
                output.append(word)
        else:
            output.append(word)
    output = get_text_from_timestamps(output)

    return output

def find_better(timestamps, time, conf):
    for el in timestamps:
        if float(el['start']) >= float(time) and el['conf'] > conf:
            return el
    return False

def get_text_from_timestamps(timestamps):
    output = ''
    for part in timestamps:
        output += ' ' + part['word']
    return output
