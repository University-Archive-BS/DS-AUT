#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sz(x) (int)(x).size()
using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef pair<int, int> pii;

template <typename T>
struct MOS{
	tree<pair<T, int>, null_type, less<pair<T, int>>, rb_tree_tag,tree_order_statistics_node_update> os;
	map<T, int> cnt;
	int size(){
		return os.size();
	}
	int order_of_key(const T &x){
		return os.order_of_key({x, 0});
	}
	void insert(const T &x){
		os.insert({x, cnt[x]++});
	}
	void erase(const T &x){
		os.erase({x, --cnt[x]});
	}
	T find_by_order(int order) {
		return os.find_by_order(order)->first;
	}
};

MOS<int> os;
int n, typ, x;

int32_t main() {
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);	
	cin >> n;
	while (n--) {
		cin >> typ;
		if (typ == 2) {
			if (sz(os) < 3) {
				cout << "No reviews yet\n";
				continue;
			}
			int k = sz(os) - sz(os)/3;
			cout << os.find_by_order(k) << '\n';
		} else {
			cin >> x;
			os.insert(x);
		}
	}
}
