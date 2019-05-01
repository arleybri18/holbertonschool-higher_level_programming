#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new node in order
 * @head: pointer to head of list
 * @number: number to insert
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *next = current->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (current->next != NULL)
	{
		if (number >= current->n && number <= next->n)
		{
			new->n = number;
			current->next = new;
			new->next = next;
			break;
		}
		current = current->next;
		next = next->next;

	}
	if (current->next == NULL)
	{
		new->n = number;
		current->next = new;
		new->next = NULL;
	}
	return (new);
}
