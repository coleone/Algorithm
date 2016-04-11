#include <stdlib.h>
#include <stdio.h>

/* The idea */

void quicksort(int* array, int length)
{
	// Initial check
	if(array == NULL)
		return;
	if(length <= 1)
		return;
	if(length == 2 && array[0] <= array[1])
		return;

	// Set pivot
	int pivot = (int)(length/2.);
	int i;

	for(i = 0; i < length; i++)
	{
		if(array[i] > array[pivot] && i < pivot)
		{
			int temp = array[pivot];
			array[pivot] = array[i];
			array[i] = temp;
		}
		if(array[i] < array[pivot] && i > pivot)
		{
			int temp = array[pivot];
			array[pivot] = array[i];
			array[i] = temp;
		}
	}

	// Allocate memory
	int* left = malloc((pivot+1)*sizeof(int));
	int* right = malloc((length-pivot-1)*sizeof(int));
	
	//Assign veriables to array
	for(i = 0; i < pivot+1; i++)
	{
		left[i] = array[i];
	}
	for(i = 0; i < length-pivot-1; i++)
	{
		right[i] = array[pivot + 1 + i];
	}
	
	// Recursive
	quicksort(left, pivot+1);
	quicksort(right, length-pivot-1);
	
	// Conquer 
	for(i = 0; i < pivot + 1; i++)
	{
		array[i] = left[i];
	}

	for(i = 0; i < length - pivot - 1; i++)
	{
		array[pivot + i + 1] = right[i];
	}
	
	free(left);
	free(right);
}

int main()
{
	int array[] = {52,31,5,20,5};
	int length = sizeof(array)/sizeof(array[0]);
	printf(" size is %d\r\n", length);
	int i = 0;

	quicksort(array, length);

	for(i = 0; i < length; i++)
		printf(" %d ", array[i]);
	return 0;
}
