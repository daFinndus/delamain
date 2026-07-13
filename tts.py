import sounddevice
import numpy

from piper.voice import PiperVoice
from piper.config import SynthesisConfig

class Piper():
    def __init__(self, volume: float, speed: float) -> None:
        self.amy = "./voices/amy.onnx"
        self.norman = "./voices/norman.onnx"

        # The higher the volume, the louder the voice.
        # The lower the speed, the faster the voice.
        self.syn_config = SynthesisConfig(
            volume=volume,
            length_scale=speed
        )

        self.voice = PiperVoice.load(self.amy)
        self.sample_rate = self.voice.config.sample_rate

    def speak(self, message: str) -> None:
        stream = sounddevice.OutputStream(
            samplerate = self.sample_rate,
            channels = 1,
            dtype = "int16",
        )

        stream.start()

        for audio_chunk in self.voice.synthesize(message, syn_config=self.syn_config):
            stream.write(numpy.frombuffer(audio_chunk.audio_int16_bytes, dtype=numpy.int16))
        stream.stop()
        stream.close()
