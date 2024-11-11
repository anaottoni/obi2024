// pontuação: 100/100

import java.util.Scanner;

public class construtora {
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[] v = new int[n];
		
		for(int i = 0; i < n; i++) {
			v[i] = sc.nextInt();
		}
		
		int maior = 0;
		int menor = v[0];
		
		for(int i = 0; i < n; i ++) {
			if (v[i] > maior)
				maior = v[i];
			if (v[i] < menor)
				menor = v[i];
		}
		int ind = 0, cont = 0, auxind = 0;
		
		while(menor < maior) {
			if(ind == n) {
				ind = 0;
				menor++;
			}
			
			if(menor == maior)
				break;
			
			if(v[ind] == menor) {
				cont++;
				auxind = 1;
				v[ind]++;
				
				for(int i = ind+1; i < n; i++) {
					if(v[i] == menor) {
						v[i]++;
						auxind ++;
					}
					else
						break;
				}
				
				ind += auxind;
			}
			else {
				ind++;
			}
		}
		
		System.out.println(cont);
		
		sc.close();
	}

}
