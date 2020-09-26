clear all
close all
clc

delete(instrfind({'port'},{'COM4'}));
puerto_serial=serial('COM4');
puerto_serial.BaudRate=9600;
fopen(puerto_serial);
pause(3)
fwrite(puerto_serial,'a')

Fs=1000;
N=2000;%N=duracion/Fs
y=zeros(N,1);
t=linspace(0,((N-1)/Fs),N);
l1=line(nan,nan,'Color','r','LineWidth',2);
ylim([-0.1 1023.1]);
xlim([0 (N-1)/Fs]);%duracion


uicontrol('String','Parar','Callback','parada=0;');
parada=1;
tic
while (parada)
    if toc>=(1/Fs)
        tic
        y(1:end-1)=y(2:end);
        y(end)=fscanf(puerto_serial,'%f');
        set(l1,'XData',t,'YData',y);
        drawnow
    end
end

fclose(puerto_serial);
        