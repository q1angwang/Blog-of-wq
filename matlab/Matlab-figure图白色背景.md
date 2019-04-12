
每次总是需要添加figure('color','w');或者figure('color',[1 1 1])或者set(gcf,'color','w');

set(0,'defaultfigurecolor','w') 


如何改变MATLAB中figure窗口的背景颜色
M 文件中 set命令 如：set( h1, ‘Color’，'r')


实例：
h1=figure(8);
subplot(1,2,1);
imshow(im,[]);
set( h1, 'Color','w')