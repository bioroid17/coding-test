import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int i = 1; i <= t; i++) {
			for(int j = 1; j <= i; j++)
				System.out.printf("*");
			System.out.println();
		}
		sc.close();
	}
}
