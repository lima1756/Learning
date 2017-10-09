#include "stdafx.h"
class value
{
private:
	int val;
	value *last = NULL;

public:
	value()
	{
		this->val = 0;
	}

	value(int *x)
	{
		this->val = *x;
	}

	value(int *x, value *last)
	{
		this->val = *x;
		this->last = last;
	}


	int getValue()
	{
		return val;
	}


	value *getLast()
	{
		return this->last;
	}
};