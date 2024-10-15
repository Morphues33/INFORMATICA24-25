#include <stdio.h>
int main() {
  int ora1, minuto1, secondi1,ora2, minuto2, secondi2;
  // uso il printf per chiedere l'orario
  printf("Inserisci l'orario : ");
  //leggo l'input dei dati per ogni variabile metto %d tra virgolette,&con ogni variabile
  scanf("%d %d %d", &ora1, &minuto1, &secondi1);

  printf("Inserisci L'orario : ");
  scanf("%d %d %d", &ora2,&minuto2,&secondi2);
     // if metto con l'operazione che voglio
  if (ora1>ora2)
      // printf con cosa voglio se esce che la cosa e reale
      printf("L'orario piu recente è:%d/%d/%d",ora1,minuto1,secondi1);
      // else if se invece e il contrario non esce > ma minore < 
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