package boj.step.string;

import java.util.Scanner;

public class Step11720 {

	//문자열 2단계. 11720번 숫자의 합
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();		//숫자의 개수
		String str = sc.next();		//숫자 N개 공백없이
		int result = 0;				//숫자 N개의 합
		
		for(int i = 0; i < num; i++) {
			result += str.charAt(i) - '0';	//char -> int 형변환 후 합
			
		}
		System.out.println(result);
		
	}

}
