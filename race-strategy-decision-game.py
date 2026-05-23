print("🏎️ SHOULD FERRARI PIT?")
print("🔥 Welcome strategist.")

import random

score = 0
round_num = 1
streak = 0

while True:

    # RANDOM CONDITIONS
    print(f"\n🏁 ROUND {round_num}")


    position = random.randint(1, 22)
    
    rain = random.choice(["None", "Light", "Heavy"])

    tyre_age = random.randint(1, 40)

    laps_left = random.randint(1, 30)

    compound = random.choice(["Softs", "Mediums", "Hards"])

    sc = random.choice(["Yes", "No"])

    track = random.choice([
        "Melbourne",
        "Shanghai",
        "Suzuka",
        "Jeddah",
        "Miami",
        "Montreal",
        "Monaco",
        "Barcelona",
        "Red Bull Ring",
        "Silverstone",
        "Spa",
        "Budapest",
        "Zandvoort",
        "Monza",
        "Madrid",
        "Baku",
        "Singapore",
        "Austin",
        "Mexico",
        "São Paulo",
        "Las Vegas",
        "Qatar",
        "Abu Dhabi"
    ])

    radio = random.choice([
        "📻 DRS Available",
        "📻 Pitlane getting busy now",
        "📻 Box, Box, Box",
        "📻 Stay out, Stay out, Stay out",
        "📻 This could be a gamble strategy",
        "📻 We need to make the decision now",
        "📻 Push now, push",
        "📻 Mode full push, full push",
        "📻 We need clean air",
        "📻 We are reviewing Plan B",
        "📻 These next laps are crucial",
        "📻 This could decide the race",
        "📻 You are racing the car behind",
        "📻 Track position is crucial",
        "📻 Must be the water"
    ])

    # DISPLAY SCENARIO

    
    print (f"Track Position: P{position}")
    print(f"🌍 Track: {track}")
    print(radio)

    print(f"🌧️ Rain: {rain}")
    print(f"🚨 Safety Car: {sc}")

    print(f"🛞 Tyre Age: {tyre_age}")
    print(f"🏁 Laps Left: {laps_left}")
    print(f"🔘 Tyre Compound: {compound}")

        # PLAYER DECISION

    decision = input("\nDecision (Pit / Stay Out): ").title().strip()

        # STRATEGY LOGIC

        # SAFETY CAR + RAIN COMBINED

    if sc == "Yes":

            if rain == "Heavy":
                correct = "Pit"

            elif rain == "Light":

                if laps_left <= 3:
                    correct = "Stay Out"

                elif tyre_age >= 10:
                    correct = "Pit"

                else:
                    correct = "Stay Out"

            else:

                if tyre_age >= 8:
                    correct = "Pit"

                else:
                    correct = "Stay Out"

        # NORMAL RACE CONDITIONS

    elif rain == "Heavy":

            correct = "Pit"

    elif rain == "Light":

            if laps_left <= 3:
                correct = "Stay Out"

            elif compound == "Softs" and tyre_age >= 12:
                correct = "Pit"

            elif compound == "Mediums" and tyre_age >= 18:
                correct = "Pit"

            elif compound == "Hards" and tyre_age >= 25:
                correct = "Pit"

            else:
                correct = "Stay Out"

    elif rain == "None":

            if laps_left <= 5:
                correct = "Stay Out"

            elif compound == "Softs" and tyre_age >= 15:
                correct = "Pit"

            elif compound == "Mediums" and tyre_age >= 22:
                correct = "Pit"

            elif compound == "Hards" and tyre_age >= 30:
                correct = "Pit"

            else:
                correct = "Stay Out"

        # RESULT

    if decision == correct:

            print("\n✅ GOOD STRATEGY")

            score += 10
            streak += 1

    else:

            print("\n❌ FERRARI MOMENT LOL")

            score -= 5
            streak -= 1

    print(f"👉 Correct Strategy: {correct}")

    print(f"🏆 Current Points: {score}")
    print(f"🔥 Strategy Streak: {streak}")
    round_num += 1
    input("\n⏭️ Press Enter for next round...")

    print("\n" * 3)



        


                



            