clear all
close all
clc
delete(instrfind({'port'},{'COM4'}));
puerto_serial=serial('COM4');
puerto_serial.BaudRate=9600;
fopen(puerto_serial);
pause(3)
fwrite(puerto_serial,'a')
start=1;
j=0;

Fs=1000;
N=1024;%N=duracion/Fs
i=0;
y=zeros(N,1);
t=linspace(0,((N-1)/Fs),N);
l1=line(nan,nan,'Color','r','LineWidth',2);
ylim([-0.1 1023.1]);
xlim([0 (N-1)/Fs]);%duracion
uicontrol('String','Parar','Callback','start=0;');

while start
    tic
    
    while i<N
        if toc>=(1/Fs)
            tic
            y(1:end-1)=y(2:end);
            y(end)=fscanf(puerto_serial,'%f');
            set(l1,'XData',t,'YData',y);
            drawnow
            i=i+1;     
        end
    end
    
    figure;
    % Realizar la transformada rapida de fourier fft
    L = length(y);
    NFFT = 2^nextpow2(L);% encontrar potencia de 2 ms cercana
    ffty = fft(y,NFFT)/L;% Eje y de la transformada de fourier
    xf = Fs/2*linspace(0,1,NFFT/2+1);% Eje x(de frecuencias) de la transformada de fourier
    ya = 2*abs(ffty(1:NFFT/2+1));
    plot(xf,ya);% Graficar la transformada
    title('Transformada de fourier de y')
    xlabel('Frecuencia (Hz)')
    ylabel('Amplitud')
    i=0;
    j=j+1;
    r(:,:,j)=[xf ; ya'];
    
end
fclose(puerto_serial);