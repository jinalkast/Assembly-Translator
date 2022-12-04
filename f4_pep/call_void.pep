         BR program 
; memory allocation
_UNIV:    .EQUATE 42

; FUNC
lresult:   .EQUATE 2 
lvalue:   .EQUATE 0

my_func: DECI lvalue, s
         LDWA lvalue, s
         ADDA _UNIV, i 
         STWA lresult, s 
         DECO lresult, s 
         RET
         

program: call my_func
         .end
         