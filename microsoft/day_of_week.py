
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

"""

Ex. 'Sat', K = 23


"""
def day_of_week(start_day: str, k: int) -> int:
    day_index = days.index(start_day)
    num_days_add = k + day_index
    # print(num_days_add)
    # if num_days_add > 6:
    #     return days[num_days_add - 7]
    
    return days[num_days_add%7]

if __name__ == "__main__":
    
    new_day = day_of_week('Sat', 25)