
void proc_file( short *sai, short *entr, short *coef, short *sample, int NSAMPLES, int TAM_COEFS,  short *W, short passo)
{
    int i, n;
   	short erro = 0;
	int d=0;
	sample[0] = entr[0];
    for( n=0; n<NSAMPLES; n++ ) 
    {
		d += coef[n]*sample[n];
	}
	
	int y=0;
	for( n=0; n<TAM_COEFS; n++ ) 
    {
		y += W[n]*sample[n];
	}
    erro = d-y;
    
    
    for( n=0; n<TAM_COEFS; n++ ) 
    {
		W[n] = W[n] + ((passo*sample[n]*erro)>>15);
	}
	
	for (n=NSAMPLES-1; n>0; n--)
    {
    	sample[n]=sample[n-1];
    }
    
    sai[0] = d>>15;

    return;
}



		
