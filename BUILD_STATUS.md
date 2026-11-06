# ARGUS 4.2 build status

Implemented:
- Continuous microphone streaming while Conversation Mode is active
- 40 ms PCM chunks
- Explicit input resampling to 16 kHz
- Gemini 3.8 Live Extended Thinking model default
- Medium thinking configuration
- Automatic language detection (language codes intentionally omitted)
- Telugu/Hindi/English code-switching instructions
- Context window compression
- Session resumption handle tracking
- GoAway-aware reconnect with bounded retry
- Audio interruption handling
- Local transcript and memory persistence
- Animated futuristic UI with mic-level feedback
- Raw audio not saved

Not implemented / not guaranteed:
- Speaker diarization in Live streaming mode
- Perfect speech recognition in every crowd/noise/accent condition
- A robust offline wake-word detector
- Guaranteed addressee detection with overlapping conversations
- 20 m speech recognition on built-in laptop microphone
- 20,000 simultaneous sessions on one laptop
- Arbitrary OS/computer command execution
- Full live web search and external action tool integrations
- Physical holographic projection

Validation:
- Python syntax compilation and ZIP integrity check.
- No physical laptop microphone/speaker/network test.
- No API key test or live model request test.


## ARGUS 4.2.2 multilingual update
- Set `input_audio_transcription.language_codes` to an explicit empty list to request automatic language identification.
- Strengthened the system instructions: never ask visitors to announce/select a language; follow the latest spoken language and code-switches.
- Requested Romanized Telugu for visible response text while keeping spoken audio in natural Telugu.
- This is a prompt/configuration improvement, not a guarantee of perfect recognition. Validate with real Telugu, Hindi, English, and code-mixed samples on the exhibition laptop.


## ARGUS 4.3 cinematic wake interface
- Replaced the conventional dashboard with a full-screen original animated core.
- Removed visible conversation activation/end buttons.
- Added local Vosk wake-word detection for "ARGUS" / "Hey ARGUS".
- Audio is processed locally before wake activation; Gemini streaming begins only after wake.
- Added original generated activation tone.
- Keyboard: Esc ends conversation and re-arms wake listener; F1 typed fallback; F2 memory; F11 fullscreen; Space manual wake fallback.
- Added accent-adaptation instructions for Indian, US, UK and Australian English and multilingual speech.
- The local wake detector is English-only and may miss unusual pronunciations; SPACE fallback remains.

- Replaced the six-attempt transient-network retry limit with indefinite capped-backoff recovery; fatal authentication/model/configuration errors still surface instead of looping.
