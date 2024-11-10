list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_team = len(list_players) // 2 # индекс середины команды

first_team = list_players[:middle_team]
second_team = list_players[middle_team:]

print(first_team)
print(second_team)
