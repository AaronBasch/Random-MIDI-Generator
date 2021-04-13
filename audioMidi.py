# find the BPM
# find the time signature
# find the start time
# make assumption that significant part of song is 16 bars in.
# take bars 16-24 as melody section.

# convert audio to midi
# make assumption that highest melody line is the lead melody
# this is our melody

import librosa
import soundfile as sf

testPath = "/MY_FILES/Code/MachineListening/Group Project/Random-MIDI-Generator/testAudio/bleat.wav"
destPath = "/MY_FILES/Code/MachineListening/Group Project/Random-MIDI-Generator/testAudio/bleatCHORUS.wav"

y,sr = librosa.load(testPath, 48000)

BPM = librosa.beat.beat_track(y=y, sr=sr)

length = int(round((3840.0/BPM[0])*sr))

startSample = length
endSample = startSample+length

y = y[startSample:endSample]

sf.write(destPath, y, sr)

# fails
