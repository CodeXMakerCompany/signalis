"""Global constants for the gesture keyboard application."""

CAMERA_INDEX = 1
COOLDOWN_MS = 2000
STABILITY_FRAMES = 4
MIN_DETECTION_CONFIDENCE = 0.85
MIN_TRACKING_CONFIDENCE = 0.8
SWIPE_VELOCITY_THRESHOLD = 0.04
SWIPE_HISTORY_LENGTH = 6
SWIPE_MIN_CONSECUTIVE = 3
FIRED_FLASH_MS = 400

SNIPPET_LANGUAGE = "typescript"

# Capture at 640x480 for 30fps.
CAPTURE_WIDTH = 640
CAPTURE_HEIGHT = 480

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

THERAPY_MODE = True

SOUND = True

GESTURE_META = {
    "OPEN_HAND": {
        "therapy": True,
        "hold_ms": 25000,
        "stability_frames": 30,
        "therapy_name": "Finger extension stretch",
        "tip": "Full finger extension decompresses carpal tunnel. Spread wide.",
    },
    "FIST": {
        "therapy": True,
        "hold_ms": 0,
        "stability_frames": 8,
        "therapy_name": "Tendon glide (fist stage)",
        "tip": "Clench slowly to complete fist. Pair with OPEN_HAND for full glide cycle.",
    },
    "THUMBS_UP": {
        "therapy": True,
        "hold_ms": 18000,
        "stability_frames": 22,
        "therapy_name": "Thumb abductor stretch",
        "tip": "Extend thumb fully. Hold 15-20s to stretch abductor pollicis longus.",
    },
    "FOUR_FINGERS": {
        "therapy": True,
        "hold_ms": 12000,
        "stability_frames": 15,
        "therapy_name": "Finger spread / dorsal stretch",
        "tip": "Hold 4-finger spread. Stretches palmar fascia and dorsal interossei.",
    },
    "PEACE": {
        "therapy": True,
        "hold_ms": 15000,
        "stability_frames": 18,
        "therapy_name": "Finger isolation / ulnar",
        "tip": "Curl ring+pinky fully while index+middle stay straight. Ulnar nerve benefit.",
    },
    "ROCK_HAND": {
        "therapy": True,
        "hold_ms": 20000,
        "stability_frames": 24,
        "therapy_name": "Ulnar nerve glide",
        "tip": "Index+pinky pillars. Add 5-10 degree wrist extension for nerve glide.",
    },
    "SHAKA": {
        "therapy": True,
        "hold_ms": 15000,
        "stability_frames": 18,
        "therapy_name": "Thumb+pinky abductor stretch",
        "tip": "Spread thumb and pinky as wide apart as possible. Hold 15s.",
    },
    "POINT_UP": {
        "therapy": True,
        "hold_ms": 12000,
        "stability_frames": 15,
        "therapy_name": "Extensor indicis isolation",
        "tip": "Keep other fingers genuinely curled. Trains extensor balance vs flexors.",
    },
    "CIRCLE_HAND": {
        "therapy": True,
        "hold_ms": 20000,
        "stability_frames": 24,
        "therapy_name": "Opponens pollicis opposition",
        "tip": "Gentle thumb-index contact (not pinch). Rehabs first weakening muscle in CTS.",
    },
    "CLAW_HAND": {
        "caution": True,
        "static_hold": False,
        "stability_frames": 3,
        "tip": "Max mechanical load on flexors. Fire quickly. Never hold statically.",
    },
    "L_SHAPE": {
        "caution": True,
        "static_hold": False,
        "stability_frames": 3,
        "tip": "Thumb extension + wrist deviation can aggravate De Quervain co-condition.",
    },
    "TIMEOUT": {
        "caution": True,
        "static_hold": False,
        "stability_frames": 3,
        "tip": "Forced wrist posture. Occasional use fine. Avoid when symptomatic.",
    },
    "THREE_FINGERS": {"therapy": False, "caution": False, "stability_frames": 5},
    "RING_UP": {"therapy": False, "caution": False, "stability_frames": 5},
    "MIDDLE_UP": {"therapy": False, "caution": False, "stability_frames": 5},
    "PINKY_UP": {"therapy": False, "caution": False, "stability_frames": 5},
    "SWIPE_RIGHT": {"therapy": False, "caution": False, "stability_frames": 4},
    "SWIPE_LEFT": {"therapy": False, "caution": False, "stability_frames": 4},
    "WRITE_PINCH": {"therapy": False, "caution": False, "stability_frames": 5},
    "CURL_WAVE": {"therapy": False, "caution": False, "stability_frames": 6},
    "BROADCAST": {
        "therapy": True,
        "hold_ms": 20000,
        "stability_frames": 24,
        "therapy_name": "Full finger extension + wrist pronation stretch",
        "tip": "Spreading all fingers while rotating the wrist outward (pronation) stretches the pronator teres and supinator muscles. Decompresses the median nerve at the pronator tunnel — a secondary CTS compression site often missed in diagnosis.",
    },
    "SWEEP": {
        "therapy": True,
        "hold_ms": 0,
        "stability_frames": 5,
        "therapy_name": "Wrist flexor stretch via horizontal wrist rotation",
        "tip": "The sweeping motion combined with an open hand rotates the wrist through its full range of radial-to-ulnar deviation. This mobilises the radiocarpal joint and stretches the extensor carpi ulnaris, reducing stiffness from prolonged keyboard use.",
    },
    "FUNNEL": {
        "therapy": True,
        "hold_ms": 22000,
        "stability_frames": 26,
        "therapy_name": "Full tendon glide — the gold-standard CTS exercise",
        "tip": "Open-to-fist is the complete tendon glide sequence. Doing it slowly (over 20+ frames) ensures each flexor digitorum superficialis and profundus tendon slides through its sheath fully, preventing adhesion formation post-inflammation.",
    },
    "SPOTLIGHT": {
        "therapy": True,
        "hold_ms": 15000,
        "stability_frames": 18,
        "therapy_name": "Index extensor isolation + thumb abductor stretch",
        "tip": "Extending index while abducting thumb simultaneously trains two antagonist muscle groups: extensor indicis proprius and abductor pollicis longus. This counteracts the flexor dominance that compresses the carpal tunnel.",
    },
    "GUARD": {
        "therapy": True,
        "hold_ms": 22000,
        "stability_frames": 26,
        "therapy_name": "Wrist extension stretch — the #1 CTS decompression",
        "tip": "Holding the wrist in gentle extension (palm-out stop position) with fingers together maximises carpal tunnel volume. Studies show 20s holds reduce intra-tunnel pressure by up to 30%. The fingers-together constraint prevents compensatory finger spreading.",
    },
    "LAUNCH": {
        "therapy": True,
        "hold_ms": 0,
        "stability_frames": 4,
        "therapy_name": "Explosive tendon glide — dynamic version for circulation",
        "tip": "The rapid fist-to-open movement pumps synovial fluid through the tendon sheaths, flushing inflammatory mediators. The upward wrist motion adds a nerve glide component, mobilising the median nerve through the carpal tunnel.",
    },
    "TEMPLE": {
        "therapy": True,
        "hold_ms": 20000,
        "stability_frames": 24,
        "therapy_name": "Thumb + index opposition with wide abduction",
        "tip": "Forming the wide thumb-index frame requires sustained activation of the first dorsal interosseous and opponens pollicis — the two muscles that atrophy earliest in CTS. Holding 20s rebuilds motor unit recruitment patterns.",
    },
    "ARROW": {
        "therapy": True,
        "hold_ms": 16000,
        "stability_frames": 20,
        "therapy_name": "Finger isolation + ulnar deviation stretch",
        "tip": "Holding index and middle tightly together while pointing requires sustained co-contraction of the lumbricals and interossei. This trains intrinsic hand muscle endurance, reducing reliance on extrinsic flexors that crowd the carpal tunnel.",
    },
    "SEAL": {
        "therapy": True,
        "hold_ms": 18000,
        "stability_frames": 22,
        "therapy_name": "Thumb flexor lock + intrinsic muscle squeeze",
        "tip": "Pressing the thumb firmly across the knuckles engages the flexor pollicis longus and adductor pollicis under isometric load. This strengthens the thenar eminence without the repetitive motion that aggravates CTS symptoms.",
    },
    "KEYMAP": {
        "therapy": True,
        "hold_ms": 25000,
        "stability_frames": 30,
        "therapy_name": "Full finger extension + nerve tension test position",
        "tip": "All fingers spread wide with maximum extension is a modified upper limb neurodynamic test (ULNT1) position. Holding 25s gently tensions the median nerve along its full path, improving nerve mobility and reducing adhesions at the transverse carpal ligament.",
    },
    "SCROLL_UP": {"therapy": False, "caution": False, "stability_frames": 5},
    "SCROLL_DOWN": {"therapy": False, "caution": False, "stability_frames": 5},
    "WARP_SIGN": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Ring isolation + index isolation",
        "tip": "Index+ring up, middle+pinky curled. Trains independent finger control.",
        "mode": "system",
    },
    "BRAVE_LION": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Intrinsic muscle isometric hold",
        "tip": "Thumb alongside fist. Isometric hold strengthens intrinsic hand muscles.",
        "mode": "system",
    },
    "CHROME_C": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Thumb opposition + finger extension combo",
        "tip": "C-shape: index curved to thumb, 3 fingers up. Trains opposition.",
        "mode": "system",
    },
    "OBS_VAULT": {
        "therapy": True,
        "hold_ms": 16000,
        "stability_frames": 20,
        "therapy_name": "Full opposition pinch",
        "tip": "All fingertips touching thumb. Full opposition strengthens thenar muscles.",
        "mode": "system",
    },
    "MISSION_M": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Middle extensor isolation",
        "tip": "Only middle finger extended. Isolates extensor digitorum to middle.",
        "mode": "system",
    },
    "SNAP_FRAME": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Precision pinch + thumb abduction combined",
        "tip": "Index+thumb right-angle frame. Trains abductor pollicis longus.",
        "mode": "system",
    },
    "MONGO_LEAF": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Lumbrical isolation — middle+ring split",
        "tip": "Middle+ring up while index+pinky curled. Isolates lumbrical control.",
        "mode": "system",
    },
    "STEAM_SIGN": {
        "therapy": True,
        "hold_ms": 14000,
        "stability_frames": 16,
        "therapy_name": "Thumb web space stretch",
        "tip": "Index+pinky up with thumb out stretches the first dorsal interosseous.",
        "mode": "system",
    },
}

LAUNCHER_STABILITY_EXTRA = 8
