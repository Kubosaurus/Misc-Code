#encrypt = "cngu bs gurfha - eryngrf abg whfg gb gurfbyne obql, ohg gurgeniry bs guruhzna obql - ovegu gb orlbaq. rvtug synzrf - rvtug fgngvbaf ba gurcngu bs yvsr? nygubhtu gurbeqre vf abg jung frrzrq vavgvnyyl boivbhf..."
#encrypt = "\'vasnapl\' - n dhvpxyl qbhfrq synzr." #'infancy' - a quickly doused flame.
#encrypt = "\'lbhgu\' - arire gehyl rkgvathvfurq." #'youth' - never truly extinguished.
#encrypt =
#encrypt = "\'vzzbegnyvgl\' - baprnpuvrirq, hadhrapunoyr." #'immortality' - onceachieved, unquenchable.

#encrypt = "evghny bs qnlf - gur pbzvat sbegu ol qnl - n sbphfvat bs yvtug hcba qnexarff. gur cevrfgubbq bs nzha qevira haqretebhaq ol ngravfgf - ranpgf gurfr evghnyf va frperg - jul urer?"

encrypt = "evghny bs yvarntr - n cenlre orsber eblnygl? pehqr qrcvpgvbaf bs nxurangra - gurfrjrer abg znqrgb ubabhe uvz. pbafvqre guranzrf - nxurangra'f anzr renfrq nsgre qrngu - ohg gung jnf abg uvf gehranzr n cenlre gb gehgu."
#encrypt =
#encrypt =

decrypt = ""
n = 13
key = {0:"a", 
       1:"b", 
       2:"c", 
       3:"d", 
       4:"e", 
       5:"f", 
       6:"g", 
       7:"h", 
       8:"i", 
       9:"j",
       10:"k", 
       11:"l", 
       12:"m", 
       13:"n", 
       14:"o", 
       15:"p", 
       16:"q", 
       17:"r", 
       18:"s", 
       19:"t", 
       20:"u", 
       21:"v", 
       22:"w", 
       23:"x", 
       24:"y", 
       25:"z"}
for c in encrypt:
    #print c
    if(c == "-" or c == "," or c == "." or c == " " or c == "\'" or c == "?"):
        decrypt+=c
    else:
        for items in key:
            if key[items] == c:
                num = (items - n) % 26
                decrypt+=key[num]
        
print encrypt
print decrypt
