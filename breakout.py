import os
import cv2


def initialize(wallpaper, bar, ball, block):
	global ball_x, ball_y, bar_x, bar_y, vector_x, vector_y, block_x, block_y, cnt
	ball_x = 246
	ball_y = 500
	bar_x = 214
	vector_x = 0
	vector_y = 3
	block_x = []
	block_y = []
	cnt = 0

	for i in range(20, 406, 77):
		for j in range(5, 100, 17):
			wallpaper[j:j+block.shape[0], i:i+block.shape[1]] = block
			block_x.append(i)
			block_y.append(j)
			cnt=cnt+1

	wallpaper[ball_y:ball_y+ball.shape[0], ball_x:ball_x+ball.shape[1]] = ball
	wallpaper[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]] = bar

	cv2.imshow('Breakout', wallpaper)
	cv2.waitKey(0)


def move_ball(): #game over is also set here.
	global ball_x, ball_y, vector_xs, vector_y, cnt
	wallpaper[ball_y:ball_y+ball.shape[0], ball_x:ball_x+ball.shape[1]] = wallpaper_ori[ball_y:ball_y+ball.shape[0], ball_x:ball_x+ball.shape[1]]
	ball_x = ball_x + vector_x
	ball_y = ball_y + vector_y
	wallpaper[ball_y:ball_y+ball.shape[0], ball_x:ball_x+ball.shape[1]] = ball
	cv2.imshow('Breakout', wallpaper)

	if ball_y == 620:
		print("GAME OVER")
		exit()

	ball_bar()
	ball_wall()

	for i in range(cnt):
		ball_block(i)

def ball_bar():
	global bar_x, ball_x, ball_y, vector_x, vector_y
	
	if ball_y>588 and bar_x<=ball_x and ball_x<=bar_x+72:
		if ball_x<=bar_x+36 and vector_x<=3:
			vector_x = vector_x + 1
		elif vector_x>=-3:
			vector_x = vector_x - 1
		vector_y = -vector_y

def ball_wall():
	global ball_x, ball_y, vector_x, vector_y, cnt

	if ball_y<8:
		vector_x = vector_x + 1
		vector_y = -vector_y

	elif ball_x<5 or ball_x>480:
		vector_x = -vector_x
		vector_y = vector_y

def ball_block(i):
	global ball_x, ball_y, vector_x, vector_y, block_x, block_y, cnt

	if block_y[i]<=ball_y and ball_y<=block_y[i]+12 and block_x[i]<=ball_x and ball_x<=block_x[i]+72:
		vector_y = -vector_y
		wallpaper[block_y[i]:block_y[i]+block.shape[0], block_x[i]:block_x[i]+block.shape[1]] = wallpaper_ori[block_y[i]:block_y[i]+block.shape[0], block_x[i]:block_x[i]+block.shape[1]]

		for n in range(cnt-i-1):
			block_x[i+n]=block_x[i+n+1]
			block_y[i+n]=block_y[i+n+1]
		cnt=cnt-1

		if cnt == 0:
			print("Clear!")
			exit()

def move_bar(k):
	global bar_x
	if k==102 and bar_x>5: #input 'F'
		wallpaper[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]] = wallpaper_ori[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]]
		bar_x = bar_x-10
		wallpaper[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]] = bar
	elif k==106 and bar_x<420: #input 'J'
		wallpaper[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]] = wallpaper_ori[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]]
		bar_x = bar_x+10
		wallpaper[600:600+bar.shape[0], bar_x:bar_x+bar.shape[1]] = bar
	cv2.imshow('Breakout', wallpaper)


PWD = os.getcwd() + "/"
global wallpaper_ori, ball_x, ball_y, bar_x, bar_y, vector_x, vector_y

wallpaper = cv2.imread(PWD + "images/osaka.jpg")
wallpaper = cv2.resize(wallpaper, (500, 650))
wallpaper_ori = cv2.resize(wallpaper, (500, 650))
bar = cv2.imread(PWD + "images/bar.png")
bar = cv2.resize(bar, (72, 12))
block = cv2.imread(PWD + "images/block.png")
block = cv2.resize(block, (72, 12))
ball = cv2.imread(PWD + "images/ball.png")
ball = cv2.resize(ball, (8, 8))

initialize(wallpaper, bar, ball, block)

while True:
	k = cv2.waitKey(5) # waiting input

	move_bar(k)

	## end game
	if k==101: # input 'e'
		print('Exit')
		exit()

	move_ball()