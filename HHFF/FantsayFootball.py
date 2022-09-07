import pygame
import random 
WIDTH = 1238
HEIGHT = 700
LT_BL = (42, 170, 250)
DR_BL = (38, 121, 173)
YL = (255,210,142)
LT_PU = (132, 17, 250)
DR_PU = (88, 3, 173)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 60
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hoosier Hills Fantasy Football')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_name = pygame.font.match_font('times new roman')
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coins.jpg').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 35 
        self.radius =  int(self.rect.width/2)
        self.coins = 100
    def bet(self):
        week = random.randint(1,10)
        points = random.randint(1,16)
        pos = ['quarter back ', 'running back','wide reciver','tight end', 'kicker']  
        i = random.randint(1,len(pos))
        return 'How many coins would you like to bet that your '+pos[i]+' will score at least '+str(points)+' points in week '+str(week)

def draw_text(surf, text, size, x, y, color):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect = (x,y)
        surf.blit(text_surface, text_rect)
def breakdown(team1):
   #QB
     draw_text(screen, 'QB', 25, 60, 240, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[0]))), 25, 238, 240, BLACK)
     draw_text(screen, str(team1[0]), 25, 418, 240, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[0]))), 25, 860, 240, BLACK)
     #RB
     draw_text(screen, 'RB', 25, 60, 305, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[1]))), 25, 238, 305, BLACK)
     draw_text(screen, str(team1[1]), 25, 418, 305, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[1]))), 25, 860, 305, BLACK)
     draw_text(screen, 'RB', 25, 60, 375, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[2]))), 25, 238, 375, BLACK)
     draw_text(screen, str(team1[2]), 25, 418, 375, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[2]))), 25, 860, 375, BLACK)
     #WR
     draw_text(screen, 'WR', 25, 60, 430, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[3]))), 25, 238, 430, BLACK)
     draw_text(screen, str(team1[3]), 25, 418, 430, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[3]))), 25, 860, 430, BLACK)
     draw_text(screen, 'WR', 25, 60, 490, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[4]))), 25, 238, 490, BLACK)
     draw_text(screen, str(team1[4]), 25, 418, 490, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[4]))), 25, 860, 490, BLACK)
     #TE
     draw_text(screen, 'TE', 25, 60, 555, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[5]))), 25, 238, 555, BLACK)
     draw_text(screen, str(team1[5]), 25, 418, 555, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[5]))), 25, 860, 555, BLACK)
     #K
     draw_text(screen, 'K', 25, 60, 615, BLACK)
     draw_text(screen, str(getNumber(getFileName(team1[6]))), 25, 238, 615, BLACK)
     draw_text(screen, str(team1[6]), 25, 418, 615, BLACK)
     draw_text(screen, str(FindAverage(getFileName(team1[6]))), 25, 860, 615, BLACK)
def opnames(names, img, state, states):
   names.remove(names[img])
   states.remove(states[state])
   names = []
   for i in range(3):
      l = len(states) - 1
      state = states.pop(random.randint(0,l))
      l = len(names) - 1
      mas =' hello'
      n = state+mas
      names.append(n)
   return names
def draw(slide, teamnum, pos, teams, img, images, state, n):
   if(slide==1):
     draw_text(screen, 'Instructions', 55, 30, 30, BLACK)
     draw_text(screen, 'ESPN Fantasy Football is a game that lets players create their own team of athletes from any of' , 25, 130, 120, BLACK)
     draw_text(screen, 'the 32 NFL teams' , 25, 130, 145, BLACK)
     draw_text(screen, 'Each week the athletes play their games and the players receive points based on their athletes\'' , 25, 130, 170, BLACK)
     draw_text(screen, 'performance' , 25, 130, 195, BLACK)
     draw_text(screen, 'Players on the ESPN Fantasy app are paired up with an opponent from their league', 25, 130, 220 ,BLACK)
     draw_text(screen, 'the player with the most points wins for that week', 25, 130, 245 ,BLACK)
     draw_text(screen, 'NFL Fantasy teams score about 150 points per-week', 25, 130, 270 ,BLACK)
     draw_text(screen, 'Fantasy Football teams have one quarterback, two running backs, two wide receivers, one tight', 25, 130, 295 ,BLACK)
     draw_text(screen, 'end, and one kicker', 25, 130, 320 ,BLACK)
     draw_text(screen, 'In this game you will be shown four random teams from the  athletes in the Hoosier Hills ', 25, 130, 345 ,BLACK)
     draw_text(screen, 'Conference in Southern Indiana, not the NFL, and will be asked to choose which team you', 25, 130, 370, BLACK)
     draw_text(screen, 'would like to draft for your fantasy team', 25, 130, 395, BLACK)
     draw_text(screen, 'Next (space bar)', 32, 955, 635, BLACK)
     pygame.display.update()
   elif(slide==2):
      draw_text(screen, 'What is your team\'s mascot?', 75, 30, 30, BLACK)
      for i in range(10):
         im = images[i]
         image = pygame.image.load(im).convert()
         if(i<5):
            screen.blit(image,(5+(210*i),140))
            draw_text(screen, str(i), 60, 55+(5+(210*i)), 315, BLACK)
         if(i>=5):
            screen.blit(image,(5+(210*(9-i)),445))
            draw_text(screen, str(i), 60, 55+(5+(210*(9-i))), 615, BLACK)
      draw_text(screen, 'Press the indicated key', 22, 955, 635, BLACK)
      pygame.display.update()
   simg = pygame.image.load('s'+images[img]).convert()
   states = ['Delaware', 'Montana', 'North Dakota', 'New Mexico', 'West Virginia', 'Oregon', 'Nebraska', 'Oklahoma','Arkansas','Conneticut']
   names = ['Cardnials', 'Royals', 'Doughnuts', 'Knights', 'Suns', 'Pirates', 'Pretzels', 'Rams', 'Shields', 'Flames']
   teamname = states[img]+' '+names[img]
   used = images.pop(img)
   used = names.pop(img)
   op1name = n[0]
   op2name = n[1]
   img = random.randint(0,len(images))
   simg1 = pygame.image.load('s'+images[img-1]).convert
   if(img == 0):
         main = (217,54,68)
         next = (180,45,52)
   if(img == 1):
         main = (217,164,4)
         next = (242,204,12)
   if(img == 2):
         main = (242,171,39)
         next = (166,83,98)
   if(img == 3):
         main = (242,29,47)
         next = (217,164,4)
   if(img == 4):
         main = (242,199,68)
         next = (108,140,131)
   if(img == 5):
         main = (217,54,84)
         next = (166,154,133)
   if(img == 6):
         main = (242,124,56)
         next = (114,70,54)
   if(img == 7):
         main = (166,54,133)
         next = (89,80,71)
   if(img == 8):
         main = (86,115,140)
         next = (191,153,153)
   if(img == 9):
         main = (217,37,52)
         next = (242,159,5)
   # Pick positions
   elif(slide==3):
     screen.blit(simg,(0,0))
     pygame.draw.rect(screen, main, (100,30,879,70))
     draw_text(screen, teamname, 55, 105, 30, WHITE)
     draw_text(screen, 'Position', 25, 60, 175, BLACK)
     pygame.draw.line(screen, BLACK, (170,140), (170,695), 2)
     draw_text(screen, 'Number', 25, 215, 175, BLACK)
     pygame.draw.line(screen, BLACK, (380,140), (380,695), 2)
     draw_text(screen, 'Name', 25, 405, 175, BLACK)
     pygame.draw.line(screen, BLACK, (815,140), (815,695), 2)
     draw_text(screen, 'Average Points Per-Week', 25, 850, 175, BLACK)
     pygame.draw.line(screen, BLACK, (40,205), (1205,205), 2)
     team1 = teams[0]
     breakdown(team1)
     pygame.draw.rect(screen, next, (950,635,230,55))
     draw_text(screen, 'Next (space bar)', 32, 955, 635, WHITE)
     pygame.display.update()
   elif(slide==4):
     screen.blit(simg1,(0,0))
     pygame.draw.rect(screen, main, (100,30,879,70))
     draw_text(screen, op1name, 55, 105, 30, WHITE)
     draw_text(screen, 'Position', 25, 60, 175, BLACK)
     pygame.draw.line(screen, BLACK, (170,140), (170,695), 2)
     draw_text(screen, 'Number', 25, 215, 175, BLACK)
     pygame.draw.line(screen, BLACK, (380,140), (380,695), 2)
     draw_text(screen, 'Name', 25, 405, 175, BLACK)
     pygame.draw.line(screen, BLACK, (815,140), (815,695), 2)
     draw_text(screen, 'Average Points Per-Week', 25, 850, 175, BLACK)
     pygame.draw.line(screen, BLACK, (40,205), (1205,205), 2)
     pygame.draw.rect(screen, next, (950,635,230,55))
     draw_text(screen, 'Next (space bar)', 32, 955, 635, WHITE)
     team1 = teams[1]
     breakdown(team1)
     pygame.display.update()
   elif(slide==5):
     screen.blit(simg,(0,0))
     pygame.draw.rect(screen, main, (100,30,879,70))
     draw_text(screen, op2name, 55, 105, 30, WHITE)
     draw_text(screen, 'Position', 25, 60, 175, BLACK)
     pygame.draw.line(screen, BLACK, (170,140), (170,695), 2)
     draw_text(screen, 'Number', 25, 215, 175, BLACK)
     pygame.draw.line(screen, BLACK, (380,140), (380,695), 2)
     draw_text(screen, 'Name', 25, 405, 175, BLACK)
     pygame.draw.line(screen, BLACK, (815,140), (815,695), 2)
     draw_text(screen, 'Average Points Per-Week', 25, 850, 175, BLACK)
     pygame.draw.line(screen, BLACK, (40,205), (1205,205), 2)
     team1 = teams[2]
     pygame.draw.rect(screen, next, (950,635,230,55))
     draw_text(screen, 'Next (space bar)', 32, 955, 635, WHITE)
     breakdown(team1)
     pygame.display.update()
   elif(slide==6):
     draw_text(screen, 'What team would you like to draft?', 75, 30, 30, BLACK)
     pygame.draw.rect(screen, main, (35,125,280,70))
     draw_text(screen, 'Team 1 (1)', 55, 40, 125, WHITE)
     draw_text(screen, 'Average Points Per-Game', 45, 240, 245, BLACK)
     draw_text(screen, str(teamAverage(teams[0])), 50, 780, 245, BLACK)
     pygame.draw.rect(screen, main, (35,315,280,70))
     draw_text(screen, 'Team 2 (2)', 55, 40, 315, WHITE)
     draw_text(screen, 'Average Points Per-Game', 45, 240, 450, BLACK)
     draw_text(screen, str(teamAverage(teams[2])), 50, 780, 450, BLACK)
     pygame.draw.rect(screen, main, (35,505,280,70))
     draw_text(screen, 'Team 3 (3)', 55, 40, 505, WHITE)
     draw_text(screen, 'Average Points Per-Game', 45, 240, 650, BLACK)
     draw_text(screen, str(teamAverage(teams[3])), 50, 780, 650, BLACK)
     pygame.draw.rect(screen, next, (950,635,230,55))
     draw_text(screen, 'Press the indicated key', 22, 955, 635, WHITE)
     pygame.display.update()
   elif(slide==7):
     screen.blit(simg,(0,0))
     pygame.draw.rect(screen, main, (100,30,879,70))
     draw_text(screen, teamname+' Breakdown', 55, 105, 30, WHITE)
     draw_text(screen, 'Week', 40, 202, 124, BLACK)
     draw_text(screen, 'Points', 40, 835, 124, BLACK)
     pygame.draw.line(screen, BLACK, (25,190), (1185,190), 2)
     pygame.draw.line(screen, BLACK, (615,140), (615,680), 2)
     scores = weekScores(teams, teamnum)
     for i in range(10):
      draw_text(screen, str(i+1), 30, 245, (200+(i*58)), BLACK)
      draw_text(screen, str(scores[i]), 30, 900, (200+(i*58)), BLACK)
     pygame.draw.rect(screen, main, (515,290,210,200))
     draw_text(screen, 'Total', 55, 555, 325, WHITE)
     draw_text(screen, str(scores[9]), 55, 545, 395, WHITE)
     pygame.draw.rect(screen, next, (995,635,230,55))
     draw_text(screen, 'Next (space bar)', 32, 1000, 635, WHITE)
     pygame.display.update()
   elif(slide==8):   
     pygame.draw.rect(screen, main, (100,30,879,70))
     draw_text(screen, str(teamnum)+' compared to '+op1name+' and '+op2name, 55, 105, 30, WHITE)
     for i in range(10):
      scores1 = weekScores(teams, teamnum)
      draw_text(screen, str(i+1), 30, 80, (185+(i*58)), BLACK)
      draw_text(screen, str(scores1[i]), 30, 240, (185+(i*58)), BLACK)
      scores2 = weekScores(teams, ot[0])
      draw_text(screen, str(scores2[i]), 30, 475, (185+(i*58)), BLACK)
      scores3 = weekScores(teams, ot[1])
      draw_text(screen, str(scores3[i]), 30, 700, (185+(i*58)), BLACK)
      if(scores1[i]>scores2[i] and scores1[i]>scores3[i]):
         draw_text(screen, str(scores1[i]), 30, 240, (185+(i*58)), next)
     pygame.draw.line(screen, BLACK, (165,140), (165,700), 2)
     pygame.draw.line(screen, BLACK, (415,140), (415,700), 2)
     pygame.draw.line(screen, BLACK, (650,140), (650,700), 2)
     pygame.draw.line(screen, BLACK, (25,175), (1090,175), 2)
     draw_text(screen, 'Week', 25, 60, 125 , WHITE)
     draw_text(screen, teamname, 20, 240, 125, WHITE)
     draw_text(screen, op1nmae, 20, 460, 125, WHITE)
     draw_text(screen, op2name, 20, 695, 125, WHITE)
     pygame.display.update()
#Gets the avrage score per-week of any team
def teamAverage(team):
   sum = 0
   for i  in range(len(team)):
      sum += FindAverage(getFileName(team[i]))
   return round(sum,2)
#Gets a players number by name 
def getNumber(name):
   r = open(name,'r')
   for record in r:
    a = record.split('\n')
    a = a[0].split('/')
    num = a[0]
   return num 
#Finds average points based on the 9 game regular season
def FindAverage(player):
  sum = 0
  len = 0
  r = open(player,'r')
  for record in r:
    a = record.split('\n')
    a = a[0].split('/')
    len = len+1
    if(a[1]=='QB'):
      sum = sum + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
    elif(a[1]=='RB'):
      sum = sum + (.1*(int(a[3]))+6*(int(a[4])))
    elif(a[1]=='WR' or a[1]=='TE'):
      sum = sum + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
    elif(a[1]=='K'):
      sum = sum + (.04*(int(a[3]))+2*(int(a[4])))
  r.close()
  avg = sum/len
  return round(avg,2)

#Turns name into the file name ex.Colin Yancey -> Colin_Yancey.txt
def getFileName(name):
  index = name.index(' ')
  first = name[0:index]
  last = name[index+1:len(name)]
  return first+'_'+last+'.txt'
  
#Truns file name into name ex. Colin_Yancey.txt --> Colin Yancey 
def getName(fileName):
  index = fileName.index('_')
  first = name[0:index]
  last = name[index+1:len(name)]
  return first+' '+last
  
#Random Teams
def randomTeams(QBnames,RBnames,WRnames,TEnames,Knames):
   teams = []
   for i in range(4):
      QB = QBnames.pop(random.randint(0,(len(QBnames)-1)))
      RB1 = RBnames.pop(random.randint(0,(len(RBnames)-1)))
      RB2 = RBnames.pop(random.randint(0,(len(RBnames)-1)))
      WR1 = WRnames.pop(random.randint(0,(len(WRnames)-1)))
      WR2 = WRnames.pop(random.randint(0,(len(WRnames)-1)))
      TE = TEnames.pop(random.randint(0,(len(TEnames)-1)))
      K = Knames.pop(random.randint(0,(len(Knames)-1)))
      team = [QB,RB1,RB2,WR1,WR2,TE,K]
      teams.append(team)
   return teams

#Finds the weekly score for 9 weeks of any team
def weekScores(teams, teamNumber):
  s1 = 0
  s2 = 0
  s3 = 0
  s4 = 0
  s5 = 0
  s6 = 0
  s7 = 0
  s8 = 0
  s9 = 0
  i = 1
  for j in range(7):
   r = open(getFileName(teams[teamNumber-1][j]),'r')
   for record in r:
    a = record.split('\n')
    a = a[0].split('/')
    # if QB
    if(j==0):
      if(i==1):
         s1 = s1+ (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
         i=i+1
      elif(i==2):
        s2 = s2 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==3):
        s3 = s3 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==4):
        s4 = s4 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==5):
        s5 = s5 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==6):
        s6 = s6 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==7):
        s7 = s7 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==8):
        s8 = s8 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      else:
        s9 = s9 + (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=1  
    # if RB
    if(j==1 or j==2):
      if(i==1):
        s1 = s1 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==2):
        s2 = s2 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==3):
        s3 = s3 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==4):
        s4 = s4 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==5):
        s5 = s5 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==6):
        s6 = s6 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==7):
        s7 = s7 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==8):
        s8 = s8 + (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      else:
        s9 = s9 +  (.1*(int(a[3]))+6*(int(a[4])))
        i = 1
    # if WR
    if(j==3 or j==4):
      if(i==1):
        s1 = s1 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==2):
        s2 = s2 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==3):
        s3 = s3 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==4):
        s4 = s4 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==5):
        s5 = s5 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==6):
        s6 = s6 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==7):
        s7 = s7 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==8):
        s8 = s8 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      else:
        s9 = s9 +  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = 1
    # if TE
    if(j==5):
      if(i==1):
        s1 = s1 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==2):
        s2 = s2 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==3):
        s3 = s3 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==4):
        s4 = s4 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==5):
        s5 = s5 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==6):
        s6 = s6 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==7):
        s7 = s7 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==8):
        s8 = s8 + (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      else:
        s9 = s9 +  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = 1  
    if(j==6):
      if(i==1):
        s1 = s1 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==2):
        s2 = s2 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==3):
        s3 = s3 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==4):
        s4 = s4 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==5):
        s5 = s5 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==6):
        s6 = s6 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==7):
        s7 = s7 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==8):
        s8 = s8 + (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      else:
        s9 = s9 +  (.04*(int(a[3]))+2*(int(a[4])))
        i = 1
  s1 = round(s1,2)
  s2 = round(s2,2)
  s3 = round(s3,2)
  s4 = round(s4,2)
  s5 = round(s5,2)
  s6 = round(s6,2)
  s7 = round(s7,2)
  s8 = round(s8,2)
  s9 = round(s9,2)
  sum = round(s1+s2+s3+s4+s5+s6+s7+s8+s9,2)
  r = [s1,s2,s3,s4,s5,s6,s7,s8,s9,sum]
  return r
#Shows how well a player does in the 9 week season
def playerScores(fileName):
  w1 = 0
  w2 = 0
  w3 = 0
  w4 = 0
  w5 = 0
  w6 = 0
  w7 = 0
  w8 = 0
  w9 = 0
  i = 1
  r = open(fileName,'r')
  for record in r:
    a = record.split('\n')
    a = a[0].split('/')
    if(a[1]=='QB'):
      if(i==1):
        w1 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==2):
        w2 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==3):
        w3 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==4):
        w4 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==5):
        w5 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==6):
        w6 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==7):
        w7 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      elif(i==8):
        w8 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
        i=i+1
      else:
        w9 = (.04*(int(a[3]))+4*(int(a[4]))-2*(int(a[5]))+.1*(int(a[6]))+6*(int(a[7])))
    elif(a[1]=='RB'):
      if(i==1):
        w1 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==2):
        w2 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==3):
        w3 = (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==4):
        w4 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==5):
        w5 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==6):
        w6 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==7):
        w7 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      elif(i==8):
        w8 =  (.1*(int(a[3]))+6*(int(a[4])))
        i = i+1
      else:
        w9 =  (.1*(int(a[3]))+6*(int(a[4])))
    elif(a[1]=='WR' or a[1]=='TE'):
      if(i==1):
        w1 =  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==2):
        w2 =  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==3):
        w3 =  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==4):
        w4 = (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==5):
        w5 =  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==6):
        w6 = (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==7):
        w7 = (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      elif(i==8):
        w8 = (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
        i = i+1
      else:
        w9 =  (.1*(int(a[3]))+1*(int(a[5]))+6*(int(a[4])))
    elif(a[1]=='K'):
      if(i==1):
        w1 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==2):
        w2 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==3):
        w3 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==4):
        w4 = (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==5):
        w5 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==6):
        w6 = (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==7):
        w7 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      elif(i==8):
        w8 =  (.04*(int(a[3]))+2*(int(a[4])))
        i = i+1
      else:
        w9 =  (.04*(int(a[3]))+2*(int(a[4])))
  r.close()
  w1 = round(w1,2)
  w2 = round(w2,2)
  w3 = round(w3,2)
  w4 = round(w4,2)
  w5 = round(w5,2)
  w6 = round(w6,2)
  w7 = round(w7,2)
  w8 = round(w8,2)
  w9 = round(w9,2)
  sum = round(w1+w2+w3+w4+w5+w6+w7+w8+w9,2)
  name = getName(fileName)
  r = name+'\n-------------\nWeek 1 Score:\t'+str(w1)+'\nWeek 2 Score:\t'+str(w2)+'\nWeek 3 Score:\t'+str(w3)+'\nWeek 4 Score:\t'+str(w4)+'\nWeek 5 Score:\t'+str(w5)+'\nWeek 6 Score:\t'+str(w6)+'\nWeek 7 Score:\t'+str(w7)+'\nWeek 8 Score:\t'+str(w8)+'\nWeek 9 Score:\t'+str(w9)+'\nTOTAL FOR WHOLE SEASON:'+str(sum)         
  return r
#main
QBNames = []
QBScores = []
RBNames = []
RBScores = []
WRNames = []
WRScores = []
TENames = []
TEScores = []
KNames = []
KScores = []
#Make Columus East team 
QBScores.append(FindAverage('Cole_Gilley.txt'))
QBNames.append('Cole Gilley')
RBScores.append(FindAverage('Tryce_Villarreal.txt'))
RBNames.append('Tryce Villarreal')
RBScores.append(FindAverage('Mark_Mcdonald.txt'))
RBNames.append('Mark Mcdonald')
TEScores.append(FindAverage('Malachi_Parks.txt'))
TENames.append('Malachi Parks')
WRScores.append(FindAverage('Collin_Phillips.txt'))
WRNames.append('Collin Phillips')
WRScores.append(FindAverage('Dalton_Back.txt'))
WRNames.append('Dalton Back')
TEScores.append(FindAverage('Lance_Greiwe.txt'))
TENames.append('Lance Greiwe')
KScores.append(FindAverage('Kai_Stidham.txt'))
KNames.append('Kai Stidham')
#Make Floyd Central Team
QBScores.append(FindAverage('Tristan_Polk.txt'))
QBNames.append('Tristan Polk')
RBScores.append(FindAverage('Wenkers_Wright.txt'))
RBNames.append('Wenkers Wright')
TEScores.append(FindAverage('Calvin_Brown.txt'))
TENames.append('Calvin Brown')
WRScores.append(FindAverage('Kaleb_Quintechet.txt'))
WRNames.append('Kaleb Quintechet')
WRScores.append(FindAverage('Landon_Deweese.txt'))
WRNames.append('Landon Deweese')
KScores.append(FindAverage('Cole_Hussung.txt'))
KNames.append('Cole Hussung')
#Make New Albany Team
QBScores.append(FindAverage('Derell_Simmons.txt'))
QBNames.append('Derell Simmons')
QBScores.append(FindAverage('Kyondre_Winford.txt'))
QBNames.append('Kyondre Winford')
RBScores.append(FindAverage('Dejon_Winburn.txt'))
RBNames.append('Dejon Winburn')
RBScores.append(FindAverage('Myles_Johnson.txt'))
RBNames.append('Myles Johnson')
#Make Seymore Team
QBScores.append(FindAverage('Brendan_Smith.txt'))
QBNames.append('Brendan Smith')
RBScores.append(FindAverage('Chandler_Drummond.txt'))
RBNames.append('Chandler Drummond')
WRScores.append(FindAverage('Ely_Henderson.txt'))
WRNames.append('Ely Henderson')
TEScores.append(FindAverage('Drew_Vehslage.txt'))
TENames.append('Drew Vehslage')
KScores.append(FindAverage('Josh_Guevara.txt'))
KNames.append('Josh Guevara')
KScores.append(FindAverage('Caleb_Elliott.txt'))
KNames.append('Caleb Elliott')
#Make Jennings County Team 
QBScores.append(FindAverage('Lance_Bailey.txt'))
QBNames.append('Lance Bailey')
RBScores.append(FindAverage('Owen_Miller.txt'))
RBNames.append('Owen Miller')
RBScores.append(FindAverage('Peyton_Hayden.txt'))
RBNames.append('Peyton Hayden')
RBScores.append(FindAverage('Owen_Deaton.txt'))
RBNames.append('Owen Deaton')
TEScores.append(FindAverage('Levi_Peacock.txt'))
TENames.append('Levi Peacock')
WRScores.append(FindAverage('Jared_Corya.txt'))
WRNames.append('Jared Corya')
KScores.append(FindAverage('Jayden_Vanosdol.txt'))
KNames.append('Jayden Vanosdol')
#Make Madison Team
QBScores.append(FindAverage('Parker_Jones.txt'))
QBNames.append('Parker Jones')
RBScores.append(FindAverage('Trenton_Barnes.txt'))
RBNames.append('Trenton Barnes')
WRScores.append(FindAverage('Colin_Yancey.txt'))
WRNames.append('Colin Yancey')
WRScores.append(FindAverage('Bryce_Foy.txt'))
WRNames.append('Bryce Foy')
#Game loop
teams = randomTeams(QBNames,RBNames,WRNames,TENames,KNames)
running = True
next = False
slide = 1
teamnum = 0
pos = ''
img = 0
state = 0
images = ['bird.jpg', 'crown.jpg','doughnut.jpg','knight.jpg','shield1.jpg','pirate.jpg','pretzel.jpg','ram.jpg','shield2.jpg','flame.jpg']
states = ['Delaware', 'Montana', 'North Dakota', 'New Mexico', 'West Virginia', 'Oregon', 'Nebraska', 'Oklahoma']
names = ['Cardnials', 'Royals', 'Doughnuts', 'Knights', 'Suns', 'Pirates', 'Pretzels', 'Rams', 'Shields', 'Flames']
n = opnames(names, img, state, states)
while running:
    # keep loop running at the right speed
    screen.fill(WHITE)
    draw(slide, teamnum, pos, teams, img, images, state, n)
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
         if event.key == 32:
            slide += 1
         #determind which logo
         if ((event.key == 48 or event.key == 256) and slide == 2):
            img = 0
            slide += 1
         if((event.key == 49 or event.key == 257) and slide == 2):
            img = 1
            slide += 1
         if((event.key == 50 or event.key == 258) and slide == 2):
            img = 2
            slide += 1
         if((event.key == 51 or event.key == 259) and slide == 2):
            img = 3
            slide += 1
         if((event.key == 52 or event.key == 260) and slide == 2):
            img = 4
            slide += 1
         if((event.key == 53 or event.key == 261) and slide == 2):
            img = 5
            slide += 1
         if((event.key == 54 or event.key == 262) and slide == 2):
            img = 6
            slide += 1
         if((event.key == 55 or event.key == 263) and slide == 2):
            img = 7
            slide += 1
         if((event.key == 56 or event.key == 264) and slide == 2):
            img = 8
            slide += 1
         if((event.key == 57 or event.key == 265) and slide == 2):
            img = 9
            slide += 1
         #determind which team to draft   
         if (event.key == 49 or event.key == 257) and slide == 7:
            teamnum = 1
            slide += 1
         if (event.key == 50 or event.key == 258) and slide == 7:
            teamnum =2 
            slide += 1
         if (event.key == 51 or event.key == 259) and slide == 7:
            teamnum = 3
            slide += 1
              
pygame.quit()