def main():
    # checks if the user wants to see the full length names of each individual part of the exam instead of abbreviations
    if input("Enter Y or y to clarify abbreviations. ") in ("Y", "y"):
            for i in clarify_abbreviations():
                print(i)
    
    score = calc_score()
    print(check_score(score))

def calc_score():
    # Key is name, value is (weight, max_score)
    information = {
        "PT1-IRR": (0.1, 30),
        "PT1-TMP": (0.1, 24),
        "PT2-IWA": (0.245, 48),
        "PT2-IMP": (0.07, 36),
        "PT2-OD": (0.035, 12),
        "EOC-A": (0.135, 15),
        "EOC-B": (0.315, 24)
    }

    score = 0.0
    for name, value in information.items():
        weight, max_score = value
        user_input = 0.0
        # checks to see is user input is valid, if not, it will continue until it is
        while True:
            try:
                user_input = int(input(f"Enter score for {name}. Max possible score is {max_score}. "))
            except ValueError:
                print("Enter a number please.")
                continue
            if user_input < 0 or user_input > max_score:
                print(f"Enter a number between 0-{max_score}.")
                continue
            # at this point user input is valid
            break
        score += user_input * weight
        print(f"Your {score = }")  
    return score

def check_score(score):
    if score >= 26.32:
        return "You got a 5."
    elif score >= 22.65:
        return "You got a 4."
    elif score >= 18.99:
        return "You got a 3."
    elif score >= 15.33:
        return "You got a 2."
    return "You got a 1"

def clarify_abbreviations():
    return [ "PT1 -> Performance Task 1",
             "IRR -> Individual Research Report",
             "TMP -> Team Multimedia Presentation",
             "PT2 -> Performance Task 2",
             "IWA -> Individual Written Argument",
             "IMP -> Individual Multimedia Presentation",
             "OD  -> Oral Defense",
             "EOC -> End of Course Exam" ]

if __name__ == "__main__":
    main()