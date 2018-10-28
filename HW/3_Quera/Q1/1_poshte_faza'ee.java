import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Main {

        public static void main(String[] args) {
            Stack<Pair> stack = new Stack<>();
            Scanner in = new Scanner(System.in);

            int operationNumber = Integer.parseInt(in.nextLine());
            ArrayList<String> operations = new ArrayList<>();
            for (int i = 0; i < operationNumber; i++) {
                operations.add(in.nextLine());
            }

            for(int i = 0 ; i < operationNumber; i++) {

                if (operations.get(i).equals("pop")) {
                    if(!stack.isEmpty())
                        stack.pop();
                }
                else if (operations.get(i).contains("push")) {
                    int x = Integer.parseInt(operations.get(i).substring(5));
                    if(stack.isEmpty())
                        stack.push(new Pair(x, x));
                    else
                        stack.push(new Pair(x, Math.min(x, stack.peek().minimum)));

                }
                else if (operations.get(i).equals("spell")) {
                    if(!stack.isEmpty())
                        System.out.println(stack.peek().minimum);
                }

            }
        }

        private static class Pair {
            int value, minimum;

            public Pair(int val, int min) {
                value = val;
                minimum = min;
            }
        }
    }

