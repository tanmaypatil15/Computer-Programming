#include<stdio.h>
#include<conio.h>
#define max 10
int topa = -1, topb = max;
int s[max];
void pusha();
void pushb();
void popa();
void popb();
void disa();
void disb();
void main() {
       int ch, ch1;
       clrscr();
       printf("menu\n1.push in stack a\n");
       printf("2.push in stack b\n");
       printf("3.pop from stack a\n");
       printf("4.pop from stack b\n");
       printf("5.display stack a\n");
       printf("6.display stack b\n");
       do {
              printf("enter choice:");
              scanf("%d", & ch);
              switch (ch) {
                     case 1:
                            pusha();
                            break;
                     case 2:
                            pushb();
                            break;
                     case 3:
                            popa();
                            break;
                     case 4:
                            popb();
                            break;
                     case 5:
                            disa();
                            break;
                     case 6:
                            disb();
                            break;
                     default:
                            printf("invalid choice\n");
                            break;
              }
              printf("do you wnt to continue...yes==1:");
              scanf("%d", & ch1);
       } while (ch1 == 1);
       getch();
}

void pusha() {
       int x;
       if (topa == topb - 1)
              printf("overflow");
       else {
              printf("enter element:");
              scanf("%d", & x);
              topa = topa + 1;
              s[topa] = x;
       }
}
void pushb() {
       int y;
       if (topb - 1 == topa)
              printf("overflow");
       else {
              printf("enter element:");
              scanf("%d", & y);
              topb = topb - 1;
              s[topb] = y;
       }
}

void popa() {
       int x;
       if (topa == -1)
              printf("underflow\n");
       else {
              x = s[topa];
              printf("%d is deleted\n", x);
              topa = topa + 1;
       }
}

void popb() {
       int y;
       if (topb == max)
              printf("underflow\n");
       else {
              y = s[topb];
              printf("%d is deleted\n", y);
              topb = topb - 1;
       }
}

void disa() {
       int j;
       if (topa == -1)
              printf("underflow");
       else {
              for (j = topa; j > -1; i--) {
                     printf("%d\n", s[j]);
              }
       }
}

void disb() {
       int i;
       if (topb == max)
              printf("underflow\n");
       else {
              for (i = topb; i < max; i++) {
                     printf("%d\n", s[i]);
              }
       }
}


OUTPUT:
       menu
1. push in stack a
2. push in stack b
3. pop from stack a
4. pop from stack b
5. diplay stack a
6. display stack b
enter choice: 1
enter element: 10
do you want to
continue… yes == 1: 1
enter choice: 1
enter element: 20
do you want to
continue… yes == 1: 1
enter choice: 1
enter element: 30
do you want to
continue… yes == 1: 1
enter choice: 2
enter element: 40
do you want to
continue… yes == 1: 1
enter choice: 2
enter element: 50
do you want to
continue… yes == 1: 1
enter choice: 2
enter element: 60
do you want to
continue… yes == 1: 1
enter choice: 5
30
20
10
do you want to
continue… yes == 1: 1
60
50
40
do you want to
continue… yes == 1: 1
enter choice: 3
30 is deleted
do you want to
continue… yes == 1: 1
enter choice: 4
60 is deleted
do you want to
continue… yes == 1: 2