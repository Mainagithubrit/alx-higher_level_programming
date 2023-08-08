#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: A pointer that points to the head of the linked list
 * @number: The number to be inserted
 *
 * Return: NULL if function fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *add;

	add = malloc(sizeof(listint_t));
	if (add == NULL)
		return (NULL);
	add->n = number;

	if (node == NULL || node->n >= number)
	{
		add->next = node;
		*head = add;
		return (add);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	add->next = node->next;
	node->next = add;

	return (add);

}
