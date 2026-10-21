section .text
global ft_strdup
extern ft_strlen
extern ft_strcpy
extern malloc

ft_strdup:
    push rbx
    mov rbx, rdi
    call ft_strlen
    inc rax
    mov rdi, rax
    
    call malloc wrt ..plt
    cmp rax, 0
    je .done
    
    mov rdi, rax
    mov rsi, rbx
    call ft_strcpy

.done:
    pop rbx
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
