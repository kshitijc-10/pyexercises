# Name: Kshitij Chavan
# Group: A  (file: scenarios_A.csv)
#
# ---------------------------------------------------------------------------
# 1. WHAT GOES IN?
#    scenarios_A.csv, separator is a comma ",". First line is a header.
#    14 columns: ID, Scenario, OptionA, OptionB, OptionC,
#    BudgetA, BudgetB, BudgetC, ReputationA, ReputationB, ReputationC,
#    FeedbackA, FeedbackB, FeedbackC.
#    The file is "wide": each option is spread over 4 columns. The impact of
#    option B is in OptionB + BudgetB + ReputationB + FeedbackB.
#    Numbers are plain integers (no "EUR", no thousands separator), negatives
#    use a minus sign (-800). They are read as text, so I convert them with int().
#    Texts with commas or quotes are wrapped in double quotes ("" = one quote).
#
# 2. WHAT HAPPENS? (one day)
#    - show the day number and both gauges
#    - show the situation and options A, B, C
#    - ask A, B or C until the answer is valid
#    - apply the budget and reputation change (reputation max 100)
#    - show the feedback line and the changes
#    - save the day in the history list (one tuple per day)
#    - check the streak bonus (my feature)
#    - if budget or reputation <= 0: fired, the game stops at once
#
# 3. WHAT COMES OUT?
#    At the end: "fired" and why, or the budget, reputation, score and title.
#    Then the best and worst move (biggest / smallest reputation change).
#    One line is appended to results.csv, for example:
#    Lea,6350,100,CMO Material,2026-11-03 19:55
#
# 4. WHAT COULD GO WRONG?
#    - Wrong key (d, 1, empty...): the program asks again until A, B or C.
#    - Lower case answer: accepted, I use .strip().upper().
#    - A gauge goes to 0 or below: the game stops at once, player is fired.
#    - Reputation above 100: it is capped at 100.
#    - Scenario file missing: a clear message is shown and the program stops
#      without crashing.
#    - Fewer than 10 scenarios in the file: the game plays as many as exist.
#    - Empty name: the player is called "Player".
#    - Ctrl+C (or Ctrl+Z / Ctrl+D) while typing: the game ends with a message, no crash.
#    - results.csv does not exist yet: it is created with a header line.
#
# FEATURE CHOSEN: a) Streak bonus - three reputation gains in a row give +500 EUR.
#    Why: it rewards players who keep a good reputation and gives a reason to
#    think about reputation every day, not only about money. It also helps
#    balance the game, because many good choices cost budget.
#
# MY THREE SCENARIOS: IDs 31, 32, 33 at the end of scenarios_A.csv.
# ---------------------------------------------------------------------------

import csv
import os
import random
import sys
from datetime import datetime

# Game settings from the brief
# The files are looked for in the same folder as this script,
# so the game works from any folder it is started in
GAME_FOLDER = os.path.dirname(os.path.abspath(__file__))
SCENARIO_FILE = os.path.join(GAME_FOLDER, "scenarios_A.csv")
RESULTS_FILE = os.path.join(GAME_FOLDER, "results.csv")
START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
STREAK_LENGTH = 3
STREAK_BONUS = 500


# Read the scenario file and return a list of dictionaries.
# Each scenario keeps its situation text and a list of 3 option tuples:
# (text, budget_change, reputation_change, feedback)
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = []
            for letter in "ABC":
                option = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
                options.append(option)
            scenarios.append({"situation": row["Scenario"], "options": options})
    return scenarios


# Read a line from the player. If the player presses Ctrl+C or Ctrl+Z/D,
# stop the game nicely instead of crashing.
def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. See you next quarter!")
        sys.exit(0)


# Ask the player's name, use "Player" if they type nothing.
def ask_name():
    name = safe_input("What is your name? ").strip()
    if name == "":
        name = "Player"
    return name


# Show the day number, both gauges, the situation and the 3 options.
def show_day(day, budget, reputation, scenario):
    print()
    print(f"--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(scenario["situation"])
    print()
    for letter, option in zip("ABC", scenario["options"]):
        print(f"   {letter}: {option[0]}")


# Ask A, B or C until the answer is valid, return the index 0, 1 or 2.
def ask_choice():
    answer = safe_input("Your choice (A, B or C): ").strip().upper()
    while answer not in ("A", "B", "C"):
        answer = safe_input("Please type A, B or C: ").strip().upper()
    return "ABC".index(answer)


# Apply the impact of one option to the gauges and return them as a tuple.
# Reputation can never go above 100.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# Turn a number into a text with its sign, like +20 or -2000.
def signed(number):
    return f"{number:+d}"


# Compute the final score and the title (only called if the player survived).
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score >= 140:
        title = "Viral Legend"
    elif score >= 120:
        title = "CMO Material"
    elif score >= 95:
        title = "Growth Hacker"
    else:
        title = "Eternal Intern"
    return score, title


# Find the best and worst move in the history.
# Each history tuple starts with the reputation change, so max() and min()
# compare on it first.
def best_and_worst(history):
    return max(history), min(history)


# Append one line to results.csv. Write the header if the file is new.
def save_result(name, budget, reputation, title):
    new_file = not os.path.exists(RESULTS_FILE)
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date])


# Main game: load, shuffle, play up to 10 days, then show and save the result.
def play_game():
    # Load the scenarios, stop cleanly if the file is missing or broken
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print(f"Error: the file {SCENARIO_FILE} was not found next to the game.")
        return
    except (KeyError, ValueError) as error:
        print(f"Error: {SCENARIO_FILE} is not in the expected format ({error}).")
        return
    if len(scenarios) == 0:
        print(f"Error: {SCENARIO_FILE} has no scenarios.")
        return

    print("=== SURVIVE THE QUARTER - Croissant Rocket ===")
    name = ask_name()

    random.shuffle(scenarios)
    days_to_play = min(DAYS, len(scenarios))

    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []     # one tuple per day: (reputation_change, day, option_text)
    streak = 0       # reputation gains in a row
    fired_reason = ""

    # One loop turn = one day
    for day in range(1, days_to_play + 1):
        scenario = scenarios[day - 1]
        show_day(day, budget, reputation, scenario)

        option = scenario["options"][ask_choice()]
        text, budget_change, reputation_change, feedback = option

        old_reputation = reputation
        budget, reputation = apply_choice(budget, reputation, option)
        real_reputation_change = reputation - old_reputation

        print(feedback)
        print(f"Budget {signed(budget_change)} EUR, Reputation {signed(real_reputation_change)}")

        history.append((real_reputation_change, day, text))

        # Feature: streak bonus, 3 reputation gains in a row = +500 EUR
        if real_reputation_change > 0:
            streak += 1
            if streak == STREAK_LENGTH:
                budget += STREAK_BONUS
                streak = 0
                print(f"Streak bonus! {STREAK_LENGTH} reputation gains in a row: +{STREAK_BONUS} EUR")
        else:
            streak = 0

        # Game over check: stop at once if a gauge is at 0 or less
        if budget <= 0 and reputation <= 0:
            fired_reason = "the bank account is empty and the internet hates you"
        elif budget <= 0:
            fired_reason = "the budget is gone"
        elif reputation <= 0:
            fired_reason = "the reputation hit zero"
        if fired_reason:
            break

    # End of the game: show the result
    print()
    print("=" * 30)
    if fired_reason:
        title = "Fired"
        print(f"You are fired on day {day}: {fired_reason}.")
        print(f"Budget: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"{name}, your title: {title}")
    else:
        score, title = get_title(budget, reputation)
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")

    # Best and worst move of the game
    print()
    best, worst = best_and_worst(history)
    print(f'Best move: day {best[1]}, "{best[2]}" ({signed(best[0])})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({signed(worst[0])})')

    # Save the result in results.csv
    try:
        save_result(name, budget, reputation, title)
        print(f"Saved in {os.path.basename(RESULTS_FILE)}")
    except OSError:
        print(f"Could not write to {RESULTS_FILE} (is it open in Excel?).")


# Start the game only when the file is run directly
if __name__ == "__main__":
    play_game()

