#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FrameSize 20
#define FREQ_ROWS 4
#define FREQ_COLS 3

#define THRESHOLD 2000

short coefs_697[] = {15634, -27339, 16383, -27339, 15634};
short coefs_770[] = {15634, -26339, 16383, -26339, 15634};
short coefs_852[] = {15634, -25113, 16383, -25113, 15634};
short coefs_941[] = {15634, -23664, 16383, -23664, 15634};
short coefs_1209[] = {15634, -18636, 16383, -18636, 15634};
short coefs_1336[] = {15634, -15951, 16383, -15951, 15634};
short coefs_1477[] = {15634, -12785, 16383, -12785, 15634};
int idx = 0;
short xnm1[1] = {0}, xnm2[1] = {0}, ynm1[1] = {0}, ynm2[1] = {0};

void applyFilter(short *xnm2, short *xnm1, short *ynm2, short *ynm1, short *coefs, short x, short *saida) {
    int y = coefs[idx] * x + coefs[1] * xnm1[idx] + coefs[2] * xnm2[idx] - coefs[3] * ynm1[idx] - coefs[4] * ynm2[idx];
    y <<= 1;
    short y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    *saida = (x - y_16) >> 1;
    idx++;
}

int ativacao_697_anterior = 0;
int ativacao_770_anterior = 0;
int ativacao_852_anterior = 0;
int ativacao_941_anterior = 0;
int ativacao_1209_anterior = 0;
int ativacao_1336_anterior = 0;
int ativacao_1477_anterior = 0;
int nova_ativacao = 0;

int detectDTMF(short *sample) {
    short saida_697, saida_770, saida_852, saida_941, saida_1209, saida_1336, saida_1477;
	idx = 0;
	int i = 0;
	int media_697 = 0;
	for (i = 0; i < FrameSize; i++) {
		applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_697, sample[i], &saida_697);
		media_697 = media_697 + saida_697;
	}
	media_697 = media_697/20;
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_697, *sample, &saida_697);
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_770, *sample, &saida_770);
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_852, *sample, &saida_852);
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_941, *sample, &saida_941);
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_1209, *sample, &saida_1209);
    int media_1209 = 0;
	for (i = 0; i < FrameSize; i++) {
		applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_1209, sample[i], &saida_1209);
		media_1209 = media_697 + saida_697;
	}
	media_1209 = media_1209/20;
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_1336, *sample, &saida_1336);
    //applyFilter(xnm2, xnm1, ynm2, ynm1, coefs_1477, *sample, &saida_1477);
	nova_ativacao = 0;
    int ativacao_697 = (fabs(media_697) > THRESHOLD) ? 1 : 0;
    //int ativacao_770 = (fabs(saida_770) > THRESHOLD) ? 1 : 0;
    //int ativacao_852 = (fabs(saida_852) > THRESHOLD) ? 1 : 0;
    //int ativacao_941 = (fabs(saida_941) > THRESHOLD) ? 1 : 0;
    int ativacao_1209 = (fabs(media_1209) > THRESHOLD) ? 1 : 0;
    //int ativacao_1336 = (fabs(saida_1336) > THRESHOLD) ? 1 : 0;
    //int ativacao_1477 = (fabs(saida_1477) > THRESHOLD) ? 1 : 0;
    
    if (ativacao_697_anterior == 0 && ativacao_697 == 1){
    	ativacao_697_anterior = 1;
    	nova_ativacao = 1;
    } else {
    	ativacao_697_anterior = ativacao_697;
    }
    
    if (ativacao_1209_anterior == 0 && ativacao_1209 == 1){
    	ativacao_1209_anterior = 1;
    	nova_ativacao = 1;
    } else {
    	ativacao_1209_anterior = ativacao_1209;
    }
	
    	//        1209 1336 1477
		//697 Hz	1	2	3	A
		//770 Hz	4	5	6	B
		//852 Hz	7	8	9	C
		//941 Hz	*	0	#	D
	if (ativacao_697 == 1 && ativacao_1209 == 1) {
		return 1;
	} //else if (ativacao_697 == 1 && ativacao_1336 == 1) {
		//return 2;
	//} else if (ativacao_697 == 1 && ativacao_1477 == 1) {
	//	return 3;
	//} else if (ativacao_770 == 1 && ativacao_1209 == 1) {
	//	return 4;
	//} else if (ativacao_770 == 1 && ativacao_1336 == 1) {
	//	return 5;
	//} else if (ativacao_770 == 1 && ativacao_1477 == 1) {
	//	return 6;
	//} else if (ativacao_852 == 1 && ativacao_1209 == 1) {
	//	return 7;
	//} else if (ativacao_852 == 1 && ativacao_1336 == 1) {
	//	return 8;
	//} else if (ativacao_852 == 1 && ativacao_1477 == 1) {
	//	return 9;
	//} else if (ativacao_941 == 1 && ativacao_1209 == 1) {
	//	return 10;
	//} else if (ativacao_941 == 1 && ativacao_1336 == 1) {
	//	return 0;
	//} else if (ativacao_941 == 1 && ativacao_1477 == 1) {
	//	return 11;
	//}

    return -1;  // Nenhuma frequência DTMF detectada
}

int main() {
    FILE *fin;
    short sample;

    fin = fopen("..\\dtmf.pcm","rb");

    if (fin == NULL) {
        perror("Erro ao abrir o arquivo");
        return 1;
    }

    while (fread(&sample, sizeof(short), FrameSize, fin) == FrameSize) {
        int dtmfCode = detectDTMF(&sample);
        if (dtmfCode != -1 && nova_ativacao == 1) {
            printf("Frequencia DTMF detectada: %d\n", dtmfCode);
        }
    }
    
    printf("Finalizou\n");

    fclose(fin);

    return 0;
}
