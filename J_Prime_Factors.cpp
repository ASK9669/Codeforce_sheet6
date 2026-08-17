#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    bool first = true;

    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            int cnt = 0;

            while (n % i == 0) {
                n /= i;
                cnt++;
            }

            if (!first) cout << "*";
            cout << "(" << i << "^" << cnt << ")";
            first = false;
        }
    }

    // If something is left, it is a prime factor
    if (n > 1) {
        if (!first) cout << "*";
        cout << "(" << n << "^1)";
    }

    cout << '\n';

    return 0;
}
