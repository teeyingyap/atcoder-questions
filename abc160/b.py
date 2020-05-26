def happinessCalculator(money):
	points = 0
	if money == 0:
		return points
	while money >= 500:
		money -= 500
		points += 1000
	while money >= 5:
		money -= 5
		points += 5
	return points

print(happinessCalculator(int(input())))
