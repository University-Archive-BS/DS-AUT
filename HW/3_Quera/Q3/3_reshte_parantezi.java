import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        String input = scanner.nextLine();
        Stack<Character> stack = new Stack<Character>();
        int temp = 0;
        ArrayList<Integer> maxes = new ArrayList<>();
        for(Character c : input.toCharArray()){
            if(c == '(')
                if (stack.isEmpty()) {
                    maxes.add(temp);
                    temp = 0;
                    stack.push('(');
                }
                else {
                    temp ++;
                    stack.push('(');
                }
            else {
                stack.pop();
                temp ++;
            }
        }

        System.out.print(Collections.max(maxes));
    }
}
