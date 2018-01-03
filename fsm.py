from transitions.extensions import GraphMachine
import time

Hp = 60
Lp = 60
Lk = 60

def TAMAGOCHI():
    ret = 'Lp: '+str(Lp)+'\n' + 'Hp: '+str(Hp)+'\n' + 'Like: '+str(Lk)+'\n'
    return ret
#def FULL_TEST():
#    if Lp <= 50:
#            ret = "尚未吃飽\n"+"[a] 繼續餵食\n"+"[b] 停止餵食\n"
#    elif Lp > 50:
#            ret = "吃尬飽飽\n"+"[b] 停止餵食\n"+"[c] 繼續餵食\n"
#    return ret
#def STATE_CHANGE(Lpa, Hpa, Lka):
#    Lp = Lp + Lpa
#    Hp = Hp + Hpa
#    Lk = Lk + Lka
#    if Hp<=0 or Lp<=0 or Lk<=0:
#        return -1
#    else:
#        return 0
     

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )


    # new
#    def is_going_to_state0(self, update):
#        text = update.message.text
#        return text.lower() == '/restart'

    def on_enter_state0(self, update):
     	time.sleep(2)

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '/start'

    def on_enter_state1(self, update):
        ret = TAMAGOCHI() + "\n來與蛋子做點事情吧\n開始冒險?[y/n]\n"
        update.message.reply_text(ret)
        self.go_back(update)


    # intro
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'y'
    
    def on_enter_state2(self, update):
        if Lp<0 or Hp<0 or Lk<0:
            self.go_back(update)
        else:
            update.message.reply_text("[3] 吃點什麼\n[4] 玩遊戲\n[5] 打掃\n")
    
    # A
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def on_enter_state3(self, update):
        ret = TAMAGOCHI() + "[4]便當\n[5]速食\n[6]牛排\n[7]麵包\n[8]泡麵\n[9]點心\n"
        update.message.reply_text(ret)

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '4'

    def on_enter_state4(self, update):  ## bendong
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Lp=Lp+5
        Hp=Hp+5
        Lk=Lk-1

    # B
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '5'
    def on_enter_state5(self, update):  ## fast_food
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Lp=Lp-5
        Hp=Hp-5
        Lk=Lk+10

    # C
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '6'
    def on_enter_state6(self, update):  ## steak
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Lp=Lp+5
        Hp=Hp-5
        Lk=Lk-1

    # D
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '7'
    def on_enter_state7(self, update):  ## bread
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Lp=Lp+5
        Hp=Hp+1
        Lk=Lk-5
    
    # E
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '8'
    def on_enter_state8(self, update):  ## fast_food
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Hp=Hp-10
        Lp=Lp-10
        Lk=Lk+5

    # F
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '9'
    def on_enter_state9(self, update):  ## snack
        update.message.reply_text("[3]繼續餵食\n[10]停止餵食\n")
        global Lp, Hp, Lk
        Hp=Hp-5
        Lp=Lp-5
        Lk=Lk+5

    # DIE
    def is_going_to_state11(self, update):
        if Lp<0 or Hp<0 or Lk<0:
            return '11'
#            update.message.reply_text("TAMAGOCHI IS DEAD")

    def on_enter_state11(self, update):
        update.message.reply_text("DIE")
        self.go_back(update)

    # back to option
    def is_going_to_state10(self, update):
        if Lp<=50:
            print("Lp<50")
        else: 
            print("Lp>50")
        text = update.message.text
        return text.lower() == '10'

    def on_enter_state10(self, update):
        self.go_back(update)

