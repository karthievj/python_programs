
# cases = {"case1":["--version=v1", ""],
#          "case2":["--version=v1", "--preferred-versions=v1,v2"],
#          "case3":["--available-versions=v1,v2", "--preferred-versions=v1,v2"],
#          "case4":["--version=v1", "--available-versions=v2,v1"],
#          "case6":["--available-versions=v1,v2","--available-versions=v2,v1"],
#          "case7":["--available-versions=v2,v1", "--available-versions=v1,v2"],
#          "case8":["--preferred-versions=v1,v2", "--preferred-versions=v2,v1"],
#          "case8":["--preferred-versions=v2,v1", "--preferred-versions=v1,v2"],
# }

# for case in cases:
#     print(case)
#     print(cases[case][0],"client")
#     print(cases[case][1],"server")
    
    
import os 

dire = "C:/Users/kakrish6/Downloads/P0 automation cases.xlsx"
if os.path.isfile(dire):
    print("yes")
else:
    print("no")


    

    