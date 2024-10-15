#include <stdio.h>

int main() {
    int numero;

    printf("Inserisci un numero: ");
    scanf("%d", &numero);

    
    if (numero % 3 == 0 && numero % 5 == 0) {
        printf("Il numero %d è divisibile  per 3 e per 5.\n", numero);
    } else {
        printf("Il numero %d non è divisibile per 3 e per 5.\n", numero);
    }

    return 0;
}
