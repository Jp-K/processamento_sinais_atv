#include <stdio.h>

#define TAM_COEFS 4
#define TAM_MEDIA 4

int main() {
    short passo = 5;
    short W[TAM_COEFS] = {0};
    short samples[TAM_COEFS] = {0};
    //short P[TAM_MEDIA] = {8192, 8192, 8192, 8192};
    short P[TAM_MEDIA] ={
   				#include "coefs_4.dat"
   };

    FILE *fin = fopen("../branco_ruido.pcm", "rb");
    FILE *fout = fopen("../saida.pcm", "wb");

    if (!fin || !fout) {
        printf("Erro ao abrir o arquivo de áudio.\n");
        return 1;
    }
    
	
    short erro;
    short Vet_entr;

    // Primeira leitura fora do loop
    if (fread(&Vet_entr, sizeof(short), 1, fin) != 1) {
        printf("Erro ao ler o arquivo de áudio.\n");
        fclose(fin);
        fclose(fout);
        return 1;
    }

    while (1) {
        short d = 0;
        int n;
		samples[0] = Vet_entr;
        // Calculando média móvel
        for (n = 0; n < TAM_MEDIA; n++) {
            d += (P[n] * samples[n]) >> 15;
        }

        short y = 0;
        for (n = 0; n < TAM_COEFS; n++) {
            y += (W[n] * samples[n]) >> 15;
        }

        // Lógica de convolução adaptativa
        erro = d - y;
        for (n = 0; n < TAM_COEFS; n++) {
            W[n] += (passo * erro * samples[n]) >> 15;
        }

        // Atualização das amostras para a próxima iteração
        for (n = TAM_COEFS - 1; n > 0; n--) {
            samples[n] = samples[n - 1];
        }

        fwrite(&erro, sizeof(short), 1, fout);

        // Leitura da próxima amostra
        if (fread(&Vet_entr, sizeof(short), 1, fin) != 1) {
            break;
        }
    }

    printf("Coeficientes finais: ");
    int i;
    for (i = 0; i < TAM_COEFS; i++) {
        printf("%d ", W[i]);
    }
    printf("\n");
    printf("Erro: %d\n", erro);

    fclose(fin);
    fclose(fout);

    return 0;
}
