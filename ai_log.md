# AI Log: Survive the Quarter

**Student:** Kshitij Chavan, Group A
**AI tool:** Claude Code (in VS Code)
**Date:** 2026-11-03

This log follows the order of my conversation with the AI. My questions are copied exactly. The AI's answers are shortened, and the code it wrote is in the project files.

---

## 1. Giving the AI the assignment

**I asked:** I pasted the assignment instructions from Teams.

**AI answered:** The brief and the scenario file weren't in my folder yet, so it couldn't start. It asked for both and for my group letter. It also said that some parts have to come from me: my name, the four answers in my own words, the block comments, my three scenarios, playing the games, and this log.

---

## 2. Checking the AI understood

**I asked:**
> have you understood

**AI answered:** It summed up the game (10 days, budget and reputation, fired at 0) and the four deliverables. It said it still needed the brief and my scenario file.

---

## 3. Giving the brief and my scenario file

**I asked:** I attached `survive-the-quarter-brief.pdf` and `scenarios_A.csv`.

**AI answered:**
- It saved `scenarios_A.csv` in my project folder.
- It wrote a first version of `survive_the_quarter.py`. It covered all 11 points of the "What your game must do" slide and used feature **d (difficulty)**.
- It tested the game on a copy in a temporary folder: wrong keys, lowercase letters, an empty name, a game where the player is fired, and a game that is survived.
- It left the header as `TODO` and didn't answer the four questions, because the brief says they must be in my own words.

---

## 4. Pointing the AI at the deliverables

**I asked:** I sent screenshots of the "Deliverables", "What it looks like", "Technical requirements" and "Before you ask an AI anything" slides and wrote:
> keep in mind this instructions and deliverables

**AI answered:** It made a checklist of each technical requirement against the code: csv module, option tuples, `budget, reputation = apply_choice(...)`, a history of tuples for the best and worst move, at least 4 functions, no crash. It also listed what I still had to do myself.

---

## 5. Asking how to do my part

**I asked:**
> The code is done. You still need to fill in the header: your name, the four answers in your own words, and why you chose the feature. You also need to reword the block comments. how to do htis

**AI answered:** It gave me guiding questions for each of the four answers, not the answers themselves. For example: "What character separates the values? How many columns? How do you find the impact of option B?" It also suggested things to try so I could see what goes wrong (type `d`, leave the name empty, rename the CSV), and showed one example of rewording a comment.

---

## 6. What I changed myself

<!-- Fill this in yourself: only what YOU actually did and why. -->
- I wrote the header: my name, my answers to the four questions, my feature choice.
- I changed the feature from **d (difficulty)** to **a (streak bonus)** because: ...
- Other changes I made to the code: ...
- My three scenarios (31, 32, 33): ...

---

## 7. Asking for this log

**I asked:**
> I ALSO WANT TO CREATE CONVERSATION MD FILE WITH AI, WITH ALL THE RELEVANT QUESTIONS TAHT SHOULD BE ASKED IN THE GAME

**AI answered:** It created this file from our real conversation. It also checked my project and found that my header mentions scenarios 31–33, but they weren't in `scenarios_A.csv` yet.

---

<!-- Keep adding each new question and answer below as you go. -->
