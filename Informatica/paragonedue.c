#include <stdio.h>

int main() {
    int giorno1, mese1, anno1,giorno2, mese2, anno2;
    

    printf("Inserisci la prima data : ");
    scanf("%d %d %d", &giorno1, &mese1, &anno1);

    printf("Inserisci la seconda data : ");
    scanf("%d %d %d", &giorno2, &mese2, &anno2);

    if (anno1>anno2)
      printf("Lanno piu recente è:%d/%d/%d",giorno1,mese1,anno1);
    else if(anno1<anno2)
    printf("L'anno piu recente è:%d/%d/%d",giorno2,mese2,anno2);

    if (mese1<mese2)
      printf("Lanno piu recente è:%d/%d/%d",giorno1,mese1,anno1);
    else if(mese2>mese1)
    printf("L'anno piu recente è:%d/%d/%d",giorno2,mese2,anno2);
    
    if (giorno1<giorno2)
      printf("Lanno piu recente è:%d/%d/%d",giorno1,mese1,anno1);
    else if(giorno2>giorno1)
    printf("L'anno piu recente è:%d/%d/%d",giorno2,mese2,anno2);
    



  }
