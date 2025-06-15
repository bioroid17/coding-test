import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i = 1;
		int num = sc.nextInt();
		while(i < 10)
		{
			System.out.println(num + " * " + i + " = " + num * i);
			i++;
		}
		sc.close();
	}
}