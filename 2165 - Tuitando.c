#include<stdio.h>
int main(){
  int tamanho;
  char letra[510];
  gets(letra);
  if(strlen(letra)<=140){printf("TWEET\n");}
  else{printf("MUTE\n");}
return 0;}
