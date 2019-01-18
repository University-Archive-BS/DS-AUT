import java.util.Arrays;
import java.util.Scanner;

public class watermelon
{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        int[] arr = new int[n];
        String[] strings = scanner.nextLine().split(" ");
        for (int i = 0; i < strings.length; i++) {
            arr[i] = Integer.parseInt(strings[i]);
        }
        Jewelry j = new Jewelry();
        System.out.println(j.howMany(arr));
    }
}

class Jewelry {
    public long howMany(int[] values) {
        Arrays.sort(values);

        int n = values.length;

        int[] fk = new int[n];
        for (int i = 0; i < n; i++) {
            fk[i] = (i > 0 && values[i] == values[i - 1]) ? fk[i - 1] + 1 : 1;
        }

        int[] gk = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            gk[i] = (i < n - 1 && values[i] == values[i + 1]) ? gk[i + 1] + 1 : 1;
        }

        int[] mc = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (values[i] == values[j]) {
                    mc[i]++;
                }
            }
        }

        long[][] ch = new long[31][62];
        for (int j = 0; j < 61; j++) {
            ch[0][j] = 1;
            for (int i = 1; i <= Math.min(j, 30); i++) {
                if (i < j) {
                    ch[i][j] = ch[i][j - 1];
                }
                ch[i][j] += ch[i - 1][j - 1];
            }
        }

        long[][] f = new long[30001][30];
        for (int k = 1; k < 30001; k++) {
            for (int i = 0; i < n; i++) {
                int v = k - values[i] * fk[i];
                if (v == 0) {
                    f[k][i] = 1;
                } else if (v > 0) {
                    for (int j = 0; j < i - fk[i] + 1; j++) {
                        f[k][i] += f[v][j] * ch[fk[j]][mc[j]];
                    }
                }
            }
        }

        long[][] g = new long[30001][30];
        for (int k = 1; k < 30001; k++) {
            for (int i = n - 1; i > 0; i--) {
                int v = k - values[i] * gk[i];
                if (v == 0) {
                    g[k][i] = 1;
                } else if (v > 0) {
                    for (int j = i + gk[i]; j < n; j++) {
                        g[k][i] += g[v][j] * ch[gk[j]][mc[j]];
                    }
                }
            }
        }

        long tot = 0;
        for (int i = 1; i < 30001; i++) {
            for (int j = 0; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int a = fk[j];
                    int b = gk[k];
                    int c = mc[j];
                    int d = mc[k];
                    long t = f[i][j] * g[i][k];

                    if (t == 0) {
                        continue;
                    }

                    if (values[j] == values[k]) {
                        t *= ch[a][c] * ch[b][c - a];
                    } else {
                        t *= ch[a][c] * ch[b][d];
                    }
                    tot += t;
                }
            }
        }

        return tot;
    }
}
