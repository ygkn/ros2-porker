from random import sample
from card import Card

class Porker:
  def __init__(self, number_of_players):
    if(number_of_players > 10):
      raise Exception("number_of_players should be less than 10.")

    # シャッフルされた52までのカードを作る
    shuffled_cards = list(map(
      lambda number: Card(int(number/13) , number % 13 + 1)
      , sample(range(52), 52)))

    # shuffled_cardsから5枚づつ取って，各プレイヤーの手札とする
    self.player_cards = list(map(
      lambda i: shuffled_cards[(i * 5):((i + 1) * 5)]
      , range(number_of_players)))

    # 残りを山札とする
    self.deck = shuffled_cards[5 * number_of_players:]

  def draw(self, player_index, card_index):
    if(len(self.deck) == 0):
      raise Exception("there is no remaining deck.")
    self.player_cards[player_index][card_index] = self.deck.pop()
  
  def cardsStr(self, player_index):
    if(len(self.player_cards) < player_index):
      raise Exception("player_index is out of range")
    return ','.join(map(
        lambda card: str(card)
      , self.player_cards[player_index]))
