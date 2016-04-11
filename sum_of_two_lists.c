#include <stdio.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    if(l1 == NULL && l2 != NULL)
    {
        return l2;
    }
    if(l1 != NULL && l2 == NULL)
    {
        return l1;
    }
    if(l1 == NULL && l2 == NULL)
    {
        return NULL;
    }
    
    int carry = 0;
    int sum = 0;
    struct ListNode* retArr = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* ret = retArr;
    struct ListNode* l1Copy = l1;
    struct ListNode* l2Copy = l2;
    
    while(l1Copy != NULL || l2Copy != NULL)
    {
        if(l1Copy -> next != NULL && l2Copy -> next != NULL)
        {
            sum = l1Copy -> val + l2Copy -> val;
            l1Copy = l1Copy -> next;
            l2Copy = l2Copy -> next;
        }
        else if(l1Copy -> next != NULL && l2Copy -> next == NULL)
        {
            sum = l1Copy -> val + l2Copy -> val;
            l1Copy = l1Copy -> next;
            l2Copy = NULL;
        }
        else if(l1Copy -> next == NULL && l2Copy -> next != NULL)
        {
            sum = l1Copy -> val + l2Copy -> val;
            l1Copy = NULL;
            l2Copy = l2Copy -> next;
        }
        else if(l1Copy -> next != NULL && l2Copy == NULL)
        {
            sum = l1Copy -> val;
            l1Copy = l1Copy -> next;
        }
        else if(l2Copy -> next != NULL && l1Copy == NULL)
        {
            sum = l2Copy -> val;
            l2Copy = l2Copy -> next;
        }
        else if(l2Copy -> next == NULL && l1Copy -> next == NULL)
        {
            sum = l1Copy -> val + l2Copy -> val;
            l1Copy = NULL;
            l2Copy = NULL;
        }
        
        /* Assign values and calculate carry */
        retArr -> val = carry;
        if(sum + carry >= 10)
        {
            sum = sum + carry - 10;
            carry = 1;
        }
        else
        {
            carry = 0;
        }
        retArr -> val = retArr -> val + sum;
        
        /* Calculate the last digit of the return list */
        if(carry == 0 && l1Copy == NULL && l2Copy == NULL)
        {
            return ret;
        }
        else
        {
            retArr = retArr -> next;
            if(carry == 1 && l1Copy == NULL && l2Copy == NULL)
            {
                retArr -> val = 1;
                retArr -> next = NULL;
                return ret;
            }
        }
    }
}


int main()
{
	struct ListNode* l1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode* l2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	
	l1 -> val = 9;
	l1 -> next -> val = 7;
	l1 -> next -> next = NULL;
	
	l2 -> val = 5;
	l2 -> next -> val = 4;
	l2 -> next -> next = NULL;
	
	printf("l1 is %d, %d", l1 -> val, l1 -> next -> val);
	printf("l2 is %d, %d", l2 -> val, l2 -> next -> val);

	return 0;
}