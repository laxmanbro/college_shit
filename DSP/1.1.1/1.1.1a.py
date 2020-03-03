import librosa   
y, s = librosa.load('audio.wav', sr=32000/4) # Downsample 32kHz to 8kHz
librosa.output.write_wav('output_audio.wav', y, s)
