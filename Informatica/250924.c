#include <stdio.h>

int main() {
    
    float litri, costoxlitro, importopagato, importototale, resto;
    
    printf("Inserisci il numero di litri: ");
    scanf("%f", &litri);
    
   
    printf("scrivi il costo per litro di carburante: ");
    scanf("%f", &costoxlitro);
    
    importototale = litri * costoxlitro;
    
    printf("la somma che devi pagare è di : %.2f euro\n", importototale);
    
    printf("di che taglio è la banconota: ");
    scanf("%f", &importopagato);
    
    resto = importopagato - importototale;
    
    if (resto < 0) {
        printf("il credito non e sufficiente.\n");
    } else {
        printf("il resto è di : %.2f euro\n", resto);
    }

    return 0;
}