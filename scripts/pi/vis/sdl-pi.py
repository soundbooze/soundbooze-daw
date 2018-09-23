from sdl2 import *
from ctypes import *
import sdl2.ext
 
win = None
renderer = None

WIDTH  = 600
HEIGHT = 300

def InitializeWindow():
    global win
    SDL_Init(SDL_INIT_VIDEO)
    win = SDL_CreateWindow(b"UDUKBotViaPenghayat",
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        WIDTH, HEIGHT, SDL_WINDOW_SHOWN)

def CreateRenderer():
    global win, renderer
    renderer = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)

def ClearRenderer(renderer):
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
    SDL_RenderFillRect(renderer, SDL_Rect(0, 0, WIDTH, HEIGHT), 1)
    SDL_RenderClear(renderer)

def ShowRenderer(renderer):
    SDL_RenderPresent(renderer)

def SetColorRenderer(renderer, r, g, b):
    SDL_SetRenderDrawColor(renderer, r, g, b, 255)

def DrawRect(x, y, w, h, r, g, b):
    SetColorRenderer(renderer, r, g, b)
    SDL_RenderDrawRects(renderer, SDL_Rect(x, y, w, h), 1)

def DrawLine(x1, y1, x2, y2, r, g, b):
    SetColorRenderer(renderer, r, g, b)
    points = [SDL_Point(x1,y1), SDL_Point(x2,y2)]
    cnt = len(points)
    pointsArray = pointer((SDL_Point * cnt)())
    for i in range(cnt):
      pointsArray.contents[i] = points[i]
    SDL_RenderDrawLines(renderer, pointsArray.contents[0], cnt)

def CleanUp():
    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(win)
    SDL_Quit()

''' main '''

InitializeWindow()
CreateRenderer()

running = True

x = 0
h = 100

while running:

  DrawRect(x, 0, 1, h, 255, 0, 0)
  DrawRect(x, 101, 1, h, 0, 255, 0)
  DrawRect(x, 201, 1, h, 0, 0, 255)
  
  DrawLine(0, HEIGHT/2, WIDTH, HEIGHT/2, 255, 255, 0)
  ShowRenderer(renderer)

  x = x + 1

  if (x > WIDTH):
    x = 0
    ClearRenderer(renderer)

  events = sdl2.ext.get_events()
  for event in events:
    if event.type == SDL_QUIT:
      running = False
      break
 
CleanUp()
