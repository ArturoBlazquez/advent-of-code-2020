from utils import read_file, print_part_1, print_part_2

# -- PARSE INPUT -- #
cards_unparsed = read_file('input.txt')
player_1_cards = [int(card) for card in cards_unparsed[1:cards_unparsed.index('')]]
player_2_cards = [int(card) for card in cards_unparsed[cards_unparsed.index('') + 2:]]

# -- PART 1 -- #
while len(player_1_cards) > 0 and len(player_2_cards) > 0:
    player_1_play = player_1_cards.pop(0)
    player_2_play = player_2_cards.pop(0)

    if player_1_play > player_2_play:
        player_1_cards.append(player_1_play)
        player_1_cards.append(player_2_play)
    else:
        player_2_cards.append(player_2_play)
        player_2_cards.append(player_1_play)

if len(player_1_cards) == 0:
    winner_cards = player_2_cards[::-1]
else:
    winner_cards = player_1_cards[::-1]

score = 0
for i in range(len(winner_cards)):
    score += (i + 1) * winner_cards[i]

print_part_1(score)


# -- PART 2 -- #
def play_recursive_combat(player_1_deck, player_2_deck):
    player_1_used_decks = []
    player_2_used_decks = []
    while len(player_1_deck) > 0 and len(player_2_deck) > 0:
        if player_1_deck in player_1_used_decks or player_2_deck in player_2_used_decks:
            return 1, player_1_deck

        player_1_used_decks.append(player_1_deck[:])
        player_2_used_decks.append(player_2_deck[:])

        player_1_play = player_1_deck.pop(0)
        player_2_play = player_2_deck.pop(0)

        if len(player_1_deck) >= player_1_play and len(player_2_deck) >= player_2_play:
            winner, _ = play_recursive_combat(player_1_deck[:player_1_play], player_2_deck[:player_2_play])

            if winner == 1:
                player_1_deck.append(player_1_play)
                player_1_deck.append(player_2_play)
            elif winner == 2:
                player_2_deck.append(player_2_play)
                player_2_deck.append(player_1_play)
        else:
            if player_1_play > player_2_play:
                player_1_deck.append(player_1_play)
                player_1_deck.append(player_2_play)
            else:
                player_2_deck.append(player_2_play)
                player_2_deck.append(player_1_play)

    if len(player_1_deck) == 0:
        return 2, player_2_deck
    else:
        return 1, player_1_deck


player_1_cards = [int(card) for card in cards_unparsed[1:cards_unparsed.index('')]]
player_2_cards = [int(card) for card in cards_unparsed[cards_unparsed.index('') + 2:]]

(winner, winner_cards) = play_recursive_combat(player_1_cards, player_2_cards)
winner_cards = winner_cards[::-1]

score = 0
for i in range(len(winner_cards)):
    score += (i + 1) * winner_cards[i]

print_part_2(score)
