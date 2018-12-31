#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sz(x) (int)(x).size()
#define int long long
using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef pair<int, int> pii;

struct MS {
	int siz=0;
	map<int, int> cnt;
	void insert(int x) { cnt[x]++; siz++; }
	int popmin() {
		int mn = cnt.begin()->first;
		if (--cnt[mn] == 0)
			cnt.erase(mn);
		siz--;
		return mn;
	}
} ms;

int32_t main() {
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n; cin >> n;
	while (n--) {
		int x; cin >> x;
		ms.insert(x);
	}
	int ans = 0;
	while (ms.siz >= 2) {
		int a = ms.popmin();
		int b = ms.popmin();
		ms.insert(a + b);
		ans += a + b;
	}
	ans += ms.popmin();
	cout << ans << '\n';
}
