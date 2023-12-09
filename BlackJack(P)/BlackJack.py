import tkinter
import tkinter.messagebox
import random
import copy
def toggle() :
    state = toggle_var.get()
    if state == 0 :
        mat.delete("Rule")
    else :
        mat.create_image(250, 350, image = Rule, tag = "Rule")  
def click_B() :
    global B_chip, K_chip, R_chip, RY_chip
    if K_chip > 0 :
        B_chip += 10
        K_chip -= 1
        mat.delete("B_chip")
        mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
        mat.delete("K_chip")
        mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
    elif R_chip > 0 :
        B_chip += 100
        R_chip -= 1
        mat.delete("B_chip")
        mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
        mat.delete("R_chip")
        mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
    elif RY_chip > 0 :
        B_chip += 1000
        RY_chip -= 1
        mat.delete("B_chip")
        mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
        mat.delete("R_chip")
        mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
def click_K() :
    global B_chip, K_chip, R_chip, RY_chip
    if R_chip > 0 :
        K_chip += 10
        R_chip -= 1
        mat.delete("K_chip")
        mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
        mat.delete("R_chip")
        mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
    elif RY_chip > 0 :
        K_chip += 100
        RY_chip -= 1
        mat.delete("K_chip")
        mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
        mat.delete("RY_chip")
        mat.create_text(437, 805, text = ("%d" %(RY_chip)), font = ("impact", 12), fill = "white", tag = "RY_chip")
def click_R() :
    global B_chip, K_chip, R_chip, RY_chip
    if RY_chip > 0 :
        R_chip += 10
        RY_chip -= 1
        mat.delete("R_chip")
        mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
        mat.delete("RY_chip")
        mat.create_text(437, 805, text = ("%d" %(RY_chip)), font = ("impact", 12), fill = "white", tag = "RY_chip")
def calculate_case():
    global p_D, p_H, c_H, num
    if stage == 10:
        Dcalculate(Cardcount[p_D])
    elif stage == 14:
        Pcalculate(Cardcount[p_H[num]])
    elif stage == 16:
        Ccalculate(Cardcount[c_H[num]])
def Dcalculate(card_v):
    global p_open1, p_open2, DP_result
    if card_v == 11:
        if Cardcount[p_open1] == 11:
            DP_result -= 10
            if DP_result > 21:
                p_open1 = 'A1'
                DP_result -= 10
        else : 
            if Cardcount[p_open2] == 11:
                DP_result -= 10
                if DP_result > 21:
                    p_open2 = 'A1'
                    DP_result -= 10
            else:
                DP_result -= 10
                if DP_result > 21:
                    DP_result += 0
    else :
        if Cardcount[p_open1] == 11:
            p_open1 = 'A1'
            DP_result -= 10
        else :
            if Cardcount[p_open2] == 11:
                p_open2 = 'A1'
                DP_result -= 10
            else:
                DP_result += 0
def Pcalculate(card_v):
    global p_open1, p_open2, P_result, num, p_H
    if card_v == 11 :
        if Cardcount[p_open1] == 11 :
            p_H[num] = 'A1'
            P_result -= 10
            if P_result > 21:
                p_open1 = 'A1'
                P_result -= 10
                if P_result > 21:
                    for i in range(num) :
                        if Cardcount[p_H[i]] == 11 :
                            p_H[i] = 'A1'
                            P_result -= 10
                            if P_result < 21:
                                break
        else : 
            if Cardcount[p_open2] == 11 :
                p_H[num] = 'A1'
                P_result -= 10
                if P_result > 21:
                    p_open2 = 'A1'
                    P_result -= 10
                    if P_result > 21:
                        for i in range(num) :
                            if Cardcount[p_H[i]] == 11 :
                                p_H[i] = 'A1'
                                P_result -= 10
                                if P_result < 21:
                                    break
            else:
                p_H[num] = 'A1'
                P_result -= 10
                if P_result > 21 :
                    for i in range(num) :
                        if Cardcount[p_H[i]] == 11 :
                            p_H[i] = 'A1'
                            P_result -= 10
                            if P_result < 21:
                                break
    else :
        if Cardcount[p_open1] == 11 :
            p_open1 = 'A1'
            P_result -= 10
            if P_result > 21 :
                for i in range(num) :
                    if Cardcount[p_H[i]] == 11 :
                        p_H[i] = 'A1'
                        P_result -= 10
                        if P_result < 21:
                            break
        else :
            if Cardcount[p_open2] == 11 :
                p_open2 = 'A1'
                P_result -= 10
                if P_result > 21 :
                    for i in range(num) :
                        if Cardcount[p_H[i]] == 11 :
                            p_H[i] = 'A1'
                            P_result -= 10
                            if P_result < 21:
                                break
def Ccalculate(card_v):
    global c_open1, c_open2, C_result, num, c_H
    if card_v == 11 :
        if Cardcount[c_open1] == 11 :
            c_H[num] = 'A1'
            C_result -= 10
            if C_result > 21:
                c_open1 = 'A1'
                C_result -= 10
                if C_result > 21:
                    for i in range(num) :
                        if Cardcount[c_H[i]] == 11 :
                            c_H[i] = 'A1'
                            C_result -= 10
                            if C_result < 21:
                                break
        else : 
            if Cardcount[c_open2] == 11 :
                c_H[num] = 'A1'
                C_result -= 10
                if C_result > 21:
                    c_open2 = 'A1'
                    C_result -= 10
                    if C_result > 21:
                        for i in range(num) :
                            if Cardcount[c_H[i]] == 11 :
                                c_H[i] = 'A1'
                                C_result -= 10
                                if C_result < 21:
                                    break
            else:
                c_H[num] = 'A1'
                C_result -= 10
                if C_result > 21 :
                    for i in range(num) :
                        if Cardcount[c_H[i]] == 11 :
                            c_H[i] = 'A1'
                            C_result -= 10
                            if C_result < 21:
                                break
    else :
        if Cardcount[c_open1] == 11 :
            c_open1 = 'A1'
            C_result -= 10
            if C_result > 21 :
                for i in range(num) :
                    if Cardcount[c_H[i]] == 11 :
                        c_H[i] = 'A1'
                        C_result -= 10
                        if C_result < 21:
                            break
        else :
            if Cardcount[c_open2] == 11 :
                c_open2 = 'A1'
                C_result -= 10
                if C_result > 21 :
                    for i in range(num) :
                        if Cardcount[c_H[i]] == 11 :
                            c_H[i] = 'A1'
                            C_result -= 10
                            if P_result < 21:
                                break
def exchange_case(C) :
    global betting, insurance
    if C == 0 :
        exchange_lose(betting)
    if C == 1 :
        insurance *= 2
        exchange_win(insurance)
    if C == 2 :
        betting *= 2
        exchange_win(betting)
    if C == 3 :
        betting *= 3
        exchange_win(betting)
    if C == 4 :
        exchange_lose(insurance)
    if C == 5 :
        exchange_win(betting)
    if C == 6 :
        exchange_lose(doublebet)
def exchange_lose(bet) :
    global money, B_chip, K_chip, R_chip, RY_chip
    money -= bet
    mat.delete("money")
    mat.create_text(265, 852, text = ("%d" %(money)), font = ("impact", 18), fill = "white", tag = "money")
    if bet <= 9000 :
        B_chip -= bet // 1000
    elif bet >= 10000 and bet <= 90000 :
        if bet // 10000 <= K_chip and bet % 10000 == 0 :
            K_chip -= bet // 10000
        elif bet // 10000 <= K_chip and bet % 10000 != 0 :
            K_chip -= bet // 10000
            B_chip -= (bet % 10000) // 1000
        else :
            B_chip -= (bet - K_chip * 10000) // 1000
            K_chip -= K_chip
    elif bet >= 100000 and bet <= 900000 :
        if bet // 100000 <= R_chip and bet % 100000 == 0 :
            R_chip -= bet // 100000
        elif bet // 100000 <= R_chip and bet % 100000 != 0 :
            R_chip -= bet // 100000
            if (bet % 100000) // 10000 <= K_chip and (bet % 100000) % 10000 == 0 :
                K_chip -= (bet % 100000) // 10000
            elif (bet % 100000) // 10000 <= K_chip and (bet % 100000) % 10000 != 0 :
                K_chip -= (bet % 100000) // 10000
                B_chip -= ((bet % 100000) % 10000) // 1000
            else :
                B_chip -= (bet % 100000 - K_chip * 10000) // 1000
                K_chip -= K_chip
        else :
            if (bet - R_chip * 100000) // 10000 <= K_chip and (bet - R_chip * 100000) % 10000 == 0 :
                K_chip -= (bet - R_chip * 100000) // 10000
                R_chip -= R_chip
            elif (bet - R_chip * 100000) // 10000 <= K_chip and (bet - R_chip * 100000) % 10000 != 0 :
                K_chip -= (bet - R_chip * 100000) // 10000
                B_chip -= ((bet - R_chip * 100000) % 10000) // 1000
                R_chip -= R_chip
            else :
                B_chip -= (bet - R_chip * 100000 - K_chip * 10000) // 1000
                R_chip -= R_chip
                K_chip -= K_chip
    else :
        if bet // 1000000 <= RY_chip and bet % 1000000 == 0 :
            RY_chip -= bet // 1000000
        elif bet // 1000000 <= RY_chip and bet % 1000000 != 0 :
            RY_chip -= bet // 1000000
            if (bet % 1000000) // 100000 <= R_chip and (bet % 1000000) % 100000 == 0 :
                R_chip -= (bet % 1000000) // 100000
            elif (bet % 1000000) // 100000 <= R_chip and (bet % 1000000) % 100000 != 0 :
                R_chip -= (bet % 1000000) // 100000
                if ((bet % 1000000) % 100000) // 10000 <= K_chip and ((bet % 1000000) % 100000) % 10000 == 0 :
                    K_chip -= ((bet % 1000000) % 100000) // 10000
                elif ((bet % 1000000) % 100000) // 10000 <= K_chip and ((bet % 1000000) % 100000) % 10000 != 0 :
                    K_chip -= ((bet % 1000000) % 100000) // 10000
                    B_chip -= (((bet % 1000000) % 100000) % 10000) // 1000
                else :
                    B_chip -= (((bet % 1000000) % 100000) - K_chip * 10000) // 1000
                    K_chip -= K_chip
            else :
                if ((bet % 1000000) - R_chip * 100000) // 10000 <= K_chip and ((bet % 1000000) - R_chip * 100000) % 10000 == 0 :
                    K_chip -= ((bet % 1000000) - R_chip * 100000) // 10000
                    R_chip -= R_chip
                elif ((bet % 1000000) - R_chip * 100000) // 10000 <= K_chip and ((bet % 1000000) - R_chip * 100000) % 10000 != 0 :
                    K_chip -= ((bet % 1000000) - R_chip * 100000) // 10000
                    B_chip -= (((bet % 1000000) - R_chip * 100000) % 10000) // 1000
                    R_chip -= R_chip
                else :
                    B_chip -= ((bet % 1000000) - R_chip * 100000 - K_chip * 10000) // 1000
                    R_chip -= R_chip
                    K_chip -= K_chip
        else :
            if (bet - RY_chip * 1000000) // 100000 <= R_chip and (bet - RY_chip * 1000000) % 100000 == 0 :
                R_chip -= (bet - RY_chip * 1000000) // 100000
                RY_chip -= RY_chip
            elif (bet - RY_chip * 1000000) // 100000 <= R_chip and (bet - RY_chip * 1000000) % 100000 != 0 :
                R_chip -= (bet - RY_chip * 1000000) // 100000
                if ((bet - RY_chip * 1000000) % 100000) // 10000 <= K_chip and ((bet - RY_chip * 1000000) % 100000) % 10000 == 0 :
                    K_chip -= ((bet - RY_chip * 1000000) % 100000) // 10000
                    RY_chip -= RY_chip
                elif ((bet - RY_chip * 1000000) % 100000) // 10000 <= K_chip and ((bet - RY_chip * 1000000) % 100000) % 10000 != 0 :
                    K_chip -= ((bet - RY_chip * 1000000) % 100000) // 10000
                    B_chip -= (((bet - RY_chip * 1000000) % 100000) % 10000) // 1000
                    RY_chip -= RY_chip
                else :
                    B_chip -= (((bet - RY_chip * 1000000) % 100000) - K_chip * 10000) // 1000
                    RY_chip -= RY_chip
                    K_chip -= K_chip
            else :
                if ((bet - RY_chip * 1000000) - R_chip * 100000) // 10000 <= K_chip and ((bet - RY_chip * 1000000) - R_chip * 100000) % 10000 == 0 :
                    K_chip -= ((bet - RY_chip * 1000000) - R_chip * 100000) // 10000
                    RY_chip -= RY_chip
                    R_chip -= R_chip
                elif ((bet - RY_chip * 1000000) - R_chip * 100000) // 10000 <= K_chip and ((bet - RY_chip * 1000000) - R_chip * 100000) % 10000 != 0 :
                    K_chip -= ((bet - RY_chip * 1000000) - R_chip * 100000) // 10000
                    B_chip -= (((bet - RY_chip * 1000000) - R_chip * 100000) % 10000) // 1000
                    RY_chip -= RY_chip
                    R_chip -= R_chip
                else :
                    B_chip -= (((bet - RY_chip * 1000000) - R_chip * 100000) - K_chip * 10000) // 1000
                    RY_chip -= RY_chip
                    R_chip -= R_chip
                    K_chip -= K_chip
    mat.delete("B_chip")
    mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
    mat.delete("K_chip")
    mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
    mat.delete("R_chip")
    mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
    mat.delete("RY_chip")
    mat.create_text(437, 805, text = ("%d" %(RY_chip)), font = ("impact", 12), fill = "white", tag = "RY_chip")
def exchange_win(bet) :
    global money, B_chip, K_chip, R_chip, RY_chip
    money += bet
    mat.delete("money")
    mat.create_text(265, 852, text = ("%d" %(money)), font = ("impact", 18), fill = "white", tag = "money")
    if bet <= 9000 :
        B_chip += bet // 1000
    elif bet >= 10000 and bet <= 90000 :
        if bet % 10000 == 0 :
            K_chip += bet // 10000
        else :
            K_chip += bet // 10000
            B_chip += (bet % 10000) // 1000
    elif bet >= 100000 and bet <= 900000 :
        if bet % 100000 == 0 :
            R_chip += bet // 100000
        elif (bet % 100000) % 10000 == 0 : 
            R_chip += bet // 100000
            K_chip += (bet % 100000) // 10000
        else :
            R_chip += bet // 100000
            K_chip += (bet % 100000) // 10000
            B_chip += ((bet % 100000) % 10000) // 1000
    else :
        if bet % 1000000 == 0 :
            RY_chip += bet // 1000000
        elif (bet % 1000000) % 100000 == 0 : 
            RY_chip += bet // 1000000
            R_chip += (bet % 1000000) // 100000
        elif ((bet % 1000000) % 100000) % 10000 == 0 :
            RY_chip += bet // 1000000
            R_chip += (bet % 1000000) // 100000
            K_chip += ((bet % 1000000) % 100000) // 10000
        else :
            RY_chip += bet // 1000000
            R_chip += (bet % 1000000) // 100000
            K_chip += ((bet % 1000000) % 100000) // 10000
            B_chip += (((bet % 1000000) % 100000) % 10000) // 1000
    mat.delete("RY_chip")
    mat.create_text(437, 805, text = ("%d" %(RY_chip)), font = ("impact", 12), fill = "white", tag = "RY_chip")
    mat.delete("R_chip")
    mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
    mat.delete("K_chip")
    mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
    mat.delete("B_chip")
    mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
def mouse_move(e) :
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
def mouse_press(e) :
    global mouse_c
    mouse_c = 1
def main_proc() :
    global stage, mouse_c, B_chip, K_chip, R_chip, RY_chip, money, betting, timer, num, pnum, cnum, x, pb, cb
    global card, p_open1, p_open2, c_open1, c_open2, doublebet, insurance, p_D, p_H, c_H, DP_result, P_result, C_result
    Button_rule.place(x=2, y=2)
    card = copy.deepcopy(BaseCard)
    if stage == 0 :
        if mouse_c == 1 :
            if 501 < mouse_x and mouse_x < 801 and 529 < mouse_y and mouse_y < 679 :
                mouse_c = 0
                mat.delete("title")
                mat.create_image(650, 450, image = bg, tag = "exchange")
                mat.create_text(650, 70, text = "   초기 자본금을 설정하세요.\n최대: 500만원 / 최소: 5,000원", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                set_m.place(x = 550, y = 160)
                stage = 1
    elif stage == 1 :
        timer += 1
        if timer == 13 :
            mouse_c = 0
        if timer == 15 :
            mat.delete("Q")
            mat.create_text(650, 70, text = "   초기 자본금을 설정하세요.\n최대: 500만원 / 최소: 5,000원", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
        if mouse_c == 1 :
            if 551 < mouse_x and mouse_x < 751 and 321 < mouse_y and mouse_y < 401 :
                money = int(set_m.get())
                if money < 5000 or money > 5000000 :
                    mat.delete("Q")
                    mat.create_text(650, 70, text = "최소 및 최대 금액 안에서 설정하시요", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    stage = 1
                    timer = 0
                    mouse_c = 0
                else :
                    set_m.destroy()
                    mat.delete("Q")
                    mat.create_text(650, 70, text = ("설정 자본금: %d원" %(money)), font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    stage = 2
                    timer = 0
                    mouse_c = 0 
    elif stage == 2 :
        timer += 1
        if timer == 15 :
            mat.delete("Q")
            mat.create_text(650, 70, text = ("교환할 칩 갯수를 선택하시요, 0개는 0으로 표기\n\t      자본금: %d원" %(money)), font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
            set_CB.place(x = 320, y = 620)
            set_CK.place(x = 515, y = 620)
            set_CR.place(x = 710, y = 620)
            set_CRY.place(x = 905, y = 620)
            timer = 0
            mouse_c = 0
            stage = 3
    elif stage == 3 :
        timer += 1
        if timer == 15 :
            mat.delete("Q")
            mat.create_text(650, 70, text = ("교환할 칩 갯수를 선택하시요, 0개는 0으로 표기\n\t      자본금: %d원" %(money)), font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
        if timer == 30 :
            mouse_c = 0
        if mouse_c == 1 :
            if 551 < mouse_x and mouse_x < 751 and 321 < mouse_y and mouse_y < 401 :
                B_chip = int(set_CB.get())
                K_chip = int(set_CK.get())
                R_chip = int(set_CR.get())
                RY_chip = int(set_CRY.get())
                if money == 1000000 * RY_chip + 100000 * R_chip + 10000 * K_chip + 1000 * B_chip :
                    mat.delete("Q")
                    mat.create_text(650, 70, text = "칩 교환 완료", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    stage = 4
                    timer = 0
                    mouse_c = 0
                elif money < 1000000 * RY_chip + 100000 * R_chip + 10000 * K_chip + 1000 * B_chip :
                    mat.delete("Q")
                    mat.create_text(650, 70, text = "자본금보다 많은 금액입니다\n       다시 입력 하세요", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    stage = 3
                    timer = 0
                    mouse_c = 0
                elif 1000000 * RY_chip + 100000 * R_chip + 10000 * K_chip + 1000 * B_chip < 5000 :
                    mat.delete("Q")
                    mat.create_text(650, 70, text = "최소 5,000원 이상 소지해야 입장 할 수 있습니다", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    stage = 3
                    timer = 0
                    mouse_c = 0
                else :
                    mat.delete("Q")
                    mat.create_text(650, 70, text = "\t칩 교환 완료\n나머지 금액은 반환되었습니다", font = ("맑은 고딕", 25, "bold"), fill = "white", tag = "Q")
                    money = 1000000 * RY_chip + 100000 * R_chip + 10000 * K_chip + 1000 * B_chip
                    stage = 4
                    timer = 0
                    mouse_c = 0     
    elif stage == 4 :
        timer += 1
        if timer == 15 :
            timer = 0
            set_CB.destroy()
            set_CK.destroy()
            set_CR.destroy()
            set_CRY.destroy()
            mat.delete("exchange")
            mat.delete("Q")
            mat.create_image(650, 450, image = Mbg, tag = "main")
            mat.create_image(1090, 92, image = Deck, tag = "deck")
            mat.create_text(81, 805, text = ("%d" %(B_chip)), font = ("impact", 12), fill = "white", tag = "B_chip")
            mat.create_text(196, 805, text = ("%d" %(K_chip)), font = ("impact", 12), fill = "white", tag = "K_chip")
            mat.create_text(318, 805, text = ("%d" %(R_chip)), font = ("impact", 12), fill = "white", tag = "R_chip")
            mat.create_text(437, 805, text = ("%d" %(RY_chip)), font = ("impact", 12), fill = "white", tag = "RY_chip")
            mat.create_text(265, 852, text = ("%d" %(money)), font = ("impact", 18), fill = "white", tag = "money")
            EC_B.place(x = 99, y = 758)
            EC_K.place(x = 214, y = 758)
            EC_R.place(x = 336, y = 758)
            mat.create_text(650, 300, text = "배팅을 하시요. 최소: 5000, 최대: 1,000,000", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            bet.delete(0, tkinter.END)
            bet.place(x= 580, y = 340)
            mat.create_rectangle(600,420,690,460, fill = "#FFC400", width = 1, outline = "black", tag = "betting")
            mat.create_text(645, 440, text = "Bet", font = ("impact", 20), fill = "black", tag = "betting")
            stage = 5
            timer = 0
    elif stage == 5 :
        timer += 1
        if timer == 10 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "배팅을 하시요. 최소: 5000, 최대: 1,000,000", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mouse_c = 0
        if mouse_c == 1 :
            if 600 < mouse_x and mouse_x < 690 and 420 < mouse_y and mouse_y < 460 :
                betting = int(bet.get())
                if betting % 1000 == 0 and betting >= 5000 and betting <= 1000000 and money >= betting :
                    if betting <= 9000 :
                        exchange_case(0)
                        mat.create_image(650, 810, image = img_chip[0], tag = "bet_chip")
                        mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                        mat.delete("Q")
                        mat.delete("betting")
                        card = copy.deepcopy(BaseCard)
                        bet.place(x = 2000, y = 2000)
                        stage = 6
                        mouse_c = 0
                        timer = 0
                    elif betting >= 10000 and betting <= 90000 :
                        exchange_case(0)
                        mat.create_image(650, 810, image = img_chip[1], tag = "bet_chip")
                        mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                        mat.delete("Q")
                        mat.delete("betting")
                        card = copy.deepcopy(BaseCard)
                        bet.place(x = 2000, y = 2000)
                        stage = 6
                        mouse_c = 0
                        timer = 0
                    elif betting >= 100000 and betting <= 900000 :
                        exchange_case(0)
                        mat.create_image(650, 810, image = img_chip[2], tag = "bet_chip")
                        mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                        mat.delete("Q")
                        mat.delete("betting")
                        card = copy.deepcopy(BaseCard)
                        bet.place(x = 2000, y = 2000)
                        stage = 6
                        mouse_c = 0
                        timer = 0
                    else :
                        exchange_case(0)
                        mat.create_image(650, 810, image = img_chip[3], tag = "bet_chip")
                        mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                        mat.delete("Q")
                        mat.delete("betting")
                        card = copy.deepcopy(BaseCard)
                        bet.place(x = 2000, y = 2000)
                        stage = 6
                        mouse_c = 0
                        timer = 0
                else :
                    mat.delete("Q")
                    mat.create_text(650, 300, text = "잘못된 배팅 금액입니다", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    stage = 5
                    mouse_c = 0
                    timer = 0
    elif stage == 6 :
        timer += 1
        a = random.randint(0, len(card) - 1)
        p_open1 = card[a]
        del card[a]
        b = random.randint(0, len(card) - 1)
        p_open2 = card[b]
        del card[b]
        c = random.randint(0, len(card) - 1)
        c_open1 = card[c]
        del card[c]
        d = random.randint(0, len(card) - 1)
        c_open2 = card[d]
        del card[d]
        if timer == 15 :
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "p_open1")
                mat.coords("p_open1", 1090 - 23 * i, 90 + 26 * i)
                mat.update()
            mat.delete("p_open1")
            mat.create_image(630, 610, image = img_card[52], tag = "p_open1")
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "p_open2")
                mat.coords("p_open2", 1090 - 21 * i, 90 + 26 * i)
                mat.update()
            mat.delete("p_open2")
            mat.create_image(670, 610, image = img_card[52], tag = "p_open2")
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "c_open1")
                mat.coords("c_open1", 1090 - 23 * i, 90 - 1 * i)
                mat.update()
            mat.delete("c_open1")
            mat.create_image(630, 70, image = img_card[52], tag = "c_open1")
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "c_open2")
                mat.coords("c_open2", 1090 - 21 * i, 90 - 1 * i)
                mat.update()
            mat.delete("c_open2")
            mat.create_image(670, 70, image = img_card[52], tag = "c_open2")
        if timer == 35 :
            mat.delete("p_open1")
            mat.delete("p_open2")
            mat.delete("c_open1")
            mat.create_image(630, 610, image = img_card[Cardnumber[p_open1]], tag = "p_open1")
            mat.create_image(670, 610, image = img_card[Cardnumber[p_open2]], tag = "p_open2")
            mat.create_image(630, 70, image = img_card[Cardnumber[c_open1]], tag = "c_open1")
            P_result = Cardcount[p_open1] + Cardcount[p_open2]
            if P_result == 22 :
                p_open1 = 'A1'
                P_result -= 10
                mat.create_text(1035, 785, text = ("%d" %(P_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 7
                timer = 0
            else :
                mat.create_text(1035, 785, text = ("%d" %(P_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 7
                timer = 0
    elif stage == 7 :
        timer += 1
        if timer == 15 :
            if P_result == 21 :
                mat.delete("Cardinfo")
                mat.delete("Q")
                mat.create_text(1035, 785, text = "Black Jack", font = ("impact", 20), fill = "white", tag = "Cardinfo")
                mat.create_text(650, 370, text = "플레이어 블랙잭!", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(650, 610, image = BJc, tag = "Q")
                stage = 15
                pb = 1
                timer = 0
            elif Cardcount[c_open1] == 11 :
                if money > 0 :
                    mat.delete("Q")
                    mat.create_text(650, 300, text = "인슈어런스 하시겠습니까?", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "insu")
                    mat.create_text(575, 420, text = "YES", font = ("impact", 20), fill = "black", tag = "insu")
                    mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "insu")
                    mat.create_text(725, 420, text = "NO", font = ("impact", 20), fill = "black", tag = "insu")
                    stage = 11
                    timer = 0
                    mouse_c = 0
                else : 
                    mat.delete("Q")
                    mat.create_text(650, 300, text = "선택하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                    mat.create_text(575, 420, text = "Hit", font = ("impact", 20), fill = "black", tag = "HS")
                    mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                    mat.create_text(725, 420, text = "Stay", font = ("impact", 20), fill = "black", tag = "HS")
                    stage = 13
                    timer = 0
            else :
                stage = 8
                timer = 0
                mouse_c = 0
    elif stage == 8 :
        timer += 1
        if timer == 10 :
            if money > 0 :
                mat.delete("Q")
                mat.create_text(650, 300, text = "더블다운을 하시겠습니까?", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "Double")
                mat.create_text(575, 420, text = "YES", font = ("impact", 20), fill = "black", tag = "Double")
                mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "Double")
                mat.create_text(725, 420, text = "NO", font = ("impact", 20), fill = "black", tag = "Double")
            else :
                mat.delete("Q")
                mat.delete("Double")
                doublebet = 0
                mat.create_text(650, 300, text = "선택하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                mat.create_text(575, 420, text = "Hit", font = ("impact", 20), fill = "black", tag = "HS")
                mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                mat.create_text(725, 420, text = "Stay", font = ("impact", 20), fill = "black", tag = "HS")
                stage = 13
                mouse_c = 0
                timer = 0
        if mouse_c == 1 :
            if 550 < mouse_x and mouse_x < 600 and 400 < mouse_y and mouse_y < 440 :
                if money - betting > 0 :
                    mat.delete("Q")
                    mat.delete("Double")
                    mat.create_text(650, 300, text = "추가 배팅을 하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    bet.delete(0, tkinter.END)
                    bet.place(x = 580, y = 340)
                    mat.create_rectangle(600,420,690,460, fill = "#FFC400", width = 1, outline = "black", tag = "betting")
                    mat.create_text(645, 440, text = "Bet", font = ("impact", 20), fill = "black", tag = "betting")
                    stage = 9
                    mouse_c = 0
                    timer = 0
            elif 700 < mouse_x and mouse_x < 750 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                mat.delete("Double")
                doublebet = 0
                mat.create_text(650, 300, text = "선택하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                mat.create_text(575, 420, text = "Hit", font = ("impact", 20), fill = "black", tag = "HS")
                mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
                mat.create_text(725, 420, text = "Stay", font = ("impact", 20), fill = "black", tag = "HS")
                stage = 13
                mouse_c = 0
                timer = 0
    elif stage == 9 :
        timer += 0
        if timer == 10 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "추가 배팅을 하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mouse_c = 0
        if mouse_c == 1 :
            if 600 < mouse_x and mouse_x < 690 and 420 < mouse_y and mouse_y < 460 :
                doublebet = int(bet.get())
                if  doublebet > betting or doublebet <= 0 :
                    mat.delete("Q")
                    mat.create_text(650, 300, text = ("%d원 내에서 배팅해야 합니다" %(betting)), font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    stage = 9
                    timer = 0
                    mouse_c = 0
                else :
                    if doublebet % 1000 == 0 and money - betting >= doublebet :
                        betting += doublebet
                        if betting <= 9000 :
                            exchange_case(6)
                            mat.delete("bet_chip")
                            mat.create_image(650, 810, image = img_chip[0], tag = "bet_chip")
                            mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 10
                            mouse_c = 0
                            timer = 0
                        elif betting >= 10000 and betting <= 90000 :
                            exchange_case(6)
                            mat.delete("bet_chip")
                            mat.create_image(650, 810, image = img_chip[1], tag = "bet_chip")
                            mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 10
                            mouse_c = 0
                            timer = 0
                        elif betting >= 100000 and betting <= 900000 :
                            exchange_case(6)
                            mat.delete("bet_chip")
                            mat.create_image(650, 810, image = img_chip[2], tag = "bet_chip")
                            mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 10
                            mouse_c = 0
                            timer = 0
                        else :
                            exchange_case(6)
                            mat.create_image(650, 810, image = img_chip[3], tag = "bet_chip")
                            mat.create_text(650, 805, text = ("%d" %(betting)), font = ("impact", 10), fill = "black", tag = "bet_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 10
                            mouse_c = 0
                            timer = 0
    elif stage == 10 :
        timer += 1
        D = random.randint(0, len(card) - 1)
        p_D = card[D]
        del card[D]
        if timer == 15 :
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "p_D")
                mat.coords("p_D", 1090 - 21 * i, 90 + 26 * i)
                mat.update()
            mat.delete("p_D")
            mat.coords("p_open1", 630 - 40, 610)
            mat.coords("p_open2", 670 - 40, 610)
            mat.update()
            mat.create_image(670, 610, image = img_card[52], tag = "p_D")
        if timer == 25 :
            DP_result = P_result + Cardcount[p_D]
            mat.delete("p_D")
            mat.create_image(670, 610, image = img_card[Cardnumber[p_D]], tag = "p_D")
            mat.delete("Cardinfo")
            if DP_result == 21 :
                mat.create_text(650, 370, text = "플레이어 합 21 완성", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_text(1035, 785, text = ("%d" %(DP_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 15
                timer = 0
            elif DP_result > 21 :
                calculate_case()
                if DP_result > 21 :
                    mat.create_text(650, 370, text = "플레이어 버스트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_image(650, 610, image = Bust, tag = "Q")
                    mat.create_text(1035, 785, text = "Bust", font = ("impact", 20), fill = "white", tag = "Cardinfo")
                    stage = 15
                    timer = 0
                else :
                    mat.create_text(650, 370, text = "플레이어 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_text(1035, 785, text = ("%d" %(DP_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                    stage = 15
                    timer = 0
            else :
                mat.create_text(650, 370, text = "플레이어 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_text(1035, 785, text = ("%d" %(DP_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 15
                timer = 0
    elif stage == 11 :
        timer += 1
        if timer == 10 :
            mouse_c = 0
        if mouse_c == 1 :
            if 550 < mouse_x and mouse_x < 600 and 400 < mouse_y and mouse_y < 440 :
                if money - betting > 0 :
                    mat.delete("Q")
                    mat.delete("insu")
                    mat.create_text(650, 300, text = "보험금을 배팅하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    bet.delete(0, tkinter.END)
                    bet.place(x = 580, y = 340)
                    mat.create_rectangle(600,420,690,460, fill = "#FFC400", width = 1, outline = "black", tag = "betting")
                    mat.create_text(645, 440, text = "Bet", font = ("impact", 20), fill = "black", tag = "betting")
                    stage = 12
                    timer = 0
                    mouse_c = 0
            elif 700 < mouse_x and mouse_x < 750 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                mat.delete("insu")
                stage = 8
                insurance = 0
                timer = 0
                mouse_c = 0
    elif stage == 12 :
        timer += 0
        if timer == 10 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "보험금을 배팅하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mouse_c = 0
        if mouse_c == 1 :
            if 600 < mouse_x and mouse_x < 690 and 420 < mouse_y and mouse_y < 460 :
                insurance = int(bet.get())
                if insurance > betting or insurance <= 0 :
                    mat.delete("Q")
                    mat.create_text(650, 300, text = ("%d원 내에서 배팅해야 합니다" %(betting)), font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    stage = 12
                    timer = 0
                    mouse_c = 0
                else :
                    if insurance % 1000 == 0 and money - betting >= insurance :
                        if insurance <= 9000 :
                            exchange_case(4)
                            mat.create_image(650, 190, image = img_chip[0], tag = "insu_chip")
                            mat.create_text(650, 185, text = ("%d" %(insurance)), font = ("impact", 10), fill = "black", tag = "insu_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 13
                            mouse_c = 0
                            timer = 0
                        elif insurance >= 10000 and insurance <= 90000 :
                            exchange_case(4)
                            mat.create_image(650, 190, image = img_chip[1], tag = "insu_chip")
                            mat.create_text(650, 185, text = ("%d" %(insurance)), font = ("impact", 10), fill = "black", tag = "insu_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 13
                            mouse_c = 0
                            timer = 0
                        elif insurance >= 100000 and insurance <= 900000 :
                            exchange_case(4)
                            mat.create_image(650, 190, image = img_chip[2], tag = "insu_chip")
                            mat.create_text(650, 185, text = ("%d" %(insurance)), font = ("impact", 10), fill = "black", tag = "insu_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 13
                            mouse_c = 0
                            timer = 0
                        else :
                            exchange_case(4)
                            mat.create_image(650, 190, image = img_chip[3], tag = "insu_chip")
                            mat.create_text(650, 185, text = ("%d" %(insurance)), font = ("impact", 10), fill = "black", tag = "insu_chip")
                            mat.delete("Q")
                            mat.delete("betting")
                            bet.place(x = 2000, y = 2000)
                            stage = 13
                            mouse_c = 0
                            timer = 0
    elif stage == 13 :
        timer += 1
        if timer == 10 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "선택하시요", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
            mat.create_text(575, 420, text = "Hit", font = ("impact", 20), fill = "black", tag = "HS")
            mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "HS")
            mat.create_text(725, 420, text = "Stay", font = ("impact", 20), fill = "black", tag = "HS")
        if mouse_c == 1 :
            if 550 < mouse_x and mouse_x < 600 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                mat.delete("HS")
                stage = 14
                mouse_c = 0
                timer = 0
            elif 700 < mouse_x and mouse_x < 750 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                mat.delete("HS")
                mat.create_text(650, 370, text = "플레이어 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                stage = 15
                num = 0
                x = 670
                mouse_c = 0
                timer = 0
    elif stage == 14 :
        timer += 1
        H = random.randint(0, len(card) - 1)
        p_H[num] = card[H]
        del card[H]
        if timer == 15 :
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "p_H")
                mat.coords("p_H", 1090 - 21 * i, 90 + 26 * i)
                mat.update()
            mat.delete("p_H")
            if num == 0 :
                mat.coords("p_open1", 630 - 40 * (num + 1), 610)
                mat.coords("p_open2", 670 - 40 * (num + 1), 610)
                mat.update()
                mat.create_image(x - 40 * num, 610, image = img_card[52], tag = pnum[num])
            else :
                for i in range(num) :
                    mat.coords(pnum[num-1], x - 80 * num, 610)
                mat.coords("p_open1", 630 - 40 * (num + 1), 610)
                mat.coords("p_open2", 670 - 40 * (num + 1), 610)
                mat.update()
                mat.create_image(x - 40 * num, 610, image = img_card[52], tag = pnum[num])
        if timer == 25 :
            mat.delete(pnum[num])
            mat.create_image(x - 40 * num, 610, image = img_card[Cardnumber[p_H[num]]], tag = pnum[num])
            mat.delete("Cardinfo")
            P_result += Cardcount[p_H[num]]
            if P_result == 21 :
                mat.create_text(650, 370, text = "플레이어 합 21 완성", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_text(1035, 785, text = ("%d" %(P_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 15
                num = 0
                x = 670
                timer = 0
            elif P_result > 21 :
                calculate_case()
                if P_result > 21 :
                    mat.create_text(650, 370, text = "플레이어 버스트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_image(650, 610, image = Bust, tag = "Q")
                    mat.create_text(1035, 785, text = "Bust", font = ("impact", 20), fill = "white", tag = "Cardinfo")
                    stage = 15
                    num = 0
                    x = 670
                    timer = 0
                else :
                    mat.create_text(1035, 785, text = ("%d" %(P_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                    stage = 13
                    num += 1
                    x += 40
                    timer = 0
            else :
                mat.create_text(1035, 785, text = ("%d" %(P_result)), font = ("impact", 20), fill = "white", tag = "Cardinfo")
                stage = 13
                num += 1
                x += 40
                timer = 0
    elif stage == 15 :
        timer += 1
        if timer == 25 :
            mat.delete("Q")
            mat.create_text(650, 370, text = "딜러 카드 공개", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mat.delete("c_open2")
            mat.create_image(670, 70, image = img_card[Cardnumber[c_open2]], tag = "c_open2")
            C_result = Cardcount[c_open1] + Cardcount[c_open2]
            mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
            if C_result == 22 :
                c_open1 = 'A1'
        if timer == 35 :
            if insurance > 0 :
                if C_result == 21 :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 블랙잭 보험금 2배 지급", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_image(650, 70, image = BJc, tag = "Q")
                    mat.delete("DCardinfo")
                    mat.create_text(205, 148, text = "Black Jack", font = ("impact", 20), fill = "white", tag = "DCardinfo")
                    mat.delete("insu_chip")
                    exchange_case(1)
                    stage = 17
                    cb = 1
                    timer = 0
                else :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "보험금 회수", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.delete("insu_chip")
                    stage = 17
                    cb = 1
                    timer = 0
            else :
                if C_result == 21 :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 블랙잭!", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_image(650, 70, image = BJc, tag = "Q")
                    mat.delete("DCardinfo")
                    mat.create_text(205, 148, text = "Black Jack", font = ("impact", 20), fill = "white", tag = "DCardinfo")
                    stage = 17
                    cb = 1
                    timer = 0
                elif 17 <= C_result < 21 :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    stage = 17
                    timer = 0
                    mouse_c = 0
                else :
                    stage = 16
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 히트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    timer = 0
                    mouse_c = 0
    elif stage == 16 :
        timer += 1
        H = random.randint(0, len(card) - 1)
        c_H[num] = card[H]
        del card[H]
        if timer == 15 :
            for i in range(20) :
                mat.create_image(1090, 90, image = img_card[52], tag = "c_H")
                mat.coords("c_H", 1090 - 21 * i, 90 - 1 * i)
                mat.update()
            mat.delete("c_H")
            if num == 0 :
                mat.coords("c_open1", 630 - 40 * (num + 1), 70)
                mat.coords("c_open2", 670 - 40 * (num + 1), 70)
                mat.update()
                mat.create_image(x - 40 * num, 70, image = img_card[52], tag = cnum[num])
            else :
                for i in range(num) :
                    mat.coords(cnum[num-1], x - 80 * num, 70)
                mat.coords("c_open1", 630 - 40 * (num + 1), 70)
                mat.coords("c_open2", 670 - 40 * (num + 1), 70)
                mat.update()
                mat.create_image(x - 40 * num, 70, image = img_card[52], tag = cnum[num])
        if timer == 30 :
            mat.delete(cnum[num])
            mat.create_image(x - 40 * num, 70, image = img_card[Cardnumber[c_H[num]]], tag = cnum[num])
            C_result += Cardcount[c_H[num]]
            mat.delete("DCardinfo")
            if C_result == 21 :
                mat.delete("Q")
                mat.create_text(650, 370, text = "딜러 합 21 완성", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
                stage = 17
                num = 0
                x = 670
                timer = 0
            elif C_result > 21 :
                calculate_case()
                if C_result > 21 :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 버스트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_image(650, 70, image = Bust, tag = "Q")
                    mat.create_text(205, 148, text = "Bust", font = ("impact", 20), fill = "white", tag = "DCardinfo")
                    stage = 17
                    num = 0
                    x = 670
                    timer = 0
                else :
                    if C_result < 17 :
                        mat.delete("Q")
                        mat.create_text(650, 370, text = "딜러 추가 히트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                        mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
                        stage = 16
                        num += 1
                        x += 40
                        timer = 0
                    else : 
                        mat.delete("Q")
                        mat.create_text(650, 370, text = "딜러 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                        mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
                        stage = 17
                        num = 0
                        x = 670
                        timer = 0
                        mouse_c = 0
            else :
                if C_result < 17 :
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 추가 히트", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
                    stage = 16
                    num += 1
                    x += 40
                    timer = 0
                else : 
                    mat.delete("Q")
                    mat.create_text(650, 370, text = "딜러 스테이", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                    mat.create_text(205, 148, text = ("%d" %(C_result)), font = ("impact", 20), fill = "white", tag = "DCardinfo")
                    stage = 17
                    num = 0
                    x = 670
                    timer = 0
                    mouse_c = 0
    elif stage == 17 :
        timer += 1
        if timer == 20 :
            mat.delete("Q")
            mat.create_text(650, 370, text = "최종 결과", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
        if timer == 30 :
            mat.delete("Q")
            if pb == 1 and cb == 1 :
                mat.create_text(650, 370, text = "무승부", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.delete("bet_chip")
                exchange_case(5)
                stage = 18
                timer = 0
                mouse_c = 0
            elif pb == 1 and cb == 0 :
                mat.create_text(650, 370, text = "플레이어 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 610, image = win, tag = "Q")
                mat.delete("bet_chip")
                exchange_case(3)
                stage = 19
                timer = 0
                mouse_c = 0
            elif pb == 0 and cb == 1 : 
                mat.create_text(650, 370, text = "딜러 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 70, image = win, tag = "Q")
                mat.delete("bet_chip")
                stage = 19
                timer = 0
                mouse_c = 0
            elif P_result > 21 or DP_result > 21 :
                mat.create_text(650, 370, text = "딜러 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 70, image = win, tag = "Q")
                mat.delete("bet_chip")
                stage = 19
                timer = 0
                mouse_c = 0
            elif (P_result <= 21 or DP_result <= 21) and C_result > 21 :
                mat.create_text(650, 370, text = "플레이어 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 610, image = win, tag = "Q")
                mat.delete("bet_chip")
                exchange_case(2)
                stage = 19
                timer = 0
                mouse_c = 0
            elif P_result == C_result or DP_result == C_result :
                mat.create_text(650, 370, text = "무승부", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.delete("bet_chip")
                exchange_case(5)
                stage = 19
                timer = 0
                mouse_c = 0
            elif P_result > C_result or DP_result > C_result :
                mat.create_text(650, 370, text = "플레이어 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 610, image = win, tag = "Q")
                mat.delete("bet_chip")
                exchange_case(2)
                stage = 19
                timer = 0
                mouse_c = 0
            else :
                mat.create_text(650, 370, text = "딜러 승리", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
                mat.create_image(765, 70, image = win, tag = "Q")
                mat.delete("bet_chip")
                stage = 19
                timer = 0
                mouse_c = 0
    elif stage == 18 :
        timer += 1
        if timer == 20 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "중단 하시겠습니까?", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mat.create_rectangle(550,400,600,440, fill = "#FFC400", width = 1, outline = "black", tag = "Q")
            mat.create_text(575, 420, text = "YES", font = ("impact", 20), fill = "black", tag = "Q")
            mat.create_rectangle(700,400,750,440, fill = "#FFC400", width = 1, outline = "black", tag = "Q")
            mat.create_text(725, 420, text = "NO", font = ("impact", 20), fill = "black", tag = "Q")
            mouse_c = 0
        if mouse_c == 1 :
            if 550 < mouse_x and mouse_x < 600 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                stage = 21
                timer = 0
            elif 700 < mouse_x and mouse_x < 750 and 400 < mouse_y and mouse_y < 440 :
                mat.delete("Q")
                stage = 19
                timer = 0
    elif stage == 19 :
        timer += 1
        if timer == 20 :
            if money >= 10000000 :
                mat.delete("Q")
                mat.create_image(650, 430, image = Gwin, tag = "Q")
                mat.delete("Cardinfo")
                mat.delete("DCardinfo")
                mat.delete("p_open1")
                mat.delete("p_open2")
                mat.delete("c_open1")
                mat.delete("c_open2")
                mat.delete("p_D")
                for i in range(0, 12) :
                    mat.delete(pnum[i])
                for i in range(0, 10) :
                    mat.delete(cnum[i])
                timer = 0
                stage = 22              
            elif money < 5000 :
                mat.delete("Q")
                mat.create_image(650, 360, image = Gover, tag = "Q")
                mat.delete("Cardinfo")
                mat.delete("DCardinfo")
                mat.delete("p_open1")
                mat.delete("p_open2")
                mat.delete("c_open1")
                mat.delete("c_open2")
                mat.delete("p_D")
                for i in range(0, 12) :
                    mat.delete(pnum[i])
                for i in range(0, 10) :
                    mat.delete(cnum[i])
                timer = 0
                stage = 22   
            else :
                stage = 20
                timer = 0
    elif stage == 20 :
        timer += 1
        if timer == 10 :
            mat.delete("Q")
            mat.create_text(650, 370, text = "카드 섞는 중", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            mat.delete("Cardinfo")
            mat.delete("DCardinfo")
            mat.delete("p_open1")
            mat.delete("p_open2")
            mat.delete("c_open1")
            mat.delete("c_open2")
            mat.delete("p_D")
            for i in range(0, 12) :
                mat.delete(pnum[i])
            for i in range(0, 10) :
                mat.delete(cnum[i])
            pb = 0
            cb = 0
            DP_result = 0
            P_result = 0
            C_result = 0
            insurance = 0
            betting = 0
            doublebet = 0
            num = 0
            x = 670
            for i in range(52) :
                card.append("0")
            for i in range(12) :
                p_H.append("0")
            for i in range(12) :
                c_H.append("0")
        if timer == 30 :
            mat.delete("Q")
            mat.create_text(650, 300, text = "배팅을 하시요. 최소: 5000, 최대: 1,000,000", font = ("맑은 고딕", 30),  fill = "white", tag = "Q")
            bet.delete(0, tkinter.END)
            bet.place(x= 580, y = 340)
            mat.create_rectangle(600,420,690,460, fill = "#FFC400", width = 1, outline = "black", tag = "betting")
            mat.create_text(645, 440, text = "Bet", font = ("impact", 20), fill = "black", tag = "betting")
            stage = 5
            timer = 0
    elif stage == 21 :
        tkinter.messagebox.showinfo("만약...", "계속했다면 전부 잃었을 것이다.")
        exit()
    elif stage == 22 :
        timer += 1
        if timer == 30 :
            if money >= 10000000 :
                tkinter.messagebox.showwarning("다음은...", "이길 수 없을 것이다.")
                exit()
            else :
                tkinter.messagebox.showwarning("명심해라", "도박은 끝은 결국 인생 전부를 거는 것이다.")
                exit()
    window.after(100, main_proc)  
Cardcount = {'A(♠)': 11, '2(♠)': 2, '3(♠)': 3, '4(♠)': 4, '5(♠)': 5, '6(♠)': 6, '7(♠)': 7, '8(♠)': 8, '9(♠)': 9, '10(♠)': 10, 'J(♠)': 10, 'Q(♠)': 10, 'K(♠)': 10,
            'A(◆)': 11, '2(◆)': 2, '3(◆)': 3, '4(◆)': 4, '5(◆)': 5, '6(◆)': 6, '7(◆)': 7, '8(◆)': 8, '9(◆)': 9, '10(◆)': 10, 'J(◆)': 10, 'Q(◆)': 10, 'K(◆)': 10,
            'A(♥)': 11, '2(♥)': 2, '3(♥)': 3, '4(♥)': 4, '5(♥)': 5, '6(♥)': 6, '7(♥)': 7, '8(♥)': 8, '9(♥)': 9, '10(♥)': 10, 'J(♥)': 10, 'Q(♥)': 10, 'K(♥)': 10,
            'A(♣)': 11, '2(♣)': 2, '3(♣)': 3, '4(♣)': 4, '5(♣)': 5, '6(♣)': 6, '7(♣)': 7, '8(♣)': 8, '9(♣)': 9, '10(♣)': 10, 'J(♣)': 10, 'Q(♣)': 10, 'K(♣)': 10, 'A1': 1}
Cardnumber = {'A(♠)': 0, '2(♠)': 1, '3(♠)': 2, '4(♠)': 3, '5(♠)': 4, '6(♠)': 5, '7(♠)': 6, '8(♠)': 7, '9(♠)': 8, '10(♠)': 9, 'J(♠)': 10, 'Q(♠)': 11, 'K(♠)': 12,
            'A(◆)': 13, '2(◆)': 14, '3(◆)': 15, '4(◆)': 16, '5(◆)': 17, '6(◆)': 18, '7(◆)': 19, '8(◆)': 20, '9(◆)': 21, '10(◆)': 22, 'J(◆)': 23, 'Q(◆)': 24, 'K(◆)': 25,
            'A(♥)': 26, '2(♥)': 27, '3(♥)': 28, '4(♥)': 29, '5(♥)': 30, '6(♥)': 31, '7(♥)': 32, '8(♥)': 33, '9(♥)': 34, '10(♥)': 35, 'J(♥)': 36, 'Q(♥)': 37, 'K(♥)': 38,
            'A(♣)': 39, '2(♣)': 40, '3(♣)': 41, '4(♣)': 42, '5(♣)': 43, '6(♣)': 44, '7(♣)': 45, '8(♣)': 46, '9(♣)': 47, '10(♣)': 48, 'J(♣)': 49, 'Q(♣)': 50, 'K(♣)': 51,}
BaseCard = ['A(♠)', '2(♠)', '3(♠)', '4(♠)', '5(♠)', '6(♠)', '7(♠)', '8(♠)', '9(♠)', '10(♠)', 'J(♠)', 'Q(♠)', 'K(♠)',
            'A(◆)', '2(◆)', '3(◆)', '4(◆)', '5(◆)', '6(◆)', '7(◆)', '8(◆)', '9(◆)', '10(◆)', 'J(◆)', 'Q(◆)', 'K(◆)',
            'A(♥)', '2(♥)', '3(♥)', '4(♥)', '5(♥)', '6(♥)', '7(♥)', '8(♥)', '9(♥)', '10(♥)', 'J(♥)', 'Q(♥)', 'K(♥)',
            'A(♣)', '2(♣)', '3(♣)', '4(♣)', '5(♣)', '6(♣)', '7(♣)', '8(♣)', '9(♣)', '10(♣)', 'J(♣)', 'Q(♣)', 'K(♣)']
card = []
for i in range(52) :
    card.append("0")
pnum = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12"]
cnum = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
p_H = []
for i in range(12) :
    p_H.append("0")
c_H = []
for i in range(12) :
    c_H.append("0")
stage = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
B_chip = 0
K_chip = 0
R_chip = 0
RY_chip = 0
money = 0
betting = 0
doublebet = 0
insurance = 0
timer = 0
DP_result = 0
P_result = 0
C_result = 0
num = 0
x = 670
pb = 0
cb = 0
window = tkinter.Tk()
window.title("Black Jack")
window.resizable(False, False)
window.bind("<Motion>", mouse_move)
window.bind("<Button>", mouse_press)
mat = tkinter.Canvas(window, width = 1300, height = 900)
mat.pack()
set_m = tkinter.Entry(width = 7, font = ("impact", 40), fg = "white", bg = "#0E471F")
set_CB = tkinter.Entry(width = 3, font = ("impact", 25), fg = "white", bg = "#0E471F")
set_CK = tkinter.Entry(width = 3, font = ("impact", 25), fg = "white", bg = "#0E471F")
set_CR = tkinter.Entry(width = 3, font = ("impact", 25), fg = "white", bg = "#0E471F")
set_CRY = tkinter.Entry(width = 3, font = ("impact", 25), fg = "white", bg = "#0E471F")
bet = tkinter.Entry(width = 7, font = ("impact", 25), fg = "white", bg = "#0E471F")
toggle_var = tkinter.IntVar()
Button_rule = tkinter.Checkbutton(text = "Rule", font = ("impact", 12), fg = "Black", bg = "#FFC400", variable=toggle_var, command = toggle)
EC_B = tkinter.Button(text = "▲", font = ("impact", 10), fg = "white", bg = "#0E471F", command = click_B)
EC_K = tkinter.Button(text = "▲", font = ("impact", 10), fg = "white", bg = "#0E471F", command = click_K)
EC_R = tkinter.Button(text = "▲", font = ("impact", 10), fg = "white", bg = "#0E471F", command = click_R)
img_card = [
    tkinter.PhotoImage(file = "Image//A(♠).png"),
    tkinter.PhotoImage(file = "Image//2(♠).png"),
    tkinter.PhotoImage(file = "Image//3(♠).png"),
    tkinter.PhotoImage(file = "Image//4(♠).png"),
    tkinter.PhotoImage(file = "Image//5(♠).png"),
    tkinter.PhotoImage(file = "Image//6(♠).png"),
    tkinter.PhotoImage(file = "Image//7(♠).png"),
    tkinter.PhotoImage(file = "Image//8(♠).png"),
    tkinter.PhotoImage(file = "Image//9(♠).png"),
    tkinter.PhotoImage(file = "Image//10(♠).png"),
    tkinter.PhotoImage(file = "Image//J(♠).png"),
    tkinter.PhotoImage(file = "Image//Q(♠).png"),
    tkinter.PhotoImage(file = "Image//K(♠).png"),
    tkinter.PhotoImage(file = "Image//A(◆).png"),
    tkinter.PhotoImage(file = "Image//2(◆).png"),
    tkinter.PhotoImage(file = "Image//3(◆).png"),
    tkinter.PhotoImage(file = "Image//4(◆).png"),
    tkinter.PhotoImage(file = "Image//5(◆).png"),
    tkinter.PhotoImage(file = "Image//6(◆).png"),
    tkinter.PhotoImage(file = "Image//7(◆).png"),
    tkinter.PhotoImage(file = "Image//8(◆).png"),
    tkinter.PhotoImage(file = "Image//9(◆).png"),
    tkinter.PhotoImage(file = "Image//10(◆).png"),
    tkinter.PhotoImage(file = "Image//J(◆).png"),
    tkinter.PhotoImage(file = "Image//Q(◆).png"),
    tkinter.PhotoImage(file = "Image//K(◆).png"),
    tkinter.PhotoImage(file = "Image//A(♥).png"),
    tkinter.PhotoImage(file = "Image//2(♥).png"),
    tkinter.PhotoImage(file = "Image//3(♥).png"),
    tkinter.PhotoImage(file = "Image//4(♥).png"),
    tkinter.PhotoImage(file = "Image//5(♥).png"),
    tkinter.PhotoImage(file = "Image//6(♥).png"),
    tkinter.PhotoImage(file = "Image//7(♥).png"),
    tkinter.PhotoImage(file = "Image//8(♥).png"),
    tkinter.PhotoImage(file = "Image//9(♥).png"),
    tkinter.PhotoImage(file = "Image//10(♥).png"),
    tkinter.PhotoImage(file = "Image//J(♥).png"),
    tkinter.PhotoImage(file = "Image//Q(♥).png"),
    tkinter.PhotoImage(file = "Image//K(♥).png"),
    tkinter.PhotoImage(file = "Image//A(♣).png"),
    tkinter.PhotoImage(file = "Image//2(♣).png"),
    tkinter.PhotoImage(file = "Image//3(♣).png"),
    tkinter.PhotoImage(file = "Image//4(♣).png"),
    tkinter.PhotoImage(file = "Image//5(♣).png"),
    tkinter.PhotoImage(file = "Image//6(♣).png"),
    tkinter.PhotoImage(file = "Image//7(♣).png"),
    tkinter.PhotoImage(file = "Image//8(♣).png"),
    tkinter.PhotoImage(file = "Image//9(♣).png"),
    tkinter.PhotoImage(file = "Image//10(♣).png"),
    tkinter.PhotoImage(file = "Image//J(♣).png"),
    tkinter.PhotoImage(file = "Image//Q(♣).png"),
    tkinter.PhotoImage(file = "Image//K(♣).png"),
    tkinter.PhotoImage(file = "Image//Back.png")
]
img_chip = [
    tkinter.PhotoImage(file = "Image//Bluechip.png"),
    tkinter.PhotoImage(file = "Image//Blackchip.png"),
    tkinter.PhotoImage(file = "Image//Redchip.png"),
    tkinter.PhotoImage(file = "Image//RYellowchip.png")
]
Deck = tkinter.PhotoImage(file = "Image//Deck.png")
Rule = tkinter.PhotoImage(file = "Image//Rule.png")
Tbg = tkinter.PhotoImage(file = "Image//TitleBG.png")
bg = tkinter.PhotoImage(file = "Image//BG.png")
Mbg = tkinter.PhotoImage(file = "Image//MainBG.png")
Bust = tkinter.PhotoImage(file = "Image//bomb.png")
win = tkinter.PhotoImage(file = "Image//win.png")
Gwin = tkinter.PhotoImage(file = "Image//gw.png")
Gover = tkinter.PhotoImage(file = "Image//go.png")
BJc = tkinter.PhotoImage(file = "Image//bj.png")
mat.create_image(650, 450, image = Tbg, tag = "Image//title")
main_proc()
window.mainloop()