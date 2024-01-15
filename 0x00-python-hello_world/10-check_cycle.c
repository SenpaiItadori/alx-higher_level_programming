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
	listint_t *temp = list, *tmp1 = list;

	if (list == NULL)
		return (0);

	while (temp && tmp1 && tmp1->next)
	{
		temp = temp->next;
		tmp1 = tmp1->next->next;
		if (temp == tmp1)
		{
			return (1);
		}
	}
	return (0);
}
