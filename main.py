from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *

    
janela = Window(1000, 500)
janela.set_title("Pong!")

teclado = janela.get_keyboard()

player1= Sprite("player.png")
player1.set_position(40, (janela.height - player1.height)/2)

player2= Sprite("player.png")
player2.set_position(janela.width - player2.width - 40, (janela.height - player2.height)/2)

ball = Sprite ("ball.png")
ball.set_position((janela.width - ball.width)/2, (janela.height - ball.height)/2)
direcao_y = 1 #Baixo
direcao_x = 1 #Cima


#Game Loop  
while True:
    janela.set_background_color((0, 0, 0))
    #Movimento para baixo
    if(teclado.key_pressed("S") and player1.y + player1.height < janela.height):
        player1.move_y(200 * janela.delta_time())
    #Movimento para cima
    if(teclado.key_pressed("W") and player1.y > 0):
        player1.move_y(-200 * janela.delta_time())    
    
    
    #Movimento para baixo 2
    if(teclado.key_pressed("K") and player2.y + player2.height < janela.height):
        player2.move_y(200 * janela.delta_time())
    #Movimento para cima 2
    if(teclado.key_pressed("I") and player1.y > 0):
        player2.move_y(-200 * janela.delta_time())    
        
        
    #Movimento da Bola    
    ball.move_x (direcao_x * 300 * janela.delta_time())
    ball.move_y (direcao_y * 300 * janela.delta_time())
    
    if (ball.y + ball.height >= janela.height):
        direcao_y = -1
    if (ball.y <= 0):
        direcao_y = 1
        
    
    player1.draw()
    player2.draw()
    ball.draw()
    janela.update()
    