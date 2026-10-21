section .text
global ft_calloc
extern malloc
extern __errno_location

ft_calloc:
    push rbx

    mov rax, rdi
    mul rsi
    cmp rdx, 0
    jne .overflow

    mov rbx, rax
    mov rdi, rax
    call malloc wrt ..plt
    
    cmp rax, 0
    je .done
    
    xor rcx, rcx

.zero_loop:
    cmp rcx, rbx
    je .done
    mov byte [rax + rcx], 0
    inc rcx
    jmp .zero_loop

.overflow:
    call __errno_location wrt ..plt
    mov dword [rax], 12
    xor rax, rax

.done:
    pop rbx
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
