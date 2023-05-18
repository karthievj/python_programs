def phone_number(digits):
    
    rule = {
        "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
    }
    num_list = []
    for i in digits:
        num_list.append(rule[i])
        
        
    def generate_combinations(num_list):
        if len(num_list)==0:
            return []
        elif len(num_list)==1:
            return [char for char in num_list[0]]
        else:
            combinations = []
            for char in num_list[0]:
                suffix_comb = generate_combinations(num_list[1:])
                for suffix in suffix_comb:
                    combinations.append(char+suffix)
            return combinations
    
    output = generate_combinations(num_list)
    
    return output

a = phone_number(digits = "345")
print(a)