#include "lists.h"

int iteration(listint_t **head, int n);
int len_list(listint_t **head);

/**
 * is_palindrome - checks to see whether a singly linked list is a palidrome
 * @head: the address of a pointer to a listint_t singlly linked list
 *
 * Return: 0 if iot is not a palidrome, 1 if it is a palidrome
 */

int is_palindrome(listint_t **head)
{
	int i, j = 0, len = 0;
	listint_t *curr = *head;

	len = len_list(head);
	if (len < 2)
		return (1);
	i = 0;
	j = len;
	while (i < j)
	{
		if (curr->n != iteration(head, j))
			return (0);
		curr = curr->next;
		i++;
		j--;
	}
	return (1);
}

/**
 * iteration - iterates n number of times in a linked list
 * @head: the address to a pointer to a listint_t list
 * @n: the number of times the listg should be iterated
 *
 * Return: the data of the node at the end of the iteration
 */

int iteration(listint_t **head, int n)
{
	int i = 0;
	listint_t *node = *head;

	while (i != n)
	{
		i++;
		node = node->next;
	}
	return (node->n);
}

/**
 * len_list - returns the length of a listint_t linked list
 * @head: the address of a pointer to a listint_t list
 *
 * Return: the number f node of a listint_t list
 */

int len_list(listint_t **head)
{
	listint_t *node = *head;
	int i = 0;

	while (node != NULL)
	{
		i++;
		node = node->next;
	}

	return (i);
}
