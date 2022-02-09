package boj.step.string;

import java.util.Scanner;

public class Step1157 {

	//문자열 5단계 - 1157번 단어 공부
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();					//단어 입력

		str = str.toUpperCase();				//단어 미리 대문자로 변경
		
		int[] arr = new int[26];				//알파벳 26개 배열
		
		for(int i = 0; i < str.length(); i++) {
			arr[str.charAt(i) - 'A']++;			//arr 배열에 사용된 알파벳의 개수 담기
		}
		
		int max = 0;
		char ch = '?';							//가장 많이 사용된 알파벳
		
		for(int i = 0; i < arr.length; i++) {
			
			if(max < arr[i]) {
				max = arr[i];
				ch = (char)(i + 65);			//대문자로 출력
			} else if(max == arr[i]) {
				ch = '?';
			}
		}
		
		System.out.println(ch);
	}

}
