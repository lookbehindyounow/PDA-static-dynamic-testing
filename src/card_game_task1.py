# I don't know if it was supposed to be part of task 1 but the specs folder should've been named tests & the class TestCardGame
# should've had unittest.TestCase passed as an argument for it to inherit the properties of TestCase.

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # single = sign where == should be for comparison
      return True
    else # missing :
      return False
   

  dif highest_card(self, card1 card2): # should say def not dif, also missing comma between card1 & card2
  if card1.value > card2.value: # this line & every following line in this method should be indented one more column
    return card # should say card1 instead of card
  else:
    return card2
  # this method doesn't account for comparing two cards of the same value, in which case they should be compared by their suit


def cards_total(self, cards): # this method is missing indentation & is outside of the class definition
  total # total has not been assigned to anything
  for card in cards:
    total += card.value
    return "You have a total of" + total # return shouldn't be inside for loop, there should be a space before the string ends (although
                                         # this is more of a bug than an error & a very mild one at that) & total needs to be converted
                                         # to a string otherwise the concatenation won't work