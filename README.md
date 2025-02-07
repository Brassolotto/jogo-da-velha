# Jogo da Velha em Python

Um jogo da velha clássico implementado em Python, jogável no terminal. O jogo permite que dois jogadores se alternem em turnos, usando 'X' e 'O' como marcadores.

## Funcionalidades

- Tabuleiro interativo 3x3
- Sistema de turnos alternados
- Validação de jogadas
- Verificação de vitória e empate
- Tratamento de erros para entradas inválidas
- Interface limpa e intuitiva no terminal

## Como Jogar

1. Execute o script Python
2. Digite a linha (0-2) e coluna (0-2) para fazer sua jogada
3. Alterne entre os jogadores até que alguém vença ou ocorra um empate

```
 Exemplo do tabuleiro:
   |   |   
-----------
   |   |   
-----------
   |   |   
```

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Brassolotto/jogo-da-velha.git
cd jogo-da-velha
```

2. Execute o jogo:
```bash
python jogo_da_velha.py
```

## Estrutura do Código

O projeto está organizado nas seguintes funções principais:

- `exibir_tabuleiro()`: Mostra o estado atual do jogo
- `fazer_jogada()`: Processa e valida as jogadas dos usuários
- `verificar_vitoria()`: Checa se há um vencedor
- `verificar_empate()`: Verifica se houve empate
- `jogar()`: Controla o fluxo principal do jogo

## Como Jogar

1. O jogo começa com o jogador 'X'
2. Digite o número da linha (0, 1 ou 2)
3. Digite o número da coluna (0, 1 ou 2)
4. O jogo alterna automaticamente entre os jogadores
5. O jogo termina quando alguém vence ou há um empate

## Regras

- Jogadores alternam turnos
- 'X' sempre começa
- Para vencer, complete uma linha, coluna ou diagonal
- Se todas as células forem preenchidas sem vencedor, é declarado empate

## Exemplos de Entrada

```
Digite a linha (0-2): 1
Digite a coluna (0-2): 1
```

## Tratamento de Erros

O jogo inclui validações para:
- Entradas não numéricas
- Números fora do intervalo 0-2
- Tentativas de jogadas em posições ocupadas

## Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

Ricardo Brassolotto - [https://github.com/Brassolotto]

## Agradecimentos

- Inspirado no jogo da velha tradicional
- Desenvolvido como projeto de estudo em Python