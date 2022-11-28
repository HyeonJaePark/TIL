#include <bits/stdc++.h>
using namespace std;


const int MX = 100005;
int dat[MX];
int pos = 0;

void push(int x) {
    dat[pos++] = x;
}

void pop() {
    pos--;
}

int top() {
    return dat[pos - 1];
}

bool empty() {
    return pos ? false : true;
}

int size() {
    return pos ? pos : 0;
}

void check_stack() {
    bool isEmpty = empty();
    cout << "isEmpty: " << isEmpty << '\n';

    cout << "check_stack: ";
    for (int i = 0; i < pos; i++) {
        cout << dat[i] << ' ';
    }
    cout << "\n";

    int len = size();
    cout << "size: " << len << "\n\n";
}

void test() {
    check_stack();
    push(13);
    check_stack();
    push(21);
    check_stack();
    push(30);
    check_stack();
    pop();
    check_stack();
    int t = top();
    cout << t << '\n';
    check_stack();
}

int main() {
    test();
    return 0;
}