# There is a small town with n houses that are arranged in a line. You are given a O-indexed integer array. For 0 <= i < n, households[i] denoting how many people live in housei.
# One day, a mysterious evil power enters the town and some of the houses started to disappear each day. After a few days of observation, this evil power rule is discovered. A house would disappear only if it had different size of households from its neighbours.
# Each day, this evil power rule would apply to all houses simultaneously at once. This evil power would leave the town only if there is no houses disappearing. Return an integer to indicate after how many days, the evil power would leave the town.

def evilPowerDays(households):
    n_days = 0
    survivors = households

    # 222 then the middle 2 will stay for 1 day 
    while len(survivors): 
        # print('survivors', len(survivors))
        remaining = survivors
        survivors = []
        i=0
        while i < len(remaining) and len(set(remaining)) > 1: # loop houses for today if houses are different 
            # survivors [2, 2, 2] has no different houses, devil left 
            print('survivors', survivors)

            count_repead = 1 # need to be 1 for starting point not 0
            # count adjancent same size houses 
            # print(i)
            while i + 1 < len(remaining) and remaining[i] == remaining[i+1]: # loop all houses after i 
                # have to put the remaining[i] == remaining[i+1] check in the while, otherwise infinity loop
                count_repead += 1 
                i+=1
            # print(remaining[i], count_repead)
            if count_repead > 2: 
                current_house_stay = [remaining[i-1]] * (count_repead-2)
                survivors+=current_house_stay
            i+=1
        
        n_days += 1
        
    return n_days



# Example usage
# households = [1, 2, 3, 2, 1, 3, 4, 5, 4, 3, 2, 1]
# days = evilPowerDays(households)
# print("Number of days until the evil power leaves:", days)

# Example usage
households = [1, 2, 2, 2, 2, 2, 2, 2, 1, 3, 3, 3, 5, 4, 3, 2, 1]
days = evilPowerDays(households)
print("Number of days until the evil power leaves:", days)
# survivors []
# survivors []
# survivors [2, 2, 2]
# survivors [2, 2, 2]
# survivors [2, 2, 2, 3]
# survivors [2, 2, 2, 3]
# survivors [2, 2, 2, 3]
# survivors [2, 2, 2, 3]
# survivors [2, 2, 2, 3]
# survivors []
# survivors [2]
# survivors []
# Number of days until the evil power leaves: 3