import java.util.Scanner;

public class Main {
	public static int max(int a, int b) {
		if (a >= b)
			return a;
		else
			return b;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int score = 0;
		if(a == b && b == c)
			score = 10000 + a * 1000;
		else if(a == b && b != c)
			score = 1000 + b * 100;
		else if(b == c && c != a)
			score = 1000 + c * 100;
		else if(c == a && a != b)
			score = 1000 + a * 100;
		else
			score = max(max(a, b), c) * 100;
		System.out.println(score);
		sc.close();
	}
}