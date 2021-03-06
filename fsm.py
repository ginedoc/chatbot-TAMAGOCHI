from transitions.extensions import GraphMachine
import time
import random

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

    def on_enter_state0(self, update):
        global Lp, Hp, Lk
        Lp = 60
        Hp = 60
        Lk = 60

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
            update.message.reply_text("[3] 吃點什麼\n[17] 講個笑話R\n[12] 來點其他的\n")
    
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

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '12'

    def on_enter_state12(self, update):
        update.message.reply_text("[13] 睡覺\n[14] 滑手機\n")

    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == '13'

    def on_enter_state13(self, update):
        update.message.reply_text("睡飽飽^^")
        global Hp, Lp, Lk
        Hp = Hp + 10
        Lp = Lp + 10
        Lk = Lk + 10
        self.go_back(update)

    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == '14'

    def on_enter_state14(self, update):
        update.message.reply_text("[15] FB\n[16] Google\n")

    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == '15'
    def on_enter_state15(self, update):
        update.message.reply_text("http://www.facebook.com")
        global Lk, Hp, Lp
        Lk = Lk + 5
        Hp = Hp - 5
        Lp = Lp - 5
        self.go_back(update)

    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == '16'
    def on_enter_state16(self, update):
        update.message.reply_text("www.google.com")
        global Lk, Hp, Lp
        Lk = Lk + 5
        Hp = Hp - 5
        Lp = Lp - 5
        self.go_back(update)

    def is_going_to_state17(self, update):
        text = update.message.text
        return text.lower() == '17'
    def on_enter_state17(self, update):
        dice = random.randint(0,3)
        if dice == 1:
            update.message.reply_text("ｘｘ個人電腦維修工作室\n這天半夜有個客人打電話來問說\n客人：「ｘｘ電腦維修公司嗎？」\n工程師：「是的！請問客人有什麼問題？」\n客人：「我的電腦不能開機。」\n工程師：「您電源插頭有插嗎？」\n客人：「有的。」\n工程師：「請檢查一下ｐｏｗｅｒ電源插頭是否有鬆落，接觸不良。」\n客人：「沒！」\n工程師：「那請您拿出紙、筆來。」\n客人：「喔好。稍等一下，我先找一下拿手電筒。」\n工程師：「為什麼要拿手電筒？」\n客人：「我家停電啊！」\n工程師：「…………」\n")
        elif dice == 2:
            update.message.reply_text("明明:我爸爸在公車上會讓人,你爸爸會嗎?\n笑笑:不會.\n明明:為什麼?\n笑笑:因為,他是公車師機.")
        elif dice == 3:
            update.message.reply_text("第一天上學的小朋友哭的很可憐，老師問他原因，他說：「我不喜歡學校，可是以後我得天天來這你，一直到15歲。」老師安慰她道：「我比你更可憐，我得天天來這裡，一直到60歲呢！」")
        else:
            update.message.reply_text("突然想不到笑話拉>.<")
        self.go_back(update)

    def force_exit(self, update):
        text = update.message.text
        return text.lower() == '/exit'
