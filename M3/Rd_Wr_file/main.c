#include <stdio.h>

#define TAM_COEFS 4
#define TAM_MEDIA 4

int main() {
    //short passo = 1638;  // Ajustando o passo para ser um short
    short passo = 5;
    short W[TAM_COEFS] = {0};
    short samples[TAM_COEFS] = {0};
    short P[TAM_MEDIA] = {8192, 8192, 8192, 8192};  // Escalando os pesos para serem shorts

    FILE *fin = fopen("..\\branco_ruido.pcm", "rb");
    if (!fin) {
        printf("Erro ao abrir o arquivo de audio.\n");
        return 1;
    }
    
    FILE *fout = fopen("..\\saida.pcm", "wb");
    if (!fout) {
        printf("Erro ao abrir o arquivo de audio.\n");
        return 1;
    }

    short erro;
    short Vet_entr;

    fread(&Vet_entr, sizeof(short), 1, fin);  // Primeira leitura fora do loop

    while (1) {
        short d = 0;
        int n = 0;
        

        samples[0] = Vet_entr;

        // Calculando m�dia m�vel
        for (n = 0; n < TAM_MEDIA; n++) {
            d += (P[n] * samples[n]) >> 15;
        }

        short y = 0;
        for (n = 0; n < TAM_COEFS; n++) {
            y += (W[n] * samples[n]) >> 15;
        }

        // L�gica de convolu��o adaptativa
        erro = d - y;
        for (n = 0; n < TAM_COEFS; n++) {
            W[n] = W[n] + ((passo * erro * samples[n]) >> 15); 
        }

        for (n = TAM_COEFS - 1; n > 0; n--) {
            samples[n] = samples[n - 1];
        }
        
        fwrite(&erro,sizeof(short),1,fout);

        if (fread(&Vet_entr, sizeof(short), 1, fin) != 1) {
            break; 
        }
    }

    printf("Coeficientes finais: ");
    int i = 0;
    for (i = 0; i < TAM_COEFS; i++) {
        printf("%d ", W[i]);
    }
    printf("\n");
    printf("erro: %d ", erro);
	// dividir por 32767 para ver o valor calculado
    fclose(fin);
    fclose(fout);

    return 0;
}
