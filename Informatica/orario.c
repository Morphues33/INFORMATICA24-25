#include <stdio.h>
int main() {
  int ora1, minuto1, secondi1,ora2, minuto2, secondi2;

  printf("Inserisci l'orario : ");
  scanf("%d %d %d", &ora1, &minuto1, &secondi1);

  printf("Inserisci L'orario : ");
  scanf("%d %d %d", &ora2,&minuto2,&secondi2);

  if (ora1>ora2)
      printf("L'orario piu recente è:%d/%d/%d",ora1,minuto1,secondi1);
  else if(ora1<ora2)
      printf("L'orario piu recente è:%d/%d/%d",ora2,minuto2,secondi2);

  if (minuto1<minuto2)
    printf("L'orario piu recente è:%d/%d/%d",ora1,minuto1,secondi1);
  else if(minuto2>minuto1)
    printf("L'orario piu recente è:%d/%d/%d",ora2,minuto2,secondi2);
    
  if (secondi1<secondi2)
    printf("L'orario piu recente è:%d/%d/%d",ora1,minuto1,secondi1);
  else if(secondi2>secondi1)
    printf("L'orario piu recente è:%d/%d/%d",ora2,minuto2,secondi2);
   
    
}