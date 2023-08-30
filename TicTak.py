from tkinter import *
from random import randint
from pygame import mixer


#MAIN WINDOW DECLARATION::::::
win=Tk()
win.geometry("500x600")
win.resizable(False,False)
win.title("TIC TAK TOE")
win.config(bg='#b5ae9a')
#GLOBAL VARIABLES:::
mixer.init()
mixer.music.load("mains\\bgm.mp3")
mixer.music.play(-1)
global MainGameFrame,NameWindowCouter,PlayerOneName,PlayerTwoName,PlayerOneNameText,PlayerTwoNameText,RandomNumOne,RandomNumTwo
global FinalNum,FirstPlayerFinal,FirstPlayerLabel,RandomNumThree,GlobalCounterForXandO,Button1,Button2,Button3,Button4,Button5,Button6,Button7,Button8,Button9
global RestTiles,MuteBgm,MusicCounter,matrix,songCounter
PlayerOneNameText='PLAYER 1'
PlayerTwoNameText='PLAYER 2'
songCounter=0
NameWindowCouter=0
MusicCounter=0
GlobalCounterForXandO=0
matrix=[[4,5,6],
		[4,5,6],
		[4,5,6]]
#FUNCTION::::::
def FirstToStartGame():
	global FirstPlayerFinal,RandomNumOne,RandomNumTwo,RandomNumThree,GlobalCounterForXandO
	RandomNumOne=randint(1,999)
	RandomNumTwo=randint(1,300)
	RandomNumThree=randint(1,7)
	RandomNumFour=randint(1,3)
	FinalNum=((RandomNumTwo+RandomNumOne)*RandomNumThree)-RandomNumFour
	if(FinalNum%2==0):
		GlobalCounterForXandO=0
		FirstPlayerFinal= True
	else:
		GlobalCounterForXandO=1
		FirstPlayerFinal= False
	print(RandomNumOne,RandomNumTwo,RandomNumThree,RandomNumFour,(FinalNum%2))
def FrameConfig():
	if(FirstPlayerFinal):
			if(PlayerOneNameText != 'PLAYER1'):
				FirstPlayerLabel.config(text=f"{PlayerOneNameText} will make first move")
			else:
				FirstPlayerLabel.config(text="Player 1 will make first move")
	else:
			if(PlayerTwoNameText != 'PLAYER2'):
				FirstPlayerLabel.config(text=f"{PlayerTwoNameText} will make first move")
			else:
				FirstPlayerLabel.config(text="Player 2 will make first move")
       	
def CreateLines():
	Frame(MainGameFrame,width=2,bg='black',height=450).place(x=150,y=0)
	Frame(MainGameFrame,width=2,bg='black',height=450).place(x=300,y=0)
	Frame(MainGameFrame,width=450,bg='black',height=3).place(x=0,y=113)
	Frame(MainGameFrame,width=450,bg='black',height=3).place(x=0,y=225)
		
def AddName():
	global NameWindowCouter,PlayerOneName,PlayerTwoName
	if(NameWindowCouter<=0):
		NameWindowCouter=NameWindowCouter+1
		SetUserNameWindow=Tk()
		SetUserNameWindow.resizable(False,False)
		SetUserNameWindow.config(bg='#b5ae9a')
		SetUserNameWindow.geometry("300x150")
		SetUserNameWindow.title("SET Name")
		Label(SetUserNameWindow,text="Player 1",bg='#b5ae9a').place(x=10,y=5)
		UserNameEntry=Entry(SetUserNameWindow, width=45)
		UserNameEntry.place(x=10,y=25,height=30)
		Label(SetUserNameWindow,text="Player 2",bg='#b5ae9a').place(x=10,y=60)
		UserName2Entry=Entry(SetUserNameWindow, width=45)
		UserName2Entry.place(x=10,y=80,height=30)
		#Sub functions
		def submit():
			global NameWindowCouter,PlayerOneNameText,PlayerTwoNameText
			PlayerOneNameText=f"{UserNameEntry.get()}"
			PlayerTwoNameText=f"{UserName2Entry.get()}"
			PlayerOneName.config(text=f"{UserNameEntry.get()}")
			PlayerTwoName.config(text=f"{UserName2Entry.get()}")
			NameWindowCouter=NameWindowCouter-1
			FrameConfig()
			SetUserNameWindow.destroy()
		Button(SetUserNameWindow,text="Submit",width=15,bg="light green",command=submit).place(x=90,y=120)
		SetUserNameWindow.mainloop()
	else:
		pass
#MUTE THE BGM::
def MuteUnMute():
	global MusicCounter
	if(MusicCounter==0):
		mixer.music.pause()
		MuteBgm.config(text="UNMUTE")
		MusicCounter=MusicCounter+1
	else:
		mixer.music.unpause()
		MuteBgm.config(text="MUTE")
		MusicCounter=MusicCounter-1
#RESET BUTTON FUNCTION:
def RestTilesFunction():
	global matrix,GlobalCounterForXandO,songCounter,MusicCounter

	Button1.config(text="",bg="white")
	Button2.config(text="",bg="white")
	Button3.config(text="",bg="white")
	Button4.config(text="",bg="white")
	Button5.config(text="",bg="white")
	Button6.config(text="",bg="white")
	Button7.config(text="",bg="white")
	Button8.config(text="",bg="white")
	Button9.config(text="",bg="white")
	Button1["state"]="normal"
	Button2["state"]="normal"
	Button3["state"]="normal"
	Button4["state"]="normal"
	Button5["state"]="normal"
	Button6["state"]="normal"
	Button7["state"]="normal"
	Button8["state"]="normal"
	Button9["state"]="normal"
	FirstToStartGame()
	FrameConfig()
	matrix=[[4,5,6],
		[4,5,6],
		[4,5,6]]
	songCounter=0
	mixer.music.load("mains\\bgm.mp3")
	mixer.music.play(-1);MuteBgm.config(text="MUTE")
	MusicCounter=MusicCounter-1
#check for 0 and 1 in the matix
def check_zero(tiles):
  # Check vertical.
  for i in range(3):
    if all(tiles[i][j] == 0 for j in range(3)):
      return True

  # Check horizontal.
  for i in range(3):
    if all(tiles[j][i] == 0 for j in range(3)):
      return True

  # Check diagonal.
  if all(tiles[i][i] == 0 for i in range(3)):
    return True
  elif all(tiles[i][2-i] == 0 for i in range(3)):
    return True
  return False

def check_one(tiles):
  # Check vertical.
  for i in range(3):
    if all(tiles[i][j] == 1 for j in range(3)):
      return True

  # Check horizontal.
  for i in range(3):
    if all(tiles[j][i] == 1 for j in range(3)):
      return True

  # Check diagonal.
  if all(tiles[i][i] == 1 for i in range(3)):
    return True
  elif all(tiles[i][2-i] == 1 for i in range(3)):
    return True
  return False
def GameOver():
	global songCounter
	if(check_zero(matrix) or check_one(matrix)):
		if(songCounter<1):
			mixer.music.load("mains\\winbgm.mp3")
			mixer.music.play(-1)
		else:
			pass
		songCounter=songCounter+1
		Button1["state"]=DISABLED
		Button2["state"]=DISABLED
		Button3["state"]=DISABLED
		Button4["state"]=DISABLED
		Button5["state"]=DISABLED
		Button6["state"]=DISABLED
		Button7["state"]=DISABLED
		Button8["state"]=DISABLED
		Button9["state"]=DISABLED
		if(GlobalCounterForXandO==0):
			FirstPlayerLabel.config(text=f"{PlayerTwoNameText} won the game.")
		else:
			FirstPlayerLabel.config(text=f"{PlayerOneNameText} won the game.")
	else:
		pass
	FirstPlayerLabel.after(10,GameOver)
#ON BUTTON PRESS FUNCTION
def ButtonOne():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[0][0]=GlobalCounterForXandO
		Button1.config(text="X",bg="light green")
		Button1["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[0][0]=GlobalCounterForXandO
		Button1.config(text="O",bg="red")
		Button1["state"] = DISABLED
def ButtonTwo():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[0][1]=GlobalCounterForXandO
		Button2.config(text="X",bg="light green")
		Button2["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[0][1]=GlobalCounterForXandO
		Button2.config(text="O",bg="red")
		Button2["state"] = DISABLED
def ButtonThree():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[0][2]=GlobalCounterForXandO
		Button3.config(text="X",bg="light green")
		Button3["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[0][2]=GlobalCounterForXandO
		Button3.config(text="O",bg="red")
		Button3["state"] = DISABLED
def ButtonFour():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[1][0]=GlobalCounterForXandO
		Button4.config(text="X",bg="light green")
		Button4["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[1][0]=GlobalCounterForXandO
		Button4.config(text="O",bg="red")
		Button4["state"] = DISABLED
def ButtonFive():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[1][1]=GlobalCounterForXandO
		Button5.config(text="X",bg="light green")
		Button5["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[1][1]=GlobalCounterForXandO
		Button5.config(text="O",bg="red")
		Button5["state"] = DISABLED
def ButtonSix():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[1][2]=GlobalCounterForXandO
		Button6.config(text="X",bg="light green")
		Button6["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[1][2]=GlobalCounterForXandO
		Button6.config(text="O",bg="red")
		Button6["state"] = DISABLED
def ButtonSeven():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[2][0]=GlobalCounterForXandO
		Button7.config(text="X",bg="light green")
		Button7["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[2][0]=GlobalCounterForXandO
		Button7.config(text="O",bg="red")
		Button7["state"] = DISABLED
def ButtonEight():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[2][1]=GlobalCounterForXandO
		Button8.config(text="X",bg="light green")
		Button8["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[2][1]=GlobalCounterForXandO
		Button8.config(text="O",bg="red")
		Button8["state"] = DISABLED
def ButtonNine():
	global GlobalCounterForXandO
	if(GlobalCounterForXandO==0):
		GlobalCounterForXandO=GlobalCounterForXandO+1
		matrix[2][2]=GlobalCounterForXandO
		Button9.config(text="X",bg="light green")
		Button9["state"] = DISABLED
	else:
		GlobalCounterForXandO=GlobalCounterForXandO-1
		matrix[2][2]=GlobalCounterForXandO
		Button9.config(text="O",bg="red")
		Button9["state"] = DISABLED
#PLAYER'S DETAIL BAR::::::::::
PlayerNameFrame=Frame(win,bg='red',height=80,width=500)
PlayerNameFrame.pack(fill='y',pady=10)

PlayerOneName=Button(PlayerNameFrame,text='PLAYER 1',height=5,width=40,command=AddName)
PlayerOneName.place(y=0)

PlayerTwoName=Button(PlayerNameFrame,text='PLAYER 2',height=5,width=40,command=AddName)
PlayerTwoName.place(x=250)


#MAIN GAME SPACE::::::::::::::
FirstPlayerLabel=Label(win,text='',bg='white',height=2,width=72)
FirstPlayerLabel.place(y=95)
MainGameFrame=Frame(win,bg='white',width=450,height=900)
MainGameFrame.pack(pady=80)
#MUTE & REST BUTTON
RestTiles=Button(win,text="REST",width=15,command=RestTilesFunction)
RestTiles.place(x=100,y=550)
MuteBgm=Button(win,text="MUTE",width=15,command=MuteUnMute)
MuteBgm.place(x=300,y=550)


#TILES BUTTON
Button1=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonOne)
Button1.place(x=0,y=0)
Button2=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonTwo)
Button2.place(x=150,y=0)
Button3=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonThree)
Button3.place(x=300,y=0)

Button4=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonFour)
Button4.place(x=0,y=113)
Button5=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonFive)
Button5.place(x=150,y=113)
Button6=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonSix)
Button6.place(x=300,y=113)

Button7=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonSeven)
Button7.place(x=0,y=225)
Button8=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonEight)
Button8.place(x=150,y=225)
Button9=Button(MainGameFrame,bg='white',width=5,height=1,relief='flat',font='times 45',command=ButtonNine)
Button9.place(x=300,y=225)


#MAIN FUNCTION
FirstToStartGame()
CreateLines()
FrameConfig()
GameOver()
win.mainloop()