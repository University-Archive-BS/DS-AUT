#include <bits/stdc++.h>
using namespace std;


priority_queue<int, vector<int> , greater<int> > se;
priority_queue<int> fi;


int main()
{
	int n;
	cin >> n;
	int sz = 0;
	for(int i=0;i<n;i++)
	{
		int type , x;
		cin >> type;
		if(type == 1)
		{
			sz++;
			cin >> x;
			if(fi.size() <= 2 || x < se.top())

			{
				fi.push(x);
				if(se.size() < sz/3)
				{
					se.push(fi.top());
					fi.pop();
				}

			}
			else 
			{	se.push(x);
				if(se.size() > sz/3)
				{
					fi.push(se.top());
					se.pop();
				}
			}
		}
		else if(type == 2)
		{
			if(sz>=3)
				cout << se.top() << endl;
			else 
				cout << "No reviews yet" << endl;
		}
	}
//	cout <<"SE" << endl;
//	while(se.size())
//	{
//		cout << se.top() << " ";
//		se.pop();
//	}
//	cout << endl;
//	cout << "FI" << endl;

//	while(fi.size())
//	{
//		cout << fi.top() <<" ";
//		fi.pop();
//	}


	return 0;
}

