package boj.step.string;

import java.util.Scanner;

public class Step2675 {

	//문자열 4단계 - 2675번 문자열 반복
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();			//테스트 케이스 개수
		
		for(int i = 0; i < num; i++) {
			
			int rNum = sc.nextInt();	//문자열 반복할 횟수
			
			String str = sc.next();		//문자열
			
			for(int j = 0; j < str.length(); j++) {
				for(int k = 0; k < rNum; k++) {
					System.out.print(str.charAt(j));	//rNum번 반복하여 만든 새 문자열
				}	
			}
			System.out.println();
			
		}
		
		
	}

}
