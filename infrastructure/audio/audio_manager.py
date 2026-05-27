"""Singleton audio manager that plays mode-switch sounds."""

import os
import threading

try:
    import pygame.mixer as mixer

    _PYGAME_AVAILABLE = True
except ImportError:
    _PYGAME_AVAILABLE = False


class AudioManager:
    """Singleton that plays audio cues on mode changes."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._ready = False

        if not _PYGAME_AVAILABLE:
            print("[AudioManager] pygame not installed — audio disabled.")
            return

        threading.Thread(target=self._init_mixer, daemon=True).start()

    def _init_mixer(self):
        try:
            mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
            self._ready = True
        except Exception as e:
            print(f"[AudioManager] Could not init mixer: {e}")
            return

        base = os.path.dirname(os.path.abspath(__file__))
        self._sounds = {
            "code": os.path.join(base, "codemode.mp3"),
            "system": os.path.join(base, "systemmode.mp3"),
        }

    def play(self, mode: str):
        """Play the sound associated with the given mode (non-blocking)."""
        import config

        if not config.SOUND or not self._ready:
            return

        path = self._sounds.get(mode)
        if path is None or not os.path.isfile(path):
            return

        threading.Thread(target=self._play_sound, args=(path,), daemon=True).start()

    def _play_sound(self, path: str):
        try:
            mixer.music.load(path)
            mixer.music.play()
        except Exception as e:
            print(f"[AudioManager] Playback error: {e}")
