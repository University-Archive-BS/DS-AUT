#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sz(x) (int)(x).size()
#define int long long
using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn = 2e3 + 11;
vector<int> g[maxn];
int n;

pii dfs(int u, int pa) {
	pii ret = {u, 0};
	for (auto x : g[u])
		if (x != pa) {
			pii temp = dfs(x, u);
			if (temp.second + 1 > ret.second) {
				ret.second = temp.second + 1;
				ret.first = temp.first;
			}
		}
	return ret;
}

int32_t main() {
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	cin >> n;
	for (int u, v, i = 0; i < n - 1; i++) {
		cin >> u >> v; u--, v--;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	int u = dfs(0, -1).first;
	cout << dfs(u, -1).second << endl;
}
