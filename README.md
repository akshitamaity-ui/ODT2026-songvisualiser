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

- [ ] `[The joystick navigates genre list, song library, queue, and player controls via WebSerial without requiring keyboard or mouse]`
- [ ] `[Selecting a song and pressing SELECT begins playback and the LED matrix visualiser pick up the frequency and get triggered]`
- [ ] `[The LED matrix produces a real-time animated waveform that visually reacts to the music]`
- [ ] `[Joystick mode switching produces perceptibly different column behaviour for Bass, Full, and Treble]`
- [ ] `[The system runs continuously without freezing, dropping serial connection, or requiring a restart]`

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
`[Write here]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

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
`[Write here]`

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
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
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
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

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
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

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
`[Write here]`

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
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

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
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

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
