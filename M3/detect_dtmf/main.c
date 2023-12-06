/*****************************************************************************
 * DetectDTMF.c
 *****************************************************************************/
 
#include <stdio.h>
#include <string.h>
#include <math.h>
#define FrameSize 1

#define FREQ_ROWS 4
#define FREQ_COLS 3

static int frameCount = 1;

unsigned int th = 500;

short coefs_697[] = {
		15634,
		-27339,
		16383,
		-27339,
		15634
	};

short coefs_770[] = {
	15634,
	-26339,
	16383,
	-26339,
	15634
};

short coefs_852[] = {
	15634,
	-25113,
	16383,
	-25113,
	15634
};

short coefs_941[] = {
	15634,
	-23664,
	16383,
	-23664,
	15634
};

short coefs_1209[] = {
	15634,
	-18636,
	16383,
	-18636,
	15634
};

short coefs_1336[] = {
	15634,
	-15951,
	16383,
	-15951,
	15634
};

short coefs_1477[] = {
	15634,
	-12785,
	16383,
	-12785,
	15634
};

short xnm1[] = {0, 0, 0, 0, 0, 0, 0};
short xnm2[] = {0, 0, 0, 0, 0, 0, 0};
short ynm1[] = {0, 0, 0, 0, 0, 0, 0};
short ynm2[] = {0, 0, 0, 0, 0, 0, 0};
int actives[] = {0, 0, 0, 0, 0, 0, 0};
int novo_valor = 0;
unsigned int valor_anterior = 0;
void proc_file( short *sai, short *entr)
{
    int i, n;
	int y=0;
	int idx = 0;
	novo_valor = 0;
	
	short x = entr[0];
    y =  (coefs_697[0] * x) + (coefs_697[1] * xnm1[idx]) + (coefs_697[2] * xnm2[idx]) - (coefs_697[3] * ynm1[idx]) - (coefs_697[4] * ynm2[idx]);
    y = y<<1;
    short y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    short saida = (x-y_16)>>1;
    
    short absValue = abs(saida);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    	//	printf("------------------------\n");
    	//	printf("atual: %d\n", absValue);
    	//	printf("saida: %d\n", saida);
    	//	printf("anterior: %d\n", valor_anterior);
    	//	printf("------------------------\n");
    	//	valor_anterior = absValue;
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	//printf("atual: %d\n", absValue);
    	actives[idx] = 0;
    }
    
    
    idx = 1;
    y =  (coefs_770[0] * x) + (coefs_770[1] * xnm1[idx]) + (coefs_770[2] * xnm2[idx]) - (coefs_770[3] * ynm1[idx]) - (coefs_770[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }
    
    
    idx = 2;
    y =  (coefs_852[0] * x) + (coefs_852[1] * xnm1[idx]) + (coefs_852[2] * xnm2[idx]) - (coefs_852[3] * ynm1[idx]) - (coefs_852[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }

	idx = 3;
    y =  (coefs_941[0] * x) + (coefs_941[1] * xnm1[idx]) + (coefs_941[2] * xnm2[idx]) - (coefs_941[3] * ynm1[idx]) - (coefs_941[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }	
    
    idx = 4;
    y =  (coefs_1209[0] * x) + (coefs_1209[1] * xnm1[idx]) + (coefs_1209[2] * xnm2[idx]) - (coefs_1209[3] * ynm1[idx]) - (coefs_1209[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }	
    
    
    idx = 5;
    y =  (coefs_1336[0] * x) + (coefs_1336[1] * xnm1[idx]) + (coefs_1336[2] * xnm2[idx]) - (coefs_1336[3] * ynm1[idx]) - (coefs_1336[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }	
    
    idx = 6;
    y =  (coefs_1477[0] * x) + (coefs_1477[1] * xnm1[idx]) + (coefs_1477[2] * xnm2[idx]) - (coefs_1477[3] * ynm1[idx]) - (coefs_1477[4] * ynm2[idx]);
    y = y<<1;
    y_16 = y >> 15;
    xnm2[idx] = xnm1[idx];
    xnm1[idx] = x;
    ynm2[idx] = ynm1[idx];
    ynm1[idx] = y_16;
    saida = (x-y_16)>>1;
    
    absValue = fabs((unsigned)saida/32767);
    
    if (absValue > th) {
    	if (actives[idx] != 1) {
    		novo_valor = 1;
    	}
    	actives[idx] = 1;
    } else {
    	actives[idx] = 0;
    }
    //sai[0] = saida;

    return;
}

int decodeDTMF(int frequencies[]) {
    int row, col;

    // Verificando a linha (frequência alta)
    for (row = 0; row < FREQ_ROWS; row++) {
        if (frequencies[row] == 1) {
            break;
        }
    }

    // Verificando a coluna (frequência baixa)
    for (col = 0; col < FREQ_COLS; col++) {
        if (frequencies[FREQ_ROWS + col] == 1) {
            break;
        }
    }
    if (row < FREQ_ROWS && col < FREQ_COLS) {
        return (row * FREQ_COLS) + col + 1;
    } else {
        return -1;
    }
}

int main( void )
{
	/* Begin adding your custom code here */
	
	FILE *fin,*fout;

    short Vet_entr[FrameSize];
    short Vet_sai[FrameSize];
    
    fin = fopen("..\\dtmf.pcm","rb");
    if ((fin)==NULL){
    	printf("\nErro: nao abriu o arquivo de Entrada\n");
    	return 0;
  	}
    fout = fopen("..\\sai_audio_tst.pcm","wb");
    if ((fout)==NULL){
    	printf("\nErro: nao abriu o arquivo de Saida\n");
    	return 0;
  	}
  	
  	int current_value = 0;
  	int cont = 0;
  	while (fread(Vet_entr,sizeof(short),FrameSize,fin) == FrameSize){

		proc_file( Vet_sai, Vet_entr);
		
		// actives : 697, 770, 852, 941, 1209, 1336, 1477
		if (novo_valor == 1) {
    		current_value = decodeDTMF(actives);
			if (current_value != -1) {
			   // printf("Número DTMF decodificado: %d\n", current_value);
			    cont++;
			}
			novo_valor = 0;
    	}
		
		//fwrite(&Vet_sai,sizeof(short),FrameSize,fout);	
	
		frameCount++;
	}
	printf("numero de numeros encontrados: %d\n", cont);

    printf("terminado!\n");
		
    
	
	fclose(fin);
	fclose(fout);
  	
  	
    
	return 0;
}
