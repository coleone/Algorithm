#include <stdio.h>

/*The idea behind merge sort is to compare individual items from two lists (list A and list B)
 ordered from least to greatest, remove the lesser of the two items and append it to a third
 list (list C). Once either list A or list B has no other items, append all items from the
 remaining list to list C in order. List C is now sorted list.*/ 

void printArr(int* arr, int size)
{
	int i = 0;
	
	for(i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	
	printf("\r\n");
}

void merge(int* arr, int l, int mid, int r)
{
	int i, j, k;
	int sizeLeft = mid - l + 1; // crucial: range
	int sizeRight = r - mid; // crucial: range
	int arrayLeft[sizeLeft], arrayRight[sizeRight];
	
	for(i = 0; i < sizeLeft; i++)
		arrayLeft[i] = arr[l + i]; // crucial: range
	for(j = 0; j < sizeRight; j++)
		arrayRight[j] = arr[mid + 1 + j]; // crucial: range
	
	i = 0;
	j = 0;
	k = l;
	
	while(i < sizeLeft && j < sizeRight)
	{
		if(arrayLeft[i] <= arrayRight[j])
		{
			arr[k] = arrayLeft[i];
			i++;
		}
		else
		{
			arr[k] = arrayRight[j];
			j++;
		}
		k++;
	}
	while(i < sizeLeft)
	{
		arr[k] = arrayLeft[i];
		i++;
		k++;
	}
	while(j < sizeRight)
	{
		arr[k] = arrayRight[j];
		j++;
		k++;
	}
}

void mergeSort(int* arr, int l, int r)
{
	int mid = (l + r) / 2;
	if(l < r)
	{
		mergeSort(arr, l, mid);
		mergeSort(arr, mid + 1, r);
		merge(arr, l, mid, r);
	}
}

int main()
{
	int array[] = {1024, 2048, 64, 32, 512, 256, 16, 4, 8};
	int size = sizeof(array) / sizeof(array[0]);
	int low = 0;
	int range = size - 1;
	
	printf("The array before merge sort is: ");
	printArr(array, size);
	
	mergeSort(array, low, range);
	
	printf("The array after merge sort is: ");
	printArr(array, size);
}

