# import random #NIKHIL SAINI BOTS
# import time #NIKHIL SAINI BOTS
# import math #NIKHIL SAINI BOTS
# import os #NIKHIL SAINI BOTS
# from vars import CREDIT #NIKHIL SAINI BOTS
# from pyrogram.errors import FloodWait #NIKHIL SAINI BOTS
# from datetime import datetime,timedelta #NIKHIL SAINI BOTS

# class Timer: #NIKHIL SAINI BOTS
#     def __init__(self, time_between=5): #NIKHIL SAINI BOTS
#         self.start_time = time.time() #NIKHIL SAINI BOTS
#         self.time_between = time_between #NIKHIL SAINI BOTS

#     def can_send(self): #NIKHIL SAINI BOTS
#         if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
#             self.start_time = time.time() #NIKHIL SAINI BOTS
#             return True #NIKHIL SAINI BOTS
#         return False #NIKHIL SAINI BOTS

# #lets do calculations #NIKHIL SAINI BOTS
# def hrb(value, digits= 2, delim= "", postfix=""): #NIKHIL SAINI BOTS
#     """Return a human-readable file size. #NIKHIL SAINI BOTS
#     """ #NIKHIL SAINI BOTS
#     if value is None: #NIKHIL SAINI BOTS
#         return None #NIKHIL SAINI BOTS
#     chosen_unit = "B" #NIKHIL SAINI BOTS
#     for unit in ("KB", "MB", "GB", "TB"): #NIKHIL SAINI BOTS
#         if value > 1000: #NIKHIL SAINI BOTS
#             value /= 1024 #NIKHIL SAINI BOTS
#             chosen_unit = unit #NIKHIL SAINI BOTS
#         else: #NIKHIL SAINI BOTS
#             break #NIKHIL SAINI BOTS
#     return f"{value:.{digits}f}" + delim + chosen_unit + postfix #NIKHIL SAINI BOTS

# def hrt(seconds, precision = 0): #NIKHIL SAINI BOTS
#     """Return a human-readable time delta as a string. #NIKHIL SAINI BOTS
#     """ #NIKHIL SAINI BOTS
#     pieces = [] #NIKHIL SAINI BOTS
#     value = timedelta(seconds=seconds) #NIKHIL SAINI BOTS

#     if value.days: #NIKHIL SAINI BOTS
#         pieces.append(f"{value.days}day") #NIKHIL SAINI BOTS

#     seconds = value.seconds #NIKHIL SAINI BOTS

#     if seconds >= 3600: #NIKHIL SAINI BOTS
#         hours = int(seconds / 3600) #NIKHIL SAINI BOTS
#         pieces.append(f"{hours}hr") #NIKHIL SAINI BOTS
#         seconds -= hours * 3600 #NIKHIL SAINI BOTS

#     if seconds >= 60: #NIKHIL SAINI BOTS
#         minutes = int(seconds / 60) #NIKHIL SAINI BOTS
#         pieces.append(f"{minutes}min") #NIKHIL SAINI BOTS
#         seconds -= minutes * 60 #NIKHIL SAINI BOTS

#     if seconds > 0 or not pieces: #NIKHIL SAINI BOTS
#         pieces.append(f"{seconds}sec") #NIKHIL SAINI BOTS

#     if not precision: #NIKHIL SAINI BOTS
#         return "".join(pieces) #NIKHIL SAINI BOTS

#     return "".join(pieces[:precision]) #NIKHIL SAINI BOTS

# timer = Timer() #NIKHIL SAINI BOTS

# async def progress_bar(current, total, reply, start): #NIKHIL SAINI BOTS
#     if timer.can_send(): #NIKHIL SAINI BOTS
#         now = time.time() #NIKHIL SAINI BOTS
#         diff = now - start #NIKHIL SAINI BOTS
#         if diff < 1: #NIKHIL SAINI BOTS
#             return #NIKHIL SAINI BOTS
#         else: #NIKHIL SAINI BOTS
#             perc = f"{current * 100 / total:.1f}%" #NIKHIL SAINI BOTS
#             elapsed_time = round(diff) #NIKHIL SAINI BOTS
#             speed = current / elapsed_time #NIKHIL SAINI BOTS
#             remaining_bytes = total - current #NIKHIL SAINI BOTS
#             if speed > 0: #NIKHIL SAINI BOTS
#                 eta_seconds = remaining_bytes / speed #NIKHIL SAINI BOTS
#                 eta = hrt(eta_seconds, precision=1) #NIKHIL SAINI BOTS
#             else: #NIKHIL SAINI BOTS
#                 eta = "-" #NIKHIL SAINI BOTS
#             sp = str(hrb(speed)) + "/s" #NIKHIL SAINI BOTS
#             tot = hrb(total) #NIKHIL SAINI BOTS
#             cur = hrb(current) #NIKHIL SAINI BOTS
#             bar_length = 10 #NIKHIL SAINI BOTS
#             completed_length = int(current * bar_length / total) #NIKHIL SAINI BOTS
#             remaining_length = bar_length - completed_length #NIKHIL SAINI BOTS

#             symbol_pairs = [ #NIKHIL SAINI BOTS
#                 ("▬", "▭"), #NIKHIL SAINI BOTS
#                 ("✅", "☑️"), #NIKHIL SAINI BOTS
#                 ("🐬", "🦈"), #NIKHIL SAINI BOTS
#                 ("💚", "💛"), #NIKHIL SAINI BOTS
#                 ("🌟", "⭐"), #NIKHIL SAINI BOTS
#                 ("▰", "▱") #NIKHIL SAINI BOTS
#             ] #NIKHIL SAINI BOTS
#             chosen_pair = random.choice(symbol_pairs) #NIKHIL SAINI BOTS
#             completed_symbol, remaining_symbol = chosen_pair #NIKHIL SAINI BOTS

#             progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #NIKHIL SAINI BOTS

#             try: #NIKHIL SAINI BOTS
#                 await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
#                 #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
#             except FloodWait as e: #NIKHIL SAINI BOTS
#                 time.sleep(e.x) #NIKHIL SAINI BOTS 
import random #SHIVAAY
import time #SHIVAAY
import math #SHIVAAY
import os #SHIVAAY
from vars import CREDIT #SHIVAAY
from pyrogram.errors import FloodWait #SHIVAAY
from datetime import datetime,timedelta #SHIVAAY

class Timer: #SHIVAAY
    def __init__(self, time_between=5): #SHIVAAY
        self.start_time = time.time() #SHIVAAY
        self.time_between = time_between #SHIVAAY

    def can_send(self): #SHIVAAY
        if time.time() > (self.start_time + self.time_between): #SHIVAAY
            self.start_time = time.time() #SHIVAAY
            return True #SHIVAAY
        return False #SHIVAAY

#lets do calculations #SHIVAAY
def hrb(value, digits= 2, delim= "", postfix=""): #SHIVAAY
    """Return a human-readable file size.""" #SHIVAAY
    if value is None: #SHIVAAY
        return None #SHIVAAY
    chosen_unit = "B" #SHIVAAY
    for unit in ("KB", "MB", "GB", "TB"): #SHIVAAY
        if value > 1000: #SHIVAAY
            value /= 1024 #SHIVAAY
            chosen_unit = unit #SHIVAAY
        else: #SHIVAAY
            break #SHIVAAY
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #SHIVAAY

def hrt(seconds, precision = 0): #SHIVAAY
    """Return a human-readable time delta as a string.""" #SHIVAAY
    pieces = [] #SHIVAAY
    value = timedelta(seconds=seconds) #SHIVAAY

    if value.days: #SHIVAAY
        pieces.append(f"{value.days}day") #SHIVAAY

    seconds = value.seconds #SHIVAAY

    if seconds >= 3600: #SHIVAAY
        hours = int(seconds / 3600) #SHIVAAY
        pieces.append(f"{hours}hr") #SHIVAAY
        seconds -= hours * 3600 #SHIVAAY

    if seconds >= 60: #SHIVAAY
        minutes = int(seconds / 60) #SHIVAAY
        pieces.append(f"{minutes}min") #SHIVAAY
        seconds -= minutes * 60 #SHIVAAY

    if seconds > 0 or not pieces: #SHIVAAY
        pieces.append(f"{seconds}sec") #SHIVAAY

    if not precision: #SHIVAAY
        return "".join(pieces) #SHIVAAY

    return "".join(pieces[:precision]) #SHIVAAY

timer = Timer() #SHIVAAY

async def progress_bar(current, total, reply, start): #SHIVAAY
    if timer.can_send(): #SHIVAAY
        now = time.time() #SHIVAAY
        diff = now - start #SHIVAAY
        if diff < 1: #SHIVAAY
            return #SHIVAAY
        else: #SHIVAAY
            perc = f"{current * 100 / total:.1f}%" #SHIVAAY
            elapsed_time = round(diff) #SHIVAAY
            speed = current / elapsed_time #SHIVAAY
            remaining_bytes = total - current #SHIVAAY
            if speed > 0: #SHIVAAY
                eta_seconds = remaining_bytes / speed #SHIVAAY
                eta = hrt(eta_seconds, precision=1) #SHIVAAY
            else: #SHIVAAY
                eta = "-" #SHIVAAY
            sp = str(hrb(speed)) + "/s" #SHIVAAY
            tot = hrb(total) #SHIVAAY
            cur = hrb(current) #SHIVAAY
            bar_length = 10 #SHIVAAY
            completed_length = int(current * bar_length / total) #SHIVAAY
            remaining_length = bar_length - completed_length #SHIVAAY

            symbol_pairs = [ #SHIVAAY
                ("▬", "▭"), #SHIVAAY
                ("✅", "☑️"), #SHIVAAY
                ("🐬", "🦈"), #SHIVAAY
                ("💚", "💛"), #SHIVAAY
                ("🌟", "⭐"), #SHIVAAY
                ("▰", "▱") #SHIVAAY
            ] #SHIVAAY
            chosen_pair = random.choice(symbol_pairs) #SHIVAAY
            completed_symbol, remaining_symbol = chosen_pair #SHIVAAY

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #SHIVAAY

            try: #SHIVAAY
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙎𝙃𝙄𝙑𝘼𝘼𝙔 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
            except FloodWait as e: #SHIVAAY
                time.sleep(e.x) #SHIVAAY
