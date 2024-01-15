#include "lists.h"

/**
 * check_cycle - checks to see if a linked list has got a cycle or not
 * @list: the listint_t linked list
 *
 * Return: 0 if there is no cycle , 1 if there is one
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	list = list->next;
	while (list->next != NULL)
	{
		if (temp == list)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
