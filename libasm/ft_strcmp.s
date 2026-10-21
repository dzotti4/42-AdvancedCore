section .text
global ft_strcmp

ft_strcmp:
    xor rcx, rcx

.loop:
    movzx eax, byte[rdi + rcx]
    movzx edx, byte[rsi + rcx]
    cmp eax, edx
    jne .different
    cmp eax, 0
    je .done
    inc rcx
    jmp .loop

.different:
    sub eax, edx

.done:
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
