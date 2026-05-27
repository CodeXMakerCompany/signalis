<img width="1080" height="607" alt="download" src="https://github.com/user-attachments/assets/3c798288-d3e9-4f0a-836b-570e66b0a995" />

## Gesture Automation for Developers

**Control your system with gestures.  
Reduce repetitive strain.  
Build muscle-memory workflows.**

SIGNALIS transforms your webcam into a real-time command interface for developers, engineers, creators, and power users.

## Launch apps. Trigger IDE shortcuts. Execute workflows.

## The Problem

Modern development destroys hands even with AI.

Hours of:

- Ctrl shortcuts
- terminal switching
- repetitive typing
- editor navigation
- mouse ↔ keyboard hopping
- launcher searching
- workflow repetition

Thousands of identical movements.

Every day.

## What is SIGNALIS?

Your webcam detects hand poses and translates them into actions.

---

## Designed for Developers

SIGNALIS is not social-media hand tracking.

It is designed around:

### Developer Flow

Control:

- IDEs
- terminals
- browsers
- launchers
- shell commands
- OS shortcuts

---

### Semantic Gesture Language

Every gesture has meaning.

Not random poses.

---

### 🌱 MONGO_LEAF

Two center fingers rising like a sprouting leaf.

**Triggers:**

Open MongoDB Compass.

**Why it fits:**

MongoDB’s logo is a leaf.

Middle + ring fingers form the central “core” pair of the hand, visually resembling a sprouting plant.

**Therapeutic concept:**

Middle + ring extension while index + pinky curl promotes:

- lumbrical isolation
- finger independence
- fine motor differentiation
- reduced typing-pattern coupling

---

### 🎮 STEAM_GRIP

Controller-style grip posture.

**Triggers:**

Launch Steam.

**Why it fits:**

The hand shape physically resembles a controller grip.

Steam = gaming.

Immediate visual recall.

**Therapeutic concept:**

Thumb inserted between index and middle stretches:

- thumb web space
- first dorsal interosseous region
- common mouse / controller fatigue zones

---

Your shortcuts become **embodied muscle memory**.

---

## Ergonomic Philosophy

SIGNALIS is built by a developer thinking about:

- RSI
- carpal tunnel strain
- repetitive motion fatigue
- long-session computing ergonomics

Some gestures intentionally introduce **motor variety** instead of forcing endless keyboard repetition.

This is not medical software.

But it is software that takes **developer hand fatigue seriously.**

---

## How SIGNALIS Works

Real-time.

Cross-platform.

No gloves.

No wearables.

No additional hardware.

---

## Example Developer Workflows

### Coding Flow

Gesture → Save

Gesture → Undo

Gesture → Toggle Terminal

Gesture → Delete Line

Gesture → Navigate Editor

---

### System Automation

Gesture → Open MongoDB Compass

Gesture → Launch Steam

Gesture → Open Browser

Gesture → Run Docker Workflow

Gesture → Start Local Development Stack

---

## Installation

### Requirements

- Python 3.10+
- Webcam
- Linux / macOS / Windows

### Setup

```bash
cd gesture_keyboard
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

Press `q` to quit.

---

## Custom Launcher Mode

Add your own applications inside `gesture_map.py`.

Example:

```python
"SOME_GESTURE": {
    "type": "launch",
    "linux": "firefox",
    "windows": "firefox.exe",
}
```

Example uses:

- launch IDEs
- open databases
- start Docker
- trigger scripts
- open dashboards
- automate local environments

---
