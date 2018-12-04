import java.util.*;
import java.util.stream.IntStream;

public class derakht
{
    public static class Graph
    {
        int V;
        ArrayList<List<Integer>> adj;

        public Graph(int V)
        {
            this.V = V;
            adj = new ArrayList<>(100000);
        }

        public void addNode(int n)
        {
            adj.add(n, new ArrayList<>());
        }

        public void addEdge(int v, int w)
        {
            adj.get(v).add(0, w);
            adj.get(w).add(0, v);
        }

        public int longestPathLength()
        {
            Pair t1, t2 = new Pair();

            t1 = bfs(0);
            t2 = bfs(t1.first);

            return t2.second;
        }

        public Pair bfs(int u)
        {
            int[] dis = new int[V];
            Arrays.fill(dis, -1);

            Queue<Integer> q = new LinkedList<>();
            q.add(u);

            dis[u] = 0;

            while (q.size() != 0)
            {
                int t = q.peek();
                q.remove();

                for (int i = 0; i < adj.get(t).size(); i++)
                {
                    int v = adj.get(t).get(i);

                    if (dis[v] == -1)
                    {
                        q.add(v);
                        dis[v] = dis[t] + 1;
                    }
                }
            }

            int maxDis = 0;
            int nodeIdx = 0;

            for (int i = 0; i < V; i++)
            {
                if (dis[i] > maxDis)
                {
                    maxDis = dis[i];
                    nodeIdx = i;
                }
            }
            return new Pair(nodeIdx, maxDis);
        }

        public class Pair
        {
            public int first;
            public int second;

            public Pair()
            {
            }

            public Pair(int first, int second)
            {
                this.first = first;
                this.second = second;
            }

        }
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        Graph derakht = new Graph(n);

        ArrayList<String> commands = new ArrayList<>(n - 1);
        int values = 0;
        int[] numbers = new int[n];
        for (int i = 0; i < n - 1; i++)
        {
            commands.add(in.nextLine());
            String temp = commands.get(i);
            if (!IntStream.of(numbers).anyMatch(x -> x == Integer.parseInt(temp.split(" ")[0])))
            {
                numbers[values] = Integer.parseInt(temp.split(" ")[0]);
                derakht.addNode(numbers[values]);
                values++;
            }
            if (!IntStream.of(numbers).anyMatch(x -> x == Integer.parseInt(temp.split(" ")[1])))
            {
                numbers[values] = Integer.parseInt(temp.split(" ")[1]);
                derakht.addNode(numbers[values]);
                values++;
            }
        }
        for (int i = 0; i < n - 1; i++)
        {
            derakht.addEdge(Integer.parseInt(commands.get(i).split(" ")[0]), Integer.parseInt(commands.get(i).split(" ")[1]));
        }
        System.out.println(derakht.longestPathLength());
    }
}
