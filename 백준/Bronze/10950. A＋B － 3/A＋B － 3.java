import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println(a+b);
			t--;
		}
		sc.close();
	}
}
