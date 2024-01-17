#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: an address to a pointer to a listint_t linked singly list
 * @number: the data of the new node of a listint_t linked list
 *
 * Return: the address of the new node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = (*head), *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (curr == NULL || curr->n >= number)
	{
		new->next = curr;
		*head = new;
		return (*head);
	}

	while (curr->next && curr && curr->next->n < number)
		curr = curr->next;

	new->next = curr->next;
	curr->next = new;

	return (new);
}
