#include <bits/stdc++.h>
int n, m, k, fire[107][107], people[107][107], ex, ey, inf = 0x3f3f3f3f;
int jump[8][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
char s[107];
int main() 
{
	scanf("%d%d%d", &n, &m, &k);
	std::queue<std::tuple<int, int>> fire_que, people_que;
	memset(fire, 0x3f, sizeof(fire));
	memset(people, 0x3f, sizeof(people));
	for (int i = 1; i <= n; i++) {
		scanf(" %s", s + 1);
		for (int j = 1; j <= m; j++) 
		{
			if (s[j] == 'f') fire_que.emplace(i, j), fire[i][j] = 0;
			else if (s[j] == 's') people_que.emplace(i, j), people[i][j] = 0;
			else if (s[j] == 't') ex = i, ey = j;
		}
	}
	int x, y, nx, ny;
	while (!fire_que.empty()) 
	{
		std::tie(x, y) = fire_que.front();
		fire_que.pop();
		for (int i = 0; i < 8; i++) 
		{
			nx = x + jump[i][0], ny = y + jump[i][1];
			if (1 <= nx && nx <= n && 1 <= ny && ny <= m && fire[nx][ny] == inf) 
			{
				fire[nx][ny] = fire[x][y] + k;
				fire_que.emplace(nx, ny);
			}
		}
	}
	while (!people_que.empty()) 
	{
		std::tie(x, y) = people_que.front();
		people_que.pop();
		for (int i = 0; i < 4; i++) {
			nx = x + jump[i][0], ny = y + jump[i][1];
			if (1 <= nx && nx <= n && 1 <= ny && ny <= m && people[nx][ny] == inf) {
				if (people[x][y] + 1 < fire[nx][ny]) {
					people[nx][ny] = people[x][y] + 1;
					people_que.emplace(nx, ny);
				}
			}
		}
	}
	if (people[ex][ey] == inf) puts("Impossible");
	else printf("%d\n", people[ex][ey]);

    return 0;
}