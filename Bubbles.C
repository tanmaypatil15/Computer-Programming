#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>
void main()
{
int x,y,i=0,j,xx,yy,rad=1;
int gd=DETECT,gm;
//cleardevice();
initgraph(&gd,&gm,"C:\\TurboC3\\BGI");

x=getmaxx();
y=getmaxy();
//setcolor(BLUE);
while(!kbhit())
{

for(i=0;i<=50;i++)
 {
 cleardevice();
setfillstyle(random(i),random(i));
rad=10*i;
circle(xx=random(x+i),yy=random(y+i),random(100));
floodfill(xx,yy,getmaxcolor());
delay(300);
}

}
 //setcolor(rand());
 /*
for(i=0;i<=500;i++)
{
circle(x,y,i);
setcolor(rand());
delay(500);
}

for(j=0;j<=100;j++)
{
circle(x,y,j);
setcolor(rand());
delay(500);
}  */

closegraph();
getch();

}