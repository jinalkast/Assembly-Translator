BR       PROGRAM
a:       .BLOCK 2
b:       .BLOCK 2

PROGRAM: DECI a,d
         DECI b,d

test:    LDWA a,d
         CPWA b,d
         BREQ end_l

if:      LDWA a,d
         CPWA b,d
         BRLE else 
         LDWA a,d
         SUBA b,d
         STWA a,d
         BR end_if

else:    LDWA b,d
         SUBA a,d
         STWA b,d

end_if:  BR test

end_l:   DECO a,d
         .END