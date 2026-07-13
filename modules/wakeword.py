import sounddevice
import numpy

from openwakeword.model import Model


class Waker:
    def __init__(self, wakeword_models: list[str], threshold: float = 0.5, vad_threshold: float = 0.5):
        self.model = Model(
            wakeword_models=wakeword_models,
            vad_threshold=vad_threshold,  # gates false positives via Silero VAD
        )

        self.threshold = threshold
        self.sample_rate = 16000
        self.chunk_size = 1280  # ~80ms frames, openWakeWord's expected chunk size

    def listen(self, on_detected):
        def callback(indata, frames, time, status):
            audio_chunk = indata[:, 0]
            prediction = self.model.predict(audio_chunk)



        with sounddevice.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size,
            callback=callback,
        ):

            print("Listening for wake word...")
            while True:
                sounddevice.sleep(100)
