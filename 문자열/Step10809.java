package boj.step.string;

import java.util.Scanner;

public class Step10809 {

	//문자열 3단계 - 10809번 알파벳 찾기
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		char c = 'a';
		
		for(int i = 0; i < 26; i++) {
			System.out.print(str.indexOf(c) + " ");
			c++;
			
		}
	}

}
