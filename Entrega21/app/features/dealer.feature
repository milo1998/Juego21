Feature: Talla para el juego de 21

Scenario: Generar baraja
	Given baraja
	When ronda inicia
	Then baraja completa

Scenario: Repartir cartas 
	Given baraja lista
	When repartir cartas talla
	Then baraja talla completa
    
    Given baraja lista 2
	When repartir cartas jugador
	Then baraja jugador completa

Scenario: Ganador
    Given juego
	When juego terminado
	Then jugador gana
    
    Given juego 2
	When juego terminado 2
	Then talla gana

