#include <stdio.h>

int main (){
    float n1,n2,n3,media,min,max;

    max=0;
    min=0;
    n1=0;
    n2=0;
    n3=0;
    media=0;

    printf("inserisci i 3 valori: ");
    scanf("%f%f%f", &n1, &n2, &n3);
    
    min=n1;
    max=n1;
    if(max<n1){
        (max=n2);
        if(max<n3);
            max=n3;
}
else
    if (min>n3);
        min=n3;
printf("il minimo è: %f",min);



media=(n1+n2+n3)/3;
printf("\nla media è:%f", media);

}