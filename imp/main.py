from impact_solution import Solution
if __name__=='__main__':

    try:
        given_days = int(input("Enter no of day:")) 
    except Exception as e:
        print("Your input is wrong. Error: {}".format(e))
    else:
        imp_solution = Solution(given_days)
        print("No. of way to attend the class in given {} day is : {}".format(given_days,imp_solution.probabilty_to_attend_class()))
        print("Probabilty to miss the chance of university ceremony is : {}".format(imp_solution.probability_to_miss_the_ceremony()))
