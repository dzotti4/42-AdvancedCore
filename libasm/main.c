#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>

size_t ft_strlen(const char *str);
char *ft_strcpy(char *dest, const char *src);
int ft_strcmp(const char *s1, const char *s2);
ssize_t ft_write(int fd, const void *buf, size_t count);
ssize_t ft_read(int fd, void *buf, size_t count);
char *ft_strdup(const char *str);
void *ft_calloc(size_t nmemb, size_t size);

static void test_strlen(void)
{
    int ok;

    ok = ft_strlen("hello") == 5 && ft_strlen("") == 0 && ft_strlen("42") == 2;
    printf("ft_strlen: %s\n", ok ? "OK" : "KO");
}

static void test_strcpy(void)
{
    char dest[100];
    char *return_value;

    return_value = ft_strcpy(dest, "hello");
    printf("ft_strcpy: %s\n", strcmp(dest, "hello") == 0 && return_value == dest ? "OK" : "KO");
}

static void test_strcmp(void)
{
    int ok;

    ok = ft_strcmp("hello", "hello") == 0 && ft_strcmp("abc", "abd") < 0 
        && ft_strcmp("abe", "abd") > 0 && ft_strcmp("", "") == 0;
    printf("ft_strcmp: %s\n", ok ? "OK" : "KO");
}

static void test_write(void)
{
    int ok;

    errno = 0;
    ok = ft_write(1, "ft_write\n", 9) == 9 && ft_write(-1, "x", 1) == -1 && errno == EBADF;
    printf("ft_write: %s\n", ok ? "OK" : "KO");
}

static void test_read(void)
{
    char buffer[6] =  {0};
    ssize_t read_result;
    int ok;

    printf("Typ hello and press Enter: ");
    fflush(stdout);
    read_result = ft_read(0, buffer, 5);

    errno = 0;
    ok =  read_result == 5 && strcmp(buffer, "hello") == 0 
        && ft_read(-1, buffer, 1) == -1 && errno == EBADF;
    printf("ft_read: %s\n", ok ? "OK" : "KO");
}

static void test_strdup(void)
{
    const char *src;
    char *copy;
    int ok;

    src = "hello";
    copy = ft_strdup(src);
    ok = copy != NULL && strcmp(copy, src) == 0 && copy != src;
    printf("ft_strdup: %s\n", ok ? "OK" : "KO");
    free(copy);
}

static void test_calloc(void)
{
    unsigned char *memory;
    void *overflow_result;
    int ok;

    memory = ft_calloc(4, 1);
    errno = 0;
    overflow_result = ft_calloc((size_t)-1, 2);

    ok = memory != NULL && memory[0] == 0 && memory[1] == 0 && memory[2] == 0
        && memory[3] == 0 && overflow_result == NULL && errno == ENOMEM;

    printf("ft_calloc: %s\n", ok ? "OK" : "KO");
    free(memory);
}

int main(void)
{
    test_strlen();
    test_strcpy();
    test_strcmp();
    test_write();
    test_read();
    test_strdup();
    test_calloc();

    return (0);
}