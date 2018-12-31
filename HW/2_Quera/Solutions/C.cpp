#include <bits/stdc++.h>
#define sz(x) (int)(x).size()
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;


const int maxn = 1e2 + 11;
int n, m, k;
string mp[maxn];
int sx, sy, tx, ty, tim[maxn][maxn], dis[maxn][maxn];

int dx[] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

inline bool ok(int x, int y) { return x < n and x >= 0 and y < m and y >= 0; }

int32_t main() {
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	cin >> n >> m >> k;

	queue< pii > bfs;
	memset(tim, 63, sizeof tim);
		
	for (int i = 0; i < n; i++) {
		cin >> mp[i];
		for (int j = 0; j < m; j++) {
			if (mp[i][j] == 'f') {
				tim[i][j] = 0;
				bfs.push({i, j});
			}
			if (mp[i][j] == 's')
				sx = i, sy = j;
			if (mp[i][j] == 't')
				tx = i, ty = j;
		}
	}

	while (!bfs.empty()) {
		pii p = bfs.front();
		int xx = p.first;
		int yy = p.second;
		bfs.pop();
		for (int i = 0; i < 8; i++) {
			int nx = xx + dx[i];
			int ny = yy + dy[i];
			if (ok(nx, ny) and tim[nx][ny] > tim[xx][yy] + k) {
				tim[nx][ny] = tim[xx][yy] + k;
				bfs.push({nx, ny});
			}
		}
	}

	memset(dis, 63, sizeof dis);
	dis[sx][sy] = 0;
	bfs.push({sx, sy});
	while (!bfs.empty()) {
		pii p = bfs.front();
		int xx = p.first;
		int yy = p.second;
		bfs.pop();
		for (int i = 0; i < 4; i++) {
			int nx = xx + dx[i];
			int ny = yy + dy[i];
			if (ok(nx, ny) and dis[nx][ny] > dis[xx][yy] + 1) {
				if (tim[nx][ny] <= dis[xx][yy] + 1)
					continue;
				dis[nx][ny] = dis[xx][yy] + 1;
				bfs.push({nx, ny});
			}
		}
			
	}

	if (dis[tx][ty] > (int)1e8)
		cout << "Impossible\n";
	else
		cout << dis[tx][ty] << '\n';
		
}
