import pyaudio
import wave

def nauhoitus(pituus, tiedosto, polku):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 # aikaisemmin oli 2 mutta ei toiminut :D eli mono vs stereo?
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = pituus # valmiin pituuden sijaan voisi olla kunnes ihminen painaa nappia taas? ja muutenkin pitää printtaa ohjeet mitä tehdä :D
    
    WAVE_OUTPUT_FILENAME = polku + "/" + tiedosto + ".wav"
     
    audio = pyaudio.PyAudio()


    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("Nauhoitus kaynnissa")
    frames = []
     
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Nauhoitus paattyi")
     
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
     
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return WAVE_OUTPUT_FILENAME
