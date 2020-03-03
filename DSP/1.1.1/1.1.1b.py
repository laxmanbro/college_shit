import librosa   
y, s = librosa.load('speech.wav', sr=32000/4) # Downsample 32kHz to 8kHz
librosa.output.write_wav('output_speech.wav', y, s)