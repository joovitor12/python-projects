import pyautogui
print('How many ores do you have?')
oreQtd = int(input())
print('Each prospection needs 5 of any ore.')
print('Sooo... you have ' + str(oreQtd) + ' ores')
prospectionTimes = oreQtd / 5
print('That means i have to prospect ' + str(prospectionTimes) + ' times!')
for i in range (int(prospectionTimes)):
    prospect = pyautogui.click(x=1174, y=1033, duration=1.5)
    ore = pyautogui.click(x=1679, y=636, duration=1.5)