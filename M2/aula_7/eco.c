#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define Fs 8000
#define T 0.2
#define A 0.9
#define B 0.5
#define TAMECO  1600

int main() {

    FILE *in_file, *out_file;
    int i, n, n_amost;
    
    short entrada, saida;

    float y=0;

    short vetor_eco[TAMECO] = {0x0};
    //int TAMECO = Fs * T;
    //printf("%d", TAMECO);
    //short vetor_eco = (short*)malloc(TAMECO * sizeof(short)); 

    //Carregando os coeficientes do filtro média móvel

    if ((in_file = fopen("alo.pcm","rb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }
    if ((out_file = fopen("saida_alo_sweep.pcm","wb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    for (i=0; i<TAMECO; i++) {
        vetor_eco[i]=0;
    }

    do {

        y=0;
        n_amost = fread(&entrada,sizeof(short),1,in_file);
		vetor_eco[0] = entrada;

        y = (A * vetor_eco[0]) + (B * vetor_eco[TAMECO-1]);
        vetor_eco[0] = y;
        for (n=TAMECO-1; n>0; n--) {
            vetor_eco[n]=vetor_eco[n-1];
        }
        saida = (short) y;
        fwrite(&saida,sizeof(short),1,out_file);

    } while (n_amost);

    fclose(out_file);
    fclose(in_file);
    return 0;

}