#include <stdio.h>
#include <stdlib.h>

#define TAM_COEFS 4
#define TAM_MEDIA 4

int main() {
    double passo = 1e-8;
    short *audio;
    double W[TAM_COEFS] = {0};
    double samples[TAM_COEFS] = {0};
    double P[TAM_MEDIA] = {0.25, 0.25, 0.25, 0.25};

    // Abrindo o arquivo de áudio
    FILE *file = fopen("./branco_ruido.pcm", "rb");
    if (!file) {
        printf("Erro ao abrir o arquivo de áudio.\n");
        return 1;
    }

    // Obtendo o tamanho do arquivo
    fseek(file, 0, SEEK_END);
    long len_audio = ftell(file) / sizeof(short);
    fseek(file, 0, SEEK_SET);

    // Alocando memória para o áudio
    audio = (short *)malloc(len_audio * sizeof(short));
    if (!audio) {
        printf("Erro de alocação de memória.\n");
        fclose(file);
        return 1;
    }

    // Lendo o áudio do arquivo
    fread(audio, sizeof(short), len_audio, file);

    // Inicializando o vetor de erros
    double *erro = (double *)malloc(len_audio * sizeof(double));

    // Processando o áudio
    for (long j = 0; j < len_audio; j++) {
        double d = 0;

        // Atualizando vetor de amostras
        samples[0] = audio[j];

        // Calculando média móvel
        for (int n = 0; n < TAM_MEDIA; n++) {
            d += P[n] * samples[n];
        }

        // Lógica de convolução adaptativa
        double y = 0;
        for (int n = 0; n < TAM_COEFS; n++) {
            y += W[n] * samples[n];
        }

        // Lógica de convolução adaptativa
        erro[j] = d - y;

        // Atualizando coeficientes
        for (int n = 0; n < TAM_COEFS; n++) {
            W[n] = W[n] + passo * erro[j] * samples[n];
        }

        // Atualizando vetor de amostras
        for (int n = TAM_COEFS - 1; n > 0; n--) {
            samples[n] = samples[n - 1];
        }
    }

    // Imprimindo coeficientes finais
    printf("Coeficientes finais: ");
    for (int i = 0; i < TAM_COEFS; i++) {
        printf("%f ", W[i]);
    }
    printf("\n");

    // Liberando memória
    free(audio);
    free(erro);
    fclose(file);

    return 0;
}
