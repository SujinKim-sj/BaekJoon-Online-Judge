package boj.step.string;

import java.util.Scanner;

public class Step2908 {
	
	//문자열 7단계 - 2908번 상수
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();		//상근이가 칠판에 적은 두 수
		
		String[] arr = str.split(" ");	//공백으로 문자열 분리
	
		String[] newNum = new String[2];	//상수가 읽은 두 수
		
		//상수가 읽은 두 수 구하기
		for(int i = 0; i < 2; i++) {
			newNum[i] = "0";
			for(int j = 3; j > 0; j--) {
				newNum[i] += arr[i].charAt(j - 1);							
			}
		}
		
		int n1 = Integer.parseInt(newNum[0]);
		int n2 = Integer.parseInt(newNum[1]);
		
		//두 수 중 큰 수를 출력 - 상수의 대답
		System.out.println(n1 > n2 ? n1 : n2);
		
	}

}
