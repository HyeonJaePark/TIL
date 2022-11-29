#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        string sentence;
        getline(cin, sentence);
        
        if (sentence == ".") break;

        stack<char> s;
        bool tf = true;
        for (auto c : sentence) {
            if (c == '(' || c == '[') s.push(c);
            else if (c == ')') {
                if (s.empty() || s.top() != '(') {
                    tf = false;
                    break;
                }
                s.pop();
            }
            else if (c == ']') {
                if (s.empty() || s.top() != '[') {
                    tf = false;
                    break;
                }
                s.pop();
            }
        }

        if (!tf) cout << "no\n";
        else cout << "yes\n";
    }

    return 0;
}
