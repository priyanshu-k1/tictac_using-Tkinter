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
win.iconbitmap("mains\\icon.ico")

mixer.init()
mixer.music.load("mains\\bgm.mp3")
mixer.music.play(-1)
global MainGameFrame,NameWindowCouter,PlayerOneName,PlayerTwoName,PlayerOneNameText,PlayerTwoNameText,RandomNumOne,RandomNumTwo
global FinalNum,FirstPlayerFinal,FirstPlayerLabel,RandomNumThree,GlobalCounterForXandO,Button1,Button2,Button3,Button4,Button5,Button6,Button7,Button8,Button9
global RestTiles,MuteBgm,MusicCounter,matrix,songCounter,PlayerOneScoreMatrix,PlayerTwoScoreMatrix
global NameLabel1,NameLabel2,ScoreScreen1,ScoreScreen2,TotalCounterSpace,ScoreCounterUpdater
global tiles1,tiles2,tiles3,tiles4,tiles5,tiles6,tiles7,tiles8,tiles9,MakeAiMove,checkISwinning,AiMode
AiMode=0
sum1=0
sum2=0
PlayerOneNameText='PLAYER 1'
PlayerTwoNameText='PLAYER 2'
songCounter=0
NameWindowCouter=0
MusicCounter=0
GlobalCounterForXandO=0
matrix=[
				[4,5,6],
				[4,5,6],
				[4,5,6]
			 ]
PlayerOneScoreMatrix=[]
PlayerTwoScoreMatrix=[]
tiles1=["notpressed",0]
tiles2=["notpressed",0]
tiles3=["notpressed",0]
tiles4=["notpressed",0]
tiles5=["notpressed",0]
tiles6=["notpressed",0]
tiles7=["notpressed",0]
tiles8=["notpressed",0]
tiles9=["notpressed",0]
#FUNCTION::::::

SecondWin=Toplevel(win)
SecondWin.iconbitmap("mains\\icon.ico")
SecondWin.title("SCORE CARD WINDOW ")
SecondWin.geometry('300x500')
SecondWin.resizable(False,False)
NameFrame=Frame(SecondWin,bg='red',height=70,width=300)
NameFrame.place(x=0,y=5)

NameLabel1=Label(NameFrame,text="Player 1",bg='blue',height=5,width=21)
NameLabel1.place(x=0)

NameLabel2=Label(NameFrame,text="Player 2",bg='green',height=5,width=21)
NameLabel2.place(x=150)

ScoreScreen1=Text(SecondWin,bg="pink",font="times 35",height=23,width=6)
ScoreScreen1.place(y=77,x=2)
ScoreScreen1.config(state=DISABLED)

ScoreScreen2=Text(SecondWin,bg="pink",font="times 35",height=23,width=6)
ScoreScreen2.place(y=77,x=151)
ScoreScreen2.config(state=DISABLED)

TotalCounterSpace=Label(SecondWin,bg='sky blue',text="0:TOTAL:0 ",font='times 15',height=2,width=27)
TotalCounterSpace.place(y=449)

def ScoreCounterUpdater():
	global sum1,sum2
	sum1=0
	sum2=0
	try:
	  for i in PlayerOneScoreMatrix:
		  sum1=sum1+i
	  for j in PlayerTwoScoreMatrix:
		  sum2=sum2+j
	except:
	  pass
	TotalCounterSpace.config(text=f"{sum1}:TOTAL:{sum2}")

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
			NameLabel1.config(text=f"{UserNameEntry.get()}")
			NameLabel2.config(text=f"{UserName2Entry.get()}")
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
	global matrix,GlobalCounterForXandO,songCounter,MusicCounter,PlayerTwoScoreMatrix,PlayerTwoScoreMatrix
	global tiles1,tiles2,tiles3,tiles4,tiles5,tiles6,tiles7,tiles8,tiles9,tileslist
	try:
		ScoreScreen1.config(state=NORMAL)
		ScoreScreen2.config(state=NORMAL)
	except:
		pass
	if(GlobalCounterForXandO==0):
		PlayerTwoScoreMatrix.insert(len(PlayerTwoScoreMatrix),1)
		try:
			ScoreScreen2.insert(END,f"\n{1}")
			ScoreScreen1.insert(END,f"\n{0}")
		except:
			pass
	else:
		PlayerOneScoreMatrix.insert(len(PlayerTwoScoreMatrix),1)
		try:
			ScoreScreen1.insert(END,f"\n{1}")
			ScoreScreen2.insert(END,f"\n{0}")
		except:
			pass
	try:
		ScoreScreen1.config(state=DISABLED)
		ScoreScreen2.config(state=DISABLED)
		ScoreCounterUpdater()
	except:
		pass
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
	tiles1=["notpressed",0]
	tiles2=["notpressed",0]
	tiles3=["notpressed",0]
	tiles4=["notpressed",0]
	tiles5=["notpressed",0]
	tiles6=["notpressed",0]
	tiles7=["notpressed",0]
	tiles8=["notpressed",0]
	tiles9=["notpressed",0]
	FirstToStartGame()
	FrameConfig()
	matrix=[[4,5,6],
		[4,5,6],
		[4,5,6]]
	songCounter=0
	mixer.music.load("mains\\bgm.mp3")
	mixer.music.play(-1)
	if(MusicCounter==1):
		MuteBgm.config(text="MUTE")
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
	try:
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
	except:
		pass
	FirstPlayerLabel.after(10,GameOver)
#ON BUTTON PRESS FUNCTION
def ButtonOne():
	global GlobalCounterForXandO,tiles1
	
	tiles1[0]="pressed"
	tiles1[1]=1
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
	global GlobalCounterForXandO,tiles2
	
	tiles2[0]="pressed"
	tiles2[1]=1
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
	global GlobalCounterForXandO,tiles3
	
	tiles3[0]="pressed"
	tiles3[1]=1
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
	global GlobalCounterForXandO,tiles4
	
	tiles4[0]="pressed"
	tiles4[1]=1
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
	global GlobalCounterForXandO,tiles5
	
	tiles5[0]="pressed"
	tiles5[1]=1
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
	global GlobalCounterForXandO,tiles6
	
	tiles6[0]="pressed"
	tiles6[1]=1
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
	global GlobalCounterForXandO,tiles7
	
	tiles7[0]="pressed"
	tiles7[1]=1
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
	global GlobalCounterForXandO,tiles8
	
	tiles8[0]="pressed"
	tiles8[1]=1
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
	global GlobalCounterForXandO,tiles9
	tiles9[0]="pressed"
	tiles9[1]=1
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

def AgainstAiFunc():
		global PlayerTwoNameText,NameLabel2,GlobalCounterForXandO
		AiMode=1
		PlayerTwoNameText='A.N.S.H.U'
		NameLabel2.config(text=PlayerTwoNameText)
		PlayerTwoName.config(text=PlayerTwoNameText)
		try:
			if(GlobalCounterForXandO==0):
				pass
				print("hello")
			else:
				checkISwinning()
				GlobalCounterForXandO=GlobalCounterForXandO+1
		except Exception as e:
			print(e)
def MakeAiMove(num):
	if(num==1):
		ButtonOne()
	elif(num==2):
		ButtonTwo()
	elif(num==3):
		ButtonThree()
	elif(num==3):
		ButtonFour()
	elif(num==5):
		ButtonFive()
	elif(num==6):
		ButtonSix()
	elif(num==7):
		ButtonSeven()
	elif(num==8):
		ButtonEight()
	elif(num==9):
		ButtonNine()
	else:
		pass
def checkISwinning():
  #1st row
  if((matrix[0][0]==1 or matrix[0][0]==0) and (matrix[0][1]==1 or matrix[0][1]==0)):
      MakeAiMove(3)

  elif((matrix[0][2]==1 or matrix[0][2]==0) and (matrix[0][1]==1 or matrix[0][1]==0)):
    MakeAiMove(1)

  elif((matrix[0][0]==1 or matrix[0][0]==0) and (matrix[0][2]==1 or matrix[0][2]==0)):
    MakeAiMove(2)

  #2nd row
  elif((matrix[1][0]==1 or matrix[1][0]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
      MakeAiMove(4)

  elif((matrix[1][2]==1 or matrix[1][2]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
   MakeAiMove(6)

  elif((matrix[1][0]==1 or matrix[1][0]==0) and (matrix[1][2]==1 or matrix[1][2]==0)):
    MakeAiMove(5)

  #3rd  row
  elif((matrix[2][0]==1 or matrix[2][0]==0) and (matrix[2][1]==1 or matrix[2][1]==0)):
      MakeAiMove(9)

  elif((matrix[2][2]==1 or matrix[2][2]==0) and (matrix[2][1]==1 or matrix[2][1]==0)):
    MakeAiMove(7)

  elif((matrix[2][0]==1 or matrix[2][0]==0) and (matrix[2][2]==1 or matrix[2][2]==0)):
    MakeAiMove(8)

  #colomn one
  elif((matrix[0][0]==1 or matrix[0][0]==0) and (matrix[1][0]==1 or matrix[1][0]==0)):
      MakeAiMove(7)

  elif((matrix[2][0]==1 or matrix[2][0]==0) and (matrix[1][0]==1 or matrix[1][0]==0)):
      MakeAiMove(1)

  elif((matrix[2][0]==1 or matrix[2][0]==0) and (matrix[0][0]==1 or matrix[0][0]==0)):
      MakeAiMove(4)

  #colomn two
  elif((matrix[0][1]==1 or matrix[0][1]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
      MakeAiMove(8)

  elif((matrix[2][1]==1 or matrix[2][1]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
      MakeAiMove(2)
      
  elif((matrix[2][1]==1 or matrix[2][1]==0) and (matrix[0][1]==1 or matrix[0][1]==0)):
      MakeAiMove(5)

  #colomn three
  elif((matrix[0][2]==1 or matrix[0][2]==0) and (matrix[1][2]==1 or matrix[1][2]==0)):
      MakeAiMove(9)

  elif((matrix[2][2]==1 or matrix[2][2]==0) and (matrix[1][2]==1 or matrix[1][2]==0)):
      MakeAiMove(3)
      
  elif((matrix[2][2]==1 or matrix[2][2]==0) and (matrix[0][2]==1 or matrix[0][2]==0)):
      MakeAiMove(6)
  #Diagnoal

  elif((matrix[0][0]==1 or matrix[0][0]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
    MakeAiMove(9)

  elif((matrix[0][0]==1 or matrix[0][0]==0) and (matrix[2][2]==1 or matrix[2][2]==0)):
    MakeAiMove(5)

  elif((matrix[1][1]==1 or matrix[1][1]==0) and (matrix[2][2]==1 or matrix[2][2]==0)):
    MakeAiMove(1)


  elif((matrix[0][2]==1 or matrix[0][2]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
    MakeAiMove(8)

  elif((matrix[0][2]==1 or matrix[0][2]==0) and (matrix[2][1]==1 or matrix[2][1]==0)):
    MakeAiMove(5)

  elif((matrix[2][1]==1 or matrix[2][1]==0) and (matrix[1][1]==1 or matrix[1][1]==0)):
    MakeAiMove(3)

  else:
  	var=randint(1,9)
  	MakeAiMove(var)
  	print(var)
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
RestTiles.place(x=40,y=550)
AgainstAi=Button(win,text="Against A.I",width=15,command=AgainstAiFunc)
AgainstAi.place(x=200,y=550)
MuteBgm=Button(win,text="MUTE",width=15,command=MuteUnMute)
MuteBgm.place(x=350,y=550)


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