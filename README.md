# ARGUS 4.3 — Cinematic Wake Interface

ARGUS 4.3 is a Windows desktop prototype with a voice-activated, cinematic
science-fiction-inspired interface. It is an original design, not a recreation
of any movie asset.

## What changed
- Removed the visible Activate Conversation Mode and End Session buttons.
- Full-screen animated neural core with microphone-reactive rings and spectrum.
- Say **“ARGUS”** to awaken the assistant.
- A short, original electronic activation tone plays when the wake word is detected.
- Offline Vosk wake-word detection runs locally. The wake-word audio is not sent
  to Gemini and is not saved.
- Gemini Live audio streaming starts only after wake-word activation.
- Transient network drops trigger ongoing capped-backoff recovery rather than ending after six attempts; the latest resumable handle and locally saved turns are reused where supported.
- Press **Esc** to end the current conversation and return to wake-word standby.
- Press **F1** to show/hide typed input.
- Press **F2** to open the local memory archive.
- Press **F11** to toggle full-screen mode.
- Press **Space** as a manual wake fallback if the local wake model is unavailable.
- Multilingual response instructions include Indian, American, British and
  Australian English varieties, broad supported-language coverage, code-switching,
  variable speech rates, and polite clarification when words remain unclear.
- Telugu display responses are requested in Romanized Telugu while spoken audio
  should remain natural Telugu.

## Install
1. Extract the project folder.
2. Use Python 3.12 x64.
3. Run `setup.bat` while connected to the internet. It installs Python packages
   and downloads the small offline English wake-word model.
4. Add your own `GEMINI_API_KEY` to `.env`. Never paste the key into chat.
5. Run `run_argus.bat`.

If the wake model download fails, press Space to start a session manually.
The local wake model recognises the English wake word “ARGUS”; heavily accented
or unusual pronunciations may need the Space fallback. The multilingual cloud
conversation begins only after wake activation.

## Language and accent support
The Gemini Live model documents broad multilingual support (including 99
languages for supported native-audio Live models). Languages are provided by
the cloud model; there are no 99 separate language packs to install.
Accent handling is probabilistic: Indian, American, British, Australian and
other accents can vary substantially, and no model guarantees perfect
recognition of every speaker, dialect, room, or utterance. Test actual visitors'
speech in the exhibition environment.

## Privacy
- Before wake word: the Vosk wake-word model processes audio locally.
- After wake word: live audio is streamed to Google's Gemini service to conduct
  the conversation.
- Raw microphone audio is not written to disk by ARGUS.
- Conversation transcripts and saved memory are stored locally in
  `%LOCALAPPDATA%\\ARGUS4\\memory.sqlite3`.
- The screen visibly indicates when live cloud conversation is active.
- Display a notice to visitors that the microphone is enabled for local wake-word
  detection and that audio is sent to the cloud after activation.

## Important limitations
- The built-in laptop microphone cannot be guaranteed to understand speech at
  20 metres in a crowded exhibition hall.
- Local wake detection uses a small English model and may miss unfamiliar
  pronunciations of “ARGUS”. The SPACE fallback is included.
- The Live model does not provide reliable perfect separation of the person
  addressing ARGUS from all nearby conversations. Do not treat it as a
  guaranteed multi-speaker diarization system.
- A single laptop is a sequential visitor station, not a server for 20,000
  simultaneous conversations.
- This is a cloud-powered assistant prototype, not literal movie-level AGI. Persistent recovery cannot overcome a prolonged outage, revoked credentials, exhausted account quota, or a server-side session that is no longer resumable.
- Check API billing and account terms with an adult before public deployment.
