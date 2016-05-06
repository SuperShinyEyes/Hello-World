## References
* http://gribblelab.org/CBootcamp/8_Pointers.html

## [Stack vs. heap](http://gribblelab.org/CBootcamp/7_Memory_Stack_vs_Heap.html)

### The Stack

What is the stack? It's a special region of your computer's memory that stores temporary variables created by each function (including the main() function). The stack is a "FILO" (first in, last out) data structure, that is managed and optimized by the CPU quite closely. Every time a function declares a new variable, it is "pushed" onto the stack. Then every time a function exits, all of the variables pushed onto the stack by that function, are freed (that is to say, they are deleted). Once a stack variable is freed, that region of memory becomes available for other stack variables.

The advantage of using the stack to store variables, is that memory is managed for you. You don't have to allocate memory by hand, or free it once you don't need it any more. What's more, because the CPU organizes stack memory so efficiently, reading from and writing to stack variables is very fast.

A key to understanding the stack is the notion that when a function exits, all of its variables are popped off of the stack (and hence lost forever). Thus stack variables are local in nature. This is related to a concept we saw earlier known as variable scope, or local vs global variables. A common bug in C programming is attempting to access a variable that was created on the stack inside some function, from a place in your program outside of that function (i.e. after that function has exited).

Another feature of the stack to keep in mind, is that there is a limit (varies with OS) on the size of variables that can be store on the stack. This is not the case for variables allocated on the heap.

To summarize the stack:

    * the stack grows and shrinks as functions push and pop local variables
    * there is no need to manage the memory yourself, variables are allocated and freed automatically
    * the stack has size limits
    * stack variables only exist while the function that created them, is running

### The Heap

The heap is a region of your computer's memory that is not managed automatically for you, and is not as tightly managed by the CPU. It is a more free-floating region of memory (and is larger). To allocate memory on the heap, you must use malloc() or calloc(), which are built-in C functions. Once you have allocated memory on the heap, you are responsible for using free() to deallocate that memory once you don't need it any more. If you fail to do this, your program will have what is known as a memory leak. That is, memory on the heap will still be set aside (and won't be available to other processes). As we will see in the debugging section, there is a tool called valgrind that can help you detect memory leaks.

Unlike the stack, the heap does not have size restrictions on variable size (apart from the obvious physical limitations of your computer). Heap memory is slightly slower to be read from and written to, because one has to use pointers to access memory on the heap. We will talk about pointers shortly.

Unlike the stack, variables created on the heap are accessible by any function, anywhere in your program. Heap variables are essentially global in scope.


### Stack vs Heap Pros and Cons
**Stack**
* very fast access
* don't have to explicitly de-allocate variables
* space is managed efficiently by CPU, memory will not become fragmented
* local variables only
* limit on stack size (OS-dependent)
* variables cannot be resized

**Heap**
* variables can be accessed globally
* no limit on memory size
* (relatively) slower access
* no guaranteed efficient use of space, memory may become fragmented over time as blocks of memory are allocated, then freed
* you must manage memory (you're in charge of allocating and freeing variables)
* variables can be resized using realloc()

### Example
```c
#include <stdio.h>

double multiplyByTwo (double input) {
  double twice = input * 2.0;
  return twice;
}

int main (int argc, char * argv[])
{
  int age = 30;
  double salary = 12345.67;
  double myList[3] = {1.2, 2.3, 3.4};

  printf("double your salary is %.3f\n", multiplyByTwo(salary));

  return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

double *multiplyByTwo (double *input) {
  double *twice = malloc(sizeof(double));
  *twice = *input * 2.0;
  return twice;
}

int main (int argc, char *argv[])
{
  int *age = malloc(sizeof(int));
  *age = 30;
  double *salary = malloc(sizeof(double));
  *salary = 12345.67;
  double *myList = malloc(3 * sizeof(double));
  myList[0] = 1.2;
  myList[1] = 2.3;
  myList[2] = 3.4;

  double *twiceSalary = multiplyByTwo(salary);

  printf("double your salary is %.3f\n", *twiceSalary);

  free(age);
  free(salary);
  free(myList);
  free(twiceSalary);

  return 0;
}
```
***asdf
As you can see, using malloc() to allocate memory on the heap and then using free() to deallocate it, is no big deal, but is a bit cumbersome. The other thing to notice is that there are a bunch of star symbols * all over the place now. What are those? The answer is, they are pointers. The malloc() (and calloc() and free()) functions deal with pointers not actual values. We will talk more about pointers shortly. The bottom line though: pointers are a special data type in C that store addresses in memory instead of storing actual values. Thus on line 5 above, the twice variable is not a double, but is a pointer to a double. It's an address in memory where the double is stored.

### When to use the Heap?

When should you use the heap, and when should you use the stack? If you need to allocate a large block of memory (e.g. a large array, or a big struct), and you need to keep that variable around a long time (like a global), then you should allocate it on the heap. If you are dealing with realtively small variables that only need to persist as long as the function using them is alive, then you should use the stack, it's easier and faster. If you need variables like arrays and structs that can change size dynamically (e.g. arrays that can grow or shrink as needed) then you will likely need to allocate them on the heap, and use dynamic memory allocation functions like malloc(), calloc(), realloc() and free() to manage that memory "by hand". We will talk about dynamically allocated data structures after we talk about pointers.


## Pointers
```c
#include <stdio.h>

int main (int argc, char *argv[])
{
  int age = 30;
  int *p;
  p = &age;
  printf("age=%d\n", age);                // age=30
  printf("p=%p\n", p);                    // p=0x7fff197ceb1c
  printf("*p=%d\n", *p);                  // *p=30
  printf("sizeof(p)=%ld\n", sizeof(p));   // sizeof(p)=8
  *p = 40;
  printf("*p=%d\n", *p);                  // *p=40
  printf("age=%d\n", age);                // age=40
  return 0;
}
```

## Allocate memory for an array
```c
double *dataDouble = (double* ) malloc(sizeof(double) * 10);
```

## Copy array
```c
#include <iostream>
#include <cstdlib>
#include <algorithm>

int main() {
    int *container = (int *) malloc(sizeof(int) * 2);
    container[0] = 10;
    container[1] = 101;
    int *dataDouble = (int *) malloc(sizeof(int) * 2);
    std::copy(container, container + 2, dataDouble);
    std::cout << *(container+1) << "\n";
    std::cout << *(dataDouble+1) << "\n";
    return 0;
}
```

## Fast sort (nth select)
```c
std::nth_element(buf.begin(), buf.begin() + buf.size()/2 - 1, buf.end());
```

## Vector types in GCC
* Always available
* Compiler uses special vector registers and instructions whenever possible
* Remember to specify the architecture
    * g++ -march=native

```c
typedef double double4_t __attribute__ ((__vector_size__ (4*sizeof(double))));
// Now these are almost equivalent:
double4_t a;
double a[4];


typedef float float8_t __attribute__ ((__vector_size__ (8*sizeof(float))));
// Now these are almost equivalent:
float8_t a;
float a[8];


// Operations on entire vectors:
float8_t a, b, c;
a += b * c;
// Same as:
for (int i = 0; i < 8; ++i) {
 a[i] += b[i] * c[i];
}
```

## Memory Alignment for Vector Instruction
* posix_memalign() to allocate memory, free() to release
* common/vector.* for helper function
    * float8_alloc(), double4_alloc()

```c
double4_t* x = double4_alloc(n);
double4_t* y = double4_alloc(n);

for (int i = 0; i < n; ++i) {
 for (int j = 0; j < 4; ++j) {
 x[i][j] = ...;
 }
}

for (int i = 0; i < n; ++i) {
 double4_t z = x[i];
 y[i] = z * z;
}

// Is equivalent to in Assembly language:
/*
 vmovapd (%rbx,%rax), %ymm0
 vmulpd %ymm0, %ymm0, %ymm0
 vmovapd %ymm0, (%r12,%rax)
 addq $32, %rax
 cmpq %rdx, %rax
 jne L42
*/
// ...pd = packed doubles = vector of doubles
// ymm.. = 256-bit register

free(x);
free(y);
```

## Vector Instruction Tips
1. Repeatedly work with a small chunk of << 32KB of data:
    * all data remains in L1
    * small latency (order of 1 ns)
    * large bandwidth
2. Random reads in >> 8MB of data:
    * most memory lookups are cache misses
    * large latency (order of 100 ns)
    * small bandwidth
3. Cases:
    * Ideal: linear read of L1
    * Good: random access of L1, linear read of L2–L3
    * Tolerable: linear read of main memory
    * Bad: random access of main memory
    * Horrible: random reads with dependencies
4. You can do useful work while you wait for data from main memory
5.  Instruction-level parallelism does it automatically, if there are some other independent operations that you can run
    * following a linked list: expensive, because all the items are independent.

![vector_instruction_benchmark](/images/vector_instruction_benchmark.png)

### Cache blocking: better locality
![Cache_blocking_1](/images/Cache_blocking_1.png)
![Cache_blocking_1](/images/Cache_blocking_2.png)
[Cache Blocking Demo](https://users.ics.aalto.fi/suomela/cache-blocking-demo/)


## C preprocessing
### Directives
Directive |	Description
---|---
#define | Substitutes a preprocessor macro.
#include | Inserts a particular header from another file.
#undef | Undefines a preprocessor macro.
#ifdef | Returns true if this macro is defined.
#ifndef | Returns true if this macro is not defined.
#if | Tests if a compile time condition is true.
#else | The alternative for #if.
#elif | #else and #if in one statement.
#endif | Ends preprocessor conditional.
#error | Prints error message on stderr.
#pragma | Issues special commands to the compiler, using a standardized method.

### Predefined Macros
Macro | Description
---|---
__DATE__ | The current date as a character literal in "MMM DD YYYY" format.
__TIME__ | The current time as a character literal in "HH:MM:SS" format.
__FILE__ | This contains the current filename as a string literal.
__LINE__ | This contains the current line number as a decimal constant.
__STDC__ | Defined as 1 when the compiler complies with the ANSI standard.

```c
#include <stdio.h>

main() {

   printf("File :%s\n", __FILE__ );    // File :test.c
   printf("Date :%s\n", __DATE__ );    // Date :Jun 2 2012
   printf("Time :%s\n", __TIME__ );    // Time :03:36:24
   printf("Line :%d\n", __LINE__ );    // Line :8
   printf("ANSI :%d\n", __STDC__ );    // ANSI :1

}
```

### Examples
```c
#undef  FILE_SIZE
#define FILE_SIZE 42

#ifdef DEBUG
   /* Your debugging statements here */
#endif

```

### The Stringize (#) Operator
```c
#include <stdio.h>

#define  message_for(a, b)  \
   printf(#a " and " #b ": We love you!\n")

int main(void) {
   message_for(Carole, Debra);    // Carole and Debra: We love you!
   return 0;
}
```

### Token pasting(##)
```c
#include <stdio.h>

#define tokenpaster(n) printf ("token" #n " = %d", token##n)

int main(void) {
   int token34 = 40;
   tokenpaster(34);    // token34 = 40
   return 0;
}
```

### Parameterized Macros
```c
int square(int x) {
   return x * x;
}

// Is equal to
#define square(x) ((x) * (x))

// More example
#define MAX(x,y) ((x) > (y) ? (x) : (y))

int main(void) {
   printf("Max between 20 and 10 is %d\n", MAX(10, 20));  
   return 0;
}
```

## What happens during compile-time
1. Editor: Programmer creates program in the editor and stores it on disk.
2. Preprocessor: Preprocessor program processes the code.
3. Compiler: Compiler creates object code and stores it on disk.
4. Linker: Linker links the object code with the libraries, creates an executable file and stores it on disk.
5. Loader: Loader puts program in memory.
6. CPU: CPU takes each instruction and executes it, possibly storing new data values as the program executes.
```c

```

##
```c

```

##
```c

```

##
```c

```
