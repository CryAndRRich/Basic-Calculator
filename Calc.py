import pygame, sys
import math
from pygame.locals import *

pygame.init()

window_width = 800
window_height = 400

DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Calculator')

BACKGROUND = pygame.image.load('background.jpg')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (140, 140, 140)
LIGHT_GRAY = (241, 243, 244)
DARK_GRAY = (218, 220, 224)
BLUE = (66, 133, 244)

font1 = pygame.font.SysFont('consolas', 30)
font2 = pygame.font.SysFont('consolas', 16)
font3 = pygame.font.SysFont('arial bold', 22)


isRadian = True
def Calculate(text):
    global isRadian
    nums = '0123456789.'
    ops = '+-x/%^()E'
    tri_log = 'colts' 
    
    text += 'E'
    stack = []
    temp = ''
    for i in range(len(text)):
        char = text[i]
        if char in nums:
            temp += char

        elif char in ops:
            if temp:
                prev = stack.pop() if stack else '+'
                num = float(temp)
                if prev == '+':
                    stack.append(num)
                elif prev == '-':
                    stack.append(-num)
                elif prev == 'x':
                    stack[-1] *= num
                elif prev == '/':
                    stack[-1] /= num
                elif prev == '%':
                    stack[-1] %= num
                elif prev == '^':
                    stack[-1] **= num
                elif prev == '(':
                    stack.append(prev)
                    stack.append(num)

            temp = ''
            if char != 'E':
                stack.append(char)

        elif char in tri_log:
            if char == 's' and stack and stack[-1] == 'c':
                continue
            if char == 'o' and stack[-1] == 'l':
                stack.pop()
            stack.append(char)
        
        elif char == '!':
            try:
                temp = str(math.factorial(int(temp)))
            except:
                return "ERROR"
        
        elif char == 'e':
            temp = '2.71828182846'

        if stack and stack[-1] == ')':
            stack.pop()
            num = 0
            while stack[-1] != '(':
                num += stack.pop()
            stack.pop()
            if stack[-1] in tri_log:
                prev = stack.pop()
                if prev == 's':
                    num = math.sin(num * math.pi / 180 if not isRadian else num)
                elif prev == 'c':
                    num = math.cos(num * math.pi / 180 if not isRadian else num)
                elif prev == 't':
                    num = math.tan(num * math.pi / 180 if not isRadian else num)
                elif prev == 'l':
                    num = math.log(num)
                else:
                    num = math.log10(num)
            
            temp = str(num)
        #print(stack)
    
    ans = sum(stack)
    return ans if ans != int(ans) else int(ans)

class calculatorScreen():
    def __init__(self):
        self.input_text = ''
        self.result_text = ''
        self.equal_buttons = False
        self.buttons = []
        self.operate = {0: 'Rad', 1: 'x!', 2: '(', 3: ')', 4: '%', 5: 'CE', 
                        6: 'e', 7: '1/x', 8: '7', 9: '8', 10: '9', 11: '/', 
                        12: 'sin', 13: 'ln', 14: '4', 15: '5', 16: '6', 17: 'x', 
                        18: 'cos', 19: 'log', 20: '1', 21: '2', 22: '3', 23: '-', 
                        24: 'tan', 25: '^', 26: '0', 27: '.', 28: '=', 29: '+'}
        self.button_color = [DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, BLUE, DARK_GRAY]
        for i in range(0, 5):
            for j in range(0, 6):
                self.buttons.append(pygame.Rect(105 + 100 * j, 140 + 45 * i, 87, 28))

    def handle_click(self, pos):
        global isRadian
        for i, button_rect in enumerate(self.buttons):
            if button_rect.collidepoint(pos):
                if self.operate[5] == 'AC':
                    if i not in [0, 1, 4, 11, 17, 23, 25, 28, 29]:
                        self.result_text = ''
                    if i != 0:
                        self.operate[5] = 'CE'

                if i == 5:
                    self.result_text = self.result_text[:-1] if self.operate[5] == 'CE' else ''
                elif i == 28:
                    self.equal_buttons = True
                    self.operate[5] = 'AC'
                elif i == 1:
                    self.result_text += '!'
                elif i == 7:
                    self.result_text += '1/'
                elif i == 0:
                    self.operate[0] = 'Deg' if isRadian else 'Rad'
                    isRadian = not isRadian
                else:
                    self.result_text += self.operate[i]
                    if i in [12, 13, 18, 19, 24]:
                        self.result_text += '('
        
                return  

    def draw_buttons(self):
        for i, button_rect in enumerate(self.buttons):
            pygame.draw.rect(DISPLAYSURF, self.button_color[i], button_rect)
            text = self.operate[i]
            text_surface = font3.render(text, True, WHITE if i == 28 else BLACK)
            text_rect = text_surface.get_rect(center = button_rect.center)
            DISPLAYSURF.blit(text_surface, text_rect)

    def draw_frame(self):
        frame = pygame.Rect(105, 60, 587, 65)
        pygame.draw.rect(DISPLAYSURF, WHITE, frame)

        text_surface_input = font2.render(self.input_text, True, GRAY)
        text_surface_result = font1.render(self.result_text, True, BLACK)
        
        text_rect_input = text_surface_input.get_rect(top = frame.top + 10, right = frame.right - 10)
        text_rect_result = text_surface_result.get_rect(bottom = frame.bottom - 5, right = frame.right - 10)

        DISPLAYSURF.blit(text_surface_input, text_rect_input)
        DISPLAYSURF.blit(text_surface_result, text_rect_result)

    def update_display(self):
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        self.draw_buttons()
        self.draw_frame()

def Calculator():
    screen = calculatorScreen()  

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                screen.input_text = ''
                screen.handle_click(event.pos)
                if len(screen.result_text) > 32:
                    screen.result_text = 'Stop! Too long!'
                    screen.operate[5] = 'AC'
                if screen.equal_buttons: 
                    try:
                        screen.input_text = screen.result_text + '='
                        screen.result_text = f'{Calculate(screen.result_text)}'
                        if len(screen.result_text) > 32:
                            screen.result_text = 'Sorry! Too long!'
                    except:
                        screen.result_text = 'ERROR'
                    
                    screen.equal_buttons = False

            screen.update_display()  
            pygame.display.update()

if __name__ == '__main__':
    Calculator()