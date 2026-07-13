# Delamain - Local Voice Assistant

A local, self-hosted voice assistant for Linux (Hyprland setup), inspired by Siri 
and Google Assistant, built to trigger custom actions via voice on the local machine.

No cloud dependency for the core pipeline.

## Description

The assistant runs as a background service, continuously listening for a wake word.
Once triggered, it records the following utterance, transcribes it locally, and
matches the transcribed text against a configurable set of actions. Matching is
tiered (exact, fuzzy) to avoid the rigid "must say the exact sentence"
problem from earlier voice assistant attempts.

## Pipeline

```
Microphone (always listening)
    -> openWakeWord (wake word detection, runs 24/7, cheap)
        -> on trigger: record utterance
            -> VAD (webrtcvad / silero-vad) detects end of speech
                -> faster-whisper (local transcription)
                    -> Intent Matcher (exact -> fuzzy -> LLM fallback)
                        -> Action Dispatcher (hyprctl, D-Bus, scripts, systemd)
                            -> (optional) Piper TTS response
```

## Tech Stack

- **Language**: Python
- **Wake word detection**: `openWakeWord`
- **Voice activity detection**: `webrtcvad` or `silero-vad`
- **Speech-to-text**: `faster-whisper` (CTranslate2, local, German-capable)
- **Intent matching**: `rapidfuzz` (fuzzy string/keyword matching)
- **Text-to-speech (optional)**: `Piper` (`norman` for male and `amy` for female)
- **Action dispatch**: `hyprctl`, D-Bus, shell scripts, systemd user units
- **Service management**: systemd `--user` unit

## Matching Strategy (Tiered)

1. **Exact match** - transcript matches a known phrase exactly.
2. **Fuzzy match** - rapidfuzz scores transcript against a list of phrasings
   per action (multiple phrasings + keyword/slot extraction instead of one
   rigid sentence per action).

## Open Questions / TODO

- [ ] Decide on Whisper model size (small vs medium)
- [ ] Decide wake word: pre-trained vs custom-trained
- [ ] Define initial actions.yaml (first batch of commands)

