X--------------------------------------------------------------------------------------------------------X

Lines of Action é um jogo de tabuleiro. Cada jogador tem 12 peças, que podem ser de cor branca ou preta. No código (ou representações textuais), as peças são geralmente denotadas como 'W' (White) e 'B' (Black).

• Objetivo do jogo:
Juntar todas as peças de um jogador de forma que fiquem conectadas entre si, ou seja, todas ligadas direta ou indiretamente, na horizontal, vertical ou diagonal.

por exemplo:

	B B • • • • • •
	• • • B B • • •
	• • • • • B • •
	• • • • • • • •
	• • W W • • • •
	• • • • W • • •
	• • • • • W • •
	• • • • • • W W

O branco ganha nesta posição, pois tem toas as suas peças ligadas entre si

Considere esta posição:
- WHITE TO MOVE

	B B • • • • • •			  B B • • • • • •					
	W • B B B • • •		W 	  • • B B B • • •
	• • • • • B • •  (1,0) -> (4,0)   • • • • • B • •	
	• • • • W • • • ----------------> • • • • W • • •
	B W W W • • • •			  W W W W • • • •	
	• • • • W • • •			  • • • • W • • •
	• • • • • W • •			  • • • • • W • •
	• • • • • • W W			  • • • • • • W W


Nesta posição é empate, pois abmos o preto e o branco tem todas as suas peças ligadas entre si. Ninguem ganha



• Regras do movimento:
- Um jogador move uma peça por turno.
- As peças movem-se em linha reta (horizontal, vertical ou diagonal).
- A distância do movimento é determinada pelo número total de peças (de ambas as cores) que existem nessa linha — incluindo a própria peça que vai ser movida.
- Pode-se saltar por cima das próprias peças, mas não se pode saltar sobre peças do adversário.
- Pode-se capturar uma peça do adversário se a jogada terminar exatamente na casa onde essa peça está.
- Não se pode mover menos ou mais casas do que o número de peças na linha.


X--------------------------------------------------------------------------------------------------------X

No folder LOA deve encontrar três ficheiros:
- Board.py
- MiniMax_Node.py
- LOA.py


Ficheiro Board.py contem a classe board, neste classe contem toda a lógica relacionado ao tabuleiro, principalmente funções pra mexer as peças, condição da vitória e função de avaliação do tabuleiro, se quizer melhorar a avaliação do tabuleiro seria nesta classe para implementar novos metodos.


Ficheiro Minimax_Node.py contem a classe MiniMaxNode, esta classe contem o algoritmo do minimax com alpha-beta pruning, a função evaluate() é a função que utilize os metodos de avaliação da classe Board para calcular uma avaliação. A função minimax_run() contem um parametro para alterar o depth da pesquisa, ou seja, altera a dificuldade do IA. Esta função retorna o melhor movimento em tuplo. (start, end)


Ficheiro LOA.py é o main loop do programa, o programa executa-se no terminal, ao executar o LOA.py apresentará opções para escolher diferentes modos de jogo, e se forem IA, é apresentado a opção de escolher a dificuldade também.


Para jogar o jogo, é só seguir as instruções que o jogo te pede para fazer os movimentos, caso o movimento for invalido, o programa vai repedir o seu input.



Feito por: Hugo Duarte de Sousa
