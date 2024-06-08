<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-4],0x7         
<+15>:    mov    DWORD PTR [rbp-8],0x6        
<+22>:    mov    eax,DWORD PTR [rbp-4]       
<+25>:    add    eax,DWORD PTR [rbp-8]       
<+28>:    shl    eax,0x4                      
<+31>:    pop    rbp
<+32>:    ret