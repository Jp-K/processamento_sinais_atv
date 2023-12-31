/* Implementação de um filtro Média Móvel 
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
Walter versão 1.0 
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define NSAMPLES       4	// Tamanho da média

int main()
{
   FILE *in_file, *out_file;
   int i, n, n_amost;
  
   short entrada, saida;
   short sample[NSAMPLES] = {0x0};

   float a,b;

   float fc = 200; 
   float fs = 8000;

   float wc = 2*3.14*fc;
   float fl = 2*fs;
   a = wc/(fl+wc);
   b = (wc-fl)/(wc-fl);

   float y=0;

   //Carregando os coeficientes do filtro média móvel
  
 
   /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("sen_200hz.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("sai_sen_200hz.pcm","wb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

   // zera vetor de amostras
   for (i=0; i<NSAMPLES; i++)
        {
        sample[i]=0;
        }

   // execução do filtro
   float yAnt = 0;
 do {
        
	   //zera saída do filtro
        y=0;

        //lê dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
		sample[0] = entrada;

        for (n=0; n<NSAMPLES; n++)
        {
            y = a*sample[n] + a*sample[n-1] - b*yAnt;
        }

        //desloca amostra
        for (n=NSAMPLES-1; n>0; n--)
                {
                sample[n]=sample[n-1];
                }

				saida = (short) y;
                yAnt = saida;

        //escreve no arquivo de saída
        fwrite(&saida,sizeof(short),1,out_file);

 } while (n_amost);


   //fecha os arquivos de entrada de saída
   fclose(out_file);
   fclose(in_file);
   return 0;
}