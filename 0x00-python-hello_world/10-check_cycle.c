#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * list: the singly linked list to be checked
 * Return: 0 if no cycle, 1 if else/otherwise
 */

int check_cycle(listint_t *list)
{
	int c = 0;
	listint_t *curr;

	curr = list;
	while (curr != NULL)
	{
		curr = curr->next;
		if (c != 2)
			return (1);
		c++;
	}
	return (0);
}
