package day03;

public class MyMethod01 {

	static int add(int a, int b) {
		return a + b;
	}

	static int minus(int a, int b) {
		return a - b;
	}

	static int mutiply(int a, int b) {
		return a * b;
	}

	public static void main(String[] args) {
		int sum = add(4, 2);
		System.out.println("sum : " + sum);
		
		int min = minus(4, 2);
		System.out.println("min : " + min);
		
		int mul = mutiply(4, 2);
		System.out.println("mul : " + mul);
		
		int div = divide(4, 2);
		System.out.println("div : " + div);
	}
	
	static int divide(int a, int b) {
		return a / b;
	}

}