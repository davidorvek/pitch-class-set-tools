# dictionary of all prime forms calculated according to Rahn's algorithm
pcs = {
    '1-1': [[0],'<000000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-1': [[0,1],'<100000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-2': [[0,2],'<010000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-3': [[0,3],'<001000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-4': [[0,4],'<000100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-5': [[0,5],'<000010>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '2-6': [[0,6],'<000001>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-1': [[0,1,2],'<210000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-2': [[0,1,3],'<111000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-3': [[0,1,4],'<101100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-4': [[0,1,5],'<100110>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-5': [[0,1,6],'<100011>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-6': [[0,2,4],'<020100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-7': [[0,2,5],'<011010>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-8': [[0,2,6],'<010101>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-9': [[0,2,7],'<010020>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-10': [[0,3,6],'<002001>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-11': [[0,3,7],'<001110>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '3-12': [[0,4,8],'<000300>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-1': [[0,1,2,3],'<321000>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-2': [[0,1,2,4],'<221100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-3': [[0,1,3,4],'<212100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-4': [[0,1,2,5],'<211110>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-5': [[0,1,2,6],'<210111>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-6': [[0,1,2,7],'<210021>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-7': [[0,1,4,5],'<201210>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-8': [[0,1,5,6],'<200121>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-9': [[0,1,6,7],'<200022>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-10': [[0,2,3,5],'<122010>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-11': [[0,1,3,5],'<121110>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-12': [[0,2,3,6],'<112101>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-13': [[0,1,3,6],'<112011>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-14': [[0,2,3,7],'<111120>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-z15': [[0,1,4,6],'<111111>',{'Z PARTNER': '4-z29'},{'FORTE': 'SAME'}],
    '4-16': [[0,1,5,7],'<110121>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-17': [[0,3,4,7],'<102210>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-18': [[0,1,4,7],'<102111>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-19': [[0,1,4,8],'<101310>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-20': [[0,1,5,8],'<101220>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-21': [[0,2,4,6],'<030201>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-22': [[0,2,4,7],'<021120>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-23': [[0,2,5,7],'<021030>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-24': [[0,2,4,8],'<020301>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-25': [[0,2,6,8],'<020202>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-26': [[0,3,5,8],'<012120>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-27': [[0,2,5,8],'<012111>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-28': [[0,3,6,9],'<004002>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '4-z29': [[0,1,3,7],'<111111>',{'Z PARTNER': '4-z15'},{'FORTE': 'SAME'}],
    '5-1': [[0,1,2,3,4],'<432100>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-2': [[0,1,2,3,5],'<332110>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-3': [[0,1,2,4,5],'<322210>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-4': [[0,1,2,3,6],'<322111>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-5': [[0,1,2,3,7],'<321121>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-6': [[0,1,2,5,6],'<311221>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-7': [[0,1,2,6,7],'<310132>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-8': [[0,2,3,4,6],'<232201>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-9': [[0,1,2,4,6],'<231211>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-10': [[0,1,3,4,6],'<223111>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-11': [[0,2,3,4,7],'<222220>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-z12': [[0,1,3,5,6],'<222121>',{'Z PARTNER': '5-z36'},{'FORTE': 'SAME'}],
    '5-13': [[0,1,2,4,8],'<221311>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-14': [[0,1,2,5,7],'<221131>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-15': [[0,1,2,6,8],'<220222>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-16': [[0,1,3,4,7],'<213211>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-z17': [[0,1,3,4,8],'<212320>',{'Z PARTNER': '5-z37'},{'FORTE': 'SAME'}],
    '5-z18': [[0,1,4,5,7],'<212221>',{'Z PARTNER': '5-z38'},{'FORTE': 'SAME'}],
    '5-19': [[0,1,3,6,7],'<212122>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-20': [[0,1,5,6,8],'<211231>',{'Z PARTNER': 'NONE'},{'FORTE': [0,1,3,7,8]}],
    '5-21': [[0,1,4,5,8],'<202420>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-22': [[0,1,4,7,8],'<202321>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-23': [[0,2,3,5,7],'<132130>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-24': [[0,1,3,5,7],'<131221>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-25': [[0,2,3,5,8],'<123121>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-26': [[0,2,4,5,8],'<122311>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-27': [[0,1,3,5,8],'<122230>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-28': [[0,2,3,6,8],'<122212>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-29': [[0,1,3,6,8],'<122131>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-30': [[0,1,4,6,8],'<121321>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-31': [[0,1,3,6,9],'<114112>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-32': [[0,1,4,6,9],'<113221>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-33': [[0,2,4,6,8],'<040402>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-34': [[0,2,4,6,9],'<032221>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-35': [[0,2,4,7,9],'<032140>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '5-z36': [[0,1,2,4,7],'<222121>',{'Z PARTNER': '5-z12'},{'FORTE': 'SAME'}],
    '5-z37': [[0,3,4,5,8],'<212320>',{'Z PARTNER': '5-z17'},{'FORTE': 'SAME'}],
    '5-z38': [[0,1,2,5,8],'<212221>',{'Z PARTNER': '5-z18'},{'FORTE': 'SAME'}],
    '6-1': [[0,1,2,3,4,5],'<543210>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-2': [[0,1,2,3,4,6],'<443211>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z3': [[0,1,2,3,5,6],'<433221>',{'Z PARTNER': '6-z36'},{'FORTE': 'SAME'}],
    '6-z4': [[0,1,2,4,5,6],'<432321>',{'Z PARTNER': '6-z37'},{'FORTE': 'SAME'}],
    '6-5': [[0,1,2,3,6,7],'<422232>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z6': [[0,1,2,5,6,7],'<421242>',{'Z PARTNER': '6-z38'},{'FORTE': 'SAME'}],
    '6-7': [[0,1,2,6,7,8],'<420243>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-8': [[0,2,3,4,5,7],'<343230>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-9': [[0,1,2,3,5,7],'<342231>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z10': [[0,1,3,4,5,7],'<333321>',{'Z PARTNER': '6-z39'},{'FORTE': 'SAME'}],
    '6-z11': [[0,1,2,4,5,7],'<333231>',{'Z PARTNER': '6-z40'},{'FORTE': 'SAME'}],
    '6-z12': [[0,1,2,4,6,7],'<332232>',{'Z PARTNER': '6-z41'},{'FORTE': 'SAME'}],
    '6-z13': [[0,1,3,4,6,7],'<324222>',{'Z PARTNER': '6-z42'},{'FORTE': 'SAME'}],
    '6-14': [[0,1,3,4,5,8],'<323430>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-15': [[0,1,2,4,5,8],'<323421>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-16': [[0,1,4,5,6,8],'<322431>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z17': [[0,1,2,4,7,8],'<322332>',{'Z PARTNER': '6-z43'},{'FORTE': 'SAME'}],
    '6-18': [[0,1,2,5,7,8],'<322242>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z19': [[0,1,3,4,7,8],'<313431>',{'Z PARTNER': '6-z44'},{'FORTE': 'SAME'}],
    '6-20': [[0,1,4,5,8,9],'<303630>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-21': [[0,2,3,4,6,8],'<242412>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-22': [[0,1,2,4,6,8],'<241422>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z23': [[0,2,3,5,6,8],'<234222>',{'Z PARTNER': '6-z45'},{'FORTE': 'SAME'}],
    '6-z24': [[0,1,3,4,6,8],'<233331>',{'Z PARTNER': '6-z46'},{'FORTE': 'SAME'}],
    '6-z25': [[0,1,3,5,6,8],'<233241>',{'Z PARTNER': '6-z47'},{'FORTE': 'SAME'}],
    '6-z26': [[0,1,3,5,7,8],'<232341>',{'Z PARTNER': '6-z48'},{'FORTE': 'SAME'}],
    '6-27': [[0,1,3,4,6,9],'<225222>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z28': [[0,1,3,5,6,9],'<224322>',{'Z PARTNER': '6-z49'},{'FORTE': 'SAME'}],
    '6-z29': [[0,2,3,6,7,9],'<224232>',{'Z PARTNER': '6-z50'},{'FORTE': [0,1,3,6,8,9]}],
    '6-30': [[0,1,3,6,7,9],'<224223>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-31': [[0,1,4,5,7,9],'<223431>',{'Z PARTNER': 'NONE'},{'FORTE': [0,1,3,5,8,9]}],
    '6-32': [[0,2,4,5,7,9],'<143250>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-33': [[0,2,3,5,7,9],'<143241>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-34': [[0,1,3,5,7,9],'<142422>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-35': [[0,2,4,6,8,10],'<060603>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '6-z36': [[0,1,2,3,4,7],'<433221>',{'Z PARTNER': '6-z3'},{'FORTE': 'SAME'}],
    '6-z37': [[0,1,2,3,4,8],'<432321>',{'Z PARTNER': '6-z4'},{'FORTE': 'SAME'}],
    '6-z38': [[0,1,2,3,7,8],'<421242>',{'Z PARTNER': '6-z6'},{'FORTE': 'SAME'}],
    '6-z39': [[0,2,3,4,5,8],'<333321>',{'Z PARTNER': '6-z10'},{'FORTE': 'SAME'}],
    '6-z40': [[0,1,2,3,5,8],'<333231>',{'Z PARTNER': '6-z11'},{'FORTE': 'SAME'}],
    '6-z41': [[0,1,2,3,6,8],'<332232>',{'Z PARTNER': '6-z12'},{'FORTE': 'SAME'}],
    '6-z42': [[0,1,2,3,6,9],'<324222>',{'Z PARTNER': '6-z13'},{'FORTE': 'SAME'}],
    '6-z43': [[0,1,2,5,6,8],'<322332>',{'Z PARTNER': '6-z17'},{'FORTE': 'SAME'}],
    '6-z44': [[0,1,2,5,6,9],'<313431>',{'Z PARTNER': '6-z19'},{'FORTE': 'SAME'}],
    '6-z45': [[0,2,3,4,6,9],'<234222>',{'Z PARTNER': '6-z23'},{'FORTE': 'SAME'}],
    '6-z46': [[0,1,2,4,6,9],'<233331>',{'Z PARTNER': '6-z24'},{'FORTE': 'SAME'}],
    '6-z47': [[0,1,2,4,7,9],'<233241>',{'Z PARTNER': '6-z25'},{'FORTE': 'SAME'}],
    '6-z48': [[0,1,2,5,7,9],'<232341>',{'Z PARTNER': '6-z26'},{'FORTE': 'SAME'}],
    '6-z49': [[0,1,3,4,7,9],'<224322>',{'Z PARTNER': '6-z28'},{'FORTE': 'SAME'}],
    '6-z50': [[0,1,4,6,7,9],'<224232>',{'Z PARTNER': '6-z29'},{'FORTE': 'SAME'}],
    '7-1': [[0,1,2,3,4,5,6],'<654321>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-2': [[0,1,2,3,4,5,7],'<554331>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-3': [[0,1,2,3,4,5,8],'<544431>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-4': [[0,1,2,3,4,6,7],'<544332>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-5': [[0,1,2,3,5,6,7],'<543342>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-6': [[0,1,2,3,4,7,8],'<533442>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-7': [[0,1,2,3,6,7,8],'<532353>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-8': [[0,2,3,4,5,6,8],'<454422>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-9': [[0,1,2,3,4,6,8],'<453432>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-10': [[0,1,2,3,4,6,9],'<445332>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-11': [[0,1,3,4,5,6,8],'<444441>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-z12': [[0,1,2,3,4,7,9],'<444342>',{'Z PARTNER': '7-z36'},{'FORTE': 'SAME'}],
    '7-13': [[0,1,2,4,5,6,8],'<443532>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-14': [[0,1,2,3,5,7,8],'<443352>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-15': [[0,1,2,4,6,7,8],'<442443>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-16': [[0,1,2,3,5,6,9],'<435432>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-z17': [[0,1,2,4,5,6,9],'<434541>',{'Z PARTNER': '7-z37'},{'FORTE': 'SAME'}],
    '7-z18': [[0,1,4,5,6,7,9],'<434442>',{'Z PARTNER': '7-z38'},{'FORTE': [0,1,2,3,5,8,9]}],
    '7-19': [[0,1,2,3,6,7,9],'<434343>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-20': [[0,1,2,5,6,7,9],'<433452>',{'Z PARTNER': 'NONE'},{'FORTE': [0,1,2,4,7,8,9]}],
    '7-21': [[0,1,2,4,5,8,9],'<424641>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-22': [[0,1,2,5,6,8,9],'<424542>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-23': [[0,2,3,4,5,7,9],'<354351>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-24': [[0,1,2,3,5,7,9],'<353442>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-25': [[0,2,3,4,6,7,9],'<345342>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-26': [[0,1,3,4,5,7,9],'<344532>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-27': [[0,1,2,4,5,7,9],'<344451>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-28': [[0,1,3,5,6,7,9],'<344433>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-29': [[0,1,2,4,6,7,9],'<344352>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-30': [[0,1,2,4,6,8,9],'<343542>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-31': [[0,1,3,4,6,7,9],'<336333>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-32': [[0,1,3,4,6,8,9],'<335442>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-33': [[0,1,2,4,6,8,10],'<262623>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-34': [[0,1,3,4,6,8,10],'<254442>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-35': [[0,1,3,5,6,8,10],'<254361>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '7-z36': [[0,1,2,3,5,6,8],'<444342>',{'Z PARTNER': '7-z12'},{'FORTE': 'SAME'}],
    '7-z37': [[0,1,3,4,5,7,8],'<434541>',{'Z PARTNER': '7-z17'},{'FORTE': 'SAME'}],
    '7-z38': [[0,1,2,4,5,7,8],'<434442>',{'Z PARTNER': '7-z18'},{'FORTE': 'SAME'}],
    '8-1': [[0,1,2,3,4,5,6,7],'<765442>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-2': [[0,1,2,3,4,5,6,8],'<665542>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-3': [[0,1,2,3,4,5,6,9],'<656542>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-4': [[0,1,2,3,4,5,7,8],'<655552>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-5': [[0,1,2,3,4,6,7,8],'<654553>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-6': [[0,1,2,3,5,6,7,8],'<654463>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-7': [[0,1,2,3,4,5,8,9],'<645652>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-8': [[0,1,2,3,4,7,8,9],'<644563>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-9': [[0,1,2,3,6,7,8,9],'<644464>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-10': [[0,2,3,4,5,6,7,9],'<566452>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-11': [[0,1,2,3,4,5,7,9],'<565552>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-12': [[0,1,3,4,5,6,7,9],'<556543>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-13': [[0,1,2,3,4,6,7,9],'<556453>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-14': [[0,1,2,4,5,6,7,9],'<555562>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-z15': [[0,1,2,3,4,6,8,9],'<555553>',{'Z PARTNER': '8-z29'},{'FORTE': 'SAME'}],
    '8-16': [[0,1,2,3,5,7,8,9],'<554563>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-17': [[0,1,3,4,5,6,8,9],'<546652>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-18': [[0,1,2,3,5,6,8,9],'<546553>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-19': [[0,1,2,4,5,6,8,9],'<545752>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-20': [[0,1,2,4,5,7,8,9],'<545662>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-21': [[0,1,2,3,4,6,8,10],'<474643>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-22': [[0,1,2,3,5,6,8,10],'<465562>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-23': [[0,1,2,3,5,7,8,10],'<465472>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-24': [[0,1,2,4,5,6,8,10],'<464743>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-25': [[0,1,2,4,6,7,8,10],'<464644>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-26': [[0,1,3,4,5,7,8,10],'<456562>',{'Z PARTNER': 'NONE'},{'FORTE': [0,1,2,4,5,7,9,10]}],
    '8-27': [[0,1,2,4,5,7,8,10],'<456553>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-28': [[0,1,3,4,6,7,9,10],'<448444>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '8-z29': [[0,1,2,3,5,6,7,9],'<555553>',{'Z PARTNER': '8-z15'},{'FORTE': 'SAME'}],
    '9-1': [[0,1,2,3,4,5,6,7,8],'<876663>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-2': [[0,1,2,3,4,5,6,7,9],'<777663>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-3': [[0,1,2,3,4,5,6,8,9],'<767763>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-4': [[0,1,2,3,4,5,7,8,9],'<766773>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-5': [[0,1,2,3,4,6,7,8,9],'<766674>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-6': [[0,1,2,3,4,5,6,8,10],'<686763>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-7': [[0,1,2,3,4,5,7,8,10],'<677673>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-8': [[0,1,2,3,4,6,7,8,10],'<676764>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-9': [[0,1,2,3,5,6,7,8,10],'<676683>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-10': [[0,1,2,3,4,6,7,9,10],'<668664>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-11': [[0,1,2,3,5,6,7,9,10],'<667773>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '9-12': [[0,1,2,4,5,6,8,9,10],'<666963>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-1': [[0,1,2,3,4,5,6,7,8,9],'<988884>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-2': [[0,1,2,3,4,5,6,7,8,10],'<898884>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-3': [[0,1,2,3,4,5,6,7,9,10],'<889884>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-4': [[0,1,2,3,4,5,6,8,9,10],'<888984>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-5': [[0,1,2,3,4,5,7,8,9,10],'<888894>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '10-6': [[0,1,2,3,4,6,7,8,9,10],'<888885>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '11-1': [[0,1,2,3,4,5,6,7,8,9,10],'<AAAAA5>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}],
    '12-1': [[0,1,2,3,4,5,6,7,8,9,10,11],'<CCCCC6>',{'Z PARTNER': 'NONE'},{'FORTE': 'SAME'}]
}

# a dictionary of triad names as strings with a 
triads = {
    'c+': [0,4,7],
    'c-': [0,3,7],
    'c#+': [1,5,8],
    'c#-': [1,4,8],
    'db+': [1,5,8],
    'db-': [1,4,8],
    'd+': [2,6,9],
    'd-': [2,5,9],
    'd#+': [3,7,10],
    'd#-': [3,6,10],
    'eb+': [3,7,10],
    'eb-': [3,6,10],
    'e+': [4,8,11],
    'e-': [4,7,11],
    'f+': [5,9,0],
    'f-': [5,8,0],
    'f#+': [6,10,1],
    'f#-': [6,9,1],
    'gb+': [6,10,1],
    'gb-': [6,9,1],
    'g+': [7,11,2],
    'g-': [7,10,2],
    'g#+': [8,0,3],
    'g#-': [8,11,3],
    'ab+': [8,0,3],
    'ab-': [8,11,3],
    'a+': [9,1,4],
    'a-': [9,0,4],
    'a#+': [10,2,5],
    'a#-': [10,1,5],
    'bb+': [10,2,5],
    'bb-': [10,1,5],
    'b+': [11,3,6],
    'b-': [11,2,6]
}

IC1_value = -1.428
IC2_value = -0.582
IC3_value = +0.594
IC4_value = +0.386
IC5_value = +1.240
IC6_value = -0.453

def trans(pc_set, n):
    trans_result = []
    for pc in pc_set:
        new_pc = pc + n
        if new_pc >= 12:
            trans_result.append(new_pc % 12)
        else:
            trans_result.append(new_pc)
    return trans_result

def inv(pc_set, n):
    inv_result = []
    for pc in pc_set:
        new_pc = n - pc
        if new_pc < 0:
            inv_result.append(new_pc + 12)
        else:
            inv_result.append(new_pc)
    return inv_result

def mult(pc_set, n):
	result = []
	for i in pc_set:
		result.append((i * n) % 12)
	return result

def find_i(root, distance):
	index = (root + (root - (5 - distance))) % 12
	return index

def int_vect(pc_set):
    sort = sorted(pc_set)
    backwards = sort[::-1]
    iv_result = []
    IC1 = 0
    IC2 = 0
    IC3 = 0
    IC4 = 0
    IC5 = 0
    IC6 = 0

    while len(backwards) > 1:
        n = len(backwards)
        x = 1
        for _ in range(n - 1):
            iv_result.append(backwards[0] - backwards[x])
            x += 1
        backwards.pop(0)

    for i in iv_result:
        if i == 1 or i == 11:
            IC1 += 1
        elif i == 2 or i == 10:
            IC2 += 1
        elif i == 3 or i == 9:
            IC3 += 1
        elif i == 4 or i == 8:
            IC4 += 1
        elif i == 5 or i == 7:
            IC5 += 1
        elif i == 6:
            IC6 += 1
        else:
            pass
    return "<%s%s%s%s%s%s>" % (IC1, IC2, IC3, IC4, IC5, IC6)

def char_func(pc_set):
    result = []
    for i in range(12):
        if i in pc_set:
            result.append(1)
        else:
            result.append(0)
    return result

def deg_sym(pc_set):
    T = 0
    I = 0
    for i in range(12):
        if sorted(trans(pc_set, i)) == sorted(pc_set):
            T += 1
        else:
            T += 0
        if sorted(inv(pc_set, i)) == sorted(pc_set):
            I += 1
        else:
            I += 0
    return T, I

def DVLS(x, y):
        if len(x) > len(y):
                n = len(x) - len(y)
                for _ in range(n):
                        y.append(0)
        elif len(y) > len(x):
                n = len(y) - len(x)
                for _ in range(n):
                        x.append(0)
        else:
                pass
        total = 0
        for a, b in zip(x, y):
                total += ((b - a) % 12)
        return (total % 12)

def find_rel(pc_set1, pc_set2):
    T = []
    I = []
    M = []
    Z = []
        
    for i in range(12):
        if sorted(trans(pc_set1, i)) == sorted(pc_set2):
            T.append(i)
        else:
            pass
        if sorted(inv(pc_set1, i)) == sorted(pc_set2):
            I.append(i)
        else:
            pass
        if sorted(mult(pc_set1, i)) == sorted(pc_set2):
            M.append(i)
        else:
            pass
        
    if int_vect(pc_set1) == int_vect(pc_set2) and T == [] and I == []:
        Z.append('YES')
    else:
        Z.append('NO')

    results = {'T': T, 'I': I, 'M': M, 'Z': Z}
    return results

def t_vect(pc_set):
    results = []
    for i in range(12):
        invariant = 0
        t_set = trans(pc_set, i)
        for j in t_set:
            if j in pc_set:
                invariant += 1
            else:
                pass
        results.append(invariant)
    return results

def i_vect(pc_set):
    results = []
    for i in range(12):
        invariant = 0
        i_set = inv(pc_set, i)
        for j in i_set:
            if j in pc_set:
                invariant += 1
            else:
                pass
        results.append(invariant)
    return results

def int_string(pc_set):
    result = []
    cycle = pc_set[1:]
    cycle.append(pc_set[0])
    for a, b in zip(cycle, pc_set):
        if (a - b) < 0:
            result.append(a - b + 12)
        else:
            result.append(a - b)
    return result

def pc_sum(pc_set):
    total = 0
    for pc in pc_set:
        total += pc
    return (total % 12)

def harm_cons(pc_set):
  sort = sorted(pc_set)
  backwards = sort[::-1]
  result = []
  vector_array = []
  IC1 = 0
  IC2 = 0
  IC3 = 0
  IC4 = 0
  IC5 = 0
  IC6 = 0
  while len(backwards) > 1:
    n = len(backwards)
    x = 1
    for _ in range(n - 1):
      result.append(backwards[0] - backwards[x])
      x += 1
    backwards.pop(0)
  for i in result:
    if i == 1 or i == 11:
      IC1 += 1
    elif i == 2 or i == 10:
      IC2 += 1
    elif i == 3  or i == 9:
      IC3 += 1
    elif i == 4 or i == 8:
      IC4 += 1
    elif i == 5 or i == 7:
      IC5 += 1
    elif i == 6:
      IC6 += 1
    else:
      pass 
  vector_array.append(IC1)
  vector_array.append(IC2)
  vector_array.append(IC3)
  vector_array.append(IC4)
  vector_array.append(IC5)
  vector_array.append(IC6)
  total = round((IC1_value * vector_array[0]) \
              + (IC2_value * vector_array[1]) \
              + (IC3_value * vector_array[2]) \
              + (IC4_value * vector_array[3]) \
              + (IC5_value * vector_array[4]) \
              + (IC6_value * vector_array[5]), 3)
  return total

def find_prime(pc_set):
    n = len(pc_set)
    transpose = sorted(list(set(pc_set)))
    invert = inv(transpose, 0)[::-1]
    trans_array = []
    inv_array = []
    for i in range(n):
        trans_rotated = transpose[i:] + transpose[:i]
        x = 12 - trans_rotated[0]
        trans_array.append(trans(trans_rotated, x))
        inv_rotated = invert[i:] + invert[:i]
        y = 12 - inv_rotated[0]
        inv_array.append(trans(inv_rotated, y))
    for z in pcs:
        prime = pcs[z][0]
        if prime in trans_array:
            return z
            break
        elif prime in inv_array:
            return z
            break
        else:
            pass

def inventory(pc_set):
    backwards = pc_set[::-1]
    result = {}
    for b in range(len(pc_set)):
        name = '%s' % (b)
        result[name] = []
        for a in backwards:
            result[name].append((a - backwards[b]) % 12)
            b = (b + 1) % len(backwards)
    return result

def rand_set():
    import random as r
    aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]
    random_set = []
    n = r.randint(1,12)
    for a in range(n):
        r.shuffle(aggregate)
        random_set.append(aggregate.pop())
    return random_set

def rel_to_prime(pc_set):
    given = pc_set
    if pcs[find_prime(pc_set)][3]['FORTE'] == 'SAME':
        prime = pcs[find_prime(pc_set)][0]
        rel = find_rel(given, prime)
        if rel['T'] == []:
            result = []
            for i in rel['I']:
                result.append('I%s' % (i))
            return result
        elif rel['I'] == []:
            result = []
            for i in rel['T']:
                result.append('T%s' % (i))
            return result
        else:
            result = []
            for i in rel['T']:
                result.append('T%s' % (i))
            for j in rel['I']:
                result.append('I%s' % (j))
            return result
    else:
        rahn_prime = pcs[find_prime(pc_set)][0]
        rahn_rel = find_rel(given, rahn_prime)
        if rahn_rel['T'] == []:
            rahn_result = []
            for i in rahn_rel['I']:
                rahn_result.append('I%s' % (i))
        elif rahn_rel['I'] == []:
            rahn_result = []
            for i in rahn_rel['T']:
                rahn_result.append('T%s' % (i))
        else:
            rahn_result = []
            for i in rahn_rel['T']:
                rahn_result.append('T%s' % (i))
            for j in rahn_rel['I']:
                rahn_result.append('I%s' % (j))
        
        forte_prime = pcs[find_prime(pc_set)][3]['FORTE']
        forte_rel = find_rel(given, forte_prime)
        if forte_rel['T'] == []:
            forte_result = []
            for i in forte_rel['I']:
                forte_result.append('I%s' % (i))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)
        elif forte_rel['I'] == []:
            forte_result = []
            for i in forte_rel['T']:
                forte_result.append('T%s' % (i))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)
        else:
            forte_result = []
            for i in forte_rel['T']:
                forte_result.append('T%s' % (i))
            for j in forte_rel['I']:
                forte_result.append('I%s' % (j))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)

def complement(pc_set):
	aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]
	for i in pc_set:
		if i in aggregate:
			aggregate.remove(i)
		else:
			pass
	return aggregate
