## constructor function  
* use Uppercase to differentiate with functions  
* ex) pygame.Rect() and pygame.Surface() are constructor functions that are in the pygame module  
```python  
import whammy # import module  
fizzy() # function  
egg = Wombat() # constructor function that returns an object. the object is saved as a variable  
egg.bluhbluh() # method call  
whammy.spam() # function call  
```  

## Surface object  
* the Surface object returned by pygame.display.set_mode() is called "display Surface"  
* everything on display Surface object will be displayed on the screen by pygame.display.update()  
* speed: draw surface object on screen < display on Surface object (since it is just changing the memory value)  
* 30FPS (Frame Per Second)  

## colors  
* (Red, Green, Blue) values: 0~255 -> total 16,777,216 (256 X 256 X 256) colors  
* ex) (0,0,0) : black  
* (Red, Green, Blue, Alpha), Alpha: transparency, if the value is 255 it is solid  
* ex) transparent code  
> `anotherSurface = DISPLAYSURF.convertalpha()`  

## rectangle  
* (x,y,width,height)
```python  
import pygame
spamRect = pygame.Rect(10,20,200,300)
```  
```python
spamRect.right
```  

