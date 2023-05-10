package boj.step.string;

import java.util.Scanner;

public class Step2941 {

	// 문자열 9단계 - 크로아티아 알파벳
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();		//단어 입력
		
		//크로아티아 알파벳을 담은 배열
		String[] arr = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		
		//크로아티아 알파벳 개수 세기
		for(int i = 0; i < arr.length; i++) {
			if(str.contains(arr[i])) {
				//크로아티아 알파벳이 있으면 1로 대체
				str = str.replace(arr[i], "1");	
			}
		}
		
		System.out.println(str.length());
	}

}
