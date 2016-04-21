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
