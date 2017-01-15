# Roman_calc
http://127.0.0.1:8000/roman_calc/result for execution

-> select POST method
-> select application/json 
-> Input / Output type
     {"qriy":"IX+X"}  ------>    XIX
     {"qriy":"C-X"}  ------>     IC
     {"qriy":"C*X"}  ------>     M
     {"qriy":"C/X"}  ------>     X
-> Error
     {"qriy":"C*AX"}    ------> | 
     {"qriy":"C C*X"}   ------> |
     {"qriy":"C"}       ------> |
     {"qriy":"C *X"}    ------> |
     {"qriy":"A * B"}   ------> |    
                                |->   Wrong formate of roman Expression-----/
                                      Roman Number Containce only IVXLCDM 
                                      ex: IX+X
-> project only handals 3 parameter
      
