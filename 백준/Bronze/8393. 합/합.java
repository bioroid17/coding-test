import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		for(int i = sc.nextInt(); i > 0; i--)
			sum += i;
		System.out.println(sum);
		sc.close();
	}
}
