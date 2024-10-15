/*DATO UN NUMERO A PIU CIFRE
ESEGIORE   LA SOMMA DELLE CIFRE E STABILIRE SE E DIVISIBILE PER 3 */

#include <stdio.h>

        int main(){
        int num=0;
        int s1,s2,s3,s4;
        int t,t1,t2,t3,risulato;

        printf("scrivi il numero:");
        scanf("%d",num);
        t=num/10;
        s1=t%10;
        t1=t/10;
        s2=t1%10;
        t2=t/10;
        s3=t2%10;
        risulato=s1+s2+s3;
        printf("il primo valore %d,risultato");


        




        }