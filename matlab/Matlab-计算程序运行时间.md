# matlab-计算程序运行时间

matlab中三种计算程序运行时间方法


1、tic和toc组合(使用最多的)  
计算tic和toc之间那段程序之间的运行时间，它的经典格式为  

tic  
。。。。。。。。。。  
toc 



2、etime(t1,t2)并和clock配合  
来计算t1，t2之间的时间差，它是通过调用windows系统的时钟进行时间差计算得到运行时间的，应用的形式  

t1=clock;  
。。。。。。。。。。。  3. t2=clock;  
etime(t2,t1)



3、cputime函数来完成  
使用方法和etime相似，只是这个是使用cpu的主频计算的，和前面原理不同，使用格式如下  

t0=cputime  
。。。。。。。。。。。。。  
t1=cputime-t0 
