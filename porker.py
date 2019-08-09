from random import sample
from card import Card

suits = ['♠', '♥', '♦', '♣' ]

class Porker:
  def __init__(self, number_of_players):
    if(number_of_players > 10):
      raise Exception("number_of_players should be less than 10.")

    # シャッフルされた52までの数字（カードを表す）を作る
    shuffled_cards = sample(range(52), 52)

    # shuffledCardsから5枚づつ取って，各プレイヤーの手札とする
    self.playerCards = list(map(
      lambda i: shuffled_cards[(i * 5):((i + 1) * 5)]
      , range(number_of_players)))

    # 残りを山札とする
    self.deck = shuffled_cards[5 * number_of_players:]

  def draw(self, player_index, card_index):
    if(len(self.deck) == 0):
      raise Exception("there is no remaining deck.")
    self.playerCards[player_index][card_index] = self.deck.pop()
  
  def cardsStr(self, player_index):
    if(len(self.playerCards) < player_index):
      raise Exception("player_index is out of range")
    return ','.join(map(
        lambda card: suits[int(card / 13)] + '-' + str(card % 5 + 1)
      ,self.playerCards[player_index]))
