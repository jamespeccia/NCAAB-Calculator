import tkinter as tk
from ncaabb_algo_calculations import calculations

master = tk.Tk()
master.title("NCAAB Simulator")
listTeams = [''] * 2
outputs = [0] * 6 
away_predicted_score, home_predicted_score = tk.StringVar(master), tk.StringVar(master)
away_win_percentage_game, home_win_percentage_game = tk.StringVar(master), tk.StringVar(master)
total_score, home_spread = tk.StringVar(master), tk.StringVar(master)

# frame containing update data button and date selection

def center_window(width, height):
    # get screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/3) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))

def createListTeams():
    listTeams[0] = away_team.get()
    listTeams[1] = home_team.get()
    return listTeams

def calculate():
    away_team, home_team = createListTeams()
    outputs = calculations(away_team, home_team)
    away_predicted_score.set("{:0.2f}".format(outputs[0]))
    home_predicted_score.set("{:0.2f}".format(outputs[1]))
    away_win_percentage_game.set("{:0.2f}".format(outputs[2]))
    home_win_percentage_game.set("{:0.2f}".format(outputs[3]))
    total_score.set("{:0.2f}".format(outputs[4]))
    home_spread.set("{:0.2f}".format(outputs[5]))

# team labels
tk.Label(master, text=" Away Team ", bg='dodger blue').grid(row=0, padx=6, sticky='nsew')
tk.Label(master, text=" Home Team ", bg='tomato2').grid(row=0, column=2, padx=4, sticky='nsew')
away_team = tk.Entry(master)
home_team = tk.Entry(master)
away_team.grid(row=0, column=1)
home_team.grid(row=0, column=3)

# simulate buttons
f1 = tk.Frame(master)
f1.grid(row=5, column=1, sticky='nsew')
tk.Button(f1, text='           Simulate           ', relief='groove', overrelief='sunken', command=calculate).pack(side='left')

# output
out1 = tk.Label(master, text="Predicted Score", bg='red')
out1.grid(row=9, column=0, padx=6, pady=5, sticky='ew')

outName1 = tk.Label(master, textvariable=away_predicted_score, bg='dodger blue')
outName1.grid(row=9, column = 1, padx=2, pady=6, sticky='nsew')
outName2 = tk.Label(master, textvariable=home_predicted_score, bg='tomato2')
outName2.grid(row=9, column = 3, padx=2, pady=6, sticky='nsew')

out3 = tk.Label(master, text="Win Probability", bg='red')
out3.grid(row= 12, column=0, padx=6, pady=5, sticky='ew')
outName3 = tk.Label(master, textvariable=away_win_percentage_game, bg='dodger blue')
outName3.grid(row=12, column = 1, padx=2, pady=6, sticky='nsew')
outName4 = tk.Label(master, textvariable=home_win_percentage_game, bg='tomato2')
outName4.grid(row=12, column = 3, padx=2, pady=6, sticky='nsew')

out5 = tk.Label(master, text="Total", bg='red')
out5.grid(row=15, column=0, padx=6, pady=5, sticky='ew')
outName5 = tk.Label(master, textvariable=total_score, bg='tomato2')
outName5.grid(row=15, column=3, padx=2, pady=6, sticky='nsew')

out6 = tk.Label(master, text="Spread", bg='red')
out6.grid(row=18, column=0, padx=6, pady=5, sticky='ew')
outName6 = tk.Label(master, textvariable=home_spread, bg='tomato2')
outName6.grid(row=18, column=3, padx=2, pady=6, sticky='nsew')


center_window(500, 200)
tk.mainloop()