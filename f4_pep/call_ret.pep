         BR program 
; memory allocation
x:       .BLOCK 2
result:   .BLOCK 2
_UNIV:    .EQUATE 42
; FUNC
lresult:   .EQUATE 0 
value:   .EQUATE 4
my_func: SUBSP 2,i 
         LDWA value, s
         ADDA _UNIV, i
         STWA lresult, s
         LDWA lresult ,s
         STWA 6,s
         ADDSP   2,i 
         RET
         

program: DECI x,d
         LDWA x,d
         SUBSP 4,i
         STWA 0, s
         call my_func
         ADDSP 2,i
         LDWA 0,s
         STWA result,d
         ADDSP 2,i
         DECO result,d
         .end
         