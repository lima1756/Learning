// hanoitower.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stack.h"


using namespace std;

bool solveHanoi(int numDisk, stack *from, stack *to, stack *a, stack *b, stack *c);

void moveDisk(stack *from, stack *to);

stack *getSparePeg(stack *from, stack *to, stack *a, stack *b, stack *c);

bool isSolved(stack *s, int total);

void printPegs(stack *a, stack *b, stack *c);

int main()
{
	stack hanoiA, hanoiB, hanoiC;
	hanoiA = *new stack('a');
	hanoiB = *new stack('b');
	hanoiC = *new stack('c');
	for (int i = 5; i > 0; i--)
	{
		hanoiA.push(i);
	}
	cout << "-----START-----" << endl;
	printPegs(&hanoiA, &hanoiB, &hanoiC);
	solveHanoi(5, &hanoiA, &hanoiC, &hanoiA, &hanoiB, &hanoiC);
	cout << "-----END-----" << endl;
	printPegs(&hanoiA, &hanoiB, &hanoiC);
	system("PAUSE");
}


void printPegs(stack *a, stack *b, stack *c)
{
	cout << "A: ";
	(*a).printStack();
	cout << "\nB: ";
	(*b).printStack();
	cout << "\nC: ";
	(*c).printStack();
	cout << endl;
}

bool solveHanoi(int numDisk, stack *from, stack *to, stack *a, stack *b, stack *c)
{
	if (numDisk == 0)
		return true;
	else
	{
		stack *spare = getSparePeg(from, to, a, b, c);
		solveHanoi(numDisk - 1, from, spare, a, b, c);
		moveDisk(from, to);
		solveHanoi(numDisk - 1, spare, to, a, b, c);
		return true;
	}
}

void moveDisk(stack *from, stack *to)
{
	(*to).push((*from).pop());
}

stack *getSparePeg(stack *from, stack *to, stack *a, stack *b, stack *c)
{
	if ((*from).getName() == 'a' && (*to).getName() == 'b')
	{
		return c;
	}
	if ((*from).getName() == 'a' && (*to).getName() == 'c')
	{
		return b;
	}
	if ((*from).getName() == 'b' && (*to).getName() == 'a')
	{
		return c;
	}
	if ((*from).getName() == 'b' && (*to).getName() == 'c')
	{
		return a;
	}
	if ((*from).getName() == 'c' && (*to).getName() == 'a')
	{
		return b;
	}
	if ((*from).getName() == 'c' && (*to).getName() == 'b')
	{
		return a;
	}
	return NULL;
}

bool isSolved(stack *s, int total)
{
	if ((*s).getSize() == total)
	{
		return true;
	}
	return false;
}