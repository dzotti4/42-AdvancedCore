*This project has been created as part of the 42 curriculum by dzotti.*

# libasm

## Description

A small library written in x86-64 assembly (NASM, Intel syntax) with these functions:

- `ft_strlen`, `ft_strcpy`, `ft_strcmp`, `ft_strdup`
- `ft_write` and `ft_read`: system calls that set `errno` on failure, like the real ones
- `ft_calloc`: extra, with an overflow check

## Instructions

Needs Linux on x86-64 and `nasm`.

```bash
make                              # builds libasm.a
gcc main.c -L. -lasm -o test      # main.c tests every function
echo hello | ./test
```

## What I learned

- The System V calling convention: arguments in `rdi`, `rsi`, `rdx`, return value in `rax`
- System calls, `errno` and calling libc (`malloc`) from assembly
- Stack alignment and position-independent code (`wrt ..plt`)
