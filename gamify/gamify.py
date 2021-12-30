def get_cur_hedons():
    global cur_hedons
    return cur_hedons
def get_cur_health():
    global cur_health
    return cur_health
def offer_star(activity):
    global cur_star
    global star_counter
    global time_since_curstar
    global time_since_star
    global star_break
    global time_since_star1
    global time_since_star2
    global star_span
    time_since_curstar = 0
    star_counter += 1
    time_since_star = time_since_star1 + time_since_star2
    if time_since_star >= 120:
        star_counter += -1
        time_since_star1 = time_since_star2
        time_since_star2 = 0
        star_span = 1
        if star_counter > 2:
            cur_star = "none"
            star_break = "activated"
        elif activity == "running":
            cur_star = "running"
        elif activity == "textbooks":
            cur_star = "textbooks"
    elif time_since_curstar < 120:
        if star_counter > 2:
            cur_star = "none"
            star_break = "activated"
        elif activity == "running":
            cur_star = "running"
            star_span = star_counter
        elif activity == "textbooks":
            cur_star = "textbooks"
            star_span = star_counter


def perform_activity(activity, duration):
    global cur_health
    global cur_hedons
    global running_duration
    global running_counter
    global resting_duration
    global user_state
    global textbooks_duration
    global textbooks_counter
    global running_hed_counter
    global star_time
    global cur_star
    global star_counter
    global time_since_star
    global time_since_curstar
    global star_break
    global time_since_star1
    global time_since_star2
    global star_span
    global textbook_hed_counter
    if activity == "running":

        running_duration += duration
        resting_duration = 0
        textbook_hed_counter = 0
        textbooks_duration = 0
        textbooks_counter = 0
        if user_state == "tired" and cur_star != "running":

            cur_hedons += duration * (-2)
            cur_star = "none"
            time_since_curstar = "not zero"
            if running_duration <= 180:
                cur_health += duration*3
                user_state = "tired"
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration

            elif running_duration >180:
                running_counter += 1
                if running_counter == 1:
                    cur_health += (running_duration - 180) + 540 - (running_duration - duration) * 3
                    user_state = "tired"
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += (duration)
                    user_state = "tired"
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
        elif user_state == "not tired" and cur_star != "running":
            running_hed_counter += 1
            user_state = "tired"
            cur_star = "none"
            time_since_curstar = "not zero"
            if running_duration <= 10:
                cur_hedons += running_duration * 2
                user_state = "tired"
                cur_health += duration * 3
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                        time_since_star2 += duration
            elif running_duration > 10 and running_hed_counter == 1:
                cur_hedons += (running_duration - 10) * (-2) + 20
                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540 - (running_duration - duration) * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += duration

                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration


            else:
                cur_hedons += duration * (-1)
                user_state = "tired"

                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration

                elif running_counter != 1:
                    cur_health += (running_duration - 180) + 540 - (running_duration - duration) * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration

        elif cur_star == "running" and user_state == "not tired" and star_break != "activated" and time_since_curstar == 0:
            user_state = "tired"
            cur_star = "none"
            time_since_curstar = "not zero"
            if duration <= 10:
                cur_hedons += 5 * duration
                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540 - (running_duration - duration) * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += duration
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
            elif duration > 10:
                cur_hedons += (duration - 10) * (-2) + 50
                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540 - (running_duration - duration) * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += duration
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
        elif cur_star == "running" and user_state == "tired" and star_break != "activated" and time_since_curstar == 0:
            user_state = "tired"
            cur_star = "none"
            time_since_curstar = "not zero"
            if duration <= 10:
                cur_hedons += duration
                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += duration
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
            elif duration > 10:
                cur_hedons += (duration - 10) * (-2) + 10
                if running_duration <= 180:
                    cur_health += duration * 3
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                elif running_duration > 180 and running_counter == 1:
                    running_counter += 1
                    cur_health += (running_duration - 180) + 540
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration
                else:
                    cur_health += duration
                    if star_span == 1:
                        time_since_star1 += duration
                    elif star_span == 2:
                        time_since_star2 += duration




    elif activity == "textbooks":
        resting_duration = 0
        cur_health = cur_health + 2 * duration
        running_duration = 0
        running_counter = 0
        textbooks_counter += 1
        textbooks_duration += duration

        if user_state == "tired" and cur_star != "textbooks":
            cur_star = "none"
            cur_hedons += duration * (-2)
            time_since_curstar = "not zero"
            user_state = "tired"

            if star_span == 1:
                time_since_star1 += duration
            elif star_span == 2:
                time_since_star2 += duration


        elif user_state == "not tired" and cur_star == "textbooks" and star_break != "activated" and time_since_curstar == 0:
            cur_star = "none"
            time_since_curstar = "not zero"

            user_state = "tired"

            if duration <= 10:
                cur_hedons += 4 * duration
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration
            elif duration <= 20:
                cur_hedons += (duration - 10) + 40
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration
            elif duration > 20:
                cur_hedons += ((duration - 20) * (-1)) + 50
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration

        elif user_state == "tired" and cur_star == "textbooks" and star_break != "activated" and time_since_curstar == 0:
            cur_star = "none"
            user_state = "tired"
            time_since_curstar = "not zero"
            if duration <= 10:
                cur_hedons += duration
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration
            elif duration > 10:
                cur_hedons += (duration - 10) * (-2) + 10
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration

        elif user_state == "not tired" and cur_star != "textbooks":
            cur_star = "none"
            user_state = "tired"
            time_since_curstar = "not zero"
            if duration <= 20:
                cur_hedons += duration
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration
            elif duration > 20 and textbook_hed_counter == 0:
                textbook_hed_counter += 1
                cur_hedons += (duration - 20) * (-1) + 20
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration
            elif duration > 20 and textbook_hed_counter != 0:
                textbook_hed_counter += 1
                cur_hedons += (duration) * (-1)
                if star_span == 1:
                    time_since_star1 += duration
                elif star_span == 2:
                    time_since_star2 += duration



    elif activity == "resting":
        running_duration = 0
        textbook_hed_counter = 0
        running_counter = 0
        textbooks_duration = 0
        textbooks_counter = 0
        resting_duration += duration
        time_since_curstar = "not zero"
        cur_star = "none"
        if resting_duration >= 120:
            user_state = "not tired"
            if star_span == 1:
                time_since_star1 += duration
            elif star_span == 2:
                time_since_star2 += duration
        else:
            if star_span == 1:
                time_since_star1 += duration
            elif star_span == 2:
                time_since_star2 += duration



def star_can_be_taken(activity):
    global cur_star
    global star_break
    global time_since_curstar
    if star_break != "activated" and cur_star == activity and time_since_curstar == 0:
        return True
    else:
        return False

def most_fun_activity_minute():
    global user_state
    global cur_state
    global running_duration
    global textbooks_duration
    if (user_state == "not tired" and running_duration < 10) or cur_star == "running":
        return "running"
    elif cur_star == "textbooks" or (textbooks_duration < 20 and user_state == "not tired"):
        return "textbooks"
    else:
        return "resting"
def initialize():
    global cur_hedons
    cur_hedons = 0
    global cur_health
    cur_health = 0
    global running_duration
    running_duration = 0
    global running_counter
    running_counter = 0
    global textbooks_duration
    textbooks_duration = 0
    global resting_duration
    resting_duration = 0
    global user_state
    user_state = "not tired"
    global cur_star
    cur_star = "none"
    global textbooks_counter
    textbooks_counter = 0
    global running_hed_counter
    running_hed_counter = 0
    global star_time
    star_time = 0
    global star_counter
    star_counter = 0
    global time_since_star
    time_since_star = 0
    global time_since_curstar
    time_since_curstar = "not zero"
    global star_break
    star_break = "not activated"
    global time_since_star1
    time_since_star1 = 0
    global time_since_star2
    time_since_star2 = 0
    global star_span
    star_span = 0
    global textbook_hed_counter
    textbook_hed_counter = 0

# Variety of tests to verify most possible conditions of the game rules were met
if __name__=="__main__":
     initialize()
     perform_activity("running", 30)
     print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
     print(get_cur_health()) # 90 = 30 * 3
     print(most_fun_activity_minute()) #resting
     perform_activity("resting", 30)
     offer_star("running")
     print(most_fun_activity_minute()) # running
     perform_activity("textbooks", 30)
     print(get_cur_health()) # 150 = 90 + 30*2
     print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
     offer_star("running")
     perform_activity("running", 20)
     print(get_cur_health()) # 210 = 150 + 20 * 3
     print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
     perform_activity("running", 170)
     print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
     print(get_cur_hedons()) # -430 = -90 + 170 * (-2)
     offer_star("running")

     initialize()
     offer_star("running")
     perform_activity("running", 30)
     print(get_cur_health()) # 90 = 30*3
     print(get_cur_hedons()) # 10 = 5 * 10 + (20 * -2)
     perform_activity("running", 30)
     print(get_cur_health()) # 180 = 90 + 90
     print(get_cur_hedons()) # -50 = 10 + (-2 * 30
     print(star_can_be_taken("running")) # False
     offer_star("textbooks")
     perform_activity("resting", 90)
     offer_star("textbooks")
     print(star_can_be_taken("textbooks")) # True
     perform_activity("resting", 120)
     offer_star("running")
     print(star_can_be_taken("running")) #False
     perform_activity("running" , 180)
     print(get_cur_health()) #  720 = 180 + (180 * 3)
     print(get_cur_hedons()) # -340 = -50 + (50 * 10) + (-2 * 170)
     initialize()
     perform_activity("resting", 120)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("running")
     perform_activity("resting", 60)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("running")
     perform_activity("running", 30)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("textbooks")
     perform_activity("running", 10)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("textbooks", 130)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("textbooks")
     perform_activity("resting", 110)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 50)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("textbooks", 110)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("resting", 110)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("textbooks", 20)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("resting", 70)
     print(get_cur_health())
     print(get_cur_hedons())
     print("----------------------------------")
     initialize()
     perform_activity("running", 50)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("running")
     perform_activity("running", 40)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("running")
     offer_star("textbooks")
     perform_activity("textbooks", 60)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 60)
     print(get_cur_health())
     print(get_cur_hedons())
     print(most_fun_activity_minute())
     offer_star("textbooks")
     perform_activity("resting", 80)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("textbooks", 40)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("textbooks", 120)
     print(get_cur_health())
     print(get_cur_hedons())
     offer_star("textbooks")
     perform_activity("running", 20)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 70)
     print(get_cur_health())
     print(get_cur_hedons())
     print("----------------------------------")
     initialize()
     perform_activity("textbooks", 10)
     print(get_cur_health())
     print(get_cur_hedons())
     print(most_fun_activity_minute())
     offer_star("running")
     offer_star("running")
     offer_star("running")
     perform_activity("resting", 50)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("resting", 30)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("resting", 30)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("resting", 90)
     print(get_cur_health())
     print(get_cur_hedons())
     print(most_fun_activity_minute())
     offer_star("textbooks")
     perform_activity("textbooks", 30)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 50)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 70)
     print(get_cur_health())
     print(get_cur_hedons())
     perform_activity("running", 130)
     print(get_cur_health())
     print(get_cur_hedons())
     initialize()
     offer_star("textbooks")
     perform_activity("textbooks", 120)
     offer_star("running")
     offer_star("textbooks")
     print(star_can_be_taken("textbooks"))
     offer_star("textbooks")
     print(star_can_be_taken("textbooks"))




