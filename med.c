#include<stdio.h>
int main (){
int  i;
float med, num, qntPositivos, soma = 0;
float positivos[4] = {};
for (i = 0; i < 6; i++){
  printf ("Digite um numero:\n");
  scanf ("%f", &num);
  if (num > 0){
    qntPositivos++;
    positivos[i] = num;
  }

}

for (size_t i = 0; i < qntPositivos; i++){
  soma = positivos[i-1] + positivos[i];
}
printf ("Positivos: %.1f\n", qntPositivos);
printf(positivos);

med = (6/qntPositivos);

printf ("\n %.1f e a media dos numeros positivos", positivos);


system("pause");
return 0;
}
