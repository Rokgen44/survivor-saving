import random
import os
import time
three_tribes = False
men = []
women = []
jury = []
bootlist = []
challenge_wins = {}
votes_against = {}
season_titles = {}
all_contestants = []
days_lasted = {}
sole_survivors = []
all_contestants2 = {}
times_played = {}
contestants = []
tribe1 = []
tribe2 = []
tribe3 = []
merge = []
season_num = 0
day = 1
special = False
merge_game = False
finale = False
ranks = {}
challenge_winners = []
tribe_idol_count = 2
overall_idol_count = 3
idols = []
with open("castaways.txt") as file:
    for line in file:
        line = line.strip()
        all_contestants.append(line)
with open("player_season_num.txt") as file:
    for line in file:
        (key, val) = line.split()
        times_played[key] = int(val)
with open("castaway_days_lasted.txt") as file:
    for line in file:
        (key, val) = line.split()
        days_lasted[key] = int(val)
with open("season_titles.txt") as file:
    for line in file:
        (key, val) = line.split()
        season_titles[int(key)] = (val)
with open("last_season.txt") as file:
    for line in file:
        (key, val) = line.split()
        all_contestants2[key] = int(val)
with open("sole_survivors.txt") as file:
    for line in file:
        line = line.strip()
        sole_survivors.append(line)
print("Every Player:")
print(all_contestants)
print("The Number of Days each player has lasted:")
print(days_lasted)
print("The Number of Times Everyone Has Played:")
print(times_played)
print("The latest season each player participated in:")
print(all_contestants2)
print("The titles of each season:")
print(season_titles)
print("The most recent ranks that each player has placed:")
print(ranks)
print("The Sole Survivors:")
print(sole_survivors)

if os.stat("player_season_num.txt").st_size != 0:
    number = max(all_contestants2, key=all_contestants2.get)
    season_num += all_contestants2[number]
    print(season_titles[season_num], "is the most recently concluded season.")


def boot_list():
    global bootlist
    print('')
    print('Bootlist:')
    for x in range(0, len(bootlist)):
        print(str(x+1) + ' -th player voted out:', bootlist[x])
    return


while True:
    returnee_season = input("Will this be a returning player kind of season?")
    if returnee_season == "yes":
        special = True
    season_num += 1
    len_contestants = int(input("How many contestants will play this season?"))
    if (len_contestants % 2) != 0:
        while True:
            len_contestants = int(input("Please choose an even number of players."))
            if (len_contestants % 2) == 0:
                break
    if (len_contestants % 3) == 0:
        tribe_count = input("Would you like to have three tribes or two tribes (type in lettering, not numbers)?")
        if tribe_count == "three":
            three_tribes = True

    print("This season will have", len_contestants, "castaways vying for the million dollar prize!")
    title = input("What will this season be called?")
    print("Welcome to Survivor:", title + "!")
    season_titles[season_num] = title

    idol_lasting = int(input("What number of players will be the last time idols can be used?"))

    half_players = int((len_contestants)/2)
    for castaways in range(half_players):
        if special == True:
            season_look = int(input("What season do you want to look back at?"))
            for key, value in all_contestants2.items():
                if value == season_look:
                    print(key, str(ranks[key]), "-th place")
        name = input("What is this guy's name?")
        if name in contestants:
            while True:
                name = input("What is his ACTUAL name?")
                if name not in contestants:
                    break
        men.append(name)
        contestants.append(name)
        votes_against[name] = 0
        if name in all_contestants:
            times_played[name] += 1
            print(name, "is returning to play for his", str(times_played[name]) + "th time!")
        elif name not in all_contestants:
            times_played[name] = 1
            all_contestants.append(name)
        name2 = input("What is this girl's name?")
        if name2 in contestants:
            while True:
                name2 = input("What is her ACTUAL name?")
                if name2 not in contestants:
                    break
        women.append(name2)
        contestants.append(name2)
        votes_against[name2] = 0
        if name2 in all_contestants:
            times_played[name2] += 1
            print(name2, "is returning to play for her", str(times_played[name2]) + "th time!")
        elif name2 not in all_contestants:
            times_played[name2] = 1
            all_contestants.append(name2)
    if three_tribes == False:
        tribe_division = input("Would you like to divide the tribes by random, by choice or by gender? (type random/type choice/type gender)")
        if tribe_division == "gender":
            for many in men:
                tribe1.append(many)
            for many2 in women:
                tribe2.append(many2)
        elif tribe_division == "choice":
            for entire_length in range(half_players):
                member = input("Who will join the first tribe?")
                if member not in contestants:
                    while True:
                        member = input("Pick an actual player.")
                        if member in contestants:
                            break
                if member in tribe1:
                    while True:
                        member = input("Pick someone not already in the tribe, preferably someone in the game.")
                        if member not in tribe1:
                            if member in contestants:
                                break
                tribe1.append(member)
            for rest in contestants:
                if rest not in tribe1:
                    tribe2.append(rest)
        elif tribe_division == "random":
            if (half_players % 2) == 0:
                half_half = int(half_players/2)
                for majority in range(half_half):
                    member = random.choice(men)
                    if member in tribe1:
                        while True:
                            member = random.choice(men)
                            if member not in tribe1:
                                break
                    tribe1.append(member)
                    member2 = random.choice(women)
                    if member2 in tribe1:
                        while True:
                            member2 = random.choice(women)
                            if member2 not in tribe1:
                                break
                    tribe1.append(member2)
            elif (half_players % 2) != 0:
                half_players2 = half_players - 1
                half_half = int(half_players2/2)
                for majority in range(half_half):
                    member = random.choice(men)
                    if member in tribe1:
                        while True:
                            member = random.choice(men)
                            if member not in tribe1:
                                break
                    tribe1.append(member)
                    member2 = random.choice(women)
                    if member2 in tribe1:
                        while True:
                            member2 = random.choice(women)
                            if member2 not in tribe1:
                                break
                    tribe1.append(member2)
                member = random.choice(men)
                if member in tribe1:
                    while True:
                        member = random.choice(men)
                        if member not in tribe1:
                            break
                tribe1.append(member)
            for therest in contestants:
                if therest not in tribe1:
                    tribe2.append(therest)
    elif three_tribes == True:
        tribe_choices = input("Would you like it by choice or by random?")
        third = int((len(contestants))/3)
        if tribe_choices == "choice":
            for tribe_choosing in range(third):
                first_member = input("Who will join the first tribe (that is not already on the tribe)?")
                if first_member not in contestants:
                    while True:
                        first_member = input("Who will actually join the first tribe?")
                        if first_member in contestants:
                            break
                if first_member in tribe1:
                    while True:
                        first_member = input("Please pick someone not already on the tribe (an actual player).")
                        if first_member not in tribe1:
                            if first_member in contestants:
                                break
                tribe1.append(first_member)
            for tribe_choosing2 in range(third):
                second_member = input("Who will join the second tribe (that is not already on the tribe)?")
                if second_member not in contestants:
                    while True:
                        second_member = input("Who will actually join the first tribe?")
                        if second_member in contestants:
                            break
                if second_member in tribe1:
                    while True:
                        second_member = input("Please pick someone not already on a tribe (an actual player).")
                        if second_member not in tribe1:
                            if second_member in contestants:
                                break
                if second_member in tribe2:
                    while True:
                        second_member = input("Please pick an actual player not on a tribe.")
                        if second_member not in tribe2:
                            if second_member not in tribe1:
                                if second_member in contestants:
                                    break
                tribe2.append(second_member)
            for third_member in contestants:
                if third_member not in tribe1:
                    if third_member not in tribe2:
                        tribe3.append(third_member)
        elif tribe_choices == "random":
            third_half = int(third/2)
            for decisions in range(third_half):
                first_option = random.choice(men)
                if first_option in tribe1:
                    while True:
                        first_option = random.choice(men)
                        if first_option not in tribe1:
                            break
                tribe1.append(first_option)
                first_female = random.choice(women)
                if first_female in tribe1:
                    while True:
                        first_female = random.choice(women)
                        if first_female not in tribe1:
                            break
                tribe1.append(first_female)
            finaltwelve = []
            for allzacookies in contestants:
                if allzacookies not in tribe1:
                    finaltwelve.append(allzacookies)
            for new_options in range(third_half):
                second_option = random.choice(men)
                if second_option not in finaltwelve:
                    while True:
                        second_option = random.choice(men)
                        if second_option in finaltwelve:
                            break
                finaltwelve.remove(second_option)
                tribe2.append(second_option)
                second_female = random.choice(women)
                if second_female not in finaltwelve:
                    while True:
                        second_female = random.choice(women)
                        if second_female in finaltwelve:
                            break
                finaltwelve.remove(second_female)
                tribe2.append(second_female)
            for restacles in contestants:
                if restacles not in tribe1:
                    if restacles not in tribe2:
                        tribe3.append(restacles)

    print(tribe1)
    tribe1_name = input("What is this tribe's name?")
    print(tribe2)
    tribe2_name = input("What is this tribe's name?")
    if three_tribes == True:
        print(tribe3)
        tribe3_name = input("What is this tribe's name?")

    while merge_game == False:
        tribes = [tribe1_name, tribe2_name]
        if three_tribes == True:
            if len(tribe3) > 0:
                tribes.append(tribe3_name)
            elif len(tribe3) == 0:
                if tribe3_name in tribes:
                    tribes.remove(tribe3_name)
        if len(tribes) > 2:
            tribe_idol_count = 3
            overall_idol_count = 4
        else:
            tribe_idol_count = 2
            overall_idol_count = 3
        if tribe1_name in challenge_winners:
            print(tribe1_name, "- Immunity Winners!")
        else:
            print(tribe1_name)
        for alldem in tribe1:
            if alldem in idols:
                print(alldem, "holds a hidden immunity idol.")
            else:
                print(alldem)
        print("\n")
        if tribe2_name in challenge_winners:
            print(tribe2_name, "- Immunity Winners!")
        else:
            print(tribe2_name)
        for alldose in tribe2:
            if alldose in idols:
                print(alldose, "holds a hidden immunity idol.")
            else:
                print(alldose)
        print("\n")
        if len(tribes) > 2:
            if tribe3_name in challenge_winners:
                print(tribe3_name, "- Immunity Winners!")
            else:
                print(tribe3_name)
            for alldat in tribe3:
                if alldat in idols:
                    print(alldat, "holds a hidden immunity idol.")
                else:
                    print(alldat)
            print("\n")
        print("Day", day)
        print("\n")
        if len(idols) < tribe_idol_count:
            finding_idol1 = ["Yes"]
            finding_idol2 = ["Yes"]
            if len(tribes) > 2:
                finding_idol3 = ["Yes"]
                for nim3 in range(len(tribe3)):
                    finding_idol3.append("No")
                    has3 = 0
                    for lookers3 in tribe3:
                        if lookers3 in idols:
                            has3 += 1
            for allnim in range(len(tribe1)):
                finding_idol1.append("No")
            for nim2 in range(len(tribe2)):
                finding_idol2.append("No")
            has1 = 0
            has2 = 0
            for lookers in tribe1:
                if lookers in idols:
                    has1 += 1
            for lookers2 in tribe2:
                if lookers2 in idols:
                    has2 += 1
            if has1 == 0:
                idol_finding = random.choice(tribe1)
                found_or_not = random.choice(finding_idol1)
                if found_or_not == "Yes":
                    print(idol_finding, "has found the hidden immunity idol!")
                    idols.append(idol_finding)
            if has2 == 0:
                idol_finding = random.choice(tribe2)
                found_or_not = random.choice(finding_idol2)
                if found_or_not == "Yes":
                    print(idol_finding, "has found the hidden immunity idol!")
                    idols.append(idol_finding)
            if len(tribes) > 2:
                if has3 == 0:
                    idol_finding = random.choice(tribe3)
                    found_or_not = random.choice(finding_idol3)
                    if found_or_not == "Yes":
                        print(idol_finding, "has found the hidden immunity idol!")
                        idols.append(idol_finding)
        game = input("What will happen next? (Type 'day' to advance to the next day; Type 'challenge' to have the tribes compete; Type 'tribal' to have a tribe go vote someone off at Tribal Council; Type 'merge' to have the tribes merge; Type 'swap' to swap the tribes) ")
        if game == "day":
            day += 1
        elif game == "merge":
            print("Congratulations, you have made it to the merge!")
            for remainder in tribe1:
                merge.append(remainder)
            for remaining in tribe2:
                merge.append(remaining)
            if len(tribes) > 2:
                for remaindat in tribe3:
                    merge.append(remaindat)
            merge_game = True
        elif game == "swap":
            t1 = len(tribe1)
            t2 = len(tribe2)
            tribe1 = []
            tribe2 = []
            if three_tribes == True:
                tribe3 = []
            swaptions = ["equal", "current"]
            lenth = len(contestants)
            if len(tribes) > 2:
                if (lenth % 2) == 0:
                    half_players = int((lenth/2))
                    for members in range(half_players):
                        gamerz = random.choice(contestants)
                        if gamerz in tribe1:
                            while True:
                                gamerz = random.choice(contestants)
                                if gamerz not in tribe1:
                                    break
                        tribe1.append(gamerz)
                    for restdo in contestants:
                        if restdo not in tribe1:
                            tribe2.append(restdo)
                else:
                    ranger = int((len(contestants) - 1)/2)
                    for zim in range(ranger):
                        gamerz = random.choice(contestants)
                        if gamerz in tribe1:
                            while True:
                                gamerz = random.choice(contestants)
                                if gamerz not in tribe1:
                                    break
                        tribe1.append(gamerz)
                    for lasters in contestants:
                        if lasters not in tribe1:
                            tribe2.append(lasters)
            else:
                if (lenth % 2) == 0:
                    how_to = random.choice(swaptions)
                    if how_to == "equal":
                        half_players = int((lenth/2))
                        for members in range(half_players):
                            gamerz = random.choice(contestants)
                            if gamerz in tribe1:
                                while True:
                                    gamerz = random.choice(contestants)
                                    if gamerz not in tribe1:
                                        break
                            tribe1.append(gamerz)
                        for restdo in contestants:
                            if restdo not in tribe1:
                                tribe2.append(restdo)
                    elif how_to == "current":
                        for zim in range(t1):
                            gamerz = random.choice(contestants)
                            if gamerz in tribe1:
                                while True:
                                    gamerz = random.choice(contestants)
                                    if gamerz not in tribe1:
                                        break
                            tribe1.append(gamerz)
                        for restdo in contestants:
                            if restdo not in tribe1:
                                tribe2.append(restdo)
                elif (lenth % 2) != 0:
                    for zim in range(t1):
                        gamerz = random.choice(contestants)
                        if gamerz in tribe1:
                            while True:
                                gamerz = random.choice(contestants)
                                if gamerz not in tribe1:
                                    break
                        tribe1.append(gamerz)
                    for restdo in contestants:
                        if restdo not in tribe1:
                            tribe2.append(restdo)
            print("The new", tribe1_name)
            print(tribe1)
            print("The new", tribe2_name)
            print(tribe2)
        elif game == "challenge":
            if len(challenge_winners) == 0:
                print("And now we'll get to today's challenge.")
                time.sleep(2)
                for winning_challenges in range(len(tribes) - 1):
                    tribal_immunity = random.choice(tribes)
                    if tribal_immunity in challenge_winners:
                        while True:
                            tribal_immunity = random.choice(tribes)
                            if tribal_immunity not in challenge_winners:
                                break
                    print(tribal_immunity, "wins immunity and will not go to tribal council tonight!")
                    time.sleep(3.5)
                    challenge_winners.append(tribal_immunity)
        elif game == "tribal":
            if len(challenge_winners) != 0:
                if len(tribes) > 2:
                    if tribe1_name not in challenge_winners:
                        losers = tribe1
                        losersName = tribe1_name
                    elif tribe2_name not in challenge_winners:
                        losers = tribe2
                        losersName = tribe2_name
                    elif tribe3_name not in challenge_winners:
                        losers = tribe3
                        losersName = tribe3_name
                elif len(tribes) == 2:
                    if tribe1_name not in challenge_winners:
                        losers = tribe1
                        losersName = tribe1_name
                    elif tribe2_name not in challenge_winners:
                        losers = tribe2
                        losersName = tribe2_name
            else:
                lost = input("Who is attending Tribal Council? (type in the losing tribe's name)")
                while True:
                    if len(tribes) > 2:
                        if lost == tribe1_name:
                            losers = tribe1
                            losersName = tribe1_name
                            break
                        elif lost == tribe2_name:
                            losers = tribe2
                            losersName = tribe2_name
                            break
                        elif lost == tribe3_name:
                            losers = tribe3
                            losersName = tribe3_name
                    elif len(tribes) == 2:
                        if lost == tribe1_name:
                            losers = tribe1
                            losersName = tribe1_name
                            break
                        elif lost == tribe2_name:
                            losers = tribe2
                            losersName = tribe2_name
                            break
            print("Welcome to Tribal Council", losersName + ".")
            tallies = []
            vote_freq = {}
            tie = []

            for voters in losers:
                print("Who will", voters, "vote?")
                print(losers)
                vote = input("Type in the vote here. ")
                if vote not in losers:
                    while True:
                        vote = input("Who will they actually vote? ")
                        if vote in losers:
                            break
                tallies.append(vote)

            for choices in tallies:
                if vote_freq.get(choices) == None:
                    vote_freq[choices] = 1
                else:
                    vote_freq[choices] += 1

            if len(idols) > 0:
                print("If anyone has the hidden immunity idol and would like to play it, now would be the time to do so.")
                idol_play = input("Will anyone play the idol tonight?")
                if idol_play == "yes":
                    count = int(input("How many people?"))
                    for idol_plays in range(count):
                        idol_player = input("Who will play the idol?")
                        if idol_player not in idols:
                            print("This is NOT a hidden immunity idol. All votes against", idol_player, "will still count.")
                        elif idol_player in idols:
                            selfishornot = input("Will they play it for themself?")
                            if selfishornot == "yes":
                                print("This is a hidden immunity idol. Any votes against", idol_player, "will not count.")
                                idols.remove(idol_player)
                                challenge_winners.append(idol_player)
                                if idol_player in vote_freq:
                                    del vote_freq[idol_player]
                            elif selfishornot == "no":
                                played_for = input("Who will they play it for?")
                                if played_for not in losers:
                                    while True:
                                        played_for = input("Who are they actually playing it for?")
                                        if played_for in losers:
                                            break
                                print("This is a hidden immunity idol. Any votes against", played_for, "will not count.")
                                idols.remove(idol_player)
                                challenge_winners.append(played_for)
                                if played_for in vote_freq:
                                    del vote_freq[played_for]

            print(vote_freq)
            boot = max(vote_freq, key=vote_freq.get)

            for people in vote_freq:
                votes_against[people] += vote_freq[people]
                if vote_freq[people] == vote_freq[boot]:
                    tie.append(people)

            if len(tie) > 1:
                tied = []
                for thosem in tie:
                    tied.append(thosem)
                print("We have a tie. Here's what's gonna happen. There will be a revote.")
                tie = []
                tallies = []
                vote_freq = {}
                for voters in losers:
                    if voters not in tied:
                        print("Who will", voters, "vote?")
                        print(tied)
                        vote = input("Type in the vote here. ")
                        if vote not in losers:
                            while True:
                                vote = input("Who will they actually vote?")
                                if vote in losers:
                                    break
                        tallies.append(vote)

                for choices in tallies:
                    if vote_freq.get(choices) == None:
                        vote_freq[choices] = 1
                    else:
                        vote_freq[choices] += 1

                print(vote_freq)
                boot = max(vote_freq, key=vote_freq.get)

                for people in vote_freq:
                    if vote_freq[people] == vote_freq[boot]:
                        tie.append(people)

                if len(tie) > 1:
                    print("And we're deadlocked.")
                    if len(tie) == 2:
                        deadlock = input("Are we deciding by fire or rocks?")
                        if deadlock == "fire":
                            print("Here's what'll happen. The two of you will compete in a trial by fire. Loser is out of the game.")
                            fire_winner = random.choice(tie)
                            print(fire_winner, "makes fire first and this challenge is over.")
                            for those in tie:
                                if those != fire_winner:
                                    boot = those
                        elif deadlock == "rocks":
                            print("Alright. So, what's gonna happen is that those involved in the tie are now safe. The rest of you will reach into a bag and pick a rock. The person who picks the purple rock is out of the game.")
                            boot = random.choice(losers)
                            if boot in tie:
                                while True:
                                    boot = random.choice(losers)
                                    if boot not in losers:
                                        break
                            print(boot, "has picked the purple rock.")
                    else:
                        print("Alright. So, what's gonna happen is that those involved in the tie are now safe. The rest of you will reach into a bag and pick a rock. The person who picks the purple rock is out of the game.")
                        boot = random.choice(losers)
                        if boot in tie:
                            while True:
                                boot = random.choice(losers)
                                if boot not in tie:
                                    break
                        print(boot, "has picked the purple rock.")
            print(boot + ", the tribe has spoken. Time for you to go.")
            time.sleep(5)
            ranks[boot] = len(contestants)
            contestants.remove(boot)
            bootlist.append(boot)
            if boot not in days_lasted:
                days_lasted[boot] = day
            elif boot in days_lasted:
                days_lasted[boot] += day
            losers.remove(boot)
            challenge_winners = []
            if boot in idols:
                idols.remove(boot)
            if boot in men:
                men.remove(boot)
            elif boot in women:
                women.remove(boot)
            day += 1

    merge_tribe_name = input("What is the merged tribe name?")
    for mergers in merge:
        challenge_wins[mergers] = 0
    while finale == False:
        print(merge_tribe_name)
        for merged_players in merge:
            if merged_players in idols:
                print(merged_players, "holds a hidden immunity idol.")
            if merged_players in challenge_winners:
                print(merged_players, "has individual immunity.")
            elif merged_players not in idols:
                if merged_players not in challenge_winners:
                    print(merged_players)
        if len(jury) > 0:
            print("\n")
            print("The Jury")
            for jurors in jury:
                print(jurors)
        print("\n")
        print("Day", day)
        print("\n")
        if len(merge) >= idol_lasting:
            if len(idols) < overall_idol_count:
                finding_idol = ["Yes"]
                for allnim in range(len(merge)):
                    finding_idol.append("No")
                idol_finding = random.choice(merge)
                found_or_not = random.choice(finding_idol)
                if found_or_not == "Yes":
                    print(idol_finding, "has found the hidden immunity idol!")
                    idols.append(idol_finding)
        elif len(merge) < idol_lasting:
            idols = []
        game = input("What will happen next? (Type 'day' to advance to the next day; Type 'challenge' to have the players compete for individual immunity; Type 'tribal' to have the players go vote someone off at Tribal Council; Type 'finale' to have the last players head to their Final Tribal Council) ")
        if game == "day":
            day += 1
        elif game == "finale":
            print("Congratulations, you've gone as far as you can go in this game. The power now shifts to the jury. Players that you have voted out now hold your fate in their hands. Get ready for your Final Tribal Council.")
            finale = True
        elif game == "challenge":
            if len(challenge_winners) == 0:
                print("And now we'll get to today's challenge.")
                time.sleep(2)
                individual_immunity = random.choice(merge)
                print(individual_immunity, "wins individual immunity, will be safe tonight and has a 1 in", (len(contestants) - 1), "shot at winning this game!")
                time.sleep(5)
                challenge_winners.append(individual_immunity)
                challenge_wins[individual_immunity] += 1
        elif game == "tribal":
            print("Welcome to Tribal Council", merge_tribe_name + ".")
            if len(jury) > 0:
                print("We'll now bring in the members of our jury.")
                print(jury)

            tallies = []
            vote_freq = {}
            tie = []

            if len(merge) > 3:
                for voters in merge:
                    print("Who will", voters, "vote?")
                    print(merge)
                    vote = input("Type in the vote here. ")
                    if vote not in merge:
                        while True:
                            vote = input("Who will they actually vote? ")
                            if vote in merge:
                                break
                    if vote in challenge_winners:
                        while True:
                            vote = input("Who will you vote that is eligible to be voted out?")
                            if vote not in challenge_winners:
                                if vote in merge:
                                    break
                    tallies.append(vote)

            elif len(merge) == 3:
                for theone in challenge_winners:
                    print(theone, "has the sole vote tonight. They will vote the final person out and send them to the jury.")
                    print(merge)
                    vote = input("Who are they voting out?")
                    if vote not in merge:
                        while True:
                            vote = input("Who will they actually vote?")
                            if vote in merge:
                                if vote not in challenge_winners:
                                    break
                    tallies.append(vote)

            for choices in tallies:
                if vote_freq.get(choices) == None:
                    vote_freq[choices] = 1
                else:
                    vote_freq[choices] += 1

            if len(idols) > 0:
                print("If anyone has the hidden immunity idol and would like to play it, now would be the time to do so.")
                idol_play = input("Will anyone play the idol tonight?")
                if idol_play == "yes":
                    count = int(input("How many people?"))
                    for idol_plays in range(count):
                        idol_player = input("Who will play the idol?")
                        if idol_player not in idols:
                            print("This is NOT a hidden immunity idol. All votes against", idol_player, "will still count.")
                        elif idol_player in idols:
                            selfishornot = input("Will they play it for themself?")
                            if selfishornot == "yes":
                                print("This is a hidden immunity idol. Any votes against", idol_player, "will not count.")
                                idols.remove(idol_player)
                                if idol_player in vote_freq:
                                    del vote_freq[idol_player]
                            elif selfishornot == "no":
                                played_for = input("Who will they play it for?")
                                if played_for not in merge:
                                    while True:
                                        played_for = input("Who are they actually playing it for?")
                                        if played_for in merge:
                                            break
                                print("This is a hidden immunity idol. Any votes against", played_for, "will not count.")
                                idols.remove(idol_player)
                                if played_for in vote_freq:
                                    del vote_freq[played_for]

            print(vote_freq)
            boot = max(vote_freq, key=vote_freq.get)

            for people in vote_freq:
                votes_against[people] += vote_freq[people]
                if vote_freq[people] == vote_freq[boot]:
                    tie.append(people)

            if len(tie) > 1:
                tied = []
                for thosem2 in tie:
                    tied.append(thosem2)
                print("We have a tie. Here's what's gonna happen. There will be a revote.")
                tallies = []
                vote_freq = {}
                tie = []
                for voters in merge:
                    if voters not in tied:
                        print("Who will", voters, "vote?")
                        print(tied)
                        vote = input("Type in the vote here. ")
                        if vote not in merge:
                            while True:
                                vote = input("Who will they actually vote?")
                                if vote in merge:
                                    break
                        tallies.append(vote)

                for choices in tallies:
                    if vote_freq.get(choices) == None:
                        vote_freq[choices] = 1
                    else:
                        vote_freq[choices] += 1

                print(vote_freq)
                boot = max(vote_freq, key=vote_freq.get)

                for people in vote_freq:
                    if vote_freq[people] == vote_freq[boot]:
                        tie.append(people)

                if len(tie) > 1:
                    print("And we're deadlocked.")
                    if len(tie) == 2:
                        deadlock = input("Are we deciding by fire or rocks?")
                        if deadlock == "fire":
                            print("Here's what'll happen. The two of you will compete in a trial by fire. Loser is out of the game.")
                            fire_winner = random.choice(tie)
                            print(fire_winner, "makes fire first and this challenge is over.")
                            for those in tie:
                                if those != fire_winner:
                                    boot = those
                        elif deadlock == "rocks":
                            print("Alright. So, what's gonna happen is that those involved in the tie are now safe. The rest of you will reach into a bag and pick a rock. The person who picks the purple rock is out of the game.")
                            eligible = []
                            for manydooz in merge:
                                if manydooz not in merge:
                                    if manydooz not in challenge_winners:
                                        eligible.append(manydooz)
                            boot = random.choice(eligible)
                            print(boot, "has picked the purple rock.")
                    else:
                        print("Alright. So, what's gonna happen is that those involved in the tie are now safe. The rest of you will reach into a bag and pick a rock. The person who picks the purple rock is out of the game.")
                        eligible = []
                        for manydooz in merge:
                            if manydooz not in tie:
                                if manydooz not in challenge_winners:
                                    eligible.append(manydooz)
                        boot = random.choice(eligible)
                        print(boot, "has picked the purple rock.")
            print(boot + ", the tribe has spoken. Time for you to go.")
            time.sleep(5)
            ranks[boot] = len(contestants)
            contestants.remove(boot)
            bootlist.append(boot)
            jury.append(boot)
            if boot not in days_lasted:
                days_lasted[boot] = day
            elif boot in days_lasted:
                days_lasted[boot] += day
            merge.remove(boot)
            challenge_winners = []
            if boot in idols:
                idols.remove(boot)
            if boot in men:
                men.remove(boot)
            elif boot in women:
                women.remove(boot)
            day += 1


    for finalists in merge:
        if finalists not in days_lasted:
            days_lasted[finalists] = day
        elif finalists in days_lasted:
            days_lasted[finalists] += day
    print(merge)
    print("We'll now bring in our jury.")
    print(jury)
    print("Welcome to the Final Tribal Council. The jury will now vote for one of you to become the Sole Survivor and win the game.")
    tallies = []
    vote_freq = {}
    for juror in jury:
        print("Who will", juror, "vote to win?")
        print(merge)
        vote = input("Type in their vote for Sole Survivor here. ")
        if vote not in merge:
            while True:
                vote = input("Please type in the name of a vote out of the finalists. ")
                if vote in merge:
                    break
        tallies.append(vote)

    for choices in tallies:
        if vote_freq.get(choices) == None:
            vote_freq[choices] = 1
        else:
            vote_freq[choices] += 1

    sole_survivor = max(vote_freq, key=vote_freq.get)
    print("The winner of Survivor:", title, sole_survivor + "!")
    sole_survivors.append(sole_survivor)
    ranks[sole_survivor] = 1
    boot_list()

    for remains in merge:
        if remains not in vote_freq:
            vote_freq[remains] = 0

    for last in vote_freq:
        if last != sole_survivor:
            lastones = min(vote_freq, key=vote_freq.get)
            ranks[lastones] = len(merge)
            bootlist.append(lastones)

    bootlist.append(sole_survivor)

    for dama in bootlist:
        all_contestants2[dama] = str(season_num)

    end = input("Would you like to end here?")
    if end == "yes":
        break

print("Sole Survivors:", sole_survivors)
print("Times Played:", times_played)
print("Days Lasted:", days_lasted)
over = input("Ya sure?")
if over == "yes":
    with open("vote_count.txt", "a") as file:
        file.write(title)
        file.write("\n")
        for voting in votes_against:
            file.write(voting)
            file.write(" ")
            file.write(str(votes_against[voting]))
            file.write("\n")
    with open("challenge_wins.txt", "a") as file:
        file.write(title)
        file.write("\n")
        for strong in challenge_wins:
            file.write(strong)
            file.write(" ")
            file.write(str(challenge_wins[strong]))
            file.write("\n")
    with open("castaways.txt", "w") as file:
        for all2 in all_contestants:
            file.write(all2)
            file.write("\n")
    with open("player_season_num.txt", "w") as file:
        for damany in times_played:
            file.write(damany)
            file.write(" ")
            file.write(str(times_played[damany]))
            file.write("\n")
    with open("last_season.txt", "w") as file:
        for damany2 in all_contestants2:
            file.write(damany2)
            file.write(" ")
            file.write(str(all_contestants2[damany2]))
            file.write("\n")
    with open("castaway_recent_ranks.txt", "a") as file:
        file.write(title)
        file.write("\n")
        for damany3 in ranks:
            file.write(damany3)
            file.write(" ")
            file.write(str(ranks[damany3]))
            file.write("\n")
    with open("sole_survivors.txt", "w") as file:
        for all3 in sole_survivors:
            file.write(all3)
            file.write("\n")
    with open("castaway_days_lasted.txt", "w") as file:
        for damany4 in days_lasted:
            file.write(damany4)
            file.write(" ")
            file.write(str(days_lasted[damany4]))
            file.write("\n")
    with open("season_titles.txt", "w") as file:
        for damany5 in season_titles:
            file.write(str(damany5))
            file.write(" ")
            file.write(str(season_titles[damany5]))
            file.write("\n")
