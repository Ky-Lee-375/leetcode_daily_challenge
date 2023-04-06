#include <iostream>
#include <stack>
class Solution {
    // private:
    // map<char, char> map = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
public:
    bool isValid(string s) {
        stack<char> stack;
        for (int i = 0; i < s.length(); i++) {
            if (s.at(i) == '(') {
                stack.push(')');
            } else if (s.at(i) == '{') {
                stack.push('}');
            } else if (s.at(i) == '[') {
                stack.push(']');
            } else if (stack.empty() || s.at(i) != stack.top()) {
                return false;
            } else {
                stack.pop();
            }
        }
        return stack.empty();
    }
};