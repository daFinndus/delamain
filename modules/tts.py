from pathlib import Path

import numpy
import sounddevice
from piper.config import SynthesisConfig
from piper.voice import PiperVoice


class Piper:
    def __init__(self, model: str, volume: float, speed: float) -> None:
        # The higher the volume, the louder the voice.
        # The lower the speed, the faster the voice.
        self.syn_config = SynthesisConfig(volume=volume, length_scale=speed)

        base_dir = Path(__file__).resolve().parent.parent
        model_path = base_dir / "models" / f"{model}.onnx"

        self.voice = PiperVoice.load(str(model_path))
        self.sample_rate = self.voice.config.sample_rate

    def speak(self, message: str) -> None:
        try:
            stream = sounddevice.OutputStream(
                samplerate=self.sample_rate,
                channels=1,
                dtype="int16",
            )

            stream.start()

            for audio_chunk in self.voice.synthesize(
                message, syn_config=self.syn_config
            ):
                stream.write(
                    numpy.frombuffer(audio_chunk.audio_int16_bytes, dtype=numpy.int16)
                )
            stream.stop()
            stream.close()
        except Exception as e:
            print(f"piper-tts failed: {e}")
