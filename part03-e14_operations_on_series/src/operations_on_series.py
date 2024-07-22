import pandas as pd

def create_series(list1, list2):
    s1 = pd.Series(list1, index=['a', 'b', 'c'])
    s2 = pd.Series(list2, index=['a', 'b', 'c'])
    return s1, s2

def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return s1, s2

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    # Create two Series
    s1, s2 = create_series(list1, list2)
    print("Initial Series:")
    print("Series 1:", s1)
    print("Series 2:", s2)
    print()
    
    # Modify the Series
    modified_s1, modified_s2 = modify_series(s1, s2)
    print("Modified Series:")
    print("Modified Series 1:", modified_s1)
    print("Modified Series 2:", modified_s2)
    
    # Add the modified Series
    added_series = modified_s1 + modified_s2
    print("\nAdded Series:")
    print(added_series)

if __name__ == "__main__":
    main()
