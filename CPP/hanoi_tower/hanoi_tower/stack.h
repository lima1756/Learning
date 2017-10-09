#include "stdafx.h"
#include "value.h"
#include <iostream>
using namespace std;

class stack
{
private:
	int size;
	char name;
	value *last;
public:
	stack() {}
	stack(char c)
	{
		size = 0;
		this->last = NULL;
		name = c;
	}

	char getName()
	{
		return this->name;
	}

	int getSize()
	{
		return this->size;
	}

	void push(int val)
	{
		if (this->size == 0)
		{
			this->last = new value(&val);
		}
		else
		{
			this->last = new value(&val, this->last);
		}
		this->size++;
	}

	int pop()
	{
		int myInt = -1;
		if (this->size > 1)
		{
			myInt = this->last->getValue();
			value *temp = this->last->getLast();
			delete this->last;
			this->last = temp;
		}
		else if (this->size == 1)
		{
			myInt = this->last->getValue();
			delete this->last;
			this->last = NULL;
		}
		else
		{
			cout << "Empty Stack";
		}
		this->size--;
		return myInt;
	}

	void printStack()
	{
		value *actualLast = this->last;
		while (actualLast != NULL)
		{
			cout << (*actualLast).getValue() << ", ";
			actualLast = (*actualLast).getLast();
		}
	}
};