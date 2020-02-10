from behave import *
from app import *

@given('baraja')
def step_impl(context):
    context.game = Game([],[],[])
    
@when('ronda inicia')
def step_impl(context):
    context.game.baraja=llenado()

@then('baraja completa')
def step_impl(context):
    assert (len(context.game.baraja) == 52)



@given('baraja lista')
def step_impl(context):
    context.game = Game([],[],[])
    context.game.baraja=llenado()
    
@when('repartir cartas talla')
def step_impl(context):
    context.game.repartirCartas([],[],context.game.baraja)
    

@then('baraja talla completa')
def step_impl(context):
    assert (len(context.game.talla) == 2)



@given('baraja lista 2')
def step_impl(context):
    context.game = Game([],[],[])
    context.game.baraja=llenado()
    
@when('repartir cartas jugador')
def step_impl(context):
    context.game.repartirCartas([],[],context.game.baraja)
    

@then('baraja jugador completa')
def step_impl(context):
    assert (len(context.game.jugador) == 2)



@given('juego')
def step_impl(context):
    context.game = Game([],[],[])
    context.game.baraja=llenado()
    context.game.repartirCartas([],[],context.game.baraja)
    
    
@when('juego terminado')
def step_impl(context):
    context.game.game(context.game.jugador,context.game.talla,context.game.baraja)
    

@then('jugador gana')
def step_impl(context):
    if (suma(context.game.jugador)<=21):
        if(suma(context.game.talla)>21 or suma(context.game.talla)<suma(context.game.jugador)):
            assert ((context.game.ganador == "jugador") or (context.game.ganador == "talla"))


@given('juego 2')
def step_impl(context):
    context.game = Game([],[],[])
    context.game.baraja=llenado()
    context.game.repartirCartas([],[],context.game.baraja)
    
    
@when('juego terminado 2')
def step_impl(context):
    context.game.game(context.game.jugador,context.game.talla,context.game.baraja)
    

@then('talla gana')
def step_impl(context):
        if(suma(context.game.talla)<=21 and suma(context.game.talla)>=suma(context.game.jugador)):
            assert (context.game.ganador == "talla")


