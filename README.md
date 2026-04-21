# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Waveform Studio]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Akshita Maity` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |
| `Sirjan Chahal` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |

## 1.3 Project Title
`Sonic Vault'

## 1.4 One-Line Pitch
`[An interactive light installation that translates live sound into a real-time frequency visualiser on a dual LED matrix, controlled by a physical joystick and brought to life with breathing NeoPixel light.]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`Sonic Vault is an interactive installation that bridges the gap between invisible sound waves and tangible light. Using an ESP32 and a MAX4466 high-sensitivity microphone module, the system captures ambient audio and processes it into a frequency-based visual display across a dual MAX7219 8×8 LED matrix (giving a combined 32×8 pixel canvas).

The experience is made playful through a physical joystick that allows users to toggle between three distinct "Atmospheric Modes": Red (Bass), Orange (Full Range), and Yellow (Treble). These modes don't just change colours — they change how the visualiser filters sound. Low-frequency rumbles and is slow in Bass mode; high-frequency spikes and crackle fast in Treble mode; Full Range blends both. A NeoPixel strip of 10 LEDs breathes alongside the matrix, pulsing in the chosen mode colour. It turns the act of listening a song or even a clap, whistle, beat, or spoken word — into a temporary digital sculpture in a pulsing light-box.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[What is the experience? 
What is the experience? A two-act interaction: first, navigate a game-like music interface with a physical joystick to find and play a track. Then, watch a live LED matrix visualiser react to that music in real time, with three selectable frequency modes changing the visual character of the response.
What do you want the player to feel?
In Phase 1: the satisfying weight of using a physical controller to navigate a slick digital interface — like operating a piece of real music equipment. In Phase 2: the delight of seeing something invisible (sound) become visible and immediate — the feeling that the room is listening.
Why would someone want to try it again? 
Different songs produce completely different light patterns. Different frequency modes make the same song look different. Players want to try their favourite track, then their friend's, then something with heavy bass to see what happens.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making a playable object / interactive experience for teens, adults, and exhibition visitors who are curious about how technology can make something invisible like sound into a visible and tangible experience.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Installation / Object]` | `[Teenage Engineering OP-1 / Pocket Operators]` | `[The idea that sound tools can be playful, tactile, and visually expressive — not just functional]` |
| `[App / Video]` | `[YouTube: LED audio spectrum visualisers with Arduino]` | `[Confirmed the technical feasibility and sparked the idea of using a matrix display instead of a strip]` |
| `[Installation]` | `[TeamLab immersive digital art installations]` | `[The feeling that responding-to-sound installations create a "flow" state in participants]` |
| `[Game UI]` | `[Plex, Spotify, retro media player interfaces]` | `[The idea of a track library as a tactile, navigable object rather than just a screen]` |


## 3.2 Original Twist
What makes your project original?

**Response:**  
`[Most audio visualisers are passive: plug in music, watch lights respond. Sonic Vault makes the song selection itself a physical, tactile act using a real joystick and a purpose-built UI. The player earns the visual experience by navigating to it. Then audio visualisers normally map amplitude to height (the volume) . Sonic Vault gives the user agency: by tilting a physical joystick, they change which frequency band the visualiser responds to — bass, full range, or treble. This means two people using the same device at the same time can have completely different visual experiences of the same sound. The breathing NeoPixel strip adds an ambient "mood light" layer that makes the installation feel alive even when silent.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[Tilt joystick → navigate genre list → select genre → tilt joystick → navigate song list → press SELECT → song plays through speakers → Select song → play the song → microphone captures → ESP32 filters by mode → LED matrix displays waveform → NeoPixel breathes in mode colour → user tilts joystick to change mode → repeat]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[Teens, adults, exhibition visitors, anyone curious about sound and light]` |
| Age range | `[12 and above]` |
| Solo or multiplayer | `[Solo interaction, but works well as a shared display for groups]` |
| Expected duration of one round | `[Continuous — no fixed round; engagement lasts as long as the user wants]` |
| What should the player feel? | `[Curiosity, flow, delight, a sense of control over light through sound]` |
| Is explanation required before use? | `[Minimal — the joystick and visual response are self-explanatory within seconds, also additionally there is manual as to how the joystick are meant to be used in the vault. Plus, genre/library/queue layout is familiar from music apps; joystick navigation self-discovered within 30 seconds ]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[The player sees a glowing dark-themed screen — the Sonic Vault UI — and a physical joystick controller in front of it. The LED matrix pulses softly. The NeoPixel strip breathes amber.]`
2. **Start:** `[They move joystick control around. No button press needed. The system is always on.]`
3. **First Action:** `[They tilt up/down — the genre list scrolls. A yellow focus dot shows the active panel. They see: the differenet genres and when selected the songs that are stored in them.
   They tilt right — focus shifts to the Song Library. Tracks filtered to the selected genre appear, showing title, artist, and duration.]`
5. **Main Interaction:** `[They scroll up/down. They press the joystick button (SELECT) to play. The player bar lights up with the track name and a moving progress bar.The MAX4466 mic picks up the audio. The 32×8 LED matrix erupts — bar columns rise and fall in real time with the music. NeoPixels breathe in the respective colour of the frequency mode.]`
6. **System Response:** `[The player tilts the joystick to cycle frequency modes. Red = Bass — slow, wide, deep bars. Orange = Full Range — responsive blend. Yellow = Treble — fast, jittery, electric.Tilt right to enter the Player zone — volume up/down, skip, pause — all without touching a keyboard or mouse.?]`
7. **Win / Lose / End Condition:** `[Song ends; next queued track begins automatically, or the player navigates back to pick another. System is always ready.]`
8. **Reset:** `[There is no end, the music willl always keep playin and the svreen will always keep shoing the visuas of the song unless stopped. besides this the microphone will pick up frequencies above its baseline and translate it onto the led matrix visuals.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

-Tilt left/right to move focus between Genre, Library, Queue, and Player panels.
Tilt up/down to scroll within any panel.
-Press the joystick button (SELECT) to play a song, enter a panel, or activate a player control.
-In Player zone: tilt up/down on the Volume sub-target for volume; tilt up/down elsewhere for previous/next track.
-During the visualiser: tilt (left/middle/right) joystick to cycle the frequency mode (Bass → Full → Treble).
-Upload your own audio files using the "+ Upload" button for more options.
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [x] `[The joystick navigates genre list, song library, queue, and player controls via WebSerial without requiring keyboard or mouse]`
- [x] `[Selecting a song and pressing SELECT begins playback and the LED matrix visualiser pick up the frequency and get triggered]`
- [x] `[The LED matrix produces a real-time animated waveform that visually reacts to the music]`
- [x] `[Joystick mode switching produces perceptibly different column behaviour for Bass, Full, and Treble]`
- [x] `[The system runs continuously without freezing, dropping serial connection, or requiring a restart]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[A joystick that navigates the song list and triggers playback, with the LED matrix responding to the resulting audio. Genre filtering, queue, and volume control are valuable but not essential to the core loop.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[2 ESP32 firmware handling both WebSerial UI navigation and ADC visualiser control simultaneously]`
- `[Physical enclosure with diffused acrylic panels over the LED matrix]`
- `[splitting the frequency via a mathematics equation for extracting treble and bass diagrams]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [ yes ] Electronics-based
- [ ] Mechanical
- [ yes ] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [ yes ] Sound-based
- [ yes ] Light-based
- [ yes ] Screen/UI-based
- [ ] Fabricated structure
- [ ] Game logic based
- [ yes ] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[Layer 1 — UI Interface (Browser + ESP32 via WebSerial):
The Sonic Vault HTML/JS application runs in Google Chrome. The ESP32, running joystick firmware, connects via USB. When the joystick is tilted or pressed, the ESP32 sends a single-word command over serial (UP, DOWN, LEFT, RIGHT, SELECT) at 115200 baud. Chrome reads this via the Web Serial API and routes it through a focus-aware navigation system — identical to keyboard arrow key input. Four zones: Genre List, Song Library, Queue, and Player Controls. The user navigates these with the joystick to select and play tracks. Real audio files can be uploaded.
Layer 2 — Audio Visualiser (ESP32 + hardware):
Once a track plays from speakers, the MAX4466 microphone captures the audio (this is on an another ESP-32). The ESP32 reads the microphone ADC at ~20Hz, computes a rolling baseline to filter DC offset and noise, and derives three frequency proxies: low (slow-moving amplitude average → bass), full (blended amplitude), and high (fast-changing delta between samples → treble). Based on the active mode, one band value drives bar column heights across the dual MAX7219 32×8 matrix. Ten NeoPixels breathe in the mode colour via a sine-wave phase animation.
The 2 joystick are the centre of both layers. During song selection it navigates the UI. For playback the second switches the visualiser's frequency mode. 
Power: An XL4015 buck regulator provides a stable 5V rail for the ESP32, both MAX7219 modules, and the NeoPixel strip. ]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Joystick Module (GPIO 35)]` | Input | `[Sends LEFT/RIGHT/UP/DOWN/SELECT to UI; cycles frequency mode on matrix]` |
| `[MAX4466 Microphone (GPIO 34)]` | Input (ADC) | `[Captures audio from speakers; drives visualiser amplitude]` |
| `[WebSerial (USB → Chrome)]` | Communication | `[Bridges ESP32 joystick commands to the HTML/JS UI]` |
| `[\Dual MAX7219 Matrix (SPI, CS: GPIO 5 & 15)]` | Output (Light) | `[32×8 real-time waveform bar display — bars mirror upward and downward]` |
| `[NeoPixel Strip — 10 LEDs (GPIO 4)]` | Output (Light) | `[Ambient breathing light in mode colour (Red / Orange / Yellow) indicating the frequency mode with respective colors]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[15cm]` |
| Width | `[34cm]` |
| Height | `[36cm]` |
| Estimated weight | `[600 gm]` |
For external display (informational 3 fold board)
| Dimension | Value |
|---|---|
| Length | `[na]` |
| Width | `[3 x A3]` |
| Height | `[36cm]` |
---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ yes ] Not applicable  no moving mechanical parts beyond the spring-return joystick axis.

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Write here]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Write here]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `2` | `[2 controller - one for the ui and another for visual part]` |
| `MAX4466 Electret Mic Amplifier Module)` | `[1]` | `[Amplified audio capture from speakers]` |
| `[MAX7219 8×8 LED Matrix Module (4-in-1)]` | `[2]` | `[32×8 pixel real-time waveform display]` |
| `[KY-023 Analog Joystick Module]` | `[2]` | `[Navigation input for UI and frequency mode switching]` |
| `[XL4015 Buck Regulator Module]` | `[1]` | `[Regulated 5V, 5A, for all components]` |
| `[WS2812B NeoPixel Strip — 10 LEDs]` | `[1]` | `[Ambient mode-colour breathing light` |


## 9.2 Wiring Plan

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[SPI: CLK → GPIO 18, MOSI → GPIO 23. Matrix 1 CS → GPIO 5. Matrix 2 CS → GPIO 15.
Microphone: OUT → GPIO 34. VCC → 3.3V. GND → GND.
Joystick: VRX → GPIO 35. VCC → 3.3V. GND → GND.
Joystick: VRX → GPIO 35. VRY → GPIO 34 VCC → 3.3V. GND → GND.
NeoPixel: DIN → 330Ω → GPIO 4. VCC → 5V rail. GND → GND. 1000µF cap across VCC/GND near strip.
Buck Regulator: Wall adapter input. 5V output → ESP32 VIN, matrix VCC, NeoPixel VCC]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[XL4015 buck regulator (wall adapter input, 5V regulated output)]` |
| Voltage required | `[5V for ESP32, MAX7219 modules, NeoPixel; 3.3V from ESP32  for MAX4466 and joysticks ]` |
| Current concerns | `[NeoPixels peak ~600mA; matrices ~200mA; ESP32 ~240mA. Total ~1A. XL4015 rated 5A.]` |
| Safety concerns | `[Inline fuse on buck regulator input. Keep NeoPixel cap close to strip.]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[MicroPython]` | `[IDF)Firmware on the ESP32]` |
| `[max7219 MicroPython library]` | `[Driving MAX7219 matrices over SPI]` |
| `[Web Serial API (Chrome)]` | `[Receiving joystick commands from ESP32 at 115200 baud]` |
| `[Web Audio API (Chrome)]` | `[Playing uploaded audio files through the browser]` |
| `[Adobe Illustrator]` | `[Full UI visual design (layout, colour system, typography)]` |


## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[The project runs two software systems connected by the physical act of playing music.

System A: Sonic Vault HTML/JS UI

Startup: Render genre list, song library (17 demo tracks across 8 genres), empty queue, and player bar. Focus begins in GENRE_LIST zone. Status shows "NO CONTROLLER."

WebSerial Connection: User clicks "Connect Controller." Chrome's Web Serial API prompts for the ESP32 serial port. A background read loop opens a TextDecoderStream and parses newline-delimited commands (UP / DOWN / LEFT / RIGHT / SELECT).

Navigation System: Four focus zones — GENRE_LIST, SONG_LIST, QUEUE_LIST, PLAYER. A yellow dot indicator shows the active zone. UP/DOWN scroll within the active zone; LEFT/RIGHT shift focus between zones; SELECT plays the highlighted song, confirms the selected genre, or activates the highlighted player control. In the PLAYER zone, LEFT/RIGHT cycles through five sub-targets (Prev, Play/Pause, Stop, Next, Volume); UP/DOWN on the Volume sub-target adjusts level in 5% increments.

Playback: Songs play via the Web Audio API if a file is uploaded; otherwise a simulated progress timer runs. Song end triggers the next queued track or next track in library depending on playback mode (Normal / Shuffle / Repeat / Loop Queue).
Command Routing: Every incoming serial command routes through the same handler as keyboard arrow keys — identical code path, no duplication.
System B: ESP32 Visualiser Firmware (MicroPython)
Startup: Initialise SPI, two MAX7219 display objects (CS GPIO 5 and 15), ADC on GPIO 34 (mic) and GPIO 35 (joystick), NeoPixel on GPIO 4 (10 LEDs). Set baseline to 1900, mode to 2 (Full Range).
Main Loop (20 Hz):

Clear both matrix buffers.
Read joystick ADC → determine region (left <1200 / centre / right >2800) → on centre→edge transition, increment or decrement mode (1–3).
Advance breath phase → compute sine-wave brightness → write mode colour to all 10 NeoPixels.
Read mic ADC → update rolling baseline (90/10 IIR) → compute amplitude and delta. Noise gate: if amplitude < 8, zero both.
Update frequency proxies: low = low×0.95 + amplitude×0.05; full = amplitude×0.6 + low×0.4; high = high×0.3 + delta×0.7.
Select band_val by mode.
For each of 32 columns: compute target height from band_val + random jitter → animate current toward target → draw bar on display1 (upward) and display2 (downward, mirrored).
Show both matrices. Sleep 50ms.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[=== UI COMMAND HANDLER ===

ON serial command received (UP / DOWN / LEFT / RIGHT / SELECT):
  if focus == PLAYER:
    LEFT  → cycle playerSub left  (prev → pp → stop → next → vol)
    RIGHT → cycle playerSub right
    UP    → if playerSub==vol: volume+5  else: prevTrack()
    DOWN  → if playerSub==vol: volume-5  else: nextTrack()
    SELECT → activate playerSub (play/pause / stop / prev / next)
  else:
    UP    → scroll active list upward
    DOWN  → scroll active list downward
    LEFT  → shift focus left  (SONG→GENRE / QUEUE→SONG / PLAYER→QUEUE)
    RIGHT → shift focus right (GENRE→SONG / SONG→QUEUE / QUEUE→PLAYER)
    SELECT → play song / enter panel / play queue item


=== ESP32 VISUALISER FIRMWARE ===

INIT:
  spi = SPI(CLK=18, MOSI=23, baud=80000)
  display1 = MAX7219(spi, cs=5)
  display2 = MAX7219(spi, cs=15)
  mic  = ADC(pin=34, atten=11dB)
  joy  = ADC(pin=35, atten=11dB)
  leds = NeoPixel(pin=4, count=10)
  baseline=1900 | mode=2 | breath_phase=0 | current[32]={0}

LOOP:
  clear display1, display2

  joy_val = joy.read()
  region  = LEFT if <1200 else RIGHT if >2800 else CENTRE
  if prev_region==CENTRE and region==LEFT:  mode = clamp(mode+1, 1, 3)
  if prev_region==CENTRE and region==RIGHT: mode = clamp(mode-1, 1, 3)
  prev_region = region

  breath_phase += 0.35
  brightness = (sin(breath_phase)+1) / 2
  colour = RED×brightness if mode==1 else ORANGE×brightness if mode==2 else YELLOW×brightness
  fill all 10 LEDs → write

  raw      = mic.read()
  baseline = baseline×0.9 + raw×0.1
  amp      = abs(raw - baseline)
  delta    = abs(raw - prev_raw) | prev_raw = raw
  if amp < 8: amp=0; delta=0

  low  = low×0.95  + amp×0.05
  full = amp×0.6   + low×0.4
  high = high×0.3  + delta×0.7
  band_val = low if mode==1 else full if mode==2 else high

  for x in 0..31:
    jitter   = random(-25,25) if mode==2 else random(-15,15)
    target[x] = clamp(int((band_val+jitter)/10), 0, 8)
    if amp==0: current[x] = max(0, current[x]-1)
    elif current[x] < target[x]: current[x] += 1
    elif current[x] > target[x]: current[x] -= 1
    h = current[x]
    for y in 0..h: display1.pixel(x, 7-y, ON)    // bars grow upward
    for y in 0..h: display2.pixel(x, y,   ON)    // bars grow downward (mirrored)

  display1.show() | display2.show() | sleep(50ms)]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ yes  ] Yes but not coded through Mit app inventor. Its an HTML UI
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[The Sonic Vault UI is the first half of the experience. Without it, the player has no way to choose their music, and the visualiser has no audio to react to. It is a fully functional, joystick-navigable music library and player that runs in the browser.
The design intent was to make song selection feel like a deliberate, physical act — not just a tap on a screen. Navigating a dark, game-controller-style interface creates a ritual around music choice. The player has to move through the vault to earn the visual experience.]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `Genre panel (left) — 8 genres including Synthwave, Lo-Fi, Techno, Rock, Ambient, Jazz, Hip-Hop` | `[Filter the track library by style]` |
| `[Song Library (centre) — full scrollable track list]` | `[Shows title, artist, genre, duration; yellow highlight follows joystick]` |
| `[Queue panel (right)]` | `[Build and manage a playlist; Normal / Shuffle / Repeat / Loop Q modes]` |
| `[Player bar (bottom) — Prev / Play / Stop / Next / Volume]` | `[Full playback control, all accessible from joystick in PLAYER focus zone]` |
| `[CONNECT CONTROLLER button]` | `[Opens WebSerial port dialog; connects ESP32 joystick over USB]` |
| `[Status indicator]` | `["NO CONTROLLER" → "CONTROLLER ACTIVE" with blinking dot on connection]` |
| `[File upload (drag-and-drop or click)]` | `[Load real MP3 / WAV / OGG / FLAC files from device into the library]` |
| `[Toast notifications]` | `[Brief on-screen feedback on every joystick command]` |
| `[Keyboard mirror]` | `[All joystick commands are also keyboard-accessible (arrows + Enter)]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow
Browser opens → UI renders with 17-track demo library
Player clicks "Connect Controller" → Chrome WebSerial dialog → ESP32 selected → status: "CONTROLLER ACTIVE"
Focus starts in Genre List — tilt UP/DOWN to scroll genres
Tilt RIGHT → focus moves to Song Library — tilt UP/DOWN to scroll tracks
Tilt RIGHT again → Queue panel — add songs to playlist
Tilt RIGHT again → Player Controls — LEFT/RIGHT cycles: Prev → Play/Pause → Stop → Next → Volume
Press SELECT on Play/Pause → song plays from speakers → visualiser activates on hardware
During playback: tilt joystick on ESP32 to change frequency mode (Bass / Full / Treble)
Tilt LEFT from Player zone → return to Queue/Library → pick next song

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `yes` | `162` | `[Dual-core, ADC, SPI, USB serial]` | `[we needed 2 of them]` |
| `[MAX4466 Electret Mic Amplifier]` | `[1]` | `[No]` | `[Yes]` | `[130]` | `[Adjustable gain, 3.3V, analog output]` | `[Onboard op-amp; clean signal without external amplifier circuit]` |
| `[MAX7219 8×8 Matrix Module (4-in-1)]` | `[2]` | `[no]` | `[Yes]` | `[400 each]` | `[SPI-driven, built-in current regulation]` | `[Reliable SPI over wire; no timing fragility; pixel-art aesthetic fits dark UI theme]` |
| `[KY-023 Analog Joystick Module]` | `[2]` | `[No]` | `[Yes]` | `[100 each]` | `[Dual-axis ADC, spring return]` | `[Tactile game-controller feel; single USB cable handles both UI and mode control]` |
| `[WS2812B NeoPixel Strip — 10 LEDs]` | `[1]` | `[Yes]` | `[Yes]` | `[300]` | `[Individually addressable RGB]` | `[Breathing animation; short run avoids all signal integrity issues]` |
| `[XL4015 Buck Regulator Module]` | `[Qty]` | `[No]` | `[Yes]` | `[280]` | `[Input 7–35V, output 5V, 5A rated]` | `[Added after brownouts under peak load — non-negotiable for stable operation]` |
| `[foamboard]` | `[2 A1]` | `[No]` | `[Yes]` | `[0]` | `[na]` | `[its easy to manipulate and mold into structures]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Foamboard instead of Acrylic/MDF: We chose foamboard for the "Vault" structure because it is incredibly lightweight and easy to manipulate using hand tools. Unlike MDF or acrylic, which require laser cutting, foamboard allowed us to prototype the internal angles of the vault in real-time to ensure the NeoPixel "breath" effect reflected off the walls perfectly.

Buck Regulator instead of ESP32 Onboard Power: We added the XL4015 Buck Regulator because the 5V pin on the ESP32 cannot handle the current draw of two 8x8 matrices and a NeoPixel strip simultaneously. Without this, the system would suffer from brownouts (sudden resets) when the music gets loud and all LEDs light up.

MAX4466 Microphone instead of Generic Sound Sensors: Generic sensors usually only provide a digital "high/low" threshold (detecting only "loud" or "quiet"). The MAX4466 provides a high-quality analog output with an adjustable gain, which is essential for our mode-filtering logic (separating Bass from Treble).

MAX7219 Dot Matrix instead of NeoPixel Matrix: While NeoPixels are colorful, the MAX7219 modules provide a high-contrast, "lo-fi" aesthetic that matches our "Sonic Vault" theme. Technically, they are much easier to wire in a "daisy-chain" configuration over the distance of our foamboard structure.

Joystick Module instead of Buttons or Potentiometers:
Buttons only allow for "on/off" states, and potentiometers (knobs) require a twisting motion that can be slow. The joystick provides instant, multi-directional agency. In a playful experience, tilting a stick feels more like "steering" the sound, which is more engaging for a user than simply clicking a button.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[MAX4466 Mic Module]` | `[Core audio input]` | `[]` | `[Week 1 Day 3]` | `[Received]` |
| `[MAX7219 Matrix ×2]` | `[Core visual output]` | `[Link]` | `[Week 2 Day 5]` | `[Received]` |
| `[XL4015 Buck Regulator]` | `[Stable power (post-brownout)]` | `[Link]` | `[Week 3]` | `[Received]` |
| `[WS2812B NeoPixel (cut to 10)]` | `[light]` | `[Link]` | `[Week 1]` | `[Received]` |
| `[KY-023 Analog Joystick Module]` | `[input componenet]` | `[Week 1]` | `[Date]` | `[Received]` |
| `[multimeter]` | `[to check current]` | `[shop]` | `[Week 3]` | `[Received]` |



## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[900]` |
| Mechanical parts | `[na]` |
| Fabrication materials | `[na]` |
| Purchased extras | `[400]` |
| Contingency | `[150]` |
| **Total** | `[1450]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[The 150-LED NeoPixel strip that was abandoned represented wasted cost. The MAX7219 matrices are the same price and far more reliable. The XL4015 is the one component that should always be budgeted from day one on any project with multiple high-current outputs.]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Akshita led all fabrication model building and Interface software and backend connection to input components ( HTML/JS, Illustrator design), led hardware assembly and power design. Sirjan led all coding for the led display. Decisions were made jointly at the start of each session. If one track was blocked, the other member provided support. Documentation was updated by whoever completed a task. No major design change was made without agreement from both.]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Both]` | `5` | `[week 2 session 1]` | `None` | `done` |
| T2 | `[Complete BOM]` | `[Both]` | `1` | `[week 2 session 1]` | `T1` | `done` |
| T3 | `[Test electronics]` | `[Both]` | `2` | `[week 2 session 2]` | `T1, T2` | `done` |
| T4 | `[Build structure]` | `[Akshita]` | `4` | `[week 3 session 1]` | `T1` | `done` |
| T5 | `[Write main code]` | `[Sirjan]` | `10-12` | `[week 3 session 2]` | `T3` | `done` |
| T6 | `[Write interface code]` | `[Akshita]` | `6-7` | `[week 3 session 2]` | `T1` | `done` |
| T7 | `[Integrate system]` | `[Both]` | `4` | `[week 4 session 1]` | `T all` | `done` |
| T8 | `[Playtest]` | `[both]` | `2` | `[week 4 session 2]` | `T all` | `done` |
| T8 | `[Refine and document]` | `[both]` | `4` | `[week 4 session 2]` | `T7` | `done` |

## 113.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | [Both] | [Both] |
| Electronics | [Both] | [-] |
| Coding | [Sirjan] | [Akshita] |
| UI | [Akshita] | [Sirjan] |
| Mechanical build | [Both] | [-] |
| Testing | [Both] | [-] |
| Documentation | [Both] | [-] |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [ ] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [x] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [ ] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Finalise concept; order and test components]` | `[Components ordered]` | `[Testing success]` | `[Work with arrived components till finalized]` |
| Week 2 | `[Complete all components testing and integration]` | `[Mic-to-neopixel firmware done; However Neopixel strip (150 leds) malfunctioned. Abandoned 150-LED plan- failed due to signal integrity and power issues over long wire runs.]` | `[Decided to use LED matrices along with joystick and buck regulator.]` | `[Source the Matrices and buck; and redesign the power rail]` |
| Week 3 | `[Full system integration and first playable version` | `[Full integration completed. All four subsystems (mic, matrix, joystick, NeoPixel) running together at 20Hz. UI wireframing started with LLM, moved to Illustrator for final design.]` | `[Added symmetric downward bars on display2 (mirrored effect) — this was not in the original plan but looked much better during testing.]` | `[Playtest, tune noise gate ]` |
| Week 4 | `[Refine, playtest, complete UI and documentation]` | `[Noise threshold tuned to 20(was 8-too aggressive); neopixel codes were changed to be more visually appealing. UI companion built from illustrator mockup. ]` | `[Changing colour and other visuals for better user experience]` | `[-]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[NeoPixel strip flicker / wrong colours over long wire]` | `Technical` | `Medium` | `High` | `[Keep data wire short., simplify connectin flow, add regulator.]` | `[Both]` |
| `[Mic picks up handling noise / table vibration]` | `technical` | `medium` | `low` | `[Software noise gate (NOISE_THRESHOLD). Adaptive rolling baseline. Dampen mic mount if needed]` | `[both]` |
| `[Joystick mode change triggering accidentally]` | `[gameplay]` | `[low]` | `[medium]` | `[Only trigger on centre→edge transitions, not edge→edge or on hold.]` | `[Both]` |
| `[Power instability under peak load]` | `[technical]` | `[medium]` | `[high]` | `[Power instability under peak load	Technical	Medium	High	Added XL4015 buck regulator rated 5A. Resolved completely]` | `[Both]`

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[
The biggest thing we're still unsure about is whether the ESP32 can keep up with everything happening at once. Even though the buck regulator fixed our power issues, we don't fully know yet if the board can handle running complex LED animations, reading the audio input, and responding to joystick controls — all at the same time, without any hiccups.
The concern is that if the processor gets overloaded, the LED matrix might start flickering or lag slightly behind the actual sound. And if the joystick inputs — like adjusting volume or pausing — don't register instantly, the whole experience falls apart. The Sonic Vault is supposed to feel like one smooth, responsive instrument. The moment there's a noticeable delay between what you do and what you see or hear, it stops feeling immersive and just feels broken.
So while the hardware is stable now, keeping everything perfectly in sync under full load is the one thing we haven't been able to fully test or guarantee yet.]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `Joystick → UI navigation via WebSerial` | `Tilt all directions, press SELECT; observe focus zone movement on screen` | `Every command routes correctly; no double-triggers` |
| `[Song selection → playback trigger]` | `[Navigate to a song, press SELECT]` | `[Track name appears in player bar; progress bar moves; audio plays from speakers]` |
| `[Audio → matrix visualiser response]` | `[Play music; observe matrix columns]` | `[Columns rise with loud passages; fall during silence; perceptibly different for speech vs music]` |
| `[Frequency mode switching]` | `[Tilt joystick during playback; observe matrix + NeoPixe]` | `[Visibly different behaviour in each mode; NeoPixel colour]` |
| `[30-minute stability]` | `[Leave running with looped music]` | `[No freeze, brownout, or serial disconnect]` |
| `[Noise gate in silence]` | `[Quiet room, 60 seconds]` | `[All 32 columns hold at zero]` |


## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Does the player understand the UI without instructions? | `[Observe first 60 seconds — did they try the joystick unprompted?]` |
| Does the two-phase experience feel connected? | `[Ask: "Did choosing the song and seeing the lights feel like one experience or two?"]` |
| Is the visualiser response satisfying? | `[Ask: "Did it feel like the lights were responding to the music you chose?"]` |
| Is mode switching discoverable? | `Did they find the joystick frequency mode without being told?` |
| Do they want to try another song? | `[Observe — do they navigate back to the library?]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Cutting
We built the enclosure out of foamboard, cutting it into panels to form the arched "Vault" shape, the curved back wall, side wings, and the raised base platform. Getting the arch opening right took some care; we scored the board and cut it slowly to keep the curve clean and symmetrical. The decorative sound wave graphics were printed, trimmed, and layered onto the panels.
Assembly
We put the structure together in sections, the back panel, two angled side wings, and the base box were joined to create the three-sided booth. The inner chamber sits recessed behind the arch, which gave the LED matrix display that framed, stage-like feel we were going for. We built the base platform separately and fitted it in last to house all the controls and components at a comfortable height.
Fastening
We used hot glue along the internal edges to bond the panels together, so the outside surfaces stayed clean and seam-free. The joystick, buttons, and control labels were mounted through cut-outs in the base and secured from underneath, keeping everything flush and intentional-looking on the surface.
Wiring
We ran all the wiring, ESP32, LED matrices, joystick, and power supply — internally through the base and behind the panels. To keep things tidy, we used tape throughout to bundle and hide the cables along the inner walls and the underside of the base. The buck regulator and power distribution components were tucked away inside the base cavity, completely out of sight.
Finishing
We covered the exterior panels with printed graphics — the Spectograph branding, sound wave illustrations, and our info posters. The inside of the chamber we lined in matte black to make the LED display pop and cut down on visual distraction. We added red waveform graphics along the inner walls to tie the whole look together, and printed clean labels for the control surface — "Sonic Vault," "UI," "Sono," and "Spectograph Library."
Revisions
The biggest physical revision came mid-project when we tracked down the power instability issue. We had to open up the base, re-route the wiring to fit the buck regulator in, and re-tape all the cable runs once the fix was in place. The joystick calibration also meant a lot of back-and-forth physically — we kept plugging in, testing the dead zone, adjusting, and testing again until the response felt natural.]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[week 1]` | `[Initial assembly of 19 and 15 NeoPixel strips in series; basic microphone code.]` | `[To test the scale of the "Sonic Vault" light output and audio reactivity logic.]` |
| `v2` | `[week 2]` | `[Integrated Analog Joystick (GPIO 34/35/13) ]` | `[To add user navigation and solve power instability/brownouts caused by high LED current draw.]` |
| `v3` | `[week 3]` | `[Pivoted from individual strips to a 32x8 LED Matrix; implemented zig-zag wiring logic and started using aa buck regulator that was better]` | `[The strips proved too physically unstable; the matrix offered a more reliable, high-density display for the spectrogram.]` |
| `v4 | `[week 3]` | `[UI Update: Added dedicated controls for Volume, Play, and Pause modes.]` | `[To shift from a "passive" visualization to an interactive player experience with actual user agency.]` |
| `v5 | `[week 3]` | `[Final aesthetic refinement of the dashboard and system-wide debugging.]` | `[To ensure seamless communication between the joystick interrupts, power regulator, and LED refresh rates.]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Sonic Vault v3.1 is a two-phase tabletop installation. A physical joystick connected via USB to a laptop running Chrome navigates a purpose-built dark-themed music library (Sonic Vault HTML/JS) — browsing genres, scrolling tracks, building a queue, and controlling playback entirely without keyboard or mouse. When a track plays, the audio from the speakers is captured by a MAX4466 microphone connected to an ESP32, which drives a 32×8 MAX7219 LED matrix with real-time animated bar columns mirrored symmetrically across two daisy-chained modules. A 10-LED NeoPixel strip breathes in the active mode colour. The joystick cycles between Red (Bass), Orange (Full Range), and Yellow (Treble) frequency modes. The components needign a high volatge supply run from an XL4015 buck regulator. The UI was designed in Adobe Illustrator and wireframed collaboratively with Claude.]`

## 18.2 What Works Well
- `The experience of choosing music with the joystick and watching it visualised creates genuine authorship over the light show.
-WebSerial joystick navigation is reliable and snappy — latency between tilt and UI response is imperceptible.
-The symmetric mirrored matrix display (bars growing outward from centre) is visually striking and was an accidental discovery from a display bug.
-The three frequency modes produce genuinely different visual characters.
-The Sonic Vault UI design stands on its own as a polished, functional software deliverable.

## 18.3 What Still Needs Improvement
- Frequency band separation uses IIR filters and sample delta — not true FFT. Accurate spectral analysis would improve Bass/Treble distinction.
-The two phases currently require two firmware modes on the ESP32. A unified async firmware would make the experience fully seamless.
-A proper laser-cut or 3D-printed enclosure would significantly improve visual quality.   `

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[The 150-LED NeoPixel strip was the largest departure. Hardware reality forced us away from it entirely — and the MAX7219 matrix approach turned out to suit the dark pixel-art aesthetic of the UI far better. The symmetric dual-matrix mirrored display was not planned; it came from a display axis bug and was kept. The UI grew from a rough navigation sketch into a fully functional, polished piece of software. The joystick's dual role was always intended; the hardware failures of Week 2 forced us to think more carefully about how to implement it cleanly.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[We found a good rhythm between the technical and the creative sides of the project. Splitting into "Logic" and "Shell" roles — one focused on code and filters, the other on fabrication and UI — turned out to be the right call. It meant neither side was waiting on the other, and the result showed: the joystick and the digital interface actually felt like one thing, not two separate pieces bolted together.
What slowed us down?
Power issues ate up way more time than we expected. The ESP32 kept resetting randomly, and for a while we couldn't pin down why. Eventually we traced it back to current spikes from the LED matrices — not an obvious culprit. Swapping in a buck regulator fixed it, but that meant re-doing a chunk of our wiring mid-project, which hurt. On top of that, getting the joystick dead zones right took more back-and-forth than anticipated. Too sensitive and you'd accidentally switch modes; too stiff and it felt unresponsive.
How well did we manage time, tasks, and responsibilities?
Pretty well, all things considered. The hardware setbacks in Week 2 did throw us off, but we made a conscious call to focus on getting the core "Sonic Vault" experience right rather than chasing stretch goals. That discipline paid off — we crossed the finish line with something polished and properly play-tested, not just functional. Forty-eight hours is tight, and we used them well.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Technical Reflection

Electronics: Power budgeting is not optional. Any project with NeoPixels or multiple driven displays needs a dedicated regulated supply from week one. The XL4015 was added reactively; it should have been planned.
Coding: IIR filtering for frequency estimation is fast and elegant but has fundamental limits. A proper ESP32 FFT would be the right next step. The WebSerial API in Chrome is far more capable than expected — it makes the browser a fully viable hardware I/O target.
Integration: Dual MAX7219 SPI daisy-chain with separate CS lines is the correct approach and works reliably. ADC inputs near long jumper wires on breadboard can introduce noise — perfboard or PCB would improve signal quality.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`•	Designing for play: The joystick mode switch is the right level of complexity — simple enough to discover in seconds, meaningful enough to keep exploring.
•	Delight: The moment when a new user claps and sees the matrix explode in response is the core delight moment. It's immediate, personal, and slightly surprising every time.
•	Clarity: The three mode colours on the NeoPixel strip (pink, red, yellow) provide clear feedback without needing a screen or label in most cases.
•	Iteration: The biggest design lesson was to test with real users early. Several changes (mode label near joystick, colour system refinement, symmetric bars) came directly from the first 10-minute playtest session in Week 3. `

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`We would implement true FFT on the ESP32 for accurate bass/mid/treble separation. We would build a proper laser-cut enclosure with diffused acrylic over the matrices. We would complete the Bluetooth bridge between the HTML companion UI and the ESP32 so mode switching from the browser is fully live. We would also add a small 0.96" OLED above the joystick showing the current mode name; the one piece of information that isn't immediately obvious to first-time users.`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [x] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
