def string_spearate():
    
    
    raw = """
    Usage Summary In Cluster:*********************************************
    management:
            received (in 494995.540 secs):
                    9 packets       1224 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    4 packets       112 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cluster:
            received (in 494995.540 secs):
                    863526 packets  158870695 bytes
                    0 pkts/sec      8 bytes/sec
            transmitted (in 494995.540 secs):
                    2928729 packets 2060806633 bytes
                    4 pkts/sec      3005 bytes/sec
    1 minute input rate 0 pkts/sec,  115 bytes/sec
    1 minute output rate 2 pkts/sec,  492 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  118 bytes/sec
    5 minute output rate 2 pkts/sec,  499 bytes/sec
    5 minute drop rate, 0 pkts/sec
    inside:
            received (in 494995.540 secs):
                    1015636 packets 81641161 bytes
                    1 pkts/sec      8 bytes/sec
            transmitted (in 494995.540 secs):
                    793564 packets  1118799648 bytes
                    1 pkts/sec      2008 bytes/sec
    1 minute input rate 1 pkts/sec,  146 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 1 pkts/sec,  165 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    outside:
            received (in 494995.540 secs):
                    2259440 packets 3059194325 bytes
                    4 pkts/sec      6006 bytes/sec
            transmitted (in 494995.540 secs):
                    537598 packets  30507708 bytes
                    1 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  33 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  37 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    nlp_int_tap:
            received (in 494995.540 secs):
                    30842 packets   1604168 bytes
                    0 pkts/sec      2 bytes/sec
            transmitted (in 494995.540 secs):
                    30830 packets   1603192 bytes
                    0 pkts/sec      2 bytes/sec
    1 minute input rate 0 pkts/sec,  2 bytes/sec
    1 minute output rate 0 pkts/sec,  2 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  2 bytes/sec
    5 minute output rate 0 pkts/sec,  2 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ccl_ha_nlp_int_tap:
            received (in 494995.540 secs):
                    4 packets       264 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    119481 packets  72795178 bytes
                    0 pkts/sec      7 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ha_ctl_nlp_int_tap:
            received (in 494995.540 secs):
                    15 packets      1020 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cmi_mgmt_int_tap:
            received (in 494995.540 secs):
                    5700 packets    260576 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    unit-1-1(LOCAL):******************************************************
    management:
            received (in 494995.540 secs):
                    8 packets       1068 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    3 packets       84 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cluster:
            received (in 494995.540 secs):
                    475458 packets  51341651 bytes
                    0 pkts/sec      8 bytes/sec
            transmitted (in 494995.540 secs):
                    985435 packets  307092779 bytes
                    1 pkts/sec      4 bytes/sec
    1 minute input rate 0 pkts/sec,  70 bytes/sec
    1 minute output rate 1 pkts/sec,  232 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  71 bytes/sec
    5 minute output rate 1 pkts/sec,  237 bytes/sec
    5 minute drop rate, 0 pkts/sec
    inside:
            received (in 494995.540 secs):
                    619888 packets  36402314 bytes
                    1 pkts/sec      4 bytes/sec
            transmitted (in 494995.540 secs):
                    793233 packets  1118771900 bytes
                    1 pkts/sec      2008 bytes/sec
    1 minute input rate 0 pkts/sec,  10 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  20 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    outside:
            received (in 494995.540 secs):
                    1153834 packets 1532403679 bytes
                    2 pkts/sec      3000 bytes/sec
            transmitted (in 494995.540 secs):
                    536210 packets  30450364 bytes
                    1 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  33 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  31 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    nlp_int_tap:
            received (in 494995.540 secs):
                    15488 packets   805760 bytes
                    0 pkts/sec      1 bytes/sec
            transmitted (in 494995.540 secs):
                    15476 packets   804784 bytes
                    0 pkts/sec      1 bytes/sec
    1 minute input rate 0 pkts/sec,  1 bytes/sec
    1 minute output rate 0 pkts/sec,  1 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  1 bytes/sec
    5 minute output rate 0 pkts/sec,  1 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ccl_ha_nlp_int_tap:
            received (in 494995.540 secs):
                    4 packets       264 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    58848 packets   3335834 bytes
                    0 pkts/sec      6 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ha_ctl_nlp_int_tap:
            received (in 494995.540 secs):
                    15 packets      1020 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cmi_mgmt_int_tap:
            received (in 494995.540 secs):
                    2857 packets    130718 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 494995.540 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    unit-2-1:*************************************************************
    management:
            received (in 491302.640 secs):
                    1 packets       156 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 491302.640 secs):
                    1 packets       28 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cluster:
            received (in 491302.640 secs):
                    388068 packets  107529044 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 491302.640 secs):
                    1943294 packets 1753713854 bytes
                    3 pkts/sec      3001 bytes/sec
    1 minute input rate 0 pkts/sec,  45 bytes/sec
    1 minute output rate 1 pkts/sec,  260 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  47 bytes/sec
    5 minute output rate 1 pkts/sec,  262 bytes/sec
    5 minute drop rate, 0 pkts/sec
    inside:
            received (in 494942.450 secs):
                    395748 packets  45238847 bytes
                    0 pkts/sec      4 bytes/sec
            transmitted (in 494942.450 secs):
                    331 packets     27748 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 1 pkts/sec,  136 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 1 pkts/sec,  145 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    outside:
            received (in 494942.450 secs):
                    1105606 packets 1526790646 bytes
                    2 pkts/sec      3006 bytes/sec
            transmitted (in 494942.450 secs):
                    1388 packets    57344 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  6 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    nlp_int_tap:
            received (in 491302.640 secs):
                    15354 packets   798408 bytes
                    0 pkts/sec      1 bytes/sec
            transmitted (in 491302.640 secs):
                    15354 packets   798408 bytes
                    0 pkts/sec      1 bytes/sec
    1 minute input rate 0 pkts/sec,  1 bytes/sec
    1 minute output rate 0 pkts/sec,  1 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  1 bytes/sec
    5 minute output rate 0 pkts/sec,  1 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ccl_ha_nlp_int_tap:
            received (in 491302.640 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 491302.640 secs):
                    60633 packets   69459344 bytes
                    0 pkts/sec      1 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    ha_ctl_nlp_int_tap:
            received (in 491302.640 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 491302.640 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    cmi_mgmt_int_tap:
            received (in 491302.640 secs):
                    2843 packets    129858 bytes
                    0 pkts/sec      0 bytes/sec
            transmitted (in 491302.640 secs):
                    0 packets       0 bytes
                    0 pkts/sec      0 bytes/sec
    1 minute input rate 0 pkts/sec,  0 bytes/sec
    1 minute output rate 0 pkts/sec,  0 bytes/sec
    1 minute drop rate, 0 pkts/sec
    5 minute input rate 0 pkts/sec,  0 bytes/sec
    5 minute output rate 0 pkts/sec,  0 bytes/sec
    5 minute drop rate, 0 pkts/sec
    """
    
    section_list = []
    current_section = ""
    for line in raw.splitlines():
        if line.strip() == "":  
            section_list.append(current_section.strip())
            current_section = ""
        else:
            current_section += line + "\n"
    if current_section.strip() != "":
        section_list.append(current_section.strip())
        
    print(len(section_list))

    
a = string_spearate()
    
    

