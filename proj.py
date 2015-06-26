
import pygame
import RPi.GPIO as GPIO
import time


count = 300
isReleased = True
startbool = True



while True :

	TRIG=23
	ECHO=24

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.output(TRIG,GPIO.LOW)
	GPIO.setup(18,GPIO.IN)
	time.sleep(0.3)

	pygame.init()
	screen = pygame.display.set_mode((950,400))
	screen.fill(pygame.Color(255,255,255))
	lfont = pygame.font.SysFont("freeserif", 72, bold = 1)
	tfont = pygame.font.SysFont("dejavusans", count, bold = 1)

	inputValue = GPIO.input(18)

	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO) == 0:
        	pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
        	pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)
	
	GPIO.cleanup()



        if (20 > distance):
                textSurface = lfont.render("Too close to the device!", 1, pygame.Color(0,0,0))
                screen.blit(textSurface, (10,10))
                pygame.display.update()
                startbool = True
        
        if (distance > 60):
                textSurface = lfont.render("Too far from the device!", 1, pygame.Color(0,0,0))
                screen.blit(textSurface, (10,10))
                pygame.display.update()
                startbool = True        
    
        if (20 < distance < 60):
                if( (inputValue == True and isReleased == True) or startbool == True):
                        startbool = False
         		count = count - 30
                        textSurface = tfont.render("5", 1, pygame.Color(255,130,0))
                        screen.blit(textSurface, (10,10))
                        pygame.display.update()

                if(inputValue == False and isReleased == False):
                        isReleased = True

        time.sleep(.01)
