## Canteen Ordering System using C Language

This repository contains a simple canteen ordering system implemented in C language. It was developed as a learning project during my college time, aimed at practicing basic programming concepts for beginners.

#### Program:

```

#include<stdio.h>
#include<malloc.h>
#include<string.h>

struct node
{
    char t[100];
    int qu;
    int qh;
    struct code *next;
 }

*start =NULL,*p,*q;

void pla();
void vada();
void thali();
void cold();
void sandw();
void display();

void main()
{
 int choice,c;
 printf("-----CANTEEN SERVICES-----\n");
 printf("-----------MENU-----------\n1.Place an Order\n2.Display\n3.Exit");
 do
 {
  printf("\nENTER YOUR CHOICE:-->");
  scanf("%d",&choice);
  switch(choice)
  {
   case 1:pla();
          break;
   case 2:display();
          break;
   case 3:break;
   }
   printf("DO YOU WANT TO CONTINUE:-->");
   scanf("%d",&c);
  }while(c==0);
}

void pla()
{
    int cho,h;
    printf("\nItem List\n1.Vada Pav\n2.Sandwich\n3.Thali\n4.Cold Drink");

    do
    {
    printf("\nENTER YOUR CHOICE:-->");
    scanf("%d",&cho);
    switch(cho)
    {
    case 1:vada();
            break;
    case 2:sandw();
            break;
    case 3:thali();
            break;
    case 4:cold();
            break;
    case 5:break;
    }
    printf("ANYTHING ELSE:-->");
    scanf("%d",&h);
    }while(h==0);
}


void vada()
{
    char va[100]="Vada Pav";
    int a=15;int n;
    int b;
    printf("ENTER QUANTITY:-->");
    scanf("%d",&n);
    b=a*n;
    p=(struct node *)malloc(sizeof(struct node *));

    p->qu=b;
    strcpy(p->t,va);
    p->qh=n;
    p->next=NULL;
    if(start==NULL)
    start=p;
    else
    {
    q=start;
    while(q->next!=NULL)
    {
    q=q->next;
    }q->next=p;
    }
}

void sandw()
{
    char sa[100]="Sandwich";
    int a=25;int n;
    int b;
    printf("ENTER QUANTITY:-->");
    scanf("%d",&n);
    b=a*n;
    p=(struct node *)malloc(sizeof(struct node *));

    p->qu=b;
    strcpy(p->t,sa);
    p->qh=n;
    p->next=NULL;
    if(start==NULL)
    start=p;
    else
    {
    q=start;
    while(q->next!=NULL)
    {
    q=q->next;
    }q->next=p;
    }
}

void thali()
{
    char ta[100]="Thali   ";
    int a=45;int n;
    int b;
    printf("ENTER QUANTITY:-->");
    scanf("%d",&n);
    b=a*n;
    p=(struct node *)malloc(sizeof(struct node *));

    p->qu=b;
    strcpy(p->t,ta);
    p->qh=n;
    p->next=NULL;
    if(start==NULL)
    start=p;
    else
    {
    q=start;
    while(q->next!=NULL)
    {
    q=q->next;
    }q->next=p;
    }

}

void cold()
{
    char co[100]="Cold Drink";
    int a=20;int n;
    int b;
    printf("ENTER QUANTITY:-->");
    scanf("%d",&n);
    b=a*n;
    p=(struct node *)malloc(sizeof(struct node *));

    p->qu=b;
    strcpy(p->t,co);
    p->qh=n;
    p->next=NULL;
    if(start==NULL)
    start=p;
    else
    {
    q=start;
    while(q->next!=NULL)
    {
    q=q->next;
    }q->next=p;
    }
}


void display()
{
    printf("-----------Canteen Record-----------\n");
    if(start==NULL){
        printf("No Orders\n");
    }
    else
    {
    printf("Item Name\tQuantity\tSum\n");
    printf("------------------------------------\n");
    int total=0;
    q=start;
    while(q!=NULL)
    {
    printf("%s\t%d\t\t%d\n",q->t,q->qh,q->qu);
    total=total+q->qu;
    q=q->next;
    }
    printf("------------------------------------\n");
    printf("TOTAL\t\t\t\t%d\n",total);
    }
}


```
#### Output:

~~~

student@project:~/Desktop$ ./a.out

-----CANTEEN SERVICES-----
-----------MENU-----------
1.Place an Order
2.Display
3.Exit
ENTER YOUR CHOICE:-->1

Item List
1.Vada Pav
2.Sandwich
3.Thali
4.Cold Drink
ENTER YOUR CHOICE:-->1
ENTER QUANTITY:-->10
ANYTHING ELSE:-->0

ENTER YOUR CHOICE:-->2
ENTER QUANTITY:-->4
ANYTHING ELSE:-->0

ENTER YOUR CHOICE:-->3
ENTER QUANTITY:-->6
ANYTHING ELSE:-->0

ENTER YOUR CHOICE:-->4
ENTER QUANTITY:-->8
ANYTHING ELSE:-->1
DO YOU WANT TO CONTINUE:-->0

ENTER YOUR CHOICE:-->2
-----------Canteen Record-----------
Item Name	Quantity	Sum
------------------------------------
Vada Pav	10		150
Sandwich	4		100
Thali   	6		270
Cold Drink	8		160
------------------------------------
TOTAL				680
DO YOU WANT TO CONTINUE:-->1


~~~