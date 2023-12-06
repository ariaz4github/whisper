import whisper
import pyaudio
import wave

def record_audio(output_filename, record_seconds=5, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=44100):
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
    print(f"Recording for {record_seconds} seconds...")

    frames = []

    # Record for the desired number of seconds
    for i in range(0, int(rate / chunk_size * record_seconds)):
        data = stream.read(chunk_size)
        frames.append(data)

    # Stop recording
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

# Example usage
record_audio("output.wav", record_seconds=10)


model = whisper.load_model("base")
result = model.transcribe("output.wav")
print(result["text"])