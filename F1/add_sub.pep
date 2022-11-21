         BR program
_UNIV:   .EQUATE 42
result:  .BLOCK 2
value:   .BLOCK 2
variable:.WORD 3
program: DECI value,d
         LDWA value,d
         ADDA _UNIV,i
         STWA result,d
         LDWA result,d
         SUBA variable,d 
         STWA result,d
         LDWA result,d
         SUBA 1,i
         STWA result,d
         DECO result,d
         .END