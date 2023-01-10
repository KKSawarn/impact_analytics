class Solution:
    def __init__(self,given_day):
        self.given_day = given_day
        self.way_to_attend = self.probabilty_to_attend_class()
    
    def number_of_ways_to_attend_classe(self):
        return len(self.way_to_attend)
    

    def probability_to_miss_the_ceremony(self):
        ineligible_ways = self.ineligible_ways_to_attend_classes()
        return str(len(ineligible_ways)) +" / " +str(self.number_of_ways_to_attend_classe())


    def probabilty_to_attend_class(self):
        lst=[]
        result_pattern = ''
        self.utils(self.given_day, result_pattern, lst)
        return lst


    def utils(self,given_day, result_pattern, lst):
        if given_day == 0:
            lst.append(result_pattern)
        else:
            self.utils(given_day - 1, result_pattern + 'A', lst) #absent
            self.utils(given_day - 1, result_pattern + 'P',lst) #present


    def ineligible_ways_to_attend_classes(self):
        # Filter out ways where 4 or more consective days classes are missed
        return list(filter(lambda way: "AAAA" in way, self.way_to_attend))
