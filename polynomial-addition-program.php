#include<stdio.h>
#include<conio.h>
struct node1 {
	int coef;
	int exp;
	struct node * next;
}* start1 = NULL;
struct node2 {
	int coef;
	int exp;
	struct node * next;
}* start2 = NULL;
struct node {
	int coef;
	int exp;
	struct node * next;
}* start = NULL;

void createp1();
void createp2();
void add();
void main() {
	int ch, ch1;
	clrscr();
	printf("MENU\N1.CREATE POLYNOMIAL 1\n2.CREATE POLYNOMIAL 2\n3.ADD PLOYNOMIAL 1 AND 2\n");
	do {
		printf("enter choice:");
		scanf("%d", & ch);
		switch (ch) {
			case 1:
				createp1();
				break;
			case 2:
				createp2();
				break;
			case 3:
				add();
				break;
			default:
				printf("invalid choice");
				break;
		}
		printf("do you want to continue if yes press 11:");
		scanf("%d", & ch1);
	} while (ch1 == 11);
}

void createp1() {
	int x, y;
	struct node1 * p1, * q1;
	p1 = (struct node * )(malloc(sizeof(struct node * )));
	printf("enter coefficient:");
	scanf("%d", & x);
	printf("enter exponent:");
	scanf("%d", & y);
	p1 - > coef = x;
	p1 - > exp = y;
	p1 - > next = NULL;
	if (start1 == NULL) {
		start1 = p1;
	} else {
		q1 = start1;
		while (q1 - > next != NULL) {
			q1 = q1 - > next;
		}
		q1 - > next = p1;
	}
}


void createp2() {
	int x, y;
	struct node2 * p2, * q2;
	p2 = (struct node * )(malloc(sizeof(struct node * )));
	printf("enter coefficient:");
	scanf("%d", & x);
	printf("enter exponent:");
	scanf("%d", & y);
	p2 - > coef = x;
	p2 - > exp = y;
	p2 - > next = NULL;
	if (start2 == NULL) {
		start2 = p2;
	} else {
		q2 = start2;
		while (q2 - > next != NULL) {
			q2 = q2 - > next;
		}
		q2 - > next = p2;
	}
}

void add() {
	struct node * p, * q;
	struct node1 * q1;
	struct node2 * q2;
	q1 = start1;
	q2 = start2;
	while (q1 != NULL && q2 != NULL) {
		p = (struct node * )(malloc(sizeof(struct node * )));
		p - > next = NULL;
		if (q1 - > exp == q2 - > exp) {
			p - > coef = q1 - > coef + q2 - > coef;
			p - > exp = q1 - > exp;
			q1 = q1 - > next;
			q2 = q2 - > next;
		} else
		if (q1 - > exp > q2 - > exp) {
			p - > coef = q1 - > coef;
			p - > exp = q1 - > exp;
			q1 = q1 - > next;
		} else
		if (q2 - > exp > q1 - > exp) {
			p - > coef = q2 - > coef;
			p - > exp = q2 - > exp;
			q2 = q2 - > next;
		}

		if (start == NULL) {
			start = p;
		} else {
			q = start;
			while (q - > next != NULL) {
				q = q - > next;
			}
			q - > next = p;
		}
	}
	while (q1 != NULL && q2 == NULL) {
		p = (struct node * )(malloc(sizeof(struct node * )));
		p - > next = NULL;
		p - > coef = q1 - > coef;
		p - > exp = q1 - > exp;
		q1 = q1 - > next;
		if (start == NULL) {
			start = p;
		} else {
			q = start;
			while (q - > next != NULL) {
				q = q - > next;
			}
			q - > next = p;
		}
	}
	while (q2 != NULL && q1 == NULL) {
		p = (struct node * )(malloc(sizeof(struct node * )));
		p - > next = NULL;
		p - > coef = q2 - > coef;
		p - > exp = q2 - > exp;
		q2 = q2 - > next;
		if (start == NULL) {
			start = p;
		} else {
			q = start;
			while (q - > next != NULL) {
				q = q - > next;
			}
			q - > next = p;
		}
	}
	printf("addition of polynomial 1 and 2 is:");
	q = start;
	while (q - > next != NULL) {
		printf("%dx^%d+", q - > coef, q - > exp);
		q = q - > next;
	}
	printf("%dx^%d", q - > coef, q - > exp);
}