
_start:
    mov eax, 47       
    mov ebx, 3        
subtract_loop:
    cmp eax, ebx      
    jl done           
    sub eax, ebx      
    jmp subtract_loop 

