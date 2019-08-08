from random import sample

suits = ['♠', '♥', '♦', '♣' ]

class Porker:
  def __init__(self, numberOfPlayers):
    if(numberOfPlayers > 10):
      raise Exception("numberOfPlayers should be less than 10.")

    # シャッフルされた52までの数字（カードを表す）を作る
    shuffledCards = sample(range(52), 52)

    # shuffledCardsから5枚づつ取って，各プレイヤーの手札とする
    self.playerCards = list(map(
      lambda i: shuffledCards[(i * 5):((i + 1) * 5)]
      , range(numberOfPlayers)))

    # 残りを山札とする
    self.deck = shuffledCards[5 * numberOfPlayers:]

  def draw(self, playerIndex, cardIndex):
    if(len(self.deck) == 0):
      raise Exception("there is no remaining deck.")
    self.playerCards[playerIndex][cardIndex] = self.deck.pop()
  
  def cardsStr(self, playerIndex):
    if(len(self.playerCards) < playerIndex):
      raise Exception("playerIndex is out of range")
    return ','.join(map(
        lambda card: suits[int(card / 13)] + '-' + str(card % 5 + 1)
      ,self.playerCards[playerIndex]))
